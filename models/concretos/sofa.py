"""
Clase concreta Sofá.
Implementa un mueble de asiento para múltiples personas.
"""

from ..categorias.asientos import Asiento


class Sofa(Asiento):
    """
    Clase concreta que representa un sofá.
    
    Un sofá es un asiento múltiple diseñado para que varias personas se sienten
    o se acuesten cómodamente.
    
    Conceptos OOP aplicados:
    - Herencia: Hereda de Asiento
    - Polimorfismo: Implementa métodos abstractos de manera específica
    - Encapsulación: Protege atributos específicos del sofá
    """
    
    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 capacidad_personas: int = 3, tiene_respaldo: bool = True,
                 material_tapizado: str = "tela", es_cama: bool = False,
                 tiene_chaise: bool = False):
        """
        Constructor del sofá.
        
        Args:
            capacidad_personas: Número de personas que pueden sentarse (mín. 2)
            es_cama: Si el sofá puede convertirse en cama
            tiene_chaise: Si tiene una sección chaise longue
            Otros argumentos heredados de Asiento
        """
        # Validar capacidad mínima
        if capacidad_personas < 2:
            capacidad_personas = 2
        
        super().__init__(nombre, material, color, precio_base,
                        capacidad_personas=capacidad_personas,
                        tiene_respaldo=tiene_respaldo,
                        material_tapizado=material_tapizado)
        
        self.es_cama = es_cama
        self.tiene_chaise = tiene_chaise
    
    @property
    def es_cama(self) -> bool:
        """Getter para verificar si es convertible a cama."""
        return self._es_cama
    
    @es_cama.setter
    def es_cama(self, value: bool) -> None:
        """Setter para es_cama con validación."""
        if not isinstance(value, bool):
            raise ValueError("es_cama debe ser un booleano")
        self._es_cama = value
    
    @property
    def tiene_chaise(self) -> bool:
        """Getter para verificar si tiene chaise longue."""
        return self._tiene_chaise
    
    @tiene_chaise.setter
    def tiene_chaise(self, value: bool) -> None:
        """Setter para tiene_chaise con validación."""
        if not isinstance(value, bool):
            raise ValueError("tiene_chaise debe ser un booleano")
        self._tiene_chaise = value
    
    def calcular_precio(self) -> float:
        """
        Implementa el cálculo de precio específico para sofás.
        
        La capacidad y características especiales incrementan el precio.
        
        Extras:
        - Por cada persona adicional (>2): +150
        - es_cama: +300
        - tiene_chaise: +250
        
        Returns:
            float: Precio final del sofá
        """
        precio = self.precio_base
        factor_comodidad = self.calcular_factor_comodidad()
        precio *= factor_comodidad
        
        # Extra por capacidad adicional
        if self.capacidad_personas > 2:
            precio += 150.0 * (self.capacidad_personas - 2)
        
        # Extras específicos
        if self.es_cama:
            precio += 300.0
        
        if self.tiene_chaise:
            precio += 250.0
        
        return round(precio, 2)
    
    def obtener_descripcion(self) -> str:
        """
        Implementa la descripción específica del sofá.
        
        Returns:
            str: Descripción completa del sofá
        """
        descripcion = f"🛋️ SOFÁ: {self.nombre}\n"
        descripcion += f"  Material: {self.material.capitalize()} | Color: {self.color.capitalize()}\n"
        descripcion += f"  {self.obtener_info_asiento()}\n"
        
        caracteristicas = []
        caracteristicas.append(f"Personas: {self.capacidad_personas}")
        if self.es_cama:
            caracteristicas.append("✓ Convertible a cama")
        if self.tiene_chaise:
            caracteristicas.append("✓ Chaise longue")
        
        if caracteristicas:
            descripcion += f"  Características: {', '.join(caracteristicas)}\n"
        
        descripcion += f"  Precio: ${self.calcular_precio():.2f}"
        
        return descripcion
    
    def convertir_a_cama(self) -> str:
        """Simula la conversión a cama."""
        if not self.es_cama:
            return f"❌ El sofá '{self.nombre}' no es convertible."
        return f"✓ El sofá '{self.nombre}' ha sido convertido a cama."

