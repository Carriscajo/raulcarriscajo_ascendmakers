from sqlalchemy.orm import Session
from app import models, schemas

#Products
def get_product(db: Session, product_id: int):
    return db.query(models.Product).fiter(models.Product.id == product_id).first()
def get_products(db: Session, skip: int = 0, limit: int = 20):
    return db.query(models.Product).offset(skip).limit(limit).all()
def create_product(db: Session, product:schemas.ProductCreate):
    db_product = models.Product(**product.dict())
    db.add(db_product)
    db.refresh(db_product)
    return db_product
#Warehouse
def get_warehouse(db: Session, warehouse_id: int):
    return db.query(models.Warehouse).fiter(models.Warehouse.id == warehouse_id).first()
def get_warehouses(db: Session, skip: int = 0, limit: int = 20):
    return db.query(models.Warehouse).offset(skip).limit(limit).all()
def create_warehouse(db: Session, warehouse:schemas.WarehouseCreate):
    db_warehouse = models.Warehouse(**warehouse.dict())
    db.add(db_warehouse)
    db.refresh(db_warehouse)
    return db_warehouse
#Deliveries
def get_delivery(db: Session, delivery_id: int):
    return db.query(models.Delivery).fiter(models.Delivery.id == delivery_id).first()
def get_deliveries(db: Session, skip: int = 0, limit: int = 20):
    return db.query(models.Delivery).offset(skip).limit(limit).all()
def create_delivery(db: Session, delivery:schemas.DeliveryCreate):
    db_delivery = models.Delivery(**delivery.dict())
    db.add(db_delivery)
    db.refresh(db_delivery)
    return db_delivery