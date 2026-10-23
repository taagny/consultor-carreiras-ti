# Relatório de Validação com Personas — Consultor Inteligente de Carreiras em TI

Documento de validação empírica referente à **Fase 4** da disciplina de Inteligência Artificial do curso de Ciência da Computação (UNIPAC Barbacena).

---

## 1. Objetivo da Validação com Personas

O propósito desta etapa é submeter o motor de inferência baseado em regras (Experta) a perfis representativos do mercado de Tecnologia da Informação (**Personas de Teste**), auditando se:
1. O sistema diagnostica a trilha de carreira correta para cada perfil.
2. As regras de produção (*IF-THEN*) cruzadas disparam de forma consistente com a matriz de decisão.
3. As áreas correlatas com potenciais sobreposições (**pares confusos**) são desambiguadas com precisão matemática e lógica.
4. O contrato de retorno da função `recomendar()` é mantido estritamente.

---

## 2. Detalhamento das 4 Personas Principais (Exigidas no PDF)

### Persona 1: Lucas (Perfil Analítico / Ciência de Dados)
* **Perfil do Usuário:** Estudante que se destaca em disciplinas quantitativas (álgebra linear, cálculo e probabilidade). Fascinado por Inteligência Artificial e treinamento de modelos de machine learning. Usa Python diariamente e busca descobrir padrões ocultos em grandes bases de dados para prever cenários futuros.
* **Respostas do Questionário:**
  - `matematica`: `alta` | `atuacao`: `dados_brutos` | `ferramenta`: `python` | `entrega`: `insights_previsoes`
  - `estetica`: `baixa` | `social`: `baixo` | `gosta_testar`: `nao` | `interesse_mobile`: `nao`
  - `terminal`: `medio` | `ataque_defesa`: `nao` | `foco_dados`: `modelagem` | `experiencia`: `intermediario`
* **Resultado Obtido na Inferência:**
  - **Trilha Vencedora:** `ciencia_dados` (13 pontos)
  - **Segunda Opção:** `back_end` (0 pontos)
  - **Regras Disparadas:**
    - `[R07]` (+5 pts): Núcleo de Ciência de Dados: fundamentação estatística/matemática avançada voltada à criação de modelos de Machine Learning.
    - `[R08]` (+4 pts): Investigação de padrões ocultos e análise exploratória de massas de dados utilizando o ecossistema Python.
    - `[R09]` (+4 pts): Busca por geração de valor através de soluções preditivas, relatórios inteligentes e modelos analíticos.

---

### Persona 2: Marina (Perfil Visual / Front-end & UI/UX)
* **Perfil da Usuária:** Desenvolvedora com apurado senso estético, apaixonada por tipografia, contraste de cores e microinterações no navegador. Prefere JavaScript e TypeScript, focando em usabilidade e na satisfação imediata do cliente ao interagir com interfaces web limpas e responsivas. Evita operações complexas de terminal.
* **Respostas do Questionário:**
  - `matematica`: `baixa` | `atuacao`: `layouts_visuais` | `ferramenta`: `javascript` | `entrega`: `produto_final`
  - `estetica`: `alta` | `social`: `medio` | `gosta_testar`: `nao` | `interesse_mobile`: `nao`
  - `terminal`: `baixo` | `ataque_defesa`: `nao` | `foco_dados`: `nenhum` | `experiencia`: `intermediario`
* **Resultado Obtido na Inferência:**
  - **Trilha Vencedora:** `front_end` (12 pontos)
  - **Segunda Opção:** `back_end` (0 pontos)
  - **Regras Disparadas:**
    - `[R04]` (+5 pts): Núcleo essencial do front-end: construção de interfaces interativas e responsivas com ecossistema JavaScript.
    - `[R05]` (+4 pts): Grande sensibilidade a design visual e usabilidade voltada para aplicações acessíveis na web.
    - `[R06]` (+3 pts): Foco na camada visual de apresentação com priorização de ergonomia e baixo uso de terminal.

---

### Persona 3: Rafael (Perfil Infra / Cibersegurança)
* **Perfil do Usuário:** Entusiasta de segurança da informação e redes. Sente fascínio por pentesting, captura de pacotes, auditorias forenses e técnicas de exploração ética de vulnerabilidades. Domina comandos de console Linux, protocolos TCP/IP e tem perfil inquisitivo, buscando sempre encontrar brechas em implementações.
* **Respostas do Questionário:**
  - `matematica`: `media` | `atuacao`: `seguranca` | `ferramenta`: `linux_redes` | `entrega`: `seguranca`
  - `estetica`: `baixa` | `social`: `baixo` | `gosta_testar`: `sim` | `interesse_mobile`: `nao`
  - `terminal`: `alto` | `ataque_defesa`: `sim` | `foco_dados`: `nenhum` | `experiencia`: `avancado`
* **Resultado Obtido na Inferência:**
  - **Trilha Vencedora:** `ciberseguranca` (12 pontos)
  - **Segunda Opção:** `back_end` (0 pontos)
  - **Regras Disparadas:**
    - `[R13]` (+5 pts): Núcleo de Cibersegurança: paixão por testes de invasão ética, análise de vulnerabilidades e defesa contra ciberataques.
    - `[R14]` (+4 pts): Compromisso prioritário com a segurança e integridade de sistemas ancorado em arquitetura de redes e Linux.
    - `[R15]` (+3 pts): Perfil investigativo e persistente para encontrar brechas e auditar conformidade de segurança.

---

### Persona 4: Beatriz (Perfil Negócios / Gestão de Produtos)
* **Perfil da Usuária:** Profissional extremamente articulada e comunicativa. Gosta de liderar cerimônias ágeis, conduzir dinâmicas de descoberta de produto com stakeholders, priorizar backlogs e traduzir metas corporativas em roadmap de software, com foco no valor percebido pelo cliente final.
* **Respostas do Questionário:**
  - `matematica`: `baixa` | `atuacao`: `negocio_produto` | `ferramenta`: `nenhuma` | `entrega`: `estrategia_produto`
  - `estetica`: `media` | `social`: `alto` | `gosta_testar`: `nao` | `interesse_mobile`: `nao`
  - `terminal`: `baixo` | `ataque_defesa`: `nao` | `foco_dados`: `nenhum` | `experiencia`: `intermediario`
* **Resultado Obtido na Inferência:**
  - **Trilha Vencedora:** `produto` (9 pontos)
  - **Segunda Opção:** `back_end` (0 pontos)
  - **Regras Disparadas:**
    - `[R25]` (+5 pts): Núcleo de Product Management: perfil negociador e comunicativo que lidera visão de produto e priorização de demandas.
    - `[R26]` (+4 pts): Realização profissional guiada pelo impacto estratégico e mercadológico da solução sobre as dores do usuário.

---

## 3. Personas Complementares e Desambiguação de Pares Confusos

Para assegurar cobertura exaustiva de todas as 10 trilhas, criamos personas especializadas para os pares correlatos:

| Persona | Trilha Esperada | Trilha Concorrente | Fator Crítico de Desambiguação | Pontuação da Vencedora |
|---|---|---|---|:---:|
| **Tiago** | `eng_dados` | `ciencia_dados` | `foco_dados == 'pipelines'` e `atuacao == 'pipelines_dados'` ativam R10, R11 e R12 | **12 pts** (vs 0 de Ciência) |
| **Gabriel** | `devops` | `cloud` / `ciberseguranca` | `atuacao == 'automacao_deploy'` e `terminal == 'alto'` isolam R16 e R17 (CI/CD) | **9 pts** (vs 4 de Cloud) |
| **Felipe** | `cloud` | `devops` | `atuacao == 'arquitetura_nuvem'` ativa R18 e R19 com foco em topologia de provedores | **9 pts** (vs 0 de DevOps) |
| **Camila** | `mobile` | `front_end` | `interesse_mobile == 'sim'` e `ferramenta == 'mobile_lang'` ativam R20, R21 e R22 | **13 pts** (vs 0 de Front-end) |
| **Larissa** | `qa` | `produto` / `back_end` | `atuacao == 'testes_qualidade'` e `gosta_testar == 'sim'` ativam R23 e R24 | **9 pts** (vs 0 de Produto) |
| **Rodrigo** | `back_end` | `front_end` | `atuacao == 'servidores'` e `ferramenta == 'backend_lang'` ativam R01 e R03 | **8 pts** (vs 0 de Front-end) |

---

## 4. Matriz Geral de Validação e Cobertura dos Testes Automatizados

A suíte em [`tests/test_personas.py`](file:///c:/Users/Taagny/Desktop/atividadeAECO/tests/test_personas.py) executa **21 testes automatizados via Pytest**:
- **4 testes unitários** dedicados às personas fundamentais exigidas no PDF (Lucas, Marina, Rafael, Beatriz).
- **10 testes parametrizados** cobrindo cada uma das 10 trilhas de forma independente com personas dedicadas.
- **4 testes de integração de pares confusos**:
  - Ciência de Dados x Engenharia de Dados
  - DevOps x Cloud x Cibersegurança
  - Back-end x Front-end x Mobile
  - QA x Produto x Back-end
- **3 testes contratuais e de robustez**:
  - Validação estrita do payload retornado por `recomendar()`.
  - Tratamento de dicionário vazio com preenchimento seguro de valores padrão.
  - Ativação da regra padrão explicativa (`R_PADRAO`) quando nenhuma regra específica pontua.

### Resultado da Execução do Pytest:
```text
collected 21 items
21 passed in 0.48s (100% de sucesso)
```

