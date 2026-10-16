from fastapi import FastAPI

NOTIFICACAO = FastAPI()

@NOTIFICACAO.get("/")
async def index():
    return {"servico": "notificacao"}

@NOTIFICACAO.post("/notificar")
async def notificar(id: int, titulo: str):
    print(f"Tarefa '{titulo}' (id={id}) finalizada!")
    return {"mensagem": "OK"}