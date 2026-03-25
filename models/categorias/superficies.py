"""
Clase abstracta para muebles para superficies de trabajo o del hogar.
"""

from abc import ABC, abstractmethod
from ..mueble import Mueble


class Superficie(Mueble, ABC):
    """
    Clase abstracta para muebles con superficie de trabajo o uso.
    
    Agrupa características comunes de mesas, escritorios, mostradores, etc.
    Estos muebles tienen principalmente una superficie plana para trabajar o colocar objetos.
    
    Conceptos OOP aplicados:
    - Herencia: Extiende la clase Mueble
    - Abstracción: Define características comunes de superficies
    - Encapsulación: Protege atributos con getters/setters
    """
    
    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 forma: str, capacidad_personas: int, alto_cm: float = None):
        """
        Constructor para muebles con superficie.
        
        Args:
            forma: Forma de la superficie ('rectangular', 'cuadrada', 'redonda', 'ovalada')
            capacidad_personas: Cantidad de personas que pueden usar la superficie
            alto_cm: Altura de la superficie en centímetros (opcional)
            Otros argumentos heredados de Mueble
        """
        super().__init__(nombre, material, color, precio_base)
        
        self.forma = forma
        self.capacidad_personas = capacidad_personas
        self.alto_cm = alto_cm
    
    @property
    def forma(self) -> str:
        """Getter para la forma de la superficie."""
        return self._forma

    @forma.setter
    def forma(self, value: str) -> None:
        """Setter para forma con validación."""
        formas_validas = {'rectangular', 'cuadrada', 'redonda', 'ovalada', 'hexagonal'}
        if not isinstance(value, str) or value.lower() not in formas_validas:
            raise ValueError(f"Forma no válida. Válidas: {formas_validas}")
        self._forma = value.lower()

    @property
    def capacidad_personas(self) -> int:
        """Getter para la capacidad de personas."""
        return self._capacidad_personas

    @capacidad_personas.setter
    def capacidad_personas(self, value: int) -> None:
        """Setter para capacidad_personas con validación."""
        if not isinstance(value, int) or value <= 0:
            raise ValueError("La capacidad debe ser un número mayor a 0")
        self._capacidad_personas = value

    @property
    def alto_cm(self) -> float:
        """Getter para el alto de la superficie."""
        return self._alto_cm

    @alto_cm.setter
    def alto_cm(self, value: float) -> None:
        """Setter para alto_cm con validación."""
        if value is not None:
            if value <= 0:
                raise ValueError("El alto debe ser mayor a 0")
            self._alto_cm = float(value)
        else:
            self._alto_cm = None
    
    def calcular_factor_superficie(self) -> float:
        """
        Calcula un factor de precio basado en características de la superficie.
        Método concreto que pueden usar las clases hijas.
        
        Returns:
            float: Factor multiplicador para el precio (1.0 = neutral)
        """
        factor = 1.0
        
        # Incremento por forma especial
        if self.forma == "redonda":
            factor += 0.15
        elif self.forma == "ovalada":
            factor += 0.12
        elif self.forma == "hexagonal":
            factor += 0.2
        
        # Incremento por capacidad de personas
        if self.capacidad_personas > 2:
            factor += 0.08 * (self.capacidad_personas - 2)
        
        # Ajuste por altura (si está especificada)
        if self.alto_cm:
            # Altura estándar de mesa es 75cm
            desviacion = abs(self.alto_cm - 75) / 75
            factor += 0.05 * desviacion
        
        return factor
    
    def obtener_info_superficie(self) -> str:
        """
        Obtiene información específica de la superficie.
        Método concreto auxiliar para las clases hijas.
        
        Returns:
            str: Información detallada de la superficie
        """
        info = f"Forma: {self.forma.capitalize()}"
        info += f", Capacidad: {self.capacidad_personas} personas"
        if self.alto_cm:
            info += f", Alto: {self.alto_cm}cm"
        return info
    
    @abstractmethod
    def calcular_precio(self) -> float:
        """
        Calcula el precio final de la superficie.
        Toma en cuenta el precio base, factor de superficie y otros ajustes.
        Cada tipo de superficie (Mesa, Escritorio, etc.) implementará su propia lógica.
        
        Returns:
            float: Precio final calculado
        """
        raise NotImplementedError("Las subclases deben implementar calcular_precio()")
    
    @abstractmethod
    def obtener_descripcion(self) -> str:
        """
        Obtiene una descripción detallada de la superficie.
        Cada tipo de superficie tendrá su propia descripción basada en sus características.
        
        Returns:
            str: Descripción completa de la superficie
        """
        raise NotImplementedError("Las subclases deben implementar obtener_descripcion()")

