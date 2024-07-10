from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import crud, models, schemas

router = APIRouter(
    prefix="/warehouses",
    tags=["warehouses"]
)

@router.post("/", response_model=schemas.Warehouse)
def create_warehouse(warehouse: schemas.WarehouseCreate, db: Session = Depends(get_db)):
    return crud.create_warehouse(db=db, warehouse=warehouse)

@router.post("/", response_model=schemas.Warehouse)
def read_warehouses(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    warehouses = crud.get_warehouses(db,skip=skip, limit=limit)
    return warehouses