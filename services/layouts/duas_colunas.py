from services.layouts.layout_base import LayoutBase

from services.renderers.tabela_duas_colunas import (
    renderizar_duas_colunas
)


class LayoutDuasColunas(LayoutBase):

    def adicionar_colunas(
        self,
        sidebar,
        corpo
    ):

        self.adicionar(
            renderizar_duas_colunas(
                sidebar,
                corpo
            )
        )