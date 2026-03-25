"""
Clase concreta Escritorio.
Implementa una mesa de trabajo específica para oficina.
"""

from ..categorias.superficies import Superficie


class Escritorio(Superficie):
    """
    Clase concreta que representa un escritorio.
    
    Un escritorio es una mesa de trabajo diseñada específicamente para
    trabajar en computadora o tareas que requieran concentración.
    
    Conceptos OOP aplicados:
    - Herencia: Hereda de Superficie
    - Polimorfismo: Implementa métodos abstractos de manera específica
    - Encapsulación: Protege atributos específicos del escritorio
    """
    
    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 forma: str = "rectangular", capacidad_personas: int = 1,
                 alto_cm: float = 75.0, tiene_cajones: bool = True,
                 tiene_organizador: bool = False, es_gamer: bool = False):
        """
        Constructor del escritorio.
        
        Args:
            tiene_cajones: Si tiene cajones para almacenar
            tiene_organizador: Si tiene organizador para cables/accesorios
            es_gamer: Si es un escritorio gaming
            Otros argumentos heredados de Superficie
        """
        super().__init__(nombre, material, color, precio_base,
                        forma=forma, capacidad_personas=capacidad_personas,
                        alto_cm=alto_cm)
        
        self.tiene_cajones = tiene_cajones
        self.tiene_organizador = tiene_organizador
        self.es_gamer = es_gamer
    
    @property
    def tiene_cajones(self) -> bool:
        """Getter para verificar si tiene cajones."""
        return self._tiene_cajones
    
    @tiene_cajones.setter
    def tiene_cajones(self, value: bool) -> None:
        """Setter para tiene_cajones con validación."""
        if not isinstance(value, bool):
            raise ValueError("tiene_cajones debe ser un booleano")
        self._tiene_cajones = value
    
    @property
    def tiene_organizador(self) -> bool:
        """Getter para verificar si tiene organizador."""
        return self._tiene_organizador
    
    @tiene_organizador.setter
    def tiene_organizador(self, value: bool) -> None:
        """Setter para tiene_organizador con validación."""
        if not isinstance(value, bool):
            raise ValueError("tiene_organizador debe ser un booleano")
        self._tiene_organizador = value
    
    @property
    def es_gamer(self) -> bool:
        """Getter para verificar si es gaming."""
        return self._es_gamer
    
    @es_gamer.setter
    def es_gamer(self, value: bool) -> None:
        """Setter para es_gamer con validación."""
        if not isinstance(value, bool):
            raise ValueError("es_gamer debe ser un booleano")
        self._es_gamer = value
    
    def calcular_precio(self) -> float:
        """
        Implementa el cálculo de precio específico para escritorios.
        
        Extras:
        - tiene_cajones: +100
        - tiene_organizador: +80
        - es_gamer: +400 (incluye RGB, metal reforzado, etc.)
        
        Returns:
            float: Precio final del escritorio
        """
        precio = self.precio_base
        factor_superficie = self.calcular_factor_superficie()
        precio *= factor_superficie
        
        # Extras específicos
        if self.tiene_cajones:
            precio += 100.0
        
        if self.tiene_organizador:
            precio += 80.0
        
        if self.es_gamer:
            precio += 400.0
        
        return round(precio, 2)
    
    def obtener_descripcion(self) -> str:
        """
        Implementa la descripción específica del escritorio.
        
        Returns:
            str: Descripción completa del escritorio
        """
        descripcion = f"💼 ESCRITORIO: {self.nombre}\n"
        descripcion += f"  Material: {self.material.capitalize()} | Color: {self.color.capitalize()}\n"
        descripcion += f"  {self.obtener_info_superficie()}\n"
        
        caracteristicas = []
        if self.tiene_cajones:
            caracteristicas.append("✓ Cajones")
        if self.tiene_organizador:
            caracteristicas.append("✓ Organizador")
        if self.es_gamer:
            caracteristicas.append("✓ Gaming")
        
        if caracteristicas:
            descripcion += f"  Características: {', '.join(caracteristicas)}\n"
        
        descripcion += f"  Precio: ${self.calcular_precio():.2f}"
        
        return descripcion
    
    def organizar_cables(self) -> str:
        """Simula la organización de cables."""
        if not self.tiene_organizador:
            return f"❌ El escritorio '{self.nombre}' no tiene organizador."
        return f"✓ Los cables del escritorio '{self.nombre}' han sido organizados."

