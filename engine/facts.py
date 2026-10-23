"""Definição das classes de Fatos (Fact) utilizadas pelo motor de inferência Experta.

Todos os fatos herdam de `experta.Fact` e representam as entidades de conhecimento
do sistema especialista: dados do usuário (Perfil), pontuações intermediárias (Pontuacao)
e o diagnóstico conclusivo (Recomendacao).
"""

import engine.compat  # Shim de retrocompatibilidade para Python 3.10+
from experta import Fact


class Perfil(Fact):
    """Fato que armazena as respostas coletadas na entrevista do usuário.

    Campos esperados:
        matematica (str): 'baixa', 'media', 'alta'
        atuacao (str): 'algoritmos_logica', 'layouts_visuais', 'servidores',
                       'dados_brutos', 'pipelines_dados', 'seguranca',
                       'automacao_deploy', 'testes_qualidade', 'negocio_produto',
                       'apps_celular', 'arquitetura_nuvem'
        ferramenta (str): 'python', 'javascript', 'backend_lang', 'mobile_lang',
                          'sql', 'linux_redes', 'nenhuma'
        entrega (str): 'produto_final', 'infraestrutura', 'seguranca',
                       'insights_previsoes', 'qualidade_confiabilidade',
                       'estrategia_produto', 'dados_confiaveis'
        estetica (str): 'baixa', 'media', 'alta'
        social (str): 'baixo', 'medio', 'alto'
        gosta_testar (str): 'sim', 'nao'
        interesse_mobile (str): 'sim', 'nao'
        terminal (str): 'baixo', 'medio', 'alto'
        ataque_defesa (str): 'sim', 'nao'
        foco_dados (str): 'modelagem', 'pipelines', 'nenhum'
        experiencia (str): 'iniciante', 'intermediario', 'avancado'
    """
    pass


class Pontuacao(Fact):
    """Fato intermediário gerado quando uma regra de produção é disparada.

    Atributos:
        trilha (str): Identificador canônico da trilha beneficiada.
        pontos (int): Valor numérico da pontuação concedida (1 a 5).
        regra_id (str): Identificador formal da regra (ex: 'R01', 'R12').
        motivo (str): Explicação em linguagem natural que justifica o disparo.
    """
    pass


class Recomendacao(Fact):
    """Fato conclusivo produzido pela regra final de tomada de decisão.

    Atributos:
        trilha (str): Identificador da trilha mais indicada para o usuário.
        segunda_opcao (str): Identificador da segunda trilha mais pontuada.
    """
    pass
