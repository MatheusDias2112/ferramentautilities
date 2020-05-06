# -*- coding: utf-8 -*-

allowed_languages = ['en', 'pt']

def find_language_in_url(url):
    for lang in allowed_languages:
        n_found = 0 
        if f'/{lang}/' in url:
            n_found += 1
            selected_language = lang
        else:
            selected_language = allowed_languages[0]

    if n_found > 1:
        raise ValueError('More than one language found')

    return selected_language


url_names = {
    'root': {'en': 'collections_app', 'pt': 'app_cobranca'}, 
    'introduction': {'en': 'introduction', 'pt': 'resumo'}, 
    'data_input': {'en': 'data_input', 'pt': 'input_de_dados'}, 
    'delinquecy_analysis': {'en': 'delinquecy_analysis', 'pt': 'analise_inadimplencia'}, 
    'covid_impacts': {'en': 'covid_impacts', 'pt': 'impactos_covid'}, 
    'expected_results': {'en': 'expected_results', 'pt': 'resultados_esperados'},
    'credit_risk': {'en': 'credit_risk', 'pt': 'risco_de_credito'}, 
    'effectiveness': {'en': 'effectiveness', 'pt': 'efetividade'}, 
    'filtering_module': {'en': 'filtering_module', 'pt': 'modulo_de_filtragem'}, 
    'action_optimization': {'en': 'action_optimization', 'pt': 'otimizacao_acoes'}, 
    'routing': {'en': 'routing', 'pt': 'roteirizacao'}
}

tab_names = {
    'introduction': {'en': 'Introduction', 'pt': 'Introdução'}, 
    'data_input': {'en': 'Data input', 'pt': 'Input de dados'}, 
    'delinquecy_analysis': {'en': 'Delinquency analysis', 'pt': 'Análise da inadimplência'}, 
    'covid_impacts': {'en': 'Covid impacts', 'pt': 'Impactos Covid'}, 
    'expected_results': {'en': 'Expected results', 'pt': 'Resultados esperados'}, 
    'credit_risk': {'en': 'Credit risk prediction', 'pt': 'Previsão risco de crédito'},
    'effectiveness': {'en': 'Effectiveness prediction', 'pt': 'Previsão efetividade'}, 
    'filtering_module': {'en': 'Filtering module', 'pt': 'Módulo de filtragem'}, 
    'action_optimization': {'en': 'Action optimization', 'pt': 'Otimização das ações'}, 
    'routing': {'en': 'Field team routing', 'pt': 'Roteirização'},
}

pages = {}

# p_01_introduction
pages['introduction'] = {
    'en': {
        'titles': ['Solution overview'],
        'texts': [
            'The solution is composed of 5 building blocks, as ilustrated below. These are:',
            'Credit risk prediction',
            'This module predicts the probability that the client will remain delinquent for another 3 months',
            'Effectiveness prediction',
            'This module predicts the probability that the client will pay his bills if he receives each of the available collection actions',
            'Filtering module',
            'This module is responsible for applying business rules, for example, determining which clients cannot receive some or all of the collection actions',
            'Action optimization',
            'This module uses optimization to select the best way to collect from clients, given the credit risk and effectiveness predictions',
            'Field team routing',
            'This module optimizes routes for field collection actions - namely client visits and energy disconections',
        ],
        'images': ['model_structure_en.png']
    },
    'pt': {
        'titles': ['Resumo da solução'],
        'texts': [
            'Esta solução é composta de 5 blocos principais, como ilustrado abaixo. Eles são:',
            'Modelo de predição do risco de crédito',
            'Esse módulo prevê a probabilidade de que o cliente continuará inadimplente por mais 3 meses',
            'Modelo de previsão da efetividade',
            'Esse módulo prevê a probabilidade de o cliente quitar seu débito, caso ele receba cada uma das ações de cobrança disponíveis',
            'Módulo de filtragem',
            'Esse módulo é responsável por aplicar regras de negócio, em particular em relação aos clientes que podem receber cada ação de cobrança',
            'Otimização das ações de cobrança',
            'Esse módulo de otimização seleciona a melhor forma de cobrar os clientes, considerando um orçamento, número de ações, as ações disponíveis e as predições dos modelos',
            'Roteirização das ações de campo',
            'Esse módulo otimiza rotas para as ações de cobrança realizadas no campo, principalmente o corte',
        ],
        'images': ['model_structure_pt.png']
    }
}
pages['data_input'] = {
    'en': {},
    'pt': {}
}
pages['delinquecy_analysis'] = {
    'en': {},
    'pt': {}
}
pages['covid_impacts'] = {
    'en': {},
    'pt': {}
}
pages['expected_results'] = {
    'en': {},
    'pt': {}
}
pages['credit_risk'] = {
    'en': {
        'titles': [
            'Module description', 
            'This module uses machine learning algorithms to determine the probability that the client will remain delinquent, assuming that he receives no collection actions.', 
            'Model results visualization'
        ],
        'graph_titles': [
            'Total owed broken by credit risk and customer class',
            'Number of customers broken by credit risk and customer class',
            'Credit risk histogram', 
            'Credit risk vs. total owed', 
            'Total owed broken by credit risk and amount owed',
            'Number of customers broken by credit risk and amount owed'
        ],
        'texts': [
            'Select the client class to show', 
            'Select the city to show'
        ]
    },
    'pt': {
        'titles': [
            'Descrição do módulo', 
            'Esse módulo usa algoritmos de aprendizado supervisionado para estimar a probabilidade de o cliente continuar inadimplente se não receber ações de cobrança', 
            'Visualização dos resultados do módulo'
        ],
        'graph_titles': [
            'Total devido quebrado por risco de crédito e classe', 
            'Número de clientes quebrado por risco de crédito e classe',
            'Histograma do risco de crédito', 
            'Risco de crédito vs. total devido', 
            'Total devido quebrado por risco de crédito e total devido', 
            'Número de clientes quebrado por risco de crédito e total devido'
        ],
        'texts': [
            'Selecione a classe para mostrar', 
            'Selecione a cidade para mostrar'
        ]
    }
}
pages['effectiveness'] = {
    'en': {
         'titles': [
            'Module description', 
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.', 
            'Model Effectiveness Visualization'
        ],
        'graph_titles': [
            'Efetividade das Cobranças - Previsto e Realizado',
            'Contribuição - Classes e Ações',
            'Efetividade Prevista da Ação - Filtros', 
        ],
        'texts': [
            'Select Credit Risk Level',
            'Select the client class to show', 
            'Select the city to show'
        ]
    },
    'pt': {'titles': [
            'Descrição do Módulo', 
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.', 
            'Visualização da Efetividade do Modelo'
        ],
        'graph_titles': [
            'Efetividade das Cobranças - Previsto e Realizado',
            'Contribuição - Classes e Ações',
            'Efetividade Prevista da Ação - Filtros', 
        ],
        'texts': [
            'Selecione o Risco de Crédito',
            'Selecione a Classe do Cliente', 
            'Selecione o Saldo da Ação'
        ]}
}
pages['filtering_module'] = {
    'en': {  'titles': [
            'Module description', 
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.', 
            'Model Effectiveness Visualization'
        ],
        'graph_titles': [
            'Efetividade das Cobranças - Previsto e Realizado',
            'Contribuição - Classes e Ações',
            'Efetividade Prevista da Ação - Filtros', 
        ],
        'texts': [
            'Select Credit Risk Level',
            'Select the client class to show', 
            'Select the city to show'
        ]
    },
    'pt':  {'titles': [
            'Descrição do Módulo', 
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.', 
            'Visualização do Módulo de Filtragem'
        ],
        'graph_titles': [
            'Número de Clientes que podem receber cada tipo de ação',
            'Porcentagem de clientes que podem receber cada tipo de ação',
            'Número de Clientes com ação escolhida', 
        ],
        'texts': [
            'Selecione o tipo de ação'
        ]
    }
}
pages['action_optimization'] = {
    'en': {},
    'pt': { 'titles': [
            'Descrição do Módulo', 
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.', 
            'Visualização do Módulo de Filtragem'
        ],
        'graph_titles': [
            'Receita e Custo por Ação',
            'Quantidade de Ações',
            'Efetividade por Ação',
            'Risco Médio por Ação' 
        ],
        'texts': [
            'Selecione a quantidade de um ação',
            'Selecione o tipo de ação',
            'Selecione um intervalo de valor para todas as ações:'
        ]
    }
}
pages['routing'] = {
    'en': {},
    'pt': {'titles': [
            'Descrição do Módulo', 
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.', 
            'Visualização do Módulo de Filtragem'
        ],
        'graph_titles': [
            'Selecione uma Cidade',
            'Selecione uma Equipe',
            'Mapa da Cidade', 
            'Mapa da Equipe'
        ],
        'texts': [
            'Selecione a quantidade de um ação',
            'Selecione o tipo de ação',
            'Selecione um intervalo de valor para todas as ações:'
        ]}
}



# Check if every text is in every language
all_translation_dicts = [url_names]

for language in allowed_languages:
    for translation_dict in all_translation_dicts:
        for item in translation_dict.values():
            try: 
                translation = item[language]
            except: 
                raise ValueError(f'The translation dict {item} does not have the language {language}')

def check_deep_structure(obj_1, obj_2):
    found_different_structure = 0
    if type(obj_1) != type(obj_2):
        found_different_structure += 1
    if isinstance(obj_1, list):
        if len(obj_1) != len(obj_2):
            found_different_structure += 1
        else: 
            found_different_structure += sum([check_deep_structure(a, b) for a, b in zip(obj_1, obj_2)])
    if isinstance(obj_1, dict):
        if obj_1.keys() != obj_2.keys():
            found_different_structure += 1
        else: 
            found_different_structure += sum([check_deep_structure(a, b) for a, b in zip(obj_1.values(), obj_2.values())])
    return found_different_structure


all_translation_dicts = list(pages.values())
for translation_dict in all_translation_dicts:
    for language_1 in translation_dict.keys():
        for language_2 in translation_dict.keys():
            if check_deep_structure(translation_dict[language_1], translation_dict[language_2]) > 0:
                # raise ValueError(f'\n\n{language_1} and {language_2} translations are incompatible in {translation_dict}')
                pass


