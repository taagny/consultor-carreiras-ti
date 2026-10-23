"""Definições das perguntas e trilhas do Consultor Inteligente de Carreiras em TI.

Esta é a ÚNICA fonte de verdade dos campos, opções e metadados das trilhas de carreira.
"""

TRILHAS = {
    "back_end": {
        "nome": "Desenvolvimento Back-end",
        "descricao": "Desenvolvimento Back-end (servidores, APIs, regras de negócio, bancos de dados)",
    },
    "front_end": {
        "nome": "Desenvolvimento Front-end & UI/UX",
        "descricao": "Desenvolvimento Front-end & UI/UX (interfaces web responsivas, experiência do usuário, frameworks reativos)",
    },
    "ciencia_dados": {
        "nome": "Ciência de Dados e Machine Learning",
        "descricao": "Ciência de Dados e Machine Learning (estatística, modelagem preditiva, grandes massas de dados, IA)",
    },
    "eng_dados": {
        "nome": "Engenharia de Dados",
        "descricao": "Engenharia de Dados (arquitetura de dados, pipelines ETL/ELT, Data Lakes)",
    },
    "ciberseguranca": {
        "nome": "Cibersegurança",
        "descricao": "Cibersegurança (defesa cibernética, vulnerabilidades, criptografia, redes seguras, pentesting)",
    },
    "devops": {
        "nome": "DevOps & SRE",
        "descricao": "DevOps & SRE (automação, CI/CD, contêineres)",
    },
    "cloud": {
        "nome": "Computação em Nuvem / Cloud Architecture",
        "descricao": "Computação em Nuvem / Cloud Architecture (planejamento, migração e gestão de infraestrutura escalável AWS/Azure/GCP)",
    },
    "mobile": {
        "nome": "Desenvolvimento Mobile",
        "descricao": "Desenvolvimento Mobile (nativo ou Flutter/React Native)",
    },
    "qa": {
        "nome": "Engenharia de Qualidade e Testes",
        "descricao": "Engenharia de Qualidade e Testes (testes automatizados, confiabilidade, processos de qualidade)",
    },
    "produto": {
        "nome": "Gestão de Produtos / Product Management",
        "descricao": "Gestão de Produtos / Product Management (ponte entre negócio, design e desenvolvimento, métodos ágeis, priorização)",
    },
}

PERGUNTAS = {
    "matematica": {
        "pergunta": "Qual é o seu nível de afinidade e conforto com matemática, estatística e raciocínio analítico?",
        "opcoes": {
            "baixa": "Baixa afinidade (prefiro focar em regras de negócio, lógica visual ou processos)",
            "media": "Média afinidade (confortável com lógica padrão, aritmética e análise de dados básica)",
            "alta": "Alta afinidade (gosto de estatística, probabilidade, cálculo e modelagem matemática)",
        },
    },
    "atuacao": {
        "pergunta": "Em qual tipo de atividade técnica você mais gostaria de atuar no seu dia a dia profissional?",
        "opcoes": {
            "algoritmos_logica": "Algoritmos e lógica pura: resolução de problemas computacionais complexos",
            "layouts_visuais": "Layouts e interfaces visuais: componentes de tela, usabilidade e interatividade web",
            "servidores": "Servidores e microsserviços: desenvolvimento de APIs, integrações e banco de dados",
            "dados_brutos": "Dados brutos e análise exploratória: identificação de tendências e padrões ocultos",
            "pipelines_dados": "Pipelines de dados: construção de rotinas de ingestão, ETL/ELT e Data Lakes",
            "seguranca": "Segurança de sistemas: análise de vulnerabilidades, criptografia e proteção de redes",
            "automacao_deploy": "Automação e deploy: pipelines de CI/CD, esteiras de entrega contínua e contêineres",
            "testes_qualidade": "Testes e qualidade: validação automatizada, planos de teste e caça a bugs",
            "negocio_produto": "Negócio e produto: estratégia, descoberta de necessidades do usuário e priorização",
            "apps_celular": "Aplicações móveis: desenvolvimento de apps interativos para smartphones",
            "arquitetura_nuvem": "Arquitetura em nuvem: estruturação e dimensionamento de ambientes AWS/Azure/GCP",
        },
    },
    "ferramenta": {
        "pergunta": "Com qual conjunto de linguagens e ferramentas você possui maior afinidade ou preferência atual?",
        "opcoes": {
            "python": "Python (análise de dados, scripts, automação e inteligência artificial)",
            "javascript": "JavaScript / TypeScript (ecossistema web, NodeJS e frameworks reativos)",
            "backend_lang": "Linguagens corporativas de back-end (Java, C#, Go)",
            "mobile_lang": "Linguagens para apps móveis (Dart/Flutter, Kotlin, Swift)",
            "sql": "SQL e bancos de dados relacionais/analíticos",
            "linux_redes": "Linux, comandos de terminal, Docker e noções de redes",
            "nenhuma": "Nenhuma ferramenta específica ainda (foco conceitual ou em início de aprendizado)",
        },
    },
    "entrega": {
        "pergunta": "Qual tipo de resultado ou entrega final gera maior sensação de realização profissional para você?",
        "opcoes": {
            "produto_final": "Ver uma aplicação completa e interativa funcionando diretamente na mão dos usuários",
            "infraestrutura": "Garantir uma infraestrutura resiliente, servidores escaláveis e deploys estáveis",
            "seguranca": "Proteger sistemas críticos contra invasões, incidentes e violações de dados",
            "insights_previsoes": "Entregar insights acionáveis, relatórios preditivos e soluções inteligentes baseadas em IA",
            "qualidade_confiabilidade": "Entregar software com padrão zero defeitos, alta confiabilidade e testado ponta a ponta",
            "estrategia_produto": "Ver um produto digital resolver a dor real do cliente e atingir métricas de negócio",
            "dados_confiaveis": "Prover repositórios de dados estruturados, limpos e acessíveis para toda a organização",
        },
    },
    "estetica": {
        "pergunta": "Qual é o seu nível de sensibilidade a design visual, harmonia de cores, tipografia e ergonomia de interfaces?",
        "opcoes": {
            "baixa": "Baixa (não me atento a detalhes visuais; prefiro focar na lógica interna ou infra)",
            "media": "Média (aprecio boas interfaces e compreendo princípios básicos de usabilidade)",
            "alta": "Alta (sou muito visual, detalhista com alinhamentos, espaçamentos e design system)",
        },
    },
    "social": {
        "pergunta": "Qual é a sua preferência em relação a interação social, negociação com pessoas e facilitação de reuniões?",
        "opcoes": {
            "baixo": "Baixo (prefiro trabalhar de maneira individual, silenciosa e com foco técnico contínuo)",
            "medio": "Médio (comunico-me bem na equipe técnica, alternando reuniões e momentos de foco)",
            "alto": "Alto (gosto de lidar com clientes, gerenciar expectativas, facilitar cerimônias e alinhar visões)",
        },
    },
    "gosta_testar": {
        "pergunta": "Você sente satisfação pessoal em encontrar erros, brechas, casos de borda e testar os limites de uma aplicação?",
        "opcoes": {
            "sim": "Sim (gosto de questionar se o sistema realmente funciona sob qualquer cenário adverso)",
            "nao": "Não (prefiro a etapa de criação de funcionalidades à etapa minuciosa de busca por falhas)",
        },
    },
    "interesse_mobile": {
        "pergunta": "Você tem interesse ativo em desenvolver e publicar aplicativos voltados especificamente para smartphones (Android/iOS)?",
        "opcoes": {
            "sim": "Sim (sou atraído pelo ecossistema móvel, sensores de celulares, touch e publicação em lojas)",
            "nao": "Não (prefiro focar em navegadores desktop, ambientes corporativos, terminais ou servidores)",
        },
    },
    "terminal": {
        "pergunta": "Qual é o seu nível de conforto operando comandos em terminal Linux, editores de texto no console e contêineres?",
        "opcoes": {
            "baixo": "Baixo (evito linha de comando e prefiro interfaces gráficas amigáveis)",
            "medio": "Médio (utilizo comandos fundamentais como git, navegação em diretórios e execução de scripts)",
            "alto": "Alto (sinto total conforto em linha de comando bash/zsh, manipulação de servidores SSH e Docker)",
        },
    },
    "ataque_defesa": {
        "pergunta": "Você tem fascínio pelo universo de invasão ética (pentesting), análise forense e defesa contra ataques cibernéticos?",
        "opcoes": {
            "sim": "Sim (acho empolgante entender como brechas são exploradas e como blindar sistemas)",
            "nao": "Não (prefiro outras vertentes da tecnologia sem foco em ameaças ou segurança ofensiva)",
        },
    },
    "foco_dados": {
        "pergunta": "Ao lidar com dados, qual abordagem mais desperta o seu interesse?",
        "opcoes": {
            "modelagem": "Modelagem: algoritmos estatísticos, treinamento de modelos de machine learning e experimentos de IA",
            "pipelines": "Pipelines: engenharia de dados, fluxos de ETL distribuídos, modelagem analítica e Data Warehouses",
            "nenhum": "Nenhum: meu interesse principal não está concentrado em fluxos analíticos de dados",
        },
    },
    "experiencia": {
        "pergunta": "Qual é o seu nível de experiência prática ou formação prévia na área de tecnologia da informação?",
        "opcoes": {
            "iniciante": "Iniciante (estudante no início do curso ou migrando de carreira sem experiência profissional prévia)",
            "intermediario": "Intermediário (já desenvolvi projetos acadêmicos/pessoais estruturados ou possuo vivência júnior)",
            "avancado": "Avançado (possuo experiência sólida de mercado, projetos complexos ou atuação profissional plena)",
        },
    },
}
