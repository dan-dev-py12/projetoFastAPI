from fastapi import APIRouter #Importando o roteador de api



auth_router = APIRouter(prefix="/auth", tags=["auth"]) #cam auth que é o prefixo para todas as requests

@auth_router.get("/")
async def auth():
    """Essa é a rota padrao de autenticação"""
    return {"mensagem": "Rota padrao de autenticação", "autenticado": False} #retorna uma mensagem padrao de autenticação e um booleano falso
