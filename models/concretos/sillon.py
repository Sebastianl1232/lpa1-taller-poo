"""
Clase concreta Sillón.
Implementa un asiento confortable para una persona.
"""

from ..categorias.asientos import Asiento


class Sillon(Asiento):
    """
    Clase concreta que representa un sillón.
    
    Un sillón es un asiento individual muy confortable con características
    como brazos, inclinación ajustable, etc.
    
    Conceptos OOP aplicados:
    - Herencia: Hereda de Asiento
    - Polimorfismo: Implementa métodos abstractos de manera específica
    - Encapsulación: Protege atributos específicos del sillón
    """
    
    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 tiene_respaldo: bool = True, material_tapizado: str = "tela",
                 tiene_brazos: bool = True, es_reclinable: bool = False,
                 tipo_sillon: str = "confort"):
        """
        Constructor del sillón.
        
        Args:
            tiene_brazos: Si el sillón tiene brazos
            es_reclinable: Si se puede inclinar/recostarse
            tipo_sillon: Tipo de sillón ('confort', 'gamer', 'ejecutivo', etc.)
            Otros argumentos heredados de Asiento
        """
        # Llamar al constructor padre con capacidad fija de 1 persona
        super().__init__(nombre, material, color, precio_base,
                        capacidad_personas=1, tiene_respaldo=tiene_respaldo,
                        material_tapizado=material_tapizado)
        
        self.tiene_brazos = tiene_brazos
        self.es_reclinable = es_reclinable
        self.tipo_sillon = tipo_sillon
    
    @property
    def tiene_brazos(self) -> bool:
        """Getter para verificar si tiene brazos."""
        return self._tiene_brazos
    
    @tiene_brazos.setter
    def tiene_brazos(self, value: bool) -> None:
        """Setter para tiene_brazos con validación."""
        if not isinstance(value, bool):
            raise ValueError("tiene_brazos debe ser un booleano")
        self._tiene_brazos = value
    
    @property
    def es_reclinable(self) -> bool:
        """Getter para verificar si es reclinable."""
        return self._es_reclinable
    
    @es_reclinable.setter
    def es_reclinable(self, value: bool) -> None:
        """Setter para es_reclinable con validación."""
        if not isinstance(value, bool):
            raise ValueError("es_reclinable debe ser un booleano")
        self._es_reclinable = value
    
    @property
    def tipo_sillon(self) -> str:
        """Getter para el tipo de sillón."""
        return self._tipo_sillon
    
    @tipo_sillon.setter
    def tipo_sillon(self, value: str) -> None:
        """Setter para tipo_sillon con validación."""
        tipos_validos = {'confort', 'gamer', 'ejecutivo', 'masaje', 'gaming'}
        if not isinstance(value, str) or value.lower() not in tipos_validos:
            raise ValueError(f"Tipo de sillón no válido. Válidos: {tipos_validos}")
        self._tipo_sillon = value.lower()
    
    def calcular_precio(self) -> float:
        """
        Implementa el cálculo de precio específico para sillones.
        
        Los sillones son más costosos que las sillas por su comodidad.
        
        Extras:
        - tiene_brazos: +75
        - es_reclinable: +150
        - tipo especial (gamer/masaje): +200-300
        
        Returns:
            float: Precio final del sillón
        """
        precio = self.precio_base
        factor_comodidad = self.calcular_factor_comodidad()
        precio *= factor_comodidad
        
        # Extras específicos del sillón
        if self.tiene_brazos:
            precio += 75.0
        
        if self.es_reclinable:
            precio += 150.0
        
        # Sobrecargo por tipo especial
        if self.tipo_sillon == "gamer":
            precio += 300.0
        elif self.tipo_sillon == "masaje":
            precio += 400.0
        elif self.tipo_sillon == "ejecutivo":
            precio += 200.0
        
        return round(precio, 2)
    
    def obtener_descripcion(self) -> str:
        """
        Implementa la descripción específica del sillón.
        
        Returns:
            str: Descripción completa del sillón
        """
        descripcion = f"🪑 SILLÓN: {self.nombre}\n"
        descripcion += f"  Material: {self.material.capitalize()} | Color: {self.color.capitalize()}\n"
        descripcion += f"  {self.obtener_info_asiento()}\n"
        
        caracteristicas = []
        if self.tiene_brazos:
            caracteristicas.append("✓ Brazos")
        if self.es_reclinable:
            caracteristicas.append("✓ Reclinable")
        caracteristicas.append(f"Tipo: {self.tipo_sillon.capitalize()}")
        
        if caracteristicas:
            descripcion += f"  Características: {', '.join(caracteristicas)}\n"
        
        descripcion += f"  Precio: ${self.calcular_precio():.2f}"
        
        return descripcion
    
    def reclinar(self) -> str:
        """Simula la inclinación del sillón."""
        if not self.es_reclinable:
            return f"❌ El sillón '{self.nombre}' no es reclinable."
        return f"✓ El sillón '{self.nombre}' ha sido reclinado."

