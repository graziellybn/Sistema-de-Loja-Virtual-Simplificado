class Endereco:
    def __init__(self, rua: str,  numero: str, bairro: str, cidade: str, cep: str, estado: str, complemento: str = ""):
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.cep = cep
        self.complemento = complemento

    def to_dict(self) -> dict:
        return {
            "rua": self.rua,
            "numero": self.numero,
            "bairro": self.bairro,
            "cidade": self.cidade,
            "estado": self.estado,
            "cep": self.cep,
            "complemento": self.complemento
        }
        

    @staticmethod
    def from_dict(dados: dict) -> "Endereco":
        return Endereco(
            rua=dados["rua"],
            numero=dados["numero"],
            bairro=dados["bairro"],
            cidade=dados["cidade"],
            estado=dados["estado"],
            cep=dados["cep"]
            complemento=dados.get("complemento", "")
        )

    def __repr__(self) -> str:
        return (
            f"Endereco(rua='{self.rua}', numero='{self.numero}', "
            f"bairro='{self.bairro}', cidade='{self.cidade}', "
            f"estado='{self.estado}', cep='{self.cep}')"
            f"complemento='{self.complemento}')"
