from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import crud, models, schemas

router = APIRouter(
    prefix="/deliveries",
    tags=["deliveries"]
)

@router.post("/", response_model=schemas.Deliery)
def create_delivery(delivery: schemas.DeliveryCreate, db: Session = Depends(get_db)):
    return crud.create_delivery(db=db, delivery=delivery)

@router.post("/", response_model=schemas.Deliery)
def read_deliveries(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    deliveries = crud.get_deliveries(db,skip=skip, limit=limit)
    return deliveries