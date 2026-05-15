def montar_prompt(
    instrucao,
    contexto,
    input_dados,
    formato_output
):

    prompt = f"""
INSTRUÇÃO:
{instrucao}

CONTEXTO:
{contexto}

DADOS:
{input_dados}

FORMATO:
{formato_output}
"""

    return prompt


def adicionar_exemplos(prompt, exemplos):

    texto = "\nEXEMPLOS:\n"

    for exemplo in exemplos:

        texto += f"""
Input: {exemplo['input']}
Output: {exemplo['output']}
"""

    return prompt + texto


def adicionar_cot(prompt, passos):

    texto = "\nPENSE PASSO A PASSO:\n"

    for i, passo in enumerate(passos, start=1):

        texto += f"{i}. {passo}\n"

    return prompt + texto