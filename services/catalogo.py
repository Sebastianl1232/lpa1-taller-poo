"""
Servicio de catálogo para centralizar la gestión y consulta de items.
Complementa la lógica de negocio de la tienda con operaciones de búsqueda,
filtro, estadísticas y carga masiva en la tienda.
"""

from typing import List, Dict, Union, TYPE_CHECKING

from ..models.mueble import Mueble
from ..models.composicion.comedor import Comedor

if TYPE_CHECKING:
	from .tienda import TiendaMuebles


CatalogoItem = Union[Mueble, Comedor]


class Catalogo:
	"""
	Catálogo de muebles y comedores.

	Conceptos OOP aplicados:
	- Encapsulación: Maneja internamente la colección de items
	- Abstracción: Expone operaciones de alto nivel para consultas
	- Composición: Puede contener muebles individuales y comedores
	"""

	def __init__(self, nombre_catalogo: str = "Catálogo General"):
		self._nombre = nombre_catalogo
		self._items: List[CatalogoItem] = []

	@property
	def nombre(self) -> str:
		"""Getter para el nombre del catálogo."""
		return self._nombre

	@property
	def total_items(self) -> int:
		"""Cantidad total de items en el catálogo."""
		return len(self._items)

	def agregar_item(self, item: CatalogoItem) -> str:
		"""
		Agrega un mueble o comedor al catálogo.
		"""
		if not isinstance(item, (Mueble, Comedor)):
			return "Error: Solo se pueden agregar Mueble o Comedor"

		try:
			precio = self._obtener_precio_item(item)
			if precio <= 0:
				return "Error: El item debe tener un precio mayor a 0"
		except Exception as e:
			return f"Error al validar el item: {str(e)}"

		self._items.append(item)
		return f"Item {item.nombre} agregado al catálogo"

	def quitar_item(self, indice: int = -1) -> str:
		"""
		Quita un item del catálogo por índice.
		"""
		if not self._items:
			return "No hay items en el catálogo para quitar"

		try:
			item_removido = self._items.pop(indice)
			return f"Item {item_removido.nombre} removido del catálogo"
		except IndexError:
			return "Índice de item inválido"

	def obtener_items(self) -> List[CatalogoItem]:
		"""
		Retorna una copia de los items del catálogo.
		"""
		return self._items.copy()

	def buscar_por_nombre(self, nombre: str) -> List[CatalogoItem]:
		"""
		Búsqueda parcial por nombre, sin distinguir mayúsculas.
		"""
		if not nombre or not nombre.strip():
			return []

		nombre_lower = nombre.lower().strip()
		resultados: List[CatalogoItem] = []

		for item in self._items:
			if nombre_lower in item.nombre.lower():
				resultados.append(item)

		return resultados

	def filtrar_por_precio(
		self,
		precio_min: float = 0,
		precio_max: float = float("inf")
	) -> List[CatalogoItem]:
		"""
		Filtra items por rango de precios.
		"""
		if precio_min < 0:
			precio_min = 0

		resultados: List[CatalogoItem] = []
		for item in self._items:
			try:
				precio = self._obtener_precio_item(item)
				if precio_min <= precio <= precio_max:
					resultados.append(item)
			except Exception:
				continue

		return resultados

	def filtrar_por_tipo(self, tipo_clase: type) -> List[CatalogoItem]:
		"""
		Filtra items por clase/tipo concreto.
		"""
		return [item for item in self._items if isinstance(item, tipo_clase)]

	def calcular_valor_total(self) -> float:
		"""
		Calcula el valor total de todos los items del catálogo.
		"""
		valor_total = 0.0
		for item in self._items:
			try:
				valor_total += self._obtener_precio_item(item)
			except Exception:
				continue
		return round(valor_total, 2)

	def obtener_estadisticas(self) -> Dict:
		"""
		Retorna métricas principales del catálogo.
		"""
		return {
			"nombre": self.nombre,
			"total_items": self.total_items,
			"valor_total": self.calcular_valor_total(),
			"conteo_por_tipo": self._contar_tipos_items(),
		}

	def cargar_en_tienda(self, tienda: "TiendaMuebles") -> Dict[str, int]:
		"""
		Carga todos los items del catálogo a una tienda.

		Nota: Se importa TiendaMuebles dentro del método para evitar
		dependencias circulares en importación de módulos.
		"""
		from .tienda import TiendaMuebles

		if not isinstance(tienda, TiendaMuebles):
			return {"muebles": 0, "comedores": 0, "errores": len(self._items)}

		resumen = {"muebles": 0, "comedores": 0, "errores": 0}

		for item in self._items:
			if isinstance(item, Comedor):
				resultado = tienda.agregar_comedor(item)
				if resultado.lower().startswith("error"):
					resumen["errores"] += 1
				else:
					resumen["comedores"] += 1
			else:
				resultado = tienda.agregar_mueble(item)
				if resultado.lower().startswith("error"):
					resumen["errores"] += 1
				else:
					resumen["muebles"] += 1

		return resumen

	def generar_reporte(self) -> str:
		"""
		Genera un reporte legible del catálogo.
		"""
		estadisticas = self.obtener_estadisticas()
		reporte = f"=== REPORTE DE CATÁLOGO - {self.nombre} ===\n\n"
		reporte += f"Total de items: {estadisticas['total_items']}\n"
		reporte += f"Valor total: ${estadisticas['valor_total']:.2f}\n\n"
		reporte += "DISTRIBUCIÓN POR TIPOS:\n"

		for tipo, cantidad in estadisticas["conteo_por_tipo"].items():
			reporte += f"- {tipo}: {cantidad} unidades\n"

		return reporte

	def _obtener_precio_item(self, item: CatalogoItem) -> float:
		"""
		Obtiene el precio de un item de catálogo según su tipo.
		"""
		if isinstance(item, Comedor):
			return item.calcular_precio_total()
		return item.calcular_precio()

	def _contar_tipos_items(self) -> Dict[str, int]:
		"""
		Cuenta cuántos items hay por tipo de clase.
		"""
		conteo: Dict[str, int] = {}
		for item in self._items:
			tipo = type(item).__name__
			conteo[tipo] = conteo.get(tipo, 0) + 1
		return conteo

