"""Motor de inferência baseado em regras com Experta para o Consultor de Carreiras em TI.

Implementa a base de conhecimento de encadeamento para frente (forward chaining),
codificando a matriz de decisão em regras de produção e executando a recomendação
determinística da melhor trilha de carreira.
"""

# Import obrigatório do shim antes de qualquer módulo do experta
import engine.compat  # noqa: F401

from experta import KnowledgeEngine, Rule, L, AS, Fact
from engine.facts import Perfil, Pontuacao, Recomendacao
from engine.opcoes import TRILHAS

# Valores neutros padrão para caso algum campo não seja informado
VALORES_PADRAO = {
    "matematica": "media",
    "atuacao": "algoritmos_logica",
    "ferramenta": "nenhuma",
    "entrega": "produto_final",
    "estetica": "media",
    "social": "medio",
    "gosta_testar": "nao",
    "interesse_mobile": "nao",
    "terminal": "medio",
    "ataque_defesa": "nao",
    "foco_dados": "nenhum",
    "experiencia": "iniciante",
}

# Mapeamentos auxiliares para o desempate determinístico
ANCORA_ATUACAO = {
    "servidores": "back_end",
    "algoritmos_logica": "back_end",
    "layouts_visuais": "front_end",
    "dados_brutos": "ciencia_dados",
    "pipelines_dados": "eng_dados",
    "seguranca": "ciberseguranca",
    "automacao_deploy": "devops",
    "arquitetura_nuvem": "cloud",
    "apps_celular": "mobile",
    "testes_qualidade": "qa",
    "negocio_produto": "produto",
}

ANCORA_ENTREGA = {
    "seguranca": ["ciberseguranca"],
    "insights_previsoes": ["ciencia_dados"],
    "dados_confiaveis": ["eng_dados"],
    "qualidade_confiabilidade": ["qa"],
    "estrategia_produto": ["produto"],
    "produto_final": ["front_end", "mobile", "back_end"],
    "infraestrutura": ["devops", "cloud"],
}

ORDEM_CANONICA = [
    "back_end",
    "front_end",
    "ciencia_dados",
    "eng_dados",
    "ciberseguranca",
    "devops",
    "cloud",
    "mobile",
    "qa",
    "produto",
]


class ConsultorCarreiras(KnowledgeEngine):
    """Motor de inferência que processa o perfil do usuário e recomenda trilhas de TI."""

    def __init__(self):
        super().__init__()
        self.resultado = None

    # =========================================================================
    # TRILHA 1: DESENVOLVIMENTO BACK-END (back_end)
    # =========================================================================

    @Rule(Perfil(atuacao="servidores", ferramenta=L("backend_lang") | L("python") | L("sql")))
    def regra_r01_backend_servidores(self):
        """R01: Afinidade com APIs/servidores combinada a linguagens corporativas ou bancos."""
        self.declare(
            Pontuacao(
                trilha="back_end",
                pontos=5,
                regra_id="R01",
                motivo="Forte vocação para o núcleo de back-end: construção de APIs, regras de negócio e banco de dados.",
            )
        )

    @Rule(Perfil(atuacao="algoritmos_logica", estetica=L("baixa") | L("media"), interesse_mobile="nao"))
    def regra_r02_backend_algoritmos(self):
        """R02: Foco em lógica algorítmica pura sem interesse em camadas visuais ou apps móveis."""
        self.declare(
            Pontuacao(
                trilha="back_end",
                pontos=4,
                regra_id="R02",
                motivo="Perfil voltado a raciocínio algorítmico e lógica de processamento sem foco em estética visual ou mobile.",
            )
        )

    @Rule(Perfil(entrega=L("produto_final") | L("infraestrutura"), ferramenta="backend_lang"))
    def regra_r03_backend_corporativo(self):
        """R03: Preferência por entregas estruturadas operando com linguagens de back-end (Java/C#/Go)."""
        self.declare(
            Pontuacao(
                trilha="back_end",
                pontos=3,
                regra_id="R03",
                motivo="Valorização de sistemas corporativos robustos sustentados por linguagens como Java, C# ou Go.",
            )
        )

    # =========================================================================
    # TRILHA 2: DESENVOLVIMENTO FRONT-END & UI/UX (front_end)
    # =========================================================================

    @Rule(Perfil(atuacao="layouts_visuais", ferramenta="javascript"))
    def regra_r04_frontend_javascript(self):
        """R04: Atuação focada em layouts visuais com domínio do ecossistema JavaScript/TypeScript."""
        self.declare(
            Pontuacao(
                trilha="front_end",
                pontos=5,
                regra_id="R04",
                motivo="Núcleo essencial do front-end: construção de interfaces interativas e responsivas com ecossistema JavaScript.",
            )
        )

    @Rule(Perfil(estetica="alta", entrega="produto_final", interesse_mobile="nao"))
    def regra_r05_frontend_estetica(self):
        """R05: Alta sensibilidade estética e foco no produto entregue diretamente para navegadores web."""
        self.declare(
            Pontuacao(
                trilha="front_end",
                pontos=4,
                regra_id="R05",
                motivo="Grande sensibilidade a design visual e usabilidade voltada para aplicações acessíveis na web.",
            )
        )

    @Rule(Perfil(atuacao="layouts_visuais", terminal=L("baixo") | L("medio")))
    def regra_r06_frontend_apresentacao(self):
        """R06: Predileção por interfaces visuais com distanciamento de linhas de comando ou terminal."""
        self.declare(
            Pontuacao(
                trilha="front_end",
                pontos=3,
                regra_id="R06",
                motivo="Foco na camada visual de apresentação com priorização de ergonomia e baixo uso de terminal.",
            )
        )

    # =========================================================================
    # TRILHA 3: CIÊNCIA DE DADOS E MACHINE LEARNING (ciencia_dados)
    # =========================================================================

    @Rule(Perfil(foco_dados="modelagem", matematica="alta"))
    def regra_r07_ciencia_dados_matematica(self):
        """R07: Foco em modelagem preditiva e IA apoiado por sólida afinidade matemática e estatística."""
        self.declare(
            Pontuacao(
                trilha="ciencia_dados",
                pontos=5,
                regra_id="R07",
                motivo="Núcleo de Ciência de Dados: fundamentação estatística/matemática avançada voltada à criação de modelos de Machine Learning.",
            )
        )

    @Rule(Perfil(atuacao="dados_brutos", ferramenta="python"))
    def regra_r08_ciencia_dados_exploracao(self):
        """R08: Exploração analítica de dados brutos com a linguagem referência em ciência de dados (Python)."""
        self.declare(
            Pontuacao(
                trilha="ciencia_dados",
                pontos=4,
                regra_id="R08",
                motivo="Investigação de padrões ocultos e análise exploratória de massas de dados utilizando o ecossistema Python.",
            )
        )

    @Rule(Perfil(entrega="insights_previsoes", foco_dados="modelagem"))
    def regra_r09_ciencia_dados_previsao(self):
        """R09: Realização centrada em entrega de inteligência preditiva e suporte a decisões baseadas em dados."""
        self.declare(
            Pontuacao(
                trilha="ciencia_dados",
                pontos=4,
                regra_id="R09",
                motivo="Busca por geração de valor através de soluções preditivas, relatórios inteligentes e modelos analíticos.",
            )
        )

    # =========================================================================
    # TRILHA 4: ENGENHARIA DE DADOS (eng_dados)
    # =========================================================================

    @Rule(Perfil(foco_dados="pipelines", atuacao="pipelines_dados"))
    def regra_r10_eng_dados_pipelines(self):
        """R10: Dedicação à concepção e suporte a pipelines de ingestão e arquitetura de Data Lakes."""
        self.declare(
            Pontuacao(
                trilha="eng_dados",
                pontos=5,
                regra_id="R10",
                motivo="Núcleo de Engenharia de Dados: estruturação de fluxos de ETL/ELT distribuídos e repositórios analíticos em escala.",
            )
        )

    @Rule(Perfil(entrega="dados_confiaveis", ferramenta=L("sql") | L("python")))
    def regra_r11_eng_dados_governanca(self):
        """R11: Compromisso com a governança, limpeza e disponibilidade de dados íntegros usando SQL ou Python."""
        self.declare(
            Pontuacao(
                trilha="eng_dados",
                pontos=4,
                regra_id="R11",
                motivo="Foco na entrega de repositórios de dados consistentes, limpos e de alto desempenho para a organização.",
            )
        )

    @Rule(Perfil(foco_dados="pipelines", terminal=L("medio") | L("alto")))
    def regra_r12_eng_dados_infra_distribuida(self):
        """R12: Afinidade com ferramentas de orquestração de dados que rodam sobre ambientes Linux e contêineres."""
        self.declare(
            Pontuacao(
                trilha="eng_dados",
                pontos=3,
                regra_id="R12",
                motivo="Aptidão para gerenciar pipelines de dados em ambientes distribuídos com suporte a contêineres e terminal.",
            )
        )

    # =========================================================================
    # TRILHA 5: CIBERSEGURANÇA (ciberseguranca)
    # =========================================================================

    @Rule(Perfil(ataque_defesa="sim", atuacao="seguranca"))
    def regra_r13_ciberseguranca_nucleo(self):
        """R13: Vocação primária para invasão ética, pentesting e proteção contra ameaças cibernéticas."""
        self.declare(
            Pontuacao(
                trilha="ciberseguranca",
                pontos=5,
                regra_id="R13",
                motivo="Núcleo de Cibersegurança: paixão por testes de invasão ética, análise de vulnerabilidades e defesa contra ciberataques.",
            )
        )

    @Rule(Perfil(entrega="seguranca", ferramenta="linux_redes"))
    def regra_r14_ciberseguranca_redes(self):
        """R14: Foco em blindagem de infraestruturas suportado por proficiência em Linux e redes."""
        self.declare(
            Pontuacao(
                trilha="ciberseguranca",
                pontos=4,
                regra_id="R14",
                motivo="Compromisso prioritário com a segurança e integridade de sistemas ancorado em arquitetura de redes e Linux.",
            )
        )

    @Rule(Perfil(ataque_defesa="sim", gosta_testar="sim"))
    def regra_r15_ciberseguranca_auditoria(self):
        """R15: Mentalidade investigativa voltada à busca por brechas de segurança e testes de estresse."""
        self.declare(
            Pontuacao(
                trilha="ciberseguranca",
                pontos=3,
                regra_id="R15",
                motivo="Perfil investigativo e persistente para encontrar brechas e auditar conformidade de segurança.",
            )
        )

    # =========================================================================
    # TRILHA 6: DEVOPS & SRE (devops)
    # =========================================================================

    @Rule(Perfil(atuacao="automacao_deploy", terminal="alto"))
    def regra_r16_devops_cicd(self):
        """R16: Automação contínua de esteiras de CI/CD associada a domínio avançado de terminal e Docker."""
        self.declare(
            Pontuacao(
                trilha="devops",
                pontos=5,
                regra_id="R16",
                motivo="Núcleo de DevOps/SRE: automação de esteiras de CI/CD, contêineres e scripts avançados de infraestrutura.",
            )
        )

    @Rule(Perfil(entrega="infraestrutura", ferramenta="linux_redes"))
    def regra_r17_devops_resiliencia(self):
        """R17: Garantia de servidores estáveis e deploys confiáveis sustentados por Linux e redes."""
        self.declare(
            Pontuacao(
                trilha="devops",
                pontos=4,
                regra_id="R17",
                motivo="Dedicação à estabilidade, observabilidade e confiabilidade do ciclo operacional de software.",
            )
        )

    # =========================================================================
    # TRILHA 7: COMPUTAÇÃO EM NUVEM / CLOUD ARCHITECTURE (cloud)
    # =========================================================================

    @Rule(Perfil(atuacao="arquitetura_nuvem", entrega="infraestrutura"))
    def regra_r18_cloud_arquitetura(self):
        """R18: Planejamento, migração e desenho estratégico de soluções escaláveis em nuvem (AWS/Azure/GCP)."""
        self.declare(
            Pontuacao(
                trilha="cloud",
                pontos=5,
                regra_id="R18",
                motivo="Núcleo de Cloud Architecture: estruturação estratégica de ambientes escaláveis e resilientes em provedores de nuvem.",
            )
        )

    @Rule(Perfil(atuacao="arquitetura_nuvem", terminal=L("medio") | L("alto")))
    def regra_r19_cloud_iac(self):
        """R19: Operação de infraestrutura em nuvem por meio de ferramentas CLI e IaC (Terraform)."""
        self.declare(
            Pontuacao(
                trilha="cloud",
                pontos=4,
                regra_id="R19",
                motivo="Gestão de recursos em nuvem apoiada em automação via linha de comando e boas práticas de arquitetura.",
            )
        )

    # =========================================================================
    # TRILHA 8: DESENVOLVIMENTO MOBILE (mobile)
    # =========================================================================

    @Rule(Perfil(interesse_mobile="sim", ferramenta="mobile_lang"))
    def regra_r20_mobile_stack(self):
        """R20: Interesse direto no ecossistema de smartphones com linguagens dedicadas (Dart, Kotlin, Swift)."""
        self.declare(
            Pontuacao(
                trilha="mobile",
                pontos=5,
                regra_id="R20",
                motivo="Núcleo Mobile: foco no desenvolvimento de apps nativos ou multiplataforma com linguagens dedicadas.",
            )
        )

    @Rule(Perfil(atuacao="apps_celular", entrega="produto_final"))
    def regra_r21_mobile_produto(self):
        """R21: Criação de aplicações completas voltadas diretamente para dispositivos móveis."""
        self.declare(
            Pontuacao(
                trilha="mobile",
                pontos=5,
                regra_id="R21",
                motivo="Entusiasmo na construção de aplicações ricas que rodam na ponta dos dedos dos usuários de celular.",
            )
        )

    @Rule(Perfil(interesse_mobile="sim", estetica=L("media") | L("alta")))
    def regra_r22_mobile_usabilidade(self):
        """R22: Apreço pela ergonomia tátil, transições suaves e componentes visuais do ecossistema móvel."""
        self.declare(
            Pontuacao(
                trilha="mobile",
                pontos=3,
                regra_id="R22",
                motivo="Atenção à usabilidade tátil, responsividade de tela e design característicos de apps móveis.",
            )
        )

    # =========================================================================
    # TRILHA 9: ENGENHARIA DE QUALIDADE E TESTES (qa)
    # =========================================================================

    @Rule(Perfil(atuacao="testes_qualidade", gosta_testar="sim"))
    def regra_r23_qa_testes(self):
        """R23: Satisfação em encontrar falhas associada à preferência diária por testes de qualidade."""
        self.declare(
            Pontuacao(
                trilha="qa",
                pontos=5,
                regra_id="R23",
                motivo="Núcleo de QA: prazer em encontrar bugs, testar limites e elaborar planos automatizados de teste.",
            )
        )

    @Rule(Perfil(entrega="qualidade_confiabilidade", gosta_testar="sim"))
    def regra_r24_qa_confiabilidade(self):
        """R24: Busca contínua por zero defeitos e estabilidade garantida por testes contínuos."""
        self.declare(
            Pontuacao(
                trilha="qa",
                pontos=4,
                regra_id="R24",
                motivo="Compromisso intransigente com a qualidade e confiabilidade de software entregue em produção.",
            )
        )

    # =========================================================================
    # TRILHA 10: GESTÃO DE PRODUTOS / PRODUCT MANAGEMENT (produto)
    # =========================================================================

    @Rule(Perfil(atuacao="negocio_produto", social="alto"))
    def regra_r25_produto_negocio_social(self):
        """R25: Articulação interpessoal de alto nível unida a decisões de negócio e produto."""
        self.declare(
            Pontuacao(
                trilha="produto",
                pontos=5,
                regra_id="R25",
                motivo="Núcleo de Product Management: perfil negociador e comunicativo que lidera visão de produto e priorização de demandas.",
            )
        )

    @Rule(Perfil(entrega="estrategia_produto", social=L("medio") | L("alto")))
    def regra_r26_produto_estrategia(self):
        """R26: Orientação ao sucesso do produto digital e alinhamento com stakeholders."""
        self.declare(
            Pontuacao(
                trilha="produto",
                pontos=4,
                regra_id="R26",
                motivo="Realização profissional guiada pelo impacto estratégico e mercadológico da solução sobre as dores do usuário.",
            )
        )

    # =========================================================================
    # REGRA FINAL DE DECISÃO E DESEMPATE DETERMINÍSTICO (Salience Baixa)
    # =========================================================================

    @Rule(AS.perfil << Perfil(), salience=-100)
    def regra_decisao_final(self, perfil):
        """Consolida as pontuações acumuladas e aplica a política de desempate determinística."""
        pontos_por_trilha = {tid: 0 for tid in TRILHAS.keys()}
        regras_disparadas = []
        pontos_peso5 = {tid: 0 for tid in TRILHAS.keys()}

        # 1. Varre todos os fatos Pontuacao declarados durante a inferência
        for fact in self.facts.values():
            if isinstance(fact, Pontuacao):
                tid = fact["trilha"]
                pts = fact["pontos"]
                pontos_por_trilha[tid] = pontos_por_trilha.get(tid, 0) + pts
                if pts >= 5:
                    pontos_peso5[tid] = pontos_peso5.get(tid, 0) + 1
                regras_disparadas.append(
                    {
                        "id": fact["regra_id"],
                        "trilha": tid,
                        "pontos": pts,
                        "motivo": fact["motivo"],
                    }
                )

        # Ordena a lista de regras disparadas pelo ID
        regras_disparadas.sort(key=lambda r: r["id"])

        pontuacao_maxima = max(pontos_por_trilha.values())

        # Caso limite: nenhuma regra disparou (perfil neutro ou atípico)
        if pontuacao_maxima == 0:
            vencedora = "back_end"
            segunda_opcao = "front_end"
            regras_disparadas.append(
                {
                    "id": "R_PADRAO",
                    "trilha": "back_end",
                    "pontos": 1,
                    "motivo": (
                        "Perfil sem forte inclinação nas regras específicas. Recomenda-se "
                        "Desenvolvimento Back-end como base sólida e abrangente para a carreira em TI."
                    ),
                }
            )
            pontos_por_trilha["back_end"] = 1
        else:
            # Identifica todas as trilhas empatadas no topo
            candidatas = [t for t, pts in pontos_por_trilha.items() if pts == pontuacao_maxima]

            if len(candidatas) == 1:
                vencedora = candidatas[0]
            else:
                # Aplica os 4 critérios determinísticos da matriz de decisão
                vencedora = self._desempatar(candidatas, perfil, pontos_peso5)

            # Define a segunda opção mais indicada (diferente da vencedora)
            outras = [t for t in TRILHAS.keys() if t != vencedora]
            outras_ordenadas = sorted(
                outras,
                key=lambda t: (
                    pontos_por_trilha[t],
                    pontos_peso5[t],
                    -ORDEM_CANONICA.index(t),
                ),
                reverse=True,
            )
            segunda_opcao = outras_ordenadas[0]

        # Declara o fato conclusivo
        self.declare(Recomendacao(trilha=vencedora, segunda_opcao=segunda_opcao))

        # Guarda o dicionário consolidado para fácil acesso pela função recomendar()
        self.resultado = {
            "trilha": vencedora,
            "pontuacoes": pontos_por_trilha,
            "regras": regras_disparadas,
            "segunda_opcao": segunda_opcao,
        }

    def _desempatar(self, candidatas: list, perfil: Fact, pontos_peso5: dict) -> str:
        """Aplica a cascata hierárquica e determinística de desempate."""
        atuacao_resp = perfil.get("atuacao")
        entrega_resp = perfil.get("entrega")

        # Critério 1: Afinidade direta com o campo de atuação diária
        trilha_ancora = ANCORA_ATUACAO.get(atuacao_resp)
        if trilha_ancora in candidatas:
            return trilha_ancora

        # Critério 2: Maior pontuação em regras de especificidade máxima (peso 5)
        max_peso5 = max(pontos_peso5[t] for t in candidatas)
        candidatas_peso5 = [t for t in candidatas if pontos_peso5[t] == max_peso5]
        if len(candidatas_peso5) == 1:
            return candidatas_peso5[0]

        # Critério 3: Correspondência com o tipo de entrega de valor preferida
        trilhas_entrega = ANCORA_ENTREGA.get(entrega_resp, [])
        candidatas_entrega = [t for t in candidatas_peso5 if t in trilhas_entrega]
        if len(candidatas_entrega) == 1:
            return candidatas_entrega[0]
        if len(candidatas_entrega) > 1:
            candidatas_peso5 = candidatas_entrega

        # Critério 4: Ordem canônica pré-fixada das 10 trilhas
        return min(candidatas_peso5, key=lambda t: ORDEM_CANONICA.index(t))


def recomendar(respostas: dict) -> dict:
    """Função pública que orquestra a inferência e retorna a recomendação completa.

    Garante integridade caso campos opcionais não sejam informados, preenchendo
    valores padrão neutros antes da inferência.

    Args:
        respostas (dict): Respostas fornecidas pelo usuário para o questionário.

    Returns:
        dict contendo:
            - "trilha": ID da trilha recomendada (vencedora)
            - "pontuacoes": dict {id_trilha: pontuacao} para todas as 10 trilhas
            - "regras": lista de dicts com as regras disparadas e justificativas
            - "segunda_opcao": ID da segunda trilha mais compatível
    """
    respostas_completas = {**VALORES_PADRAO, **respostas}

    motor = ConsultorCarreiras()
    motor.reset()
    motor.declare(Perfil(**respostas_completas))
    motor.run()

    return motor.resultado
