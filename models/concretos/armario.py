"""
Clase concreta Armario.
Implementa un mueble de almacenamiento para ropa.
"""

from ..categorias.almacenamiento import Almacenamiento


class Armario(Almacenamiento):
    """
    Clase concreta que representa un armario.
    
    Un armario es un mueble de almacenamiento diseñado specifically para
    guardar y organizar ropa y accesorios.
    
    Conceptos OOP aplicados:
    - Herencia: Hereda de Almacenamiento
    - Polimorfismo: Implementa métodos abstractos de manera específica
    - Encapsulación: Protege atributos específicos del armario
    """
    
    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 capacidad_volumen: float = 1500.0, numero_compartimentos: int = 2,
                 tiene_puertas: bool = True, tipo_cierre: str = "bisagra",
                 numero_perchas: int = 20, tiene_espejo: bool = False,
                 tiene_barra_colgar: bool = True):
        """
        Constructor del armario.
        
        Args:
            numero_perchas: Cantidad de perchas para colgar ropa
            tiene_espejo: Si tiene espejo integrado
            tiene_barra_colgar: Si tiene barra para colgar ropa
            Otros argumentos heredados de Almacenamiento
        """
        super().__init__(nombre, material, color, precio_base,
                        capacidad_volumen=capacidad_volumen,
                        numero_compartimentos=numero_compartimentos,
                        tiene_puertas=tiene_puertas,
                        tipo_cierre=tipo_cierre)
        
        self.numero_perchas = numero_perchas
        self.tiene_espejo = tiene_espejo
        self.tiene_barra_colgar = tiene_barra_colgar
    
    @property
    def numero_perchas(self) -> int:
        """Getter para el número de perchas."""
        return self._numero_perchas
    
    @numero_perchas.setter
    def numero_perchas(self, value: int) -> None:
        """Setter para numero_perchas con validación."""
        if not isinstance(value, int) or value < 0:
            raise ValueError("El número de perchas debe ser un número no negativo")
        self._numero_perchas = value
    
    @property
    def tiene_espejo(self) -> bool:
        """Getter para verificar si tiene espejo."""
        return self._tiene_espejo
    
    @tiene_espejo.setter
    def tiene_espejo(self, value: bool) -> None:
        """Setter para tiene_espejo con validación."""
        if not isinstance(value, bool):
            raise ValueError("tiene_espejo debe ser un booleano")
        self._tiene_espejo = value
    
    @property
    def tiene_barra_colgar(self) -> bool:
        """Getter para verificar si tiene barra para colgar."""
        return self._tiene_barra_colgar
    
    @tiene_barra_colgar.setter
    def tiene_barra_colgar(self, value: bool) -> None:
        """Setter para tiene_barra_colgar con validación."""
        if not isinstance(value, bool):
            raise ValueError("tiene_barra_colgar debe ser un booleano")
        self._tiene_barra_colgar = value
    
    def calcular_precio(self) -> float:
        """
        Implementa el cálculo de precio específico para armarios.
        
        Extras:
        - numero_perchas: +5 por cada percha
        - tiene_espejo: +150
        - tiene_barra_colgar: +100
        
        Returns:
            float: Precio final del armario
        """
        precio = self.precio_base
        factor_almacenamiento = self.calcular_factor_almacenamiento()
        precio *= factor_almacenamiento
        
        # Extra por perchas
        precio += self.numero_perchas * 5.0
        
        # Extras específicos
        if self.tiene_espejo:
            precio += 150.0
        
        if self.tiene_barra_colgar:
            precio += 100.0
        
        return round(precio, 2)
    
    def obtener_descripcion(self) -> str:
        """
        Implementa la descripción específica del armario.
        
        Returns:
            str: Descripción completa del armario
        """
        descripcion = f"🚪 ARMARIO: {self.nombre}\n"
        descripcion += f"  Material: {self.material.capitalize()} | Color: {self.color.capitalize()}\n"
        descripcion += f"  {self.obtener_info_almacenamiento()}\n"
        
        caracteristicas = []
        caracteristicas.append(f"Perchas: {self.numero_perchas}")
        if self.tiene_espejo:
            caracteristicas.append("✓ Espejo")
        if self.tiene_barra_colgar:
            caracteristicas.append("✓ Barra para colgar")
        
        if caracteristicas:
            descripcion += f"  Características: {', '.join(caracteristicas)}\n"
        
        descripcion += f"  Precio: ${self.calcular_precio():.2f}"
        
        return descripcion
    
    def colgar_ropa(self, numero_prendas: int = 1) -> str:
        """Simula colgar ropa en el armario."""
        if not self.tiene_barra_colgar:
            return f"❌ El armario '{self.nombre}' no tiene barra para colgar."
        
        if numero_prendas > self.numero_perchas:
            return f"⚠️ No hay suficientes perchas. Máximo: {self.numero_perchas}"
        
        return f"✓ Se han colgado {numero_prendas} prenda(s) en el armario '{self.nombre}'."

