"""
Clase concreta Silla.
Implementa un mueble de asiento específico para una persona.
"""

# TODO: Importar la clase padre Asiento
# from ..categorias.asientos import Asiento
from categorias.asientos import Asiento


class Silla(Asiento):
    """
    Clase concreta que representa una silla.
    
    Una silla es un asiento individual con características específicas
    como altura regulable, ruedas, etc.
    
    Conceptos OOP aplicados:
    - Herencia: Hereda de Asiento
    - Polimorfismo: Implementa métodos abstractos de manera específica
    - Encapsulación: Protege atributos específicos de la silla
    """
    
    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 tiene_respaldo: bool = True, material_tapizado: str = None,
                 altura_regulable: bool = False, tiene_ruedas: bool = False):
        """
        Constructor de la silla.
        
        Args:
            altura_regulable: Si la silla puede regular su altura
            tiene_ruedas: Si la silla tiene ruedas
            Otros argumentos heredados de Asiento
        """
        # TODO: Llamar al constructor padre con capacidad fija de 1 persona
        # Una silla siempre es para 1 persona
        super().__init__(nombre, material, color, precio_base, 
                         capacidad_personas=1, tiene_respaldo=tiene_respaldo, 
                         material_tapizado=material_tapizado)
        
        # TODO: Inicializar atributos específicos de la silla
        self.altura_regulable = altura_regulable
        self.tiene_ruedas = tiene_ruedas
    
    # TODO: Implementar propiedades para los nuevos atributos
    # @property
    # def altura_regulable(self) -> bool:
    #     """Getter para altura regulable."""
    #     return self._altura_regulable
    
    # @altura_regulable.setter
    # def altura_regulable(self, value: bool) -> None:
    #     """Setter para altura regulable."""
    #     self._altura_regulable = value
    @property
    def altura_regulable(self) -> bool:
        """Getter para altura regulable."""
        return self._altura_regulable
    
    @altura_regulable.setter
    def altura_regulable(self, value: bool) -> None:
        """Setter para altura regulable con validación."""
        if not isinstance(value, bool):
            raise ValueError("altura_regulable debe ser un booleano")
        self._altura_regulable = value
    
    @property
    def tiene_ruedas(self) -> bool:
        """Getter para verificar si tiene ruedas."""
        return self._tiene_ruedas
    
    @tiene_ruedas.setter
    def tiene_ruedas(self, value: bool) -> None:
        """Setter para tiene_ruedas con validación."""
        if not isinstance(value, bool):
            raise ValueError("tiene_ruedas debe ser un booleano")
        self._tiene_ruedas = value
    
    def calcular_precio(self) -> float:
        """
        Implementa el cálculo de precio específico para sillas.
        
        Fórmula:
        precio = precio_base * factor_comodidad + extras
        
        Extras:
        - altura_regulable: +50
        - tiene_ruedas: +100
        
        Returns:
            float: Precio final de la silla
        """
        # TODO: Implementar cálculo de precio para silla

        # 1. Comenzar con el precio base
        precio = self.precio_base
        
        # 2. Aplicar factor de comodidad heredado (de la clase Asiento)
        factor_comodidad = self.calcular_factor_comodidad()
        precio *= factor_comodidad
        
        # 3. Agregar costos por características especiales
        if self.altura_regulable:
            precio += 50.0
        
        if self.tiene_ruedas:
            precio += 100.0
        
        # 4. Retornar precio redondeado a 2 decimales
        return round(precio, 2)
    
    def obtener_descripcion(self) -> str:
        """
        Implementa la descripción específica de la silla.
        
        Retorna información completa incluyendo:
        - Nombre y tipo de mueble
        - Material y color
        - Características de asiento (respaldo, tapizado)
        - Características específicas (altura regulable, ruedas)
        - Precio
        
        Returns:
            str: Descripción completa de la silla
        """
        # TODO: Crear y retornar descripción detallada
        
        descripcion = f"🪑 SILLA: {self.nombre}\n"
        descripcion += f"  Material: {self.material.capitalize()} | Color: {self.color.capitalize()}\n"
        descripcion += f"  {self.obtener_info_asiento()}\n"
        
        # Agregar características específicas
        caracteristicas = []
        if self.altura_regulable:
            caracteristicas.append("✓ Altura regulable")
        if self.tiene_ruedas:
            caracteristicas.append("✓ Ruedas")
        
        if caracteristicas:
            descripcion += f"  Características: {', '.join(caracteristicas)}\n"
        
        descripcion += f"  Precio: ${self.calcular_precio():.2f}"
        
        return descripcion
    
    def regular_altura(self, nueva_altura: int) -> str:
        """
        Simula la regulación de altura de la silla.
        Método específico de la clase Silla.
        
        Solo funciona si altura_regulable es True.
        La altura debe estar entre 30 y 60 cm.
        
        Args:
            nueva_altura: Nueva altura en centímetros
            
        Returns:
            str: Mensaje del resultado de la operación
        """
        # TODO: Implementar lógica de regulación
        
        # Validar que la silla tenga altura regulable
        if not self.altura_regulable:
            return f"❌ La silla '{self.nombre}' no tiene altura regulable."
        
        # Validar rango de altura
        if not isinstance(nueva_altura, int) or nueva_altura < 30 or nueva_altura > 60:
            return "❌ Altura inválida. Debe estar entre 30 y 60 cm."
        
        # Si todo es válido, simular la regulación
        return f"✓ La silla '{self.nombre}' ha sido regulada a {nueva_altura}cm de altura."
    
    def es_silla_oficina(self) -> bool:
        """
        Determina si la silla es adecuada para oficina.
        
        Una silla de oficina debe tener:
        - Ruedas (para moverse fácilmente)
        - Altura regulable (para ajustarse al escritorio)
        
        Returns:
            bool: True si es silla de oficina, False en caso contrario
        """
        # TODO: Una silla es de oficina si tiene ruedas Y altura regulable
        return self.tiene_ruedas and self.altura_regulable

