class Produto:
    def __init__(self, sku: str, nome: str, categoria: str, preco: float, estoque: int):
        self.sku = sku
        self.nome = nome
        self.categoria = categoria
        self.preco = preco
        self.estoque = estoque

    def to_dict(self) -> dict:
        return {
            "sku": self.sku,
            "nome": self.nome,
            "categoria": self.categoria,
            "preco": self.preco,
            "estoque": self.estoque,
            "tipo": "produto"
        }

    @staticmethod
    def from_dict(dados: dict) -> "Produto":
        return Produto(
            sku=dados["sku"],
            nome=dados["nome"],
            categoria=dados["categoria"],
            preco=dados["preco"],
            estoque=dados["estoque"]
        )

    def __repr__(self) -> str:
        return (
            f"Produto(sku='{self.sku}', nome='{self.nome}', "
            f"categoria='{self.categoria}', preco={self.preco}, "
            f"estoque={self.estoque})"
        )
