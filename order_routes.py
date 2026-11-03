from fastapi import APIRouter


order_router = APIRouter(prefix="/order", tags=["order"])

@order_router.get("/")
async def orders():
    """Essa é a rota padrao de pedidos, todas as rotas de pedidos precisam de autenticação"""
    return {"mensagem": "Listando todos os pedidos"}