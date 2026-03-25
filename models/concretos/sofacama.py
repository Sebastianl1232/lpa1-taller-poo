"""
Clase SofaCama que implementa herencia múltiple.
Esta clase hereda tanto de Sofa como de Cama.
"""

# TODO: Importar las clases padre
# from .sofa import Sofa
from .sofa import Sofa
# from .cama import Cama
from .cama import Cama

class SofaCama(Sofa, Cama):
    """
    Clase que implementa herencia múltiple heredando de Sofa y Cama.
    
    Un sofá-cama es un mueble que funciona tanto como asiento durante el día
    como cama durante la noche.
    
    Conceptos OOP aplicados:
    - Herencia múltiple: Hereda de Sofa y Cama
    - Resolución MRO: Maneja el orden de resolución de métodos
    - Polimorfismo: Implementa comportamientos únicos combinando funcionalidades
    - Super(): Usa super() para resolver conflictos de herencia
    
    MRO (Method Resolution Order):
    SofaCama -> Sofa -> Cama -> Asiento -> Mueble -> ABC -> object
    """
    
    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 capacidad_personas: int = 3, material_tapizado: str = "tela",
                 tamaño_cama: str = "matrimonial", incluye_colchon: bool = True,
                 mecanismo_conversion: str = "plegable"):
        """
        Constructor del sofá-cama.
        
        Args:
            mecanismo_conversion: Tipo de mecanismo de conversión (plegable, extensible, etc.)
            Otros argumentos se pasan a las clases padre
        """
        # TODO: Inicializar usando las clases padre
        # Nota: En herencia múltiple, solo se llama super().__init__ una vez
        # Esto llama al primer padre en el MRO (Method Resolution Order)
        # Super llama a Sofa, que internamente llama a Cama a través del MRO
        super().__init__(nombre, material, color, precio_base, 
                        capacidad_personas=capacidad_personas, 
                        tiene_respaldo=True,
                        material_tapizado=material_tapizado,
                        es_cama=True,
                        tiene_chaise=False)
        
        # TODO: Inicializar atributos específicos de cama
        # Necesitamos configurar manualmente los atributos de Cama ya que solo se llama un __init__
        self._tamaño_cama = tamaño_cama
        self._incluye_colchon = incluye_colchon
        self._tipo_estructura = "tapizada"  # Los sofá-cama son siempre tapizados
        
        # TODO: Inicializar atributos únicos del sofá-cama
        self._mecanismo_conversion = mecanismo_conversion
        self._modo_actual = "sofa"  # Puede ser "sofa" o "cama"
    
    @property
    def tamaño_cama(self) -> str:
        """Getter para el tamaño de cama (heredado de Cama)."""
        return self._tamaño_cama
    
    @tamaño_cama.setter
    def tamaño_cama(self, value: str) -> None:
        """Setter para tamaño_cama (usa validación de Cama)."""
        tamaños_validos = {'individual', 'matrimonial', 'queen', 'king', 'doble'}
        if not isinstance(value, str) or value.lower() not in tamaños_validos:
            raise ValueError(f"Tamaño no válido. Válidos: {tamaños_validos}")
        self._tamaño_cama = value.lower()
    
    @property
    def incluye_colchon(self) -> bool:
        """Getter para incluye_colchon (heredado de Cama)."""
        return self._incluye_colchon
    
    @incluye_colchon.setter
    def incluye_colchon(self, value: bool) -> None:
        """Setter para incluye_colchon con validación."""
        if not isinstance(value, bool):
            raise ValueError("incluye_colchon debe ser un booleano")
        self._incluye_colchon = value
    
    @property
    def mecanismo_conversion(self) -> str:
        """Getter para el mecanismo de conversión."""
        return self._mecanismo_conversion
    
    @mecanismo_conversion.setter
    def mecanismo_conversion(self, value: str) -> None:
        """Setter para mecanismo_conversion con validación."""
        mecanismos_validos = {'plegable', 'extensible', 'giratorio', 'telescopico'}
        if not isinstance(value, str) or value.lower() not in mecanismos_validos:
            raise ValueError(f"Mecanismo no válido. Válidos: {mecanismos_validos}")
        self._mecanismo_conversion = value.lower()
    
    @property
    def modo_actual(self) -> str:
        """Getter para el modo actual."""
        return self._modo_actual
    
    def calcular_precio(self) -> float:
        """
        Implementa el cálculo de precio combinando lógica de Sofa y Cama.
        
        El sofá-cama es más caro porque combina funcionalidades de ambos.
        
        Precio = (precio_sofa + precio_cama) / 2 + sobrecargo mecanismo
        
        Sobrecargo por mecanismo:
        - plegable: +100
        - extensible: +150
        - giratorio: +300
        - telescopico: +250
        
        Returns:
            float: Precio final del sofá-cama
        """
        # Calcular precio base como promedio de Sofa y Cama
        precio = self.precio_base
        factor_sofa = self.calcular_factor_comodidad()  # Factor de Asiento (ambos heredan)
        
        # Precio como sofá: base × factor + extras de personas
        precio_sofa = precio * factor_sofa
        if self.capacidad_personas > 2:
            precio_sofa += 150.0 * (self.capacidad_personas - 2)
        
        # Precio como cama con colchón
        precio_cama = precio * factor_sofa
        if self.incluye_colchon:
            precio_cama += 500.0
        
        # Combinar precios (promedio más sobrecargo)
        precio_final = (precio_sofa + precio_cama) / 2
        
        # Sobrecargo por mecanismo especial
        mecanismo_extras = {
            'plegable': 100.0,
            'extensible': 150.0,
            'giratorio': 300.0,
            'telescopico': 250.0
        }
        precio_final += mecanismo_extras.get(self.mecanismo_conversion, 0)
        
        # Bonus por funcionalidad dual
        precio_final *= 1.15  # +15% por ser dos muebles en uno
        
        return round(precio_final, 2)
    
    def obtener_descripcion(self) -> str:
        """
        Implementa la descripción combinando info de Sofa y Cama.
        
        Returns:
            str: Descripción completa del sofá-cama
        """
        descripcion = f"🛋️↔️🛏️ SOFÁ-CAMA: {self.nombre}\n"
        descripcion += f"  Material: {self.material.capitalize()} | Color: {self.color.capitalize()}\n"
        descripcion += f"\n  📍 COMO SOFÁ:\n"
        descripcion += f"    Capacidad: {self.capacidad_personas} personas\n"
        descripcion += f"    Respaldo: {'Sí' if self.tiene_respaldo else 'No'}\n"
        
        if self.material_tapizado:
            descripcion += f"    Tapizado: {self.material_tapizado}\n"
        
        descripcion += f"\n  📍 COMO CAMA:\n"
        descripcion += f"    Tamaño: {self.tamaño_cama.capitalize()}\n"
        descripcion += f"    Colchón: {'Incluido' if self.incluye_colchon else 'No incluido'}\n"
        descripcion += f"    Mecanismo: {self.mecanismo_conversion.capitalize()}\n"
        
        descripcion += f"\n  Modo actual: {self.modo_actual.upper()}\n"
        descripcion += f"  Precio: ${self.calcular_precio():.2f}"
        
        return descripcion
    
    def convertir_a_cama(self) -> str:
        """
        Convierte el sofá-cama a modo cama.
        
        Returns:
            str: Mensaje del resultado de la operación
        """
        if self.modo_actual == "cama":
            return f"⚠️ El sofá-cama '{self.nombre}' ya está en modo cama."
        
        self._modo_actual = "cama"
        return f"✓ El sofá-cama '{self.nombre}' ha sido convertido a cama ({self.tamaño_cama.capitalize()})."
    
    def convertir_a_sofa(self) -> str:
        """
        Convierte el sofá-cama a modo sofá.
        
        Returns:
            str: Mensaje del resultado de la operación
        """
        if self.modo_actual == "sofa":
            return f"⚠️ El sofá-cama '{self.nombre}' ya está en modo sofá."
        
        self._modo_actual = "sofa"
        return f"✓ El sofá-cama '{self.nombre}' ha sido convertida a sofá ({self.capacidad_personas} personas)."
    
    def obtener_capacidad_total(self) -> dict:
        """
        Retorna las capacidades en ambos modos.
        
        Returns:
            dict: Diccionario con capacidades como sofá y cama
        """
        return {
            "modo_sofa": f"{self.capacidad_personas} personas",
            "modo_cama": f"Cama {self.tamaño_cama.capitalize()}"
        }

    
    # TODO: Implementar propiedades para los nuevos atributos
    # @property
    # def mecanismo_conversion(self) -> str:
    #     """Getter para el mecanismo de conversión."""
    #     return self._mecanismo_conversion
    
    # @property
    # def modo_actual(self) -> str:
    #     """Getter para el modo actual (sofa o cama)."""
    #     return self._modo_actual
    
    def convertir_a_cama(self) -> str:
        """
        Convierte el sofá en cama.
        Método específico del sofá-cama.
        
        Returns:
            str: Mensaje del resultado de la conversión
        """
        # TODO: Implementar lógica de conversión
        # if self._modo_actual == "cama":
        #     return "El sofá-cama ya está en modo cama"
        
        # self._modo_actual = "cama"
        # return f"Sofá convertido a cama usando mecanismo {self.mecanismo_conversion}"
        pass
    
    def convertir_a_sofa(self) -> str:
        """
        Convierte la cama en sofá.
        Método específico del sofá-cama.
        
        Returns:
            str: Mensaje del resultado de la conversión
        """
        # TODO: Implementar lógica de conversión
        # if self._modo_actual == "sofa":
        #     return "El sofá-cama ya está en modo sofá"
        
        # self._modo_actual = "sofa"
        # return f"Cama convertida a sofá usando mecanismo {self.mecanismo_conversion}"
        pass
    
    def calcular_precio(self) -> float:
        """
        Calcula el precio combinando las funcionalidades de sofá y cama.
        
        Returns:
            float: Precio final del sofá-cama
        """
        # TODO: Implementar cálculo de precio combinado
        # El sofá-cama es más caro que un sofá o cama individual
        # 1. Comenzar con precio base
        # precio = self.precio_base
        
        # 2. Aplicar factor de comodidad de asiento
        # precio *= self.calcular_factor_comodidad()
        
        # 3. Agregar valor por funcionalidad dual
        # precio *= 1.5  # 50% más caro por ser dual
        
        # 4. Agregar costo por mecanismo de conversión
        # if self.mecanismo_conversion == "electrico":
        #     precio += 200
        # elif self.mecanismo_conversion == "hidraulico":
        #     precio += 150
        # else:  # manual/plegable
        #     precio += 100
        
        # 5. Agregar costo si incluye colchón
        # if self.incluye_colchon:
        #     precio += 300
        
        # return round(precio, 2)
        pass
    
    def obtener_descripcion(self) -> str:
        """
        Descripción que combina características de sofá y cama.
        
        Returns:
            str: Descripción completa del sofá-cama
        """
        # TODO: Crear descripción combinada
        # descripcion = f"Sofá-cama {self.nombre} fabricado en {self.material} color {self.color}."
        # descripcion += f"\n{self.obtener_info_asiento()}"
        # descripcion += f"\nTamaño de cama: {self.tamaño_cama}"
        # descripcion += f"\nMecanismo de conversión: {self.mecanismo_conversion}"
        # descripcion += f"\nColchón incluido: {'Sí' if self.incluye_colchon else 'No'}"
        # descripcion += f"\nModo actual: {self.modo_actual}"
        # descripcion += f"\nPrecio: ${self.calcular_precio():.2f}"
        # return descripcion
        pass
    
    def obtener_capacidad_total(self) -> dict:
        """
        Obtiene la capacidad tanto como sofá como cama.
        Método único del sofá-cama.
        
        Returns:
            dict: Capacidades en ambos modos
        """
        # TODO: Implementar capacidades
        # capacidades = {
        #     "como_sofa": self.capacidad_personas,
        #     "como_cama": 2 if self.tamaño_cama in ["matrimonial", "queen", "king"] else 1
        # }
        # return capacidades
        pass
    
    # TODO: Implementar método para verificar compatibilidad de modo
    # def puede_usar_como_cama(self) -> bool:
    #     """Verifica si actualmente puede usarse como cama."""
    #     return self._modo_actual == "cama"
    
    # def puede_usar_como_sofa(self) -> bool:
    #     """Verifica si actualmente puede usarse como sofá."""
    #     return self._modo_actual == "sofa"
    
    def __str__(self) -> str:
        """
        Representación en cadena del sofá-cama.
        Sobrescribe el método heredado para mostrar información específica.
        """
        # TODO: Implementar representación personalizada
        # return f"Sofá-cama {self.nombre} (modo: {self.modo_actual})"
        pass

