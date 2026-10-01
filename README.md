# Análise E-commerce Olist

# 🛒 Pipeline de Análise de E-Commerce End-to-End (Olist)

![Data Quality & CI Pipeline](https://github.com/isaqueabednego/analise-olist-ecommerce/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![PowerBI](https://img.shields.io/badge/Power_BI-Dashboard-yellow?logo=powerbi)
![SQLite](https://img.shields.io/badge/SQLite-Database-lightgrey?logo=sqlite)

## 📌 Visão Geral do Projeto
Este projeto consiste no desenvolvimento de um pipeline analítico de dados *end-to-end* focado no ecossistema de e-commerce da Olist. O objetivo principal é extrair, tratar e modelar dados operacionais para transformar registros brutos em relatórios estratégicos e dashboards executivos de apoio à tomada de decisão.

---

## 🛠️ Arquitetura & Tecnologias
* **Linguagem & Bibliotecas:** Python 3.11 (Pandas, SQLite3, Pytest).
* **Banco de Dados:** SQLite (`data/processed/olist.db`).
* **Modelagem Dimensional & BI:** Power BI (Modelagem em Estrela / Star Schema, DAX).
* **Qualidade de Dados & CI/CD:** GitHub Actions (Execução automatizada de testes e pipeline ETL).
* **Governança:** Dicionário de dados semântico padronizado em Excel (`docs/dicionario_dados.xlsx`).

---

## 🏗️ Estrutura do Repositório
```text
analise-olist-ecommerce/
├── .github/workflows/   # Pipeline de CI/CD no GitHub Actions
├── data/                # Dados brutos (raw) e banco SQLite processado
├── docs/                # Dicionário de dados e documentação semântica
├── powerbi/             # Arquivo .pbix do Dashboard executivo
├── sql/                 # Queries analíticas (JOINs, Window Functions, Agregações)
├── src/                 # Scripts Python do pipeline ETL (Extract, Transform, Load)
├── tests/               # Testes unitários e integrados com Pytest
├── README.md            # Documentação técnica do projeto
└── requirements.txt     # Dependências do projeto