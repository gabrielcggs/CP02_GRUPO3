from src.prompt_builder import (
    montar_prompt,
    adicionar_exemplos,
    adicionar_cot
)

import json

with open(
    "prompts/system_prompts.json",
    "r",
    encoding="utf-8"
) as f:

    personas = json.load(f)


def zero_shot(tarefa, entrada):

    return montar_prompt(
        tarefa["instrucao"],
        "Nenhum contexto adicional",
        entrada,
        tarefa["formato_output"]
    )


def few_shot(tarefa, entrada, exemplos):

    prompt = montar_prompt(
        tarefa["instrucao"],
        "Use os exemplos",
        entrada,
        tarefa["formato_output"]
    )

    return adicionar_exemplos(prompt, exemplos)


def chain_of_thought(tarefa, entrada, passos):

    prompt = montar_prompt(
        tarefa["instrucao"],
        "Raciocine cuidadosamente",
        entrada,
        tarefa["formato_output"]
    )

    return adicionar_cot(prompt, passos)


def role_prompting(tarefa, entrada, persona):

    system = personas[persona]

    user = montar_prompt(
        tarefa["instrucao"],
        "Use sua experiência profissional",
        entrada,
        tarefa["formato_output"]
    )

    return system, user