# Sistema de Loja Virtual Simplificado

## 📌 Objetivo
Este projeto é um **sistema de loja virtual simplificada**, desenvolvido em **Python**, na disciplina de Programação Orientada a Objetos, ministrada pelo Professor Jayr Pereira, no curso de Engenharia de Software da Universidade Federal do Cariri (UFCA).  O objetivo é aplicar conceitos fundamentais de Engenharia de Software, como encapsulamento, herança, arquitetura em camadas, utilizando **POO**, **persistência em JSON** e uma **Interface de Linha de Comando (CLI)**.

---

## Arquitetura do Projeto

O projeto segue uma arquitetura em camadas, organizada da seguinte forma:

* **Classes (`classes/`)**: representam as entidades do domínio (Produto, Cliente, etc.)
* **Persistência (`persistencia/`)**: responsável por salvar e carregar dados em arquivos JSON
* **Serviços (`servicos/`)**: camada de regras de negócio e coordenação entre modelos e persistência
* **Configurações (`settings/`)**: arquivo central de configurações do sistema
* **CLI (`main.py`)**: interface de interação com o usuário

---

## 📁 Estrutura de Pastas

```
projeto_crud/
│
├── main.py
├── settings.py
├── requirements.txt
│
├── db/
│   ├── clientes.json
│   └── produtos.json
│
└── src/
    ├── __init__.py
    ├── modelos/
    │   ├── __init__.py
    │   ├── cliente.py
    │   ├── endereco.py
    │   ├── produto.py
    │   ├── produto_fisico.py
    │   └── produto_digital.py
    │
    └── persistencia/
        ├── __init__.py
        ├── clientes_repo.py
        └── produtos_repo.py


---

## Principais Funcionalidades

* Cadastro de clientes e múltiplos endereços
* Cadastro de produtos físicos e digitais
* Controle de estoque por produto
* Persistência de dados em arquivos JSON

---

## Conceitos Aplicados

* **POO (Programação Orientada a Objetos)**
* **Herança** (`Produto`, `ProdutoFisico`, `ProdutoDigital`)
* **Encapsulamento** (uso de `@property` para atributos críticos)
* **Persistência sem banco de dados (JSON)**

---

## Como Executar o Projeto

### Pré-requisitos

* Python 3.10 ou superior

### Passos

1. Clone ou extraia o projeto
2. Certifique-se de que os arquivos JSON existem dentro da pasta `dados/`
3. No terminal, execute:

```bash
python main.py
```

4. Utilize o menu interativo no terminal para operar o sistema

---

## 👩‍💻 Autoria

Projeto desenvolvido para fins acadêmicos.
