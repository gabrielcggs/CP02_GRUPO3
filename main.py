from src.tasks import tarefas
from src.techniques import (
    zero_shot,
    few_shot,
    chain_of_thought,
    role_prompting
)

from src.llm_client import LLMClient
from src.evaluator import medir_acuracia
from src.report import gerar_tabela

import json

client = LLMClient()

with open("data/inputs.json", "r", encoding="utf-8") as f:
    inputs = json.load(f)

resultados = []

for tarefa in tarefas:

    nome = tarefa["nome"]

    for item in inputs[nome]:

        entrada = item["input"]
        esperado = item["esperado"]

        tecnicas = {
            "Zero-Shot": zero_shot(tarefa, entrada),
            "Few-Shot": few_shot(
                tarefa,
                entrada,
                tarefa["exemplos_fewshot"]
            ),
            "CoT": chain_of_thought(
                tarefa,
                entrada,
                tarefa["passos_cot"]
            ),
            "Role": role_prompting(
                tarefa,
                entrada,
                tarefa["persona"]
            )
        }

        for tecnica, prompt in tecnicas.items():

            if tecnica == "Role":
                system, user = prompt
                resposta = client.chat(user, system=system)
            else:
                resposta = client.chat(prompt)

            acuracia = medir_acuracia(
                resposta["resposta"],
                esperado
            )

            resultados.append({
                "tarefa": nome,
                "tecnica": tecnica,
                "input": entrada,
                "resposta": resposta["resposta"],
                "esperado": esperado,
                "acuracia": acuracia,
                "tokens": resposta["tokens_prompt"]
            })

gerar_tabela(resultados)

print("Projeto executado com sucesso.")