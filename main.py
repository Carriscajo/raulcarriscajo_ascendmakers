from fastapi import FastAPI
from app.routes import produts, warehouse, routes, deliveries

app = FastAPI()

app.include_router(produts.router)
app.include_router(warehouse.router)
app.include_router(deliveries.router)
app.include_router(routes.router)

def read_root():
    return {"message": "Bienvenido a FastDelivery - Lider en Gestión de Entregas"}