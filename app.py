"""Consultor Inteligente de Carreiras em TI.

Interface Web interativa construída com Streamlit e integrada ao motor de inferência
Experta (IA Simbólica / Sistema Especialista baseado em regras de encadeamento para frente).
Desenvolvido para a disciplina de Inteligência Artificial do curso de Ciência da Computação
(UNIPAC Barbacena).
"""

import streamlit as st
import pandas as pd

# Shim de compatibilidade para Python 3.10+
import engine.compat  # noqa: F401

from engine.opcoes import PERGUNTAS, TRILHAS
from engine.knowledge_base import recomendar

# -----------------------------------------------------------------------------
# Configuração da Página
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Consultor Inteligente de Carreiras em TI",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -----------------------------------------------------------------------------
# Barra Lateral (Sidebar): Contexto Teórico e Mecânica do Sistema
# -----------------------------------------------------------------------------
with st.sidebar:
    st.title("🎯 Sobre o Sistema")
    st.markdown(
        """
        **Consultor Inteligente de Carreiras em TI** é um **Sistema Especialista baseado em Regras**
        desenvolvido para a disciplina de **Inteligência Artificial** (Ciência da Computação — UNIPAC Barbacena).
        
        ### 🧠 Como Funciona?
        - **Motor de Inferência:** Utiliza a biblioteca **Experta** com algoritmo Rete adaptado.
        - **Estratégia de Raciocínio:** **Encadeamento para Frente (*Forward Chaining*)**, orientado a dados.
        - **Base de Conhecimento:** 26 regras lógicas cruzadas de produção (*IF-THEN*) com pesos calibrados de 1 a 5.
        - **Desempate Determinístico:** Política hierárquica em 4 níveis (Âncora de Atuação, Especificidade Peso 5, Entrega e Ordem Canônica).
        
        ### 🧭 Escopo das 10 Trilhas
        O sistema analisa suas respostas e diagnostica a melhor trilha dentre:
        1. Back-end
        2. Front-end & UI/UX
        3. Ciência de Dados & ML
        4. Engenharia de Dados
        5. Cibersegurança
        6. DevOps & SRE
        7. Cloud Architecture
        8. Desenvolvimento Mobile
        9. QA & Testes
        10. Gestão de Produtos
        """
    )
    st.markdown("---")
    st.caption("UNIPAC Barbacena • Ciência da Computação • IA Simbólica")

# -----------------------------------------------------------------------------
# Cabeçalho Principal
# -----------------------------------------------------------------------------
st.title("💼 Consultor Inteligente de Carreiras em TI")
st.subheader("Diagnóstico Vocacional Especialista por Encadeamento para Frente")
st.markdown(
    "Responda ao questionário objetivo abaixo para que o motor de inferência avalie seu perfil, "
    "dispare as regras de produção correspondentes e apresente a **recomendação justificada** "
    "da trilha ideal para você."
)
st.markdown("---")

# Mapeamento dos campos nas 4 seções temáticas solicitadas
SECOES = {
    "👤 Perfil e Afinidades": ["matematica", "estetica", "social"],
    "⚙️ Preferências de Trabalho": ["atuacao", "gosta_testar", "ataque_defesa"],
    "🛠️ Conhecimentos": ["ferramenta", "terminal", "experiencia"],
    "🎯 Objetivos": ["entrega", "foco_dados", "interesse_mobile"],
}

# -----------------------------------------------------------------------------
# Fluxo de Visualização: Formulário vs. Tela de Resultado
# -----------------------------------------------------------------------------
if "resultado" in st.session_state and st.session_state["resultado"] is not None:
    resultado = st.session_state["resultado"]
    vencedora_id = resultado["trilha"]
    vencedora_info = TRILHAS[vencedora_id]
    pontos_vencedora = resultado["pontuacoes"].get(vencedora_id, 0)

    # 1. Trilha Recomendada em Destaque
    st.success("### 🎉 Diagnóstico Concluído com Sucesso!")
    col_destaque1, col_destaque2 = st.columns([3, 1])
    with col_destaque1:
        st.markdown(f"## 🏆 Trilha Recomendada: **{vencedora_info['nome']}**")
        st.markdown(f"**Descrição da Carreira:** {vencedora_info['descricao']}")
    with col_destaque2:
        st.metric(label="Pontuação Obtida", value=f"{pontos_vencedora} pts")

    # 2. Segunda Opção como Alternativa
    segunda_id = resultado.get("segunda_opcao")
    if segunda_id and segunda_id in TRILHAS:
        segunda_info = TRILHAS[segunda_id]
        pontos_segunda = resultado["pontuacoes"].get(segunda_id, 0)
        st.info(
            f"**🥈 Segunda Opção Mais Compatível:** **{segunda_info['nome']}** ({pontos_segunda} pts)\n\n"
            f"*{segunda_info['descricao']}*"
        )

    st.markdown("---")

    # 3. Justificativa Transparente: "Por que esta trilha?"
    st.subheader("💡 Por que esta trilha? (Justificativa das Regras)")
    regras_vencedora = [r for r in resultado["regras"] if r["trilha"] == vencedora_id]

    if regras_vencedora:
        st.markdown(
            "O motor de inferência disparou as seguintes regras de produção que fundamentam esta recomendação:"
        )
        for r in regras_vencedora:
            st.markdown(f"- **Regra `{r['id']}` (+{r['pontos']} pts):** {r['motivo']}")
    else:
        st.markdown(
            "- Nenhuma regra exclusiva pontuou acima do limiar. A trilha foi definida pelo critério padrão/desempate."
        )

    # Expander opcional com todas as regras que pontuaram na sessão
    todas_outras = [r for r in resultado["regras"] if r["trilha"] != vencedora_id]
    if todas_outras:
        with st.expander("🔍 Ver todas as demais regras disparadas na sessão de inferência"):
            for r in todas_outras:
                nome_t = TRILHAS.get(r["trilha"], {}).get("nome", r["trilha"])
                st.markdown(f"- **Regra `{r['id']}` (+{r['pontos']} pts para {nome_t}):** {r['motivo']}")

    st.markdown("---")

    # 4. Gráfico e Tabela de Pontuação das 10 Trilhas
    st.subheader("📊 Comparativo Geral de Pontuações (Todas as 10 Trilhas)")
    dados_tabela = []
    for tid, pts in resultado["pontuacoes"].items():
        dados_tabela.append(
            {
                "Trilha": TRILHAS[tid]["nome"],
                "Pontos": pts,
                "Status": "🏆 Recomendada" if tid == vencedora_id else ("🥈 2ª Opção" if tid == segunda_id else ""),
            }
        )

    df_pontuacoes = pd.DataFrame(dados_tabela).sort_values(by="Pontos", ascending=False).reset_index(drop=True)

    col_graf, col_tab = st.columns([3, 2])
    with col_graf:
        st.bar_chart(df_pontuacoes.set_index("Trilha")["Pontos"])
    with col_tab:
        st.dataframe(df_pontuacoes, use_container_width=True, hide_index=True)

    st.markdown("---")

    # 5. Botão para Refazer a Entrevista
    if st.button("🔄 Refazer Entrevista", type="primary", use_container_width=True):
        st.session_state.clear()
        st.rerun()

else:
    # -------------------------------------------------------------------------
    # Formulário de Entrevista
    # -------------------------------------------------------------------------
    st.info("📋 Por favor, selecione uma opção para cada uma das perguntas organizadas nas seções abaixo:")

    respostas = {}

    for nome_secao, campos in SECOES.items():
        with st.expander(nome_secao, expanded=True):
            cols = st.columns(len(campos))
            for idx, campo in enumerate(campos):
                info_p = PERGUNTAS[campo]
                with cols[idx]:
                    st.markdown(f"**{info_p['pergunta']}**")
                    opcoes_chaves = list(info_p["opcoes"].keys())
                    escolha = st.radio(
                        label=f"Seleção para {campo}",
                        options=opcoes_chaves,
                        format_func=lambda k, campo=campo: info_p["opcoes"][k],
                        index=None,
                        key=f"input_{campo}",
                        label_visibility="collapsed",
                    )
                    respostas[campo] = escolha

    st.markdown("---")

    col_btn1, col_btn2 = st.columns([3, 1])

    with col_btn1:
        if st.button("🚀 Descobrir Minha Trilha", type="primary", use_container_width=True):
            campos_faltando = [c for c, v in respostas.items() if v is None]
            if campos_faltando:
                st.error(
                    f"⚠️ Por favor, responda a todas as 12 perguntas antes de continuar. "
                    f"Ainda restam {len(campos_faltando)} pergunta(s) sem resposta."
                )
            else:
                with st.spinner("Executando motor de inferência Experta (Forward Chaining)..."):
                    resultado = recomendar(respostas)
                    st.session_state["resultado"] = resultado
                    st.rerun()

    with col_btn2:
        if st.button("🧹 Limpar Seleções", use_container_width=True):
            st.session_state.clear()
            st.rerun()
