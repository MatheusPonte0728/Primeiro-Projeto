# 🚀 API de Controle de Clientes e Análise de Crédito

> Uma API RESTful de alta performance desenvolvida com **Python** e **FastAPI** para gestão de cadastro de clientes e controle de limites de crédito.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.95%2B-green)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red)

## 📋 Sobre o Projeto

Este projeto foi desenvolvido para resolver um problema comum em ambientes financeiros e comerciais: o gerenciamento eficiente e seguro de dados de clientes e seus respectivos limites de crédito.

O sistema permite operações de **CRUD** (Create, Read, Update, Delete) completas, garantindo a integridade dos dados através de validações rígidas (como unicidade de CPF e E-mail) e persistência em banco de dados relacional.

### 🎯 Destaques Técnicos
* **Arquitetura Limpa:** Separação clara de responsabilidades entre Modelos (Banco), Schemas (Validação/Pydantic) e Rotas (Controladores).
* **Alta Performance:** Utilização do FastAPI, um dos frameworks mais rápidos do mercado atual.
* **Segurança de Dados:** Uso de ORM (SQLAlchemy) para prevenção de injeção de SQL e Pydantic para tipagem forte de dados.
* **Documentação Automática:** Swagger UI integrado para testes e documentação interativa.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python
* **Framework Web:** FastAPI
* **Banco de Dados:** SQLite (pode ser facilmente migrado para PostgreSQL ou MySQL)
* **ORM:** SQLAlchemy
* **Validação de Dados:** Pydantic
* **Servidor:** Uvicorn

---

## ⚙️ Funcionalidades (Endpoints)

A API disponibiliza os seguintes endpoints:

* `POST /clientes/`: Cadastro de novos clientes com validação de CPF único.
* `GET /clientes/`: Listagem geral da base de clientes.
* `GET /clientes/{id}`: Busca detalhada de um cliente específico.
* `PUT /clientes/{id}`: Atualização de dados cadastrais e **limite de crédito**.
* `DELETE /clientes/{id}`: Remoção segura de registros.

---

## 🚀 Como Rodar o Projeto

Siga os passos abaixo para executar a aplicação em sua máquina local.

### 1. Pré-requisitos
* Python 3.9 ou superior instalado.
* Git instalado.

### 2. Clonar o repositório

```bash
git clone https://github.com/MatheusPonte0728/Primeiro-Projeto
cd api-clientes
