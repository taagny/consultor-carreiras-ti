"""Suíte de testes de validação com Personas para o Consultor Inteligente de Carreiras em TI.

Verifica se o motor de inferência Experta acerta as recomendações para personas
representativas das diferentes áreas de tecnologia, contemplando os requisitos
da Fase 4 da disciplina de Inteligência Artificial (UNIPAC Barbacena).
"""

import pytest
import engine.compat  # noqa: F401
from engine.knowledge_base import recomendar
from engine.opcoes import TRILHAS


# =============================================================================
# DEFINIÇÃO DAS PERSONAS DE TESTE
# =============================================================================

PERSONAS = {
    "analitico_ciencia_dados": {
        "nome": "Lucas - Perfil Analítico / Ciência de Dados",
        "respostas": {
            "matematica": "alta",
            "atuacao": "dados_brutos",
            "ferramenta": "python",
            "entrega": "insights_previsoes",
            "estetica": "baixa",
            "social": "baixo",
            "gosta_testar": "nao",
            "interesse_mobile": "nao",
            "terminal": "medio",
            "ataque_defesa": "nao",
            "foco_dados": "modelagem",
            "experiencia": "intermediario",
        },
        "trilha_esperada": "ciencia_dados",
        "regras_esperadas": ["R07", "R08", "R09"],
    },
    "visual_frontend": {
        "nome": "Marina - Perfil Visual / Front-end & UI/UX",
        "respostas": {
            "matematica": "baixa",
            "atuacao": "layouts_visuais",
            "ferramenta": "javascript",
            "entrega": "produto_final",
            "estetica": "alta",
            "social": "medio",
            "gosta_testar": "nao",
            "interesse_mobile": "nao",
            "terminal": "baixo",
            "ataque_defesa": "nao",
            "foco_dados": "nenhum",
            "experiencia": "intermediario",
        },
        "trilha_esperada": "front_end",
        "regras_esperadas": ["R04", "R05", "R06"],
    },
    "infra_ciberseguranca": {
        "nome": "Rafael - Perfil Infra / Cibersegurança",
        "respostas": {
            "matematica": "media",
            "atuacao": "seguranca",
            "ferramenta": "linux_redes",
            "entrega": "seguranca",
            "estetica": "baixa",
            "social": "baixo",
            "gosta_testar": "sim",
            "interesse_mobile": "nao",
            "terminal": "alto",
            "ataque_defesa": "sim",
            "foco_dados": "nenhum",
            "experiencia": "avancado",
        },
        "trilha_esperada": "ciberseguranca",
        "regras_esperadas": ["R13", "R14", "R15"],
    },
    "negocios_produto": {
        "nome": "Beatriz - Perfil Negócios / Gestão de Produtos",
        "respostas": {
            "matematica": "baixa",
            "atuacao": "negocio_produto",
            "ferramenta": "nenhuma",
            "entrega": "estrategia_produto",
            "estetica": "media",
            "social": "alto",
            "gosta_testar": "nao",
            "interesse_mobile": "nao",
            "terminal": "baixo",
            "ataque_defesa": "nao",
            "foco_dados": "nenhum",
            "experiencia": "intermediario",
        },
        "trilha_esperada": "produto",
        "regras_esperadas": ["R25", "R26"],
    },
    "engenharia_dados": {
        "nome": "Tiago - Perfil Engenharia de Dados",
        "respostas": {
            "matematica": "media",
            "atuacao": "pipelines_dados",
            "ferramenta": "sql",
            "entrega": "dados_confiaveis",
            "estetica": "baixa",
            "social": "baixo",
            "gosta_testar": "nao",
            "interesse_mobile": "nao",
            "terminal": "alto",
            "ataque_defesa": "nao",
            "foco_dados": "pipelines",
            "experiencia": "avancado",
        },
        "trilha_esperada": "eng_dados",
        "regras_esperadas": ["R10", "R11", "R12"],
    },
    "devops_sre": {
        "nome": "Gabriel - Perfil DevOps & SRE",
        "respostas": {
            "matematica": "media",
            "atuacao": "automacao_deploy",
            "ferramenta": "linux_redes",
            "entrega": "infraestrutura",
            "estetica": "baixa",
            "social": "medio",
            "gosta_testar": "sim",
            "interesse_mobile": "nao",
            "terminal": "alto",
            "ataque_defesa": "nao",
            "foco_dados": "nenhum",
            "experiencia": "avancado",
        },
        "trilha_esperada": "devops",
        "regras_esperadas": ["R16", "R17"],
    },
    "cloud_architecture": {
        "nome": "Felipe - Perfil Cloud Architecture",
        "respostas": {
            "matematica": "media",
            "atuacao": "arquitetura_nuvem",
            "ferramenta": "linux_redes",
            "entrega": "infraestrutura",
            "estetica": "baixa",
            "social": "medio",
            "gosta_testar": "nao",
            "interesse_mobile": "nao",
            "terminal": "alto",
            "ataque_defesa": "nao",
            "foco_dados": "nenhum",
            "experiencia": "avancado",
        },
        "trilha_esperada": "cloud",
        "regras_esperadas": ["R18", "R19"],
    },
    "mobile_developer": {
        "nome": "Camila - Perfil Mobile Developer",
        "respostas": {
            "matematica": "media",
            "atuacao": "apps_celular",
            "ferramenta": "mobile_lang",
            "entrega": "produto_final",
            "estetica": "alta",
            "social": "medio",
            "gosta_testar": "nao",
            "interesse_mobile": "sim",
            "terminal": "baixo",
            "ataque_defesa": "nao",
            "foco_dados": "nenhum",
            "experiencia": "intermediario",
        },
        "trilha_esperada": "mobile",
        "regras_esperadas": ["R20", "R21", "R22"],
    },
    "qa_engineer": {
        "nome": "Larissa - Perfil QA / Qualidade de Software",
        "respostas": {
            "matematica": "media",
            "atuacao": "testes_qualidade",
            "ferramenta": "python",
            "entrega": "qualidade_confiabilidade",
            "estetica": "media",
            "social": "medio",
            "gosta_testar": "sim",
            "interesse_mobile": "nao",
            "terminal": "medio",
            "ataque_defesa": "nao",
            "foco_dados": "nenhum",
            "experiencia": "intermediario",
        },
        "trilha_esperada": "qa",
        "regras_esperadas": ["R23", "R24"],
    },
    "backend_developer": {
        "nome": "Rodrigo - Perfil Back-end Corporativo",
        "respostas": {
            "matematica": "media",
            "atuacao": "servidores",
            "ferramenta": "backend_lang",
            "entrega": "infraestrutura",
            "estetica": "baixa",
            "social": "baixo",
            "gosta_testar": "nao",
            "interesse_mobile": "nao",
            "terminal": "medio",
            "ataque_defesa": "nao",
            "foco_dados": "nenhum",
            "experiencia": "intermediario",
        },
        "trilha_esperada": "back_end",
        "regras_esperadas": ["R01", "R03"],
    },
}


# =============================================================================
# TESTES DAS 4 PERSONAS PRINCIPAIS EXIGIDAS NO PDF
# =============================================================================

def test_persona_analitica_ciencia_dados():
    """Valida a Persona 1: Perfil Analítico / Ciência de Dados."""
    dados = PERSONAS["analitico_ciencia_dados"]
    res = recomendar(dados["respostas"])

    assert res["trilha"] == dados["trilha_esperada"]
    regras_ids = [r["id"] for r in res["regras"]]
    for regra_esp in dados["regras_esperadas"]:
        assert regra_esp in regras_ids, f"Regra {regra_esp} não foi disparada."
    assert res["pontuacoes"]["ciencia_dados"] >= 10


def test_persona_visual_frontend():
    """Valida a Persona 2: Perfil Visual / Front-end & UI/UX."""
    dados = PERSONAS["visual_frontend"]
    res = recomendar(dados["respostas"])

    assert res["trilha"] == dados["trilha_esperada"]
    regras_ids = [r["id"] for r in res["regras"]]
    for regra_esp in dados["regras_esperadas"]:
        assert regra_esp in regras_ids, f"Regra {regra_esp} não foi disparada."
    assert res["pontuacoes"]["front_end"] >= 10


def test_persona_infra_ciberseguranca():
    """Valida a Persona 3: Perfil Infra / Cibersegurança."""
    dados = PERSONAS["infra_ciberseguranca"]
    res = recomendar(dados["respostas"])

    assert res["trilha"] == dados["trilha_esperada"]
    regras_ids = [r["id"] for r in res["regras"]]
    for regra_esp in dados["regras_esperadas"]:
        assert regra_esp in regras_ids, f"Regra {regra_esp} não foi disparada."
    assert res["pontuacoes"]["ciberseguranca"] >= 10


def test_persona_negocios_produto():
    """Valida a Persona 4: Perfil Negócios / Gestão de Produtos."""
    dados = PERSONAS["negocios_produto"]
    res = recomendar(dados["respostas"])

    assert res["trilha"] == dados["trilha_esperada"]
    regras_ids = [r["id"] for r in res["regras"]]
    for regra_esp in dados["regras_esperadas"]:
        assert regra_esp in regras_ids, f"Regra {regra_esp} não foi disparada."
    assert res["pontuacoes"]["produto"] >= 9


# =============================================================================
# TESTES PARAMETRIZADOS PARA TODAS AS 10 PERSONAS / TRILHAS
# =============================================================================

@pytest.mark.parametrize("persona_key", list(PERSONAS.keys()))
def test_todas_as_personas_alcancaveis(persona_key):
    """Garante que cada uma das 10 personas atinge exatamente sua trilha esperada."""
    dados = PERSONAS[persona_key]
    res = recomendar(dados["respostas"])
    assert res["trilha"] == dados["trilha_esperada"], (
        f"Falha na persona {dados['nome']}: esperado {dados['trilha_esperada']}, "
        f"obtido {res['trilha']} (pontuações: {res['pontuacoes']})"
    )


# =============================================================================
# TESTES DE DESAMBIGUAÇÃO DE PARES CONFUSOS
# =============================================================================

def test_desambiguacao_ciencia_dados_vs_engenharia_dados():
    """Valida a separação estrita entre Cientista de Dados e Engenheiro de Dados."""
    res_ciencia = recomendar(PERSONAS["analitico_ciencia_dados"]["respostas"])
    res_eng = recomendar(PERSONAS["engenharia_dados"]["respostas"])

    assert res_ciencia["trilha"] == "ciencia_dados"
    assert res_ciencia["pontuacoes"]["ciencia_dados"] > res_ciencia["pontuacoes"]["eng_dados"]

    assert res_eng["trilha"] == "eng_dados"
    assert res_eng["pontuacoes"]["eng_dados"] > res_eng["pontuacoes"]["ciencia_dados"]


def test_desambiguacao_devops_vs_cloud_vs_ciberseguranca():
    """Valida a diferenciação precisa entre as três vertentes de infraestrutura."""
    res_devops = recomendar(PERSONAS["devops_sre"]["respostas"])
    res_cloud = recomendar(PERSONAS["cloud_architecture"]["respostas"])
    res_sec = recomendar(PERSONAS["infra_ciberseguranca"]["respostas"])

    assert res_devops["trilha"] == "devops"
    assert res_cloud["trilha"] == "cloud"
    assert res_sec["trilha"] == "ciberseguranca"


def test_desambiguacao_backend_vs_frontend_vs_mobile():
    """Valida a segregação entre desenvolvimento Back-end, Front-end e Mobile."""
    res_back = recomendar(PERSONAS["backend_developer"]["respostas"])
    res_front = recomendar(PERSONAS["visual_frontend"]["respostas"])
    res_mob = recomendar(PERSONAS["mobile_developer"]["respostas"])

    assert res_back["trilha"] == "back_end"
    assert res_front["trilha"] == "front_end"
    assert res_mob["trilha"] == "mobile"


def test_desambiguacao_qa_vs_produto_vs_backend():
    """Valida a diferenciação entre QA, Gestão de Produtos e Back-end."""
    res_qa = recomendar(PERSONAS["qa_engineer"]["respostas"])
    res_prod = recomendar(PERSONAS["negocios_produto"]["respostas"])
    res_back = recomendar(PERSONAS["backend_developer"]["respostas"])

    assert res_qa["trilha"] == "qa"
    assert res_prod["trilha"] == "produto"
    assert res_back["trilha"] == "back_end"


# =============================================================================
# TESTES DE ESTRUTURA DO CONTRATO E CASOS LIMITES
# =============================================================================

def test_estrutura_retorno_recomendar():
    """Valida que o dicionário de retorno de recomendar() cumpre o contrato rigoroso."""
    res = recomendar(PERSONAS["analitico_ciencia_dados"]["respostas"])

    assert "trilha" in res
    assert "pontuacoes" in res
    assert "regras" in res
    assert "segunda_opcao" in res

    assert res["trilha"] in TRILHAS
    assert len(res["pontuacoes"]) == 10
    for tid in TRILHAS.keys():
        assert tid in res["pontuacoes"]
        assert isinstance(res["pontuacoes"][tid], int)

    assert isinstance(res["regras"], list)
    assert len(res["regras"]) > 0
    for r in res["regras"]:
        assert "id" in r
        assert "trilha" in r
        assert "pontos" in r
        assert "motivo" in r


def test_perfil_vazio_valores_padrao():
    """Garante que um dicionário vazio preenche valores neutros padrão e recomenda com segurança."""
    res = recomendar({})
    assert res["trilha"] == "back_end"
    assert "back_end" in res["pontuacoes"]
    assert len(res["regras"]) > 0


def test_perfil_sem_regras_fallback():
    """Garante que um perfil sem disparos de regras específicas ativa a regra padrão explicativa."""
    res = recomendar({
        "matematica": "baixa",
        "atuacao": "nenhuma",
        "ferramenta": "nenhuma",
        "entrega": "nenhuma",
        "foco_dados": "nenhum",
        "interesse_mobile": "nao",
    })
    assert res["trilha"] == "back_end"
    assert res["segunda_opcao"] == "front_end"
    ids_regras = [r["id"] for r in res["regras"]]
    assert "R_PADRAO" in ids_regras

