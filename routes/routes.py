from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Warehouse, Delivery

router = APIRouter(
    prefix="routes",
    tags=["routes"]
)

def get_optimal_route(deliveries: list[int], warehouse_id: int, db: Session = Depends(get_db)):
    #obtener las coordenadas de las entregas y del alamacen
    deliveries_object = db.query(Delivery).filter(Delivery.id.in_(deliveries)).all()
    warehouse = db.query(Warehouse).filter(Warehouse.id.in_(warehouse)).first()

    if not warehouse:
        raise HTTPException(status_code=404, detail="Warehouse not Found")
    
    optimal_route = estiamte_route(deliveries_object, warehouse)

def estiamte_route(deliveries, warehouse):
    ## Logica comentada en el ReadMe.md
    return deliveries