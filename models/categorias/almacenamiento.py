"""
Clase abstracta para muebles de almacenamiento.
"""

from abc import ABC, abstractmethod
from ..mueble import Mueble


class Almacenamiento(Mueble, ABC):
    """
    Clase abstracta para muebles de almacenamiento.
    
    Agrupa características comunes de armarios, cajoneras, estantes, etc.
    Estos muebles tienen la función principal de guardar y organizar objetos.
    
    Conceptos OOP aplicados:
    - Herencia: Extiende la clase Mueble
    - Abstracción: Define características comunes de almacenamiento
    - Encapsulación: Protege atributos con getters/setters
    """
    
    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 capacidad_volumen: float, numero_compartimentos: int = 1,
                 tiene_puertas: bool = True, tipo_cierre: str = None):
        """
        Constructor para muebles de almacenamiento.
        
        Args:
            capacidad_volumen: Volumen total de almacenamiento en litros
            numero_compartimentos: Cantidad de compartimentos o secciones
            tiene_puertas: Si el mueble tiene puertas
            tipo_cierre: Tipo de cierre ('bisagra', 'corredizo', 'abatible', etc.)
            Otros argumentos heredados de Mueble
        """
        super().__init__(nombre, material, color, precio_base)
        
        self.capacidad_volumen = capacidad_volumen
        self.numero_compartimentos = numero_compartimentos
        self.tiene_puertas = tiene_puertas
        self.tipo_cierre = tipo_cierre
    
    @property
    def capacidad_volumen(self) -> float:
        """Getter para la capacidad de volumen."""
        return self._capacidad_volumen

    @capacidad_volumen.setter
    def capacidad_volumen(self, value: float) -> None:
        """Setter para capacidad_volumen con validación."""
        if value <= 0:
            raise ValueError("La capacidad de volumen debe ser mayor a 0")
        self._capacidad_volumen = float(value)

    @property
    def numero_compartimentos(self) -> int:
        """Getter para el número de compartimentos."""
        return self._numero_compartimentos

    @numero_compartimentos.setter
    def numero_compartimentos(self, value: int) -> None:
        """Setter para numero_compartimentos con validación."""
        if not isinstance(value, int) or value < 1:
            raise ValueError("El número de compartimentos debe ser un número mayor a 0")
        self._numero_compartimentos = value

    @property
    def tiene_puertas(self) -> bool:
        """Getter para verificar si tiene puertas."""
        return self._tiene_puertas

    @tiene_puertas.setter
    def tiene_puertas(self, value: bool) -> None:
        """Setter para tiene_puertas con validación."""
        if not isinstance(value, bool):
            raise ValueError("tiene_puertas debe ser un booleano")
        self._tiene_puertas = value

    @property
    def tipo_cierre(self) -> str:
        """Getter para el tipo de cierre."""
        return self._tipo_cierre

    @tipo_cierre.setter
    def tipo_cierre(self, value: str) -> None:
        """Setter para tipo_cierre con validación."""
        if value is not None:
            if not isinstance(value, str) or not value.strip():
                raise ValueError("El tipo de cierre debe ser un texto válido")
            self._tipo_cierre = value.strip()
        else:
            self._tipo_cierre = None
    
    def calcular_factor_almacenamiento(self) -> float:
        """
        Calcula un factor de almacenamiento basado en características.
        Método concreto que pueden usar las clases hijas.
        
        Returns:
            float: Factor multiplicador para el precio (1.0 = neutral)
        """
        factor = 1.0
        
        # Incremento por capacidad de volumen
        # Base: 1000 litros = factor 1.2
        if self.capacidad_volumen > 500:
            factor += 0.1
        if self.capacidad_volumen > 1000:
            factor += 0.15
        
        # Incremento por compartimentos
        if self.numero_compartimentos > 1:
            factor += 0.05 * (self.numero_compartimentos - 1)
        
        # Incremento por puertas
        if self.tiene_puertas:
            factor += 0.1
        
        # Incremento por tipo de cierre especial
        if self.tipo_cierre:
            if self.tipo_cierre.lower() == "corredizo":
                factor += 0.15
            elif self.tipo_cierre.lower() == "abatible":
                factor += 0.1
        
        return factor
    
    def obtener_info_almacenamiento(self) -> str:
        """
        Obtiene información específica del almacenamiento.
        Método concreto auxiliar para las clases hijas.
        
        Returns:
            str: Información detallada del almacenamiento
        """
        info = f"Capacidad: {self.capacidad_volumen}L"
        info += f", Compartimentos: {self.numero_compartimentos}"
        info += f", Puertas: {'Sí' if self.tiene_puertas else 'No'}"
        if self.tipo_cierre:
            info += f", Cierre: {self.tipo_cierre}"
        return info
    
    @abstractmethod
    def calcular_precio(self) -> float:
        """
        Calcula el precio final del almacenamiento.
        Toma en cuenta el precio base, factor de almacenamiento y otros ajustes.
        Cada tipo de almacenamiento (Armario, Cajonera, etc.) implementará su propia lógica.
        
        Returns:
            float: Precio final calculado
        """
        raise NotImplementedError("Las subclases deben implementar calcular_precio()")
    
    @abstractmethod
    def obtener_descripcion(self) -> str:
        """
        Obtiene una descripción detallada del almacenamiento.
        Cada tipo de almacenamiento tendrá su propia descripción basada en sus características.
        
        Returns:
            str: Descripción completa del almacenamiento
        """
        raise NotImplementedError("Las subclases deben implementar obtener_descripcion()")

