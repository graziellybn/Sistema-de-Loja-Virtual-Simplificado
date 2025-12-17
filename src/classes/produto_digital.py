from src.classes.produto import Produto

class ProdutoDigital(Produto):
    def __init__(self, sku: str, nome: str, categoria: str, preco: float, estoque: int, tamanho_arquivo: float):
        super().__init__(sku, nome, categoria, preco, estoque)
        self.tamanho_arquivo = tamanho_arquivo

    def to_dict(self) -> dict:
        dados = super().to_dict()
        dados["tamanho_arquivo"] = self.tamanho_arquivo
        dados["tipo"] = "digital"
        return dados

    @staticmethod
    def from_dict(dados: dict) -> "ProdutoDigital":
        return ProdutoDigital(
            sku=dados["sku"],
            nome=dados["nome"],
            categoria=dados["categoria"],
            preco=dados["preco"],
            estoque=dados["estoque"],
            tamanho_arquivo=dados["tamanho_arquivo"]
        )

    def __repr__(self) -> str:
        return (
            f"ProdutoDigital(sku='{self.sku}', nome='{self.nome}', "
            f"preco={self.preco}, estoque={self.estoque}, "
            f"tamanho_arquivo={self.tamanho_arquivo})"
        )
