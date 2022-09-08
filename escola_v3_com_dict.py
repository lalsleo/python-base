#!/usr/bin/env python3
"""Exibe relatório de crianças por atividade.

Imprimir a lista de crianças agrupadas por sala
que frequentas cada uma das atividades.
"""
__version__ = "0.1.0"

from pprint import pprint

# Dados
salas = {
    "sala1":["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"],
    "sala2": ["Joao", "Antonio", "Carlos", "Maria", "Isolda"],
}

aulas = {
    "ingles": ["Erik", "Maia","Joana", "Carlos", "Antonio"],
    "musica": ["Erik", "Carlos", "Maria"],
    "danca": ["Gustavo", "Sofia", "Joana", "Antonio"],
}

for aula in aulas:

    print(f"Alunos da atividade {aula}\n")
    print("-" * 40)

    atividade_sala1 = set(salas["sala1"]) & set(aulas[aula])
    atividade_sala2 = set(salas["sala2"]) & set(aulas[aula])

    print("Sala1 ", atividade_sala1)
    print("Sala2 ", atividade_sala2)

    print()
    print("#" * 40) 
      