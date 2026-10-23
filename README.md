# 💼 Consultor Inteligente de Carreiras em TI
### Sistema Especialista Baseado em Regras com Encadeamento para Frente (*Forward Chaining*)

Trabalho prático desenvolvido para a disciplina de **Inteligência Artificial** do curso de **Ciência da Computação** no **Centro Universitário Presidente Antônio Carlos (UNIPAC Barbacena)**.
**Professor:** Felipe Roncalli de Paula Carneiro

---

## 📌 1. Visão Geral do Projeto

O mercado de tecnologia da informação é dinâmico, multifacetado e repleto de ramificações, gerando dúvidas frequentes em estudantes e profissionais sobre qual carreira seguir. 

O **Consultor Inteligente de Carreiras em TI** é uma aplicação de **Inteligência Artificial Simbólica** que atua como um conselheiro vocacional técnico. O sistema conduz uma entrevista dinâmica e estruturada por meio de 12 perguntas objetivas, avalia o perfil do usuário utilizando um **motor de inferência baseado em regras (biblioteca Experta)** com encadeamento para frente e diagnostica a trilha profissional mais adequada dentre **10 opções possíveis**, justificando formalmente sua conclusão com base nas regras disparadas.

---

## 🧭 2. As 10 Trilhas de Carreira

O sistema diferencia com rigor conceitual e recomenda precisamente uma das seguintes carreiras:

1. **Desenvolvimento Back-end (`back_end`):** Foco em lógica de servidores, construção de APIs REST/GraphQL, microsserviços, regras de negócio e bancos de dados transacionais.
2. **Desenvolvimento Front-end & UI/UX (`front_end`):** Foco em interfaces web responsivas, componentes reativos, ergonomia visual e experiência do usuário no navegador.
3. **Ciência de Dados e Machine Learning (`ciencia_dados`):** Foco em estatística, probabilidade, modelagem preditiva, análise exploratória de massas de dados e inteligência artificial.
4. **Engenharia de Dados (`eng_dados`):** Foco em arquitetura de dados, esteiras de ETL/ELT distribuídas, governança e sustentação de Data Lakes e Data Warehouses.
5. **Cibersegurança / Pentesting (`ciberseguranca`):** Foco em defesa cibernética, testes de invasão ética, análise de vulnerabilidades, criptografia e segurança de redes.
6. **DevOps & SRE (`devops`):** Foco em automação de processos, integração e entrega contínua (CI/CD), contêineres Docker/Kubernetes e observabilidade operacional.
7. **Computação em Nuvem / Cloud Architecture (`cloud`):** Foco em planejamento, migração, topologia escalável e governança de custos em nuvens hiper-escala (AWS/Azure/GCP).
8. **Desenvolvimento Mobile (`mobile`):** Foco no ecossistema de smartphones e tablets, desenvolvimento nativo (Kotlin/Swift) ou multiplataforma (Flutter/React Native).
9. **Engenharia de Qualidade e Testes / QA (`qa`):** Foco em automação de testes funcionais/regressivos, caça sistemática a bugs, confiabilidade e processos de qualidade.
10. **Gestão de Produtos / Product Management (`produto`):** Foco na interseção entre estratégia de negócio, design e desenvolvimento, metodologias ágeis e priorização de valor.

---

## ⚙️ 3. O Motor de Inferência (IA Simbólica)

O núcleo do sistema foi desenvolvido em Python com a biblioteca **Experta** (baseada na arquitetura CLIPS e no algoritmo Rete adaptado):

```
+--------------------+        +-----------------------+        +----------------------+
| Respostas do       |  --->  |  Fato: Perfil(...)    |  --->  | Motor de Inferência  |
| Usuário na Web     |        | (Memória de Trabalho) |        | (ConsultorCarreiras) |
+--------------------+        +-----------------------+        +----------+-----------+
                                                                          |
                                      +-----------------------------------+
                                      | Disparo de Regras @Rule (R01 a R26)
                                      v
                              +---------------------------------------+
                              | Fatos Intermediários: Pontuacao(...)  |
                              +---------------------------------------+
                                      |
                                      | Salience Baixa (-100) & Desempate
                                      v
                              +---------------------------------------+
                              | Fato Conclusivo: Recomendacao(...)    |
                              +---------------------------------------+
```

### Elementos da Base de Conhecimento:
* **Fatos (`engine/facts.py`):**
  - `Perfil`: Encapsula as respostas das 12 dimensões avaliadas (matemática, atuação, ferramenta, entrega, estética, social, etc.).
  - `Pontuacao`: Gerado a cada regra ativada contendo trilha beneficiada, pontos somados (1 a 5), ID da regra e a justificativa em linguagem natural.
  - `Recomendacao`: Fato conclusivo gerado na fase final com a trilha vencedora e a segunda alternativa.
* **Regras de Produção (`engine/knowledge_base.py`):**
  - **26 regras lógicas cruzadas (R01 a R26):** Cada regra cruza pelo menos duas dimensões simultâneas (ex: `foco_dados == 'modelagem'` E `matematica == 'alta'`), impedindo diagnósticos superficiais baseados em uma única resposta.
* **Política Hierárquica de Desempate (Determinística):**
  Caso ocorra empate na pontuação máxima acumulada, o motor aplica a seguinte cascata resolutiva:
  1. **Critério 1 (Âncora de Atuação):** Prevalece a trilha que for correspondente direto à resposta dada no campo `atuacao`.
  2. **Critério 2 (Especificidade / Regras Peso 5):** Prevalece a trilha com maior número de disparos de peso máximo.
  3. **Critério 3 (Âncora de Entrega):** Prevalece a trilha alinhada à preferência indicada no campo `entrega`.
  4. **Critério 4 (Ordem Canônica Estável):** Ordem pré-fixada do catálogo (`back_end` > `front_end` > ... > `produto`).
* **Tratamento de Exceção (*Fallback*):** Perfis sem afinidades acentuadas recebem a trilha geral `back_end` acompanhada de justificativa explicativa padrão (`R_PADRAO`).

Para consultar a tabela de decisão completa e as condições lógicas formais, consulte o documento [`docs/matriz_decisao.md`](docs/matriz_decisao.md).

---

## 👥 4. Validação com Personas de Teste

O sistema foi rigorosamente validado por meio de personas sintéticas cobrindo os perfis contrastantes do mercado e os **pares confusos** (ex: Ciência de Dados vs. Engenharia de Dados):

| Persona | Perfil Comportamental | Trilha Recomendada | Pontos | Regras Disparadas |
|---|---|:---:|:---:|:---:|
| **Lucas** | Analítico, foco em estatística, exploração de dados brutos e IA em Python | `ciencia_dados` | **13 pts** | `R07`, `R08`, `R09` |
| **Marina** | Visual, foco em interfaces web, design tátil, usabilidade e JS/TS | `front_end` | **12 pts** | `R04`, `R05`, `R06` |
| **Rafael** | Infraestrutura, foco em segurança defensiva/ofensiva, redes e Linux | `ciberseguranca` | **12 pts** | `R13`, `R14`, `R15` |
| **Beatriz** | Negócios, articulação com stakeholders, visão de produto e agilidade | `produto` | **9 pts** | `R25`, `R26` |
| **Tiago** | Dados, arquitetura de pipelines ETL, governança de Data Lakes e SQL | `eng_dados` | **12 pts** | `R10`, `R11`, `R12` |
| **Gabriel** | Automação contínua de esteiras CI/CD, contêineres Docker e Linux | `devops` | **9 pts** | `R16`, `R17` |
| **Felipe** | Estruturação topológica, dimensionamento de nuvem AWS/Azure e IaC | `cloud` | **9 pts** | `R18`, `R19` |
| **Camila** | Ecossistema móvel de smartphones, Dart/Flutter/Kotlin e apps de bolso | `mobile` | **13 pts** | `R20`, `R21`, `R22` |
| **Larissa** | Caça persistente a bugs, planos de teste automatizados e zero defeitos | `qa` | **9 pts** | `R23`, `R24` |
| **Rodrigo** | Lógica de microsserviços, linguagens corporativas (Java/C#) e APIs | `back_end` | **8 pts** | `R01`, `R03` |

Para mais detalhes sobre as personas e o relatório de desambiguação dos pares confusos, veja [`docs/resultados_personas.md`](docs/resultados_personas.md).

---

## 🛠️ 5. Estrutura de Diretórios do Projeto

```text
atividadeAECO/
├── .gitignore                   # Exclusão de venv, cache, IDEs e arquivos temporários
├── pytest.ini                   # Configuração de execução do Pytest (pythonpath = .)
├── README.md                    # Este documento completo
├── requirements.txt             # Dependências fixadas (experta, frozendict, streamlit, pytest)
├── app.py                       # Interface Web gráfica desenvolvida em Streamlit
├── docs/
│   ├── matriz_decisao.md        # Tabela com as 26 regras, justificativas e desempate
│   └── resultados_personas.md   # Relatório com os perfis e validação das personas
├── engine/
│   ├── __init__.py              # Pacote Python do motor
│   ├── compat.py                # Shim de retrocompatibilidade do Experta para Python 3.10+
│   ├── facts.py                 # Classes Fact (Perfil, Pontuacao, Recomendacao)
│   ├── knowledge_base.py        # Motor ConsultorCarreiras e função recomendar()
│   └── opcoes.py                # Única fonte de verdade das 10 trilhas e 12 perguntas
└── tests/
    ├── .gitkeep                 # Preservação do diretório
    └── test_personas.py         # 21 testes automatizados (unitários, parametrizados e pares)
```

---

## 🧩 6. Nota de Compatibilidade (Python 3.10+ e Experta)

A biblioteca oficial `experta` (versão 1.9.4) foi construída quando classes abstratas de coleção residiam no módulo `collections`. A partir do Python 3.10, essas classes foram transferidas integralmente para `collections.abc`, provocando falhas de importação em ambientes modernos (`AttributeError: module 'collections' has no attribute 'Mapping'`).

Para resolver esse problema de forma elegante e transparente sem exigir modificações manuais no código-fonte instalado:
1. Criou-se o módulo [`engine/compat.py`](engine/compat.py), que atua interceptando as classes (`Mapping`, `MutableMapping`, `Sequence`, `Iterable`, `Callable`) e mapeando-as de `collections.abc` para `collections` antes de qualquer chamada ao `experta`.
2. As dependências foram estritamente fixadas no [`requirements.txt`](requirements.txt) com `experta==1.9.4` e `frozendict==1.2`.

---

## 🚀 7. Instalação e Execução Passo a Passo

### Pré-requisitos
* **Python 3.10** ou superior instalado na máquina.
* **Git** instalado para controle de versão local.

### Passo 1: Clonar ou Acessar a Pasta do Projeto
Abra o terminal (PowerShell, Bash ou Prompt de Comando) na raiz do projeto:
```bash
cd atividadeAECO
```

### Passo 2: Criar e Ativar o Ambiente Virtual
* **No Windows (PowerShell):**
  ```powershell
  python -m venv .venv
  .\.venv\Scripts\Activate.ps1
  ```
* **No Linux / macOS (Bash):**
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  ```

### Passo 3: Instalar as Dependências
Com o ambiente virtual ativado, instale os pacotes necessários:
```bash
pip install -r requirements.txt
```

### Passo 4: Executar a Interface Web (Streamlit)
Inicie a aplicação interativa:
```bash
streamlit run app.py
```
O Streamlit abrirá automaticamente no seu navegador padrão no endereço `http://localhost:8501`.

### Passo 5: Executar os Testes Automatizados (Pytest)
Para rodar a suíte completa de 21 testes com verificação detalhada:
```bash
pytest -v
```

---

## 👤 8. Identificação do Autor

* **Estudante / Autor:** Taagny Augusto Reis da Silva
* **Matrícula:** 231-002750
* **Curso:** Ciência da Computação
* **Disciplina:** Inteligência Artificial
* **Instituição:** Centro Universitário Presidente Antônio Carlos — UNIPAC Barbacena
* **Professor Responsável:** Felipe Roncalli de Paula Carneiro
* **Ano / Semestre:** 2026/2
