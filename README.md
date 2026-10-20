# ✈️ DataTour Analytics

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)

> **Produto Mínimo Viável (MVP)** desenvolvido como Trabalho de Conclusão de Curso (Projeto Integrador) do **Curso Técnico em Ciência de Dados** do SENAC-DF (Turma 108 • 2026).

## 📖 Sobre o Projeto

O **DataTour Analytics** atua como uma ponte transparente entre os direitos do passageiro e a eficiência operacional das agências de turismo. O objetivo central é utilizar **Engenharia e Ciência de Dados** para estancar a degradação e elevar a confiabilidade dos registros públicos e corporativos de incidentes no setor de turismo.

A aplicação atende a dois perfis principais:
1. **Viajante (B2C):** Ferramentas ágeis para entender seus direitos (ANAC, ANTT, CDC) e gerar rascunhos padronizados de reclamações.
2. **Agência de Turismo (B2B):** Monitoramento corporativo de SLAs e índices de resolução através de dados tratados, validados e consolidados em um modelo dimensional (Star Schema).

---

## 🚀 Principais Funcionalidades

- **🧳 Gerador de Ocorrências Padronizadas:** Formulário inteligente com validação (Regex) que gera relatórios em texto fundamentados em leis, prontos para uso em canais oficiais (Consumidor.gov.br, Procon, etc.).
- **⚖️ FAQ de Direitos do Viajante:** Guia rápido de consulta sobre atrasos de voo, extravio de bagagem, overbooking, problemas com hotéis e locação de veículos.
- **🗺️ Guia do Turista:** Integração embarcada com plataforma de respostas rápidas para destinos no Brasil.
- **🐍 Estatísticas e Qualidade de Dados (Python):** Módulo de Análise Exploratória (EDA) validando a efetividade do pipeline ETL. Traz gráficos gerados dinamicamente em `Matplotlib` mostrando impacto da limpeza de dados, redução de quarentena de falhas e distribuição de outliers.
- **📊 Dashboard Agência (Power BI):** Painel gerencial embarcado diretamente na plataforma web, alimentado por um banco relacional MySQL modelado em *Star Schema*.

---

## 🛠️ Arquitetura e Tecnologias

A solução foi desenhada cobrindo todo o pipeline de dados:

* **Extração e Tratamento (ETL):** `Python` + `Pandas`
* **Validação de Qualidade:** `Great Expectations` + Validações Regex
* **Armazenamento e Modelagem:** `MySQL` (Modelagem Dimensional Star Schema)
* **Análise Exploratória (EDA):** `Matplotlib` + `NumPy`
* **Visualização de Dados (BI):** `Power BI`
* **Interface e Deploy Web:** `Streamlit` + `Streamlit Community Cloud`

---

## 💻 Como rodar o projeto localmente

Siga os passos abaixo para testar a interface do projeto na sua máquina:

1. Clone o repositório:
```bash
git clone https://github.com/SEU_USUARIO/datatour-analytics.git
cd datatour-analytics
```

2. Crie e ative um ambiente virtual (opcional, mas recomendado):
```bash
python -m venv .venv
# No Windows:
.venv\Scripts\activate
# No Linux/Mac:
source .venv/bin/activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Execute a aplicação:
```bash
streamlit run app.py
```

---

## 🎓 Equipe Técnica — Turma 108

* **Bárbara Cavalcanti**
* **Cláudia Santos**
* **Daiana Ribeiro**
* **Evanildo Silva**
* **Luis Eduardo Sousa**

### 👨‍🏫 Orientação
Agradecimento especial aos professores e instrutores **Diego Lohan** e **Cleiton Sousa** (SENAC-DF) por toda a base técnica e apoio ao longo da formação.
