"""
Clase abstracta para muebles de asiento.
Esta clase agrupa las características comunes de sillas, sillones y sofás.
"""

# TODO: Importar la clase padre Mueble
# from ..mueble import Mueble
from ..mueble import Mueble
# TODO: Importar ABC y abstractmethod si es necesario
from abc import ABC, abstractmethod



class Asiento(Mueble, ABC):
    """
    Clase abstracta para todos los muebles donde las personas se sientan.
    
    Hereda de Mueble y añade características específicas de los asientos
    como capacidad de personas, tipo de respaldo, etc.
    
    Conceptos OOP aplicados:
    - Herencia: Extiende la clase Mueble
    - Abstracción: Agrupa características comunes de asientos
    - Polimorfismo: Permite diferentes implementaciones del cálculo de comodidad
    """
    
    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 capacidad_personas: int, tiene_respaldo: bool, material_tapizado: str = None):
        """
        Constructor para muebles de asiento.
        
        Args:
            capacidad_personas: Número de personas que pueden sentarse
            tiene_respaldo: Si el asiento tiene respaldo o no
            material_tapizado: Material del tapizado (opcional)
            Otros argumentos heredados de Mueble
        """
        # TODO: Llamar al constructor de la clase padre usando super()
        # super() permite acceder al constructor de Mueble sin duplicar código
        super().__init__(nombre, material, color, precio_base)
        
        # TODO: Inicializar los atributos específicos de asiento
        # Usar encapsulación con atributos privados
        self.capacidad_personas = capacidad_personas
        self.tiene_respaldo = tiene_respaldo
        self.material_tapizado = material_tapizado
    
    # TODO: Implementar propiedades (getters) para los nuevos atributos
    # @property
    # def capacidad_personas(self) -> int:
    #     """Getter para la capacidad de personas."""
    #     return self._capacidad_personas
    @property
    def capacidad_personas(self) -> int:
        """Getter para la capacidad de personas."""
        return self._capacidad_personas

    # TODO: Implementar setters con validaciones apropiadas
    # @capacidad_personas.setter
    # def capacidad_personas(self, value: int) -> None:
    #     """Setter para capacidad con validación."""
    #     if value <= 0:
    #         raise ValueError("La capacidad debe ser mayor a 0")
    #     self._capacidad_personas = value
    @capacidad_personas.setter
    def capacidad_personas(self, value: int) -> None:
        """Setter para capacidad con validación."""
        if not isinstance(value, int) or value <= 0:
            raise ValueError("La capacidad debe ser un número mayor a 0")
        self._capacidad_personas = value

    @property
    def tiene_respaldo(self) -> bool:
        """Getter para verificar si tiene respaldo."""
        return self._tiene_respaldo

    @tiene_respaldo.setter
    def tiene_respaldo(self, value: bool) -> None:
        """Setter para tiene_respaldo con validación."""
        if not isinstance(value, bool):
            raise ValueError("tiene_respaldo debe ser un booleano")
        self._tiene_respaldo = value

    @property
    def material_tapizado(self) -> str:
        """Getter para el material de tapizado."""
        return self._material_tapizado

    @material_tapizado.setter
    def material_tapizado(self, value: str) -> None:
        """Setter para material_tapizado con validación."""
        if value is not None:
            if not isinstance(value, str) or not value.strip():
                raise ValueError("El material de tapizado debe ser un texto válido")
            self._material_tapizado = value.strip()
        else:
            self._material_tapizado = None
    
    def calcular_factor_comodidad(self) -> float:
        """
        Calcula un factor de comodidad basado en las características del asiento.
        Este es un método concreto que pueden usar las clases hijas.
        
        Returns:
            float: Factor multiplicador para el precio (1.0 = neutral)
        """
        # TODO: Implementar lógica de cálculo de comodidad
        # Considerar factores como:
        # - Si tiene respaldo (+0.1)
        # - Material del tapizado (cuero +0.2, tela +0.1)
        # - Capacidad de personas (más personas = más cómodo)
        
        factor = 1.0
        
        # TODO: Agregar lógica aquí
        # if self.tiene_respaldo:
        #     factor += 0.1
        # 
        # if self.material_tapizado:
        #     if self.material_tapizado.lower() == "cuero":
        #         factor += 0.2
        #     elif self.material_tapizado.lower() == "tela":
        #         factor += 0.1
        
        # Aplicar lógica de comodidad
        if self.tiene_respaldo:
            factor += 0.1
        
        if self.material_tapizado:
            if self.material_tapizado.lower() == "cuero":
                factor += 0.2
            elif self.material_tapizado.lower() == "tela":
                factor += 0.1
            elif self.material_tapizado.lower() == "terciopelo":
                factor += 0.25
        
        # Ajuste por capacidad de personas (más personas = más estructura)
        if self.capacidad_personas > 1:
            factor += 0.05 * (self.capacidad_personas - 1)
        
        return factor
    
    def obtener_info_asiento(self) -> str:
        """
        Obtiene información específica del asiento.
        Método concreto auxiliar para las clases hijas.
        
        Returns:
            str: Información detallada del asiento
        """
        # TODO: Implementar retornando información del asiento
        # info = f"Capacidad: {self.capacidad_personas} personas"
        # info += f", Respaldo: {'Sí' if self.tiene_respaldo else 'No'}"
        # if self.material_tapizado:
        #     info += f", Tapizado: {self.material_tapizado}"
        # return info
        info = f"Capacidad: {self.capacidad_personas} personas"
        info += f", Respaldo: {'Sí' if self.tiene_respaldo else 'No'}"
        if self.material_tapizado:
            info += f", Tapizado: {self.material_tapizado}"
        return info
    
    # TODO: Mantener el método calcular_precio como abstracto
    # Las clases concretas deben implementar su propio cálculo
    @abstractmethod
    def calcular_precio(self) -> float:
        """
        Calcula el precio final del asiento.
        Toma en cuenta el precio base, factor de comodidad y otros ajustes.
        Cada tipo de asiento (Silla, Sillón, Sofá) implementará su propia lógica.
        
        Returns:
            float: Precio final calculado
        """
        raise NotImplementedError("Las subclases deben implementar calcular_precio()")
    
    # TODO: Mantener el método obtener_descripcion como abstracto
    # Cada tipo de asiento tendrá su propia descripción
    @abstractmethod
    def obtener_descripcion(self) -> str:
        """
        Obtiene una descripción detallada del asiento.
        Cada tipo de asiento tendrá su propia descripción basada en sus características.
        
        Returns:
            str: Descripción completa del asiento
        """
        raise NotImplementedError("Las subclases deben implementar obtener_descripcion()")

