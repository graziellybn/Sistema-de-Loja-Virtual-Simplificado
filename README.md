# Sistema de Loja Virtual Simplificado

## 📌 Objetivo
Este projeto é um **sistema de loja virtual simplificada**, desenvolvido em **Python**, na disciplina de Programação Orientada a Objetos, ministrada pelo Professor Jayr Pereira, no curso de Engenharia de Software da Universidade Federal do Cariri (UFCA).  O objetivo é aplicar conceitos fundamentais de Engenharia de Software, como encapsulamento, herança, arquitetura em camadas, utilizando **POO**, **persistência em JSON** e uma **Interface de Linha de Comando (CLI)**.

---

## Arquitetura do Projeto

O projeto segue uma arquitetura em camadas, organizada da seguinte forma:

* **Modelos (`modelos/`)**: representam as entidades do domínio (Produto, Cliente, Pedido etc.)
* **Persistência (`persistencia/`)**: responsável por salvar e carregar dados em arquivos JSON
* **Serviços (`servicos/`)**: camada de regras de negócio e coordenação entre modelos e persistência
* **Configurações (`config/`)**: arquivo central de configurações do sistema
* **CLI (`main.py`)**: interface de interação com o usuário

Essa separação garante um código organizado, reutilizável e fácil de manter.

---

## 📁 Estrutura de Pastas

```
projeto_loja/
│
├── main.py
├── requirements.txt
├── settings.txt
├── dados/
│   ├── produtos.json
│   ├── clientes.json
│   ├── pedidos.json
│   └── pagamentos.json
│
└── src/
    ├── classes/
    │   ├── produto.py
    │   ├── produto_fisico.py
    │   ├── produto_digital.py
    │   ├── cliente.py
    │   ├── endereco.py
    │   ├── carrinho.py
    │   ├── item_carrinho.py
    │   ├── pedido.py
    │   ├── item_pedido.py
    │   ├── pagamento.py
    │   └── frete.py
    │
    ├── persistencia/
    │   ├── repositorio_produtos.py
    │   ├── repositorio_clientes.py
    │   ├── repositorio_pedidos.py
    │   └── repositorio_pagamentos.py
    │
    └── servicos/
        ├── servico_produtos.py
        ├── servico_clientes.py
        ├── servico_carrinho.py
        ├── servico_pedidos.py
        ├── servico_pagamentos.py
        └── servico_frete.py
```

---

## Principais Funcionalidades

* Cadastro de clientes e múltiplos endereços
* Cadastro de produtos físicos e digitais
* Controle de estoque por produto
* Criação de carrinho de compras
* Geração de pedidos a partir do carrinho
* Cálculo de frete para produtos físicos
* Processamento de pagamento
* Persistência de dados em arquivos JSON

---

## Conceitos Aplicados

* **POO (Programação Orientada a Objetos)**
* **Herança** (`Produto`, `ProdutoFisico`, `ProdutoDigital`)
* **Encapsulamento** (uso de `@property` para atributos críticos)
* **Responsabilidade Única (SRP)**
* **Separação de Camadas**
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
