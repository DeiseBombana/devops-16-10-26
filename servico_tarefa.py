from fastapi import FastAPI
from datetime import datetime

APP = FastAPI()

TAREFAS = []

# Estrutura da tarefa
"""
{
    "id": int,uvicorn servico_notificacao:APP --port 8002 --reload
    "titulo": str,
    "descricao": str,
    "concluida": bool,
    "criada_em": datetime,
    "concluida_em": datetime | None
}
"""


def criar_tarefa(titulo, descricao):
    return {
        "id": len(TAREFAS),
        "titulo": titulo,
        "descricao": descricao,
        "concluida": False,
        "criada_em": datetime.now(),
        "concluida_em": None
    }


# GET /tarefas
@APP.get("/tarefas")
async def listar_tarefas():

    lista = []

    for tarefa in TAREFAS:
        lista.append({
            "id": tarefa["id"],
            "titulo": tarefa["titulo"]
        })

    return lista


# POST /tarefas
@APP.post("/tarefas")
async def criar(titulo: str, descricao: str):

    tarefa = criar_tarefa(titulo, descricao)

    TAREFAS.append(tarefa)

    return {
        "mensagem": "Tarefa criada",
        "tarefa": tarefa
    }


# GET /tarefas/{id}
@APP.get("/tarefas/{id}")
async def consultar_tarefa(id: int):

    for tarefa in TAREFAS:
        if tarefa["id"] == id:
            return tarefa

    return {"mensagem": "Tarefa não existe"}


# PUT /tarefas/{id}
@APP.put("/tarefas/{id}")
async def concluir_tarefa(id: int):

    for tarefa in TAREFAS:
        if tarefa["id"] == id:

            tarefa["concluida"] = True
            tarefa["concluida_em"] = datetime.now()

            return {
                "mensagem": "Tarefa concluída",
                "tarefa": tarefa
            }

    return {"mensagem": "Tarefa não existe"}


# DELETE /tarefas/{id}
@APP.delete("/tarefas/{id}")
async def apagar_tarefa(id: int):

    for indice, tarefa in enumerate(TAREFAS):

        if tarefa["id"] == id:
            TAREFAS.pop(indice)

            return {
                "mensagem": "Tarefa apagada"
            }

    return {"mensagem": "Tarefa não existe"}


@APP.get("/")
async def index():
    return {"servico": "tarefa"}