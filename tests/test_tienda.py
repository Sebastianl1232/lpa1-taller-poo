"""
Pruebas unitarias para la Tienda.
"""

from services.tienda import TiendaMuebles
from services.catalogo import Catalogo
from models.concretos.silla import Silla
from models.concretos.mesa import Mesa
from models.composicion.comedor import Comedor


class TestTiendaMuebles:
	def setup_method(self):
		self.tienda = TiendaMuebles("Tienda Test")
		self.silla = Silla("Silla Test", "Madera", "Café", 100.0, True)
		self.mesa = Mesa("Mesa Test", "Metal", "Negro", 300.0, "rectangular", 4)

	def test_agregar_y_buscar_mueble(self):
		r1 = self.tienda.agregar_mueble(self.silla)
		r2 = self.tienda.agregar_mueble(self.mesa)
		assert "exitosamente" in r1.lower()
		assert "exitosamente" in r2.lower()

		resultados = self.tienda.buscar_muebles_por_nombre("test")
		assert len(resultados) == 2

	def test_filtros_material_precio_tipo(self):
		self.tienda.agregar_mueble(self.silla)
		self.tienda.agregar_mueble(self.mesa)

		por_material = self.tienda.filtrar_por_material("madera")
		por_precio = self.tienda.filtrar_por_precio(100, 200)
		por_tipo = self.tienda.obtener_muebles_por_tipo(Silla)

		assert len(por_material) == 1
		assert len(por_precio) == 1
		assert len(por_tipo) == 1

	def test_venta_con_descuento(self):
		self.tienda.agregar_mueble(self.silla)
		self.tienda.aplicar_descuento("silla", 10)

		venta = self.tienda.realizar_venta(self.silla, "Ana")
		assert "error" not in venta
		assert venta["cliente"] == "Ana"
		assert venta["descuento"] == 10
		assert venta["precio_final"] < venta["precio_original"]

	def test_estadisticas_y_reporte(self):
		self.tienda.agregar_mueble(self.silla)

		comedor = Comedor("Comedor Test", self.mesa, [self.silla])
		self.tienda.agregar_comedor(comedor)

		stats = self.tienda.obtener_estadisticas()
		reporte = self.tienda.generar_reporte_inventario()

		assert stats["total_muebles"] == 1
		assert stats["total_comedores"] == 1
		assert "REPORTE DE INVENTARIO" in reporte


class TestCatalogo:
	def setup_method(self):
		self.catalogo = Catalogo("Catálogo Test")
		self.tienda = TiendaMuebles("Tienda Cat")
		self.silla = Silla("Silla Cat", "Madera", "Café", 120.0, True)
		self.mesa = Mesa("Mesa Cat", "Metal", "Gris", 250.0, "rectangular", 4)

	def test_agregar_buscar_filtrar(self):
		self.catalogo.agregar_item(self.silla)
		self.catalogo.agregar_item(self.mesa)

		assert self.catalogo.total_items == 2
		assert len(self.catalogo.buscar_por_nombre("cat")) == 2
		assert len(self.catalogo.filtrar_por_tipo(Silla)) == 1

	def test_carga_a_tienda(self):
		self.catalogo.agregar_item(self.silla)
		self.catalogo.agregar_item(self.mesa)

		resumen = self.catalogo.cargar_en_tienda(self.tienda)
		assert resumen["muebles"] == 2
		assert resumen["errores"] == 0
		assert self.tienda.total_muebles == 2
