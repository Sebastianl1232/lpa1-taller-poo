"""
Clase concreta Cajonera.
Implementa un mueble de almacenamiento con cajones.
"""

from ..categorias.almacenamiento import Almacenamiento


class Cajonera(Almacenamiento):
    """
    Clase concreta que representa una cajonera.
    
    Una cajonera es un mueble de almacenamiento con múltiples cajones
    para organizar objetos pequeños y medianos.
    
    Conceptos OOP aplicados:
    - Herencia: Hereda de Almacenamiento
    - Polimorfismo: Implementa métodos abstractos de manera específica
    - Encapsulación: Protege atributos específicos de la cajonera
    """
    
    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 capacidad_volumen: float = 800.0, numero_compartimentos: int = 4,
                 tiene_puertas: bool = False, tipo_cierre: str = None,
                 profundidad_cajones: float = 40.0, tipo_rieletas: str = "basica"):
        """
        Constructor de la cajonera.
        
        Args:
            profundidad_cajones: Profundidad de los cajones en cm
            tipo_rieletas: Tipo de rieletas ('basica', 'doble', 'telescopica')
            Otros argumentos heredados de Almacenamiento
        """
        # Las cajoneras normalmente no tienen puertas
        super().__init__(nombre, material, color, precio_base,
                        capacidad_volumen=capacidad_volumen,
                        numero_compartimentos=numero_compartimentos,
                        tiene_puertas=False,
                        tipo_cierre=None)
        
        self.profundidad_cajones = profundidad_cajones
        self.tipo_rieletas = tipo_rieletas
    
    @property
    def profundidad_cajones(self) -> float:
        """Getter para la profundidad de los cajones."""
        return self._profundidad_cajones
    
    @profundidad_cajones.setter
    def profundidad_cajones(self, value: float) -> None:
        """Setter para profundidad_cajones con validación."""
        if value <= 0:
            raise ValueError("La profundidad de los cajones debe ser mayor a 0")
        self._profundidad_cajones = float(value)
    
    @property
    def tipo_rieletas(self) -> str:
        """Getter para el tipo de rieletas."""
        return self._tipo_rieletas
    
    @tipo_rieletas.setter
    def tipo_rieletas(self, value: str) -> None:
        """Setter para tipo_rieletas con validación."""
        tipos_validos = {'basica', 'doble', 'telescopica', 'suave'}
        if not isinstance(value, str) or value.lower() not in tipos_validos:
            raise ValueError(f"Tipo de rieletas no válido. Válidos: {tipos_validos}")
        self._tipo_rieletas = value.lower()
    
    def calcular_precio(self) -> float:
        """
        Implementa el cálculo de precio específico para cajoneras.
        
        Extras por rieletas:
        - basica: +0
        - doble: +100
        - telescopica: +200
        - suave: +150
        
        Extras adicionales:
        - Profundidad > 40cm: +50
        
        Returns:
            float: Precio final de la cajonera
        """
        precio = self.precio_base
        factor_almacenamiento = self.calcular_factor_almacenamiento()
        precio *= factor_almacenamiento
        
        # Extra por tipo de rieletas
        rieletas_extras = {
            'basica': 0,
            'doble': 100.0,
            'telescopica': 200.0,
            'suave': 150.0
        }
        precio += rieletas_extras.get(self.tipo_rieletas, 0)
        
        # Extra por profundidad
        if self.profundidad_cajones > 40:
            precio += 50.0
        
        return round(precio, 2)
    
    def obtener_descripcion(self) -> str:
        """
        Implementa la descripción específica de la cajonera.
        
        Returns:
            str: Descripción completa de la cajonera
        """
        descripcion = f"📦 CAJONERA: {self.nombre}\n"
        descripcion += f"  Material: {self.material.capitalize()} | Color: {self.color.capitalize()}\n"
        descripcion += f"  Cajones: {self.numero_compartimentos} | Profundidad: {self.profundidad_cajones}cm\n"
        descripcion += f"  Rieletas: {self.tipo_rieletas.capitalize()}\n"
        
        descripcion += f"  Precio: ${self.calcular_precio():.2f}"
        
        return descripcion
    
    def abrir_cajon(self, numero_cajon: int = 1) -> str:
        """Simula abrir un cajón."""
        if numero_cajon < 1 or numero_cajon > self.numero_compartimentos:
            return f"❌ Cajón inválido. La cajonera tiene {self.numero_compartimentos} cajones."
        
        return f"✓ El cajón {numero_cajon} de la cajonera '{self.nombre}' ha sido abierto."
    
    def utilizar_rieletas(self) -> str:
        """Simula el uso de las rieletas."""
        velocidad = {
            'basica': 'normal',
            'doble': 'suave',
            'telescopica': 'muy suave con extensión completa',
            'suave': 'suave con cierre amortiguado'
        }
        modo = velocidad.get(self.tipo_rieletas, 'normal')
        return f"✓ Las rieletas de la cajonera '{self.nombre}' funcionan con movimiento {modo}."

