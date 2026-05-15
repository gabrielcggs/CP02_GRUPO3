tarefas = [

    {
        "nome": "classificacao_sentimento",

        "tipo": "classificacao",

        "instrucao":
        "Classifique o sentimento.",

        "formato_output":
        "POSITIVO, NEGATIVO ou MISTO",

        "exemplos_fewshot": [
            {
                "input": "Excelente produto",
                "output": "POSITIVO"
            },
            {
                "input": "Produto horrível",
                "output": "NEGATIVO"
            }
        ],

        "passos_cot": [
            "Identifique pontos positivos",
            "Identifique pontos negativos",
            "Classifique"
        ],

        "persona": "analista_cx"
    }
]