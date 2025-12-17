class Cliente:
    def __init__(self, cpf: str, nome: str, email: str, telefone: str):
        self.cpf = cpf
        self.nome = nome
        self.email = email
        self.telefone = telefone

    def to_dict(self) -> dict:
        return {
            "cpf": self.cpf,
            "nome": self.nome,
            "email": self.email,
            "telefone": self.telefone
        }

    @staticmethod
    def from_dict(dados: dict) -> "Cliente":
        return Cliente(
            cpf=dados["cpf"],
            nome=dados["nome"],
            email=dados["email"],
            telefone=dados["telefone"]
        )

    def __repr__(self) -> str:
        return (
            f"Cliente(cpf='{self.cpf}', "
            f"nome='{self.nome}', "
            f"email='{self.email}', "
            f"telefone='{self.telefone}')"
        )
