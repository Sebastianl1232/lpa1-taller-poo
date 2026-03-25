"""
Clase concreta Cama.
Implementa un mueble de asiento/dormir.
"""

from ..categorias.asientos import Asiento


class Cama(Asiento):
    """
    Clase concreta que representa una cama.
    
    Una cama es un mueble diseñado para dormir con características como
    tipo de colchón, tamaño, etc.
    
    Conceptos OOP aplicados:
    - Herencia: Hereda de Asiento
    - Polimorfismo: Implementa métodos abstractos de manera específica
    - Encapsulación: Protege atributos específicos de la cama
    """
    
    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 capacidad_personas: int = 2, tiene_respaldo: bool = False,
                 material_tapizado: str = None, tamaño_cama: str = "matrimonial",
                 incluye_colchon: bool = True, tipo_estructura: str = "madera"):
        """
        Constructor de la cama.
        
        Args:
            tamaño_cama: Tamaño ('individual', 'matrimonial', 'queen', 'king')
            incluye_colchon: Si incluye colchón en el precio
            tipo_estructura: Tipo de estructura ('madera', 'metal', 'tapizada')
            Otros argumentos heredados de Asiento
        """
        super().__init__(nombre, material, color, precio_base,
                        capacidad_personas=capacidad_personas,
                        tiene_respaldo=tiene_respaldo,
                        material_tapizado=material_tapizado)
        
        self.tamaño_cama = tamaño_cama
        self.incluye_colchon = incluye_colchon
        self.tipo_estructura = tipo_estructura
    
    @property
    def tamaño_cama(self) -> str:
        """Getter para el tamaño de la cama."""
        return self._tamaño_cama
    
    @tamaño_cama.setter
    def tamaño_cama(self, value: str) -> None:
        """Setter para tamaño_cama con validación."""
        tamaños_validos = {'individual', 'matrimonial', 'queen', 'king', 'doble'}
        if not isinstance(value, str) or value.lower() not in tamaños_validos:
            raise ValueError(f"Tamaño no válido. Válidos: {tamaños_validos}")
        self._tamaño_cama = value.lower()
    
    @property
    def incluye_colchon(self) -> bool:
        """Getter para verificar si incluye colchón."""
        return self._incluye_colchon
    
    @incluye_colchon.setter
    def incluye_colchon(self, value: bool) -> None:
        """Setter para incluye_colchon con validación."""
        if not isinstance(value, bool):
            raise ValueError("incluye_colchon debe ser un booleano")
        self._incluye_colchon = value
    
    @property
    def tipo_estructura(self) -> str:
        """Getter para el tipo de estructura."""
        return self._tipo_estructura
    
    @tipo_estructura.setter
    def tipo_estructura(self, value: str) -> None:
        """Setter para tipo_estructura con validación."""
        tipos_validos = {'madera', 'metal', 'tapizada', 'hierro'}
        if not isinstance(value, str) or value.lower() not in tipos_validos:
            raise ValueError(f"Tipo de estructura no válido. Válidos: {tipos_validos}")
        self._tipo_estructura = value.lower()
    
    def calcular_precio(self) -> float:
        """
        Implementa el cálculo de precio específico para camas.
        
        El precio varía bastante según tamaño y características.
        
        Extras por tamaño:
        - individual: +0
        - matrimonial: +200
        - queen: +400
        - king: +600
        
        Extras adicionales:
        - incluye_colchon: +500
        - tipo_estructura especial: +100-200
        
        Returns:
            float: Precio final de la cama
        """
        precio = self.precio_base
        factor_comodidad = self.calcular_factor_comodidad()
        precio *= factor_comodidad
        
        # Extra por tamaño
        tamaño_extras = {
            'individual': 0,
            'matrimonial': 200.0,
            'queen': 400.0,
            'king': 600.0,
            'doble': 200.0
        }
        precio += tamaño_extras.get(self.tamaño_cama, 0)
        
        # Extra por colchón incluido
        if self.incluye_colchon:
            precio += 500.0
        
        # Extra por tipo de estructura
        if self.tipo_estructura == "tapizada":
            precio += 150.0
        elif self.tipo_estructura == "metal":
            precio += 100.0
        
        return round(precio, 2)
    
    def obtener_descripcion(self) -> str:
        """
        Implementa la descripción específica de la cama.
        
        Returns:
            str: Descripción completa de la cama
        """
        descripcion = f"🛏️ CAMA: {self.nombre}\n"
        descripcion += f"  Material: {self.material.capitalize()} | Color: {self.color.capitalize()}\n"
        descripcion += f"  Tamaño: {self.tamaño_cama.capitalize()}\n"
        descripcion += f"  Estructura: {self.tipo_estructura.capitalize()}\n"
        
        caracteristicas = []
        if self.incluye_colchon:
            caracteristicas.append("✓ Con colchón")
        caracteristicas.append(f"Capacidad: {self.capacidad_personas} personas")
        
        if caracteristicas:
            descripcion += f"  Características: {', '.join(caracteristicas)}\n"
        
        descripcion += f"  Precio: ${self.calcular_precio():.2f}"
        
        return descripcion
    
    def cambiar_colchon(self) -> str:
        """Simula el cambio de colchón."""
        return f"✓ El colchón de la cama '{self.nombre}' ha sido cambiado."

