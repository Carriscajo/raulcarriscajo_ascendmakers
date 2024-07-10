from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import crud, models, schemas

router = APIRouter(
    prefix="/products",
    tags=["products"]
)

@router.post("/", response_model=schemas.Product)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db=db, product=product)

@router.post("/", response_model=schemas.Product)
def read_products(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    products = crud.get_products(db,skip=skip, limit=limit)
    return products