"""
Pruebas unitarias para las clases de composición.
"""

import pytest

from models.concretos.mesa import Mesa
from models.concretos.silla import Silla
from models.composicion.comedor import Comedor


class TestComposicionComedor:
	def setup_method(self):
		self.mesa = Mesa("Mesa Composición", "Madera", "Roble", 400.0, "rectangular", 6)
		self.silla_1 = Silla("Silla A", "Madera", "Roble", 100.0, True)
		self.silla_2 = Silla("Silla B", "Madera", "Roble", 100.0, True)
		self.comedor = Comedor("Set Comedor", self.mesa, [self.silla_1, self.silla_2])

	def test_comedor_contiene_componentes(self):
		assert self.comedor.mesa is self.mesa
		assert len(self.comedor.sillas) == 2

	def test_agregar_y_quitar_silla(self):
		nueva = Silla("Silla C", "Madera", "Roble", 100.0, True)
		agregado = self.comedor.agregar_silla(nueva)
		assert "agregada" in agregado.lower()
		assert len(self.comedor.sillas) == 3

		removido = self.comedor.quitar_silla()
		assert "removida" in removido.lower()
		assert len(self.comedor.sillas) == 2

	def test_precio_total_y_len(self):
		total = self.comedor.calcular_precio_total()
		assert total > 0
		assert len(self.comedor) == 3

	def test_descuento_set_completo(self):
		self.comedor.agregar_silla(Silla("Silla C", "Madera", "Roble", 100.0, True))
		self.comedor.agregar_silla(Silla("Silla D", "Madera", "Roble", 100.0, True))

		subtotal = self.mesa.calcular_precio() + sum(s.calcular_precio() for s in self.comedor.sillas)
		total = self.comedor.calcular_precio_total()
		assert total == pytest.approx(round(subtotal * 0.95, 2))

	def test_resumen_y_materiales(self):
		resumen = self.comedor.obtener_resumen()
		assert resumen["nombre"] == "Set Comedor"
		assert resumen["total_muebles"] == len(self.comedor)
		assert "Madera" in resumen["materiales_utilizados"]
