"""
Clase concreta Mesa.
Implementa una mesa para trabajar o comer.
"""

from ..categorias.superficies import Superficie


class Mesa(Superficie):
    """
    Clase concreta que representa una mesa.
    
    Una mesa es una superficie de trabajo o comida con características
    específicas como extensibilidad, número de patas, etc.
    
    Conceptos OOP aplicados:
    - Herencia: Hereda de Superficie
    - Polimorfismo: Implementa métodos abstractos de manera específica
    - Encapsulación: Protege atributos específicos de la mesa
    """
    
    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 forma: str = "rectangular", capacidad_personas: int = 4,
                 alto_cm: float = 75.0, es_extensible: bool = False,
                 numero_patas: int = 4):
        """
        Constructor de la mesa.
        
        Args:
            forma: Forma de la mesa ('rectangular', 'cuadrada', 'redonda', etc.)
            capacidad_personas: Número de personas que pueden comer/trabajar
            alto_cm: Alto de la mesa en centímetros (estándar 75cm)
            es_extensible: Si la mesa puede extenderse
            numero_patas: Número de patas de la mesa
            Otros argumentos heredados de Superficie
        """
        # TODO: Llamar al constructor padre
        super().__init__(nombre, material, color, precio_base,
                        forma=forma, capacidad_personas=capacidad_personas,
                        alto_cm=alto_cm)
        
        # TODO: Inicializar atributos específicos de la mesa
        self.es_extensible = es_extensible
        self.numero_patas = numero_patas
    
    # TODO: Implementar propiedades para los nuevos atributos
    @property
    def es_extensible(self) -> bool:
        """Getter para verificar si es extensible."""
        return self._es_extensible
    
    @es_extensible.setter
    def es_extensible(self, value: bool) -> None:
        """Setter para es_extensible con validación."""
        if not isinstance(value, bool):
            raise ValueError("es_extensible debe ser un booleano")
        self._es_extensible = value
    
    @property
    def numero_patas(self) -> int:
        """Getter para el número de patas."""
        return self._numero_patas
    
    @numero_patas.setter
    def numero_patas(self, value: int) -> None:
        """Setter para numero_patas con validación."""
        if not isinstance(value, int) or value < 1 or value > 8:
            raise ValueError("El número de patas debe estar entre 1 y 8")
        self._numero_patas = value
    
    def calcular_precio(self) -> float:
        """
        Implementa el cálculo de precio específico para mesas.
        
        Fórmula:
        precio = precio_base * factor_superficie + extras
        
        Extras:
        - es_extensible: +200
        - número de patas especial (≠ 4): +50 por pata diferente
        
        Returns:
            float: Precio final de la mesa
        """
        # TODO: Implementar cálculo de precio para mesa

        # 1. Comenzar con el precio base
        precio = self.precio_base
        
        # 2. Aplicar factor de superficie heredado
        factor_superficie = self.calcular_factor_superficie()
        precio *= factor_superficie
        
        # 3. Agregar costos por características especiales
        if self.es_extensible:
            precio += 200.0
        
        # Ajuste por número de patas (distinto de 4, que es estándar)
        if self.numero_patas != 4:
            precio += 50.0 * abs(self.numero_patas - 4)
        
        # 4. Retornar precio redondeado a 2 decimales
        return round(precio, 2)
    
    def obtener_descripcion(self) -> str:
        """
        Implementa la descripción específica de la mesa.
        
        Returns:
            str: Descripción completa de la mesa
        """
        # TODO: Crear y retornar descripción detallada
        
        descripcion = f"🪑 MESA: {self.nombre}\n"
        descripcion += f"  Material: {self.material.capitalize()} | Color: {self.color.capitalize()}\n"
        descripcion += f"  {self.obtener_info_superficie()}\n"
        
        # Agregar características específicas
        caracteristicas = []
        if self.es_extensible:
            caracteristicas.append("✓ Extensible")
        caracteristicas.append(f"Patas: {self.numero_patas}")
        
        if caracteristicas:
            descripcion += f"  Características: {', '.join(caracteristicas)}\n"
        
        descripcion += f"  Precio: ${self.calcular_precio():.2f}"
        
        return descripcion
    
    def extender_mesa(self) -> str:
        """
        Simula la extensión de la mesa.
        Método específico de la clase Mesa.
        
        Returns:
            str: Mensaje del resultado de la operación
        """
        # TODO: Implementar lógica de extensión
        
        if not self.es_extensible:
            return f"❌ La mesa '{self.nombre}' no es extensible."
        
        return f"✓ La mesa '{self.nombre}' ha sido extendida para {self.capacidad_personas + 2} personas."
    
    def es_mesa_comedor(self) -> bool:
        """
        Determina si la mesa es adecuada para comedor.
        
        Una mesa de comedor debe:
        - Tener forma rectangular o ovalada
        - Capacidad para al menos 4 personas
        
        Returns:
            bool: True si es mesa de comedor
        """
        # TODO: Validar que sea mesa de comedor
        
        es_forma_comedor = self.forma in {'rectangular', 'ovalada'}
        es_capacidad_comedor = self.capacidad_personas >= 4
        
        return es_forma_comedor and es_capacidad_comedor

