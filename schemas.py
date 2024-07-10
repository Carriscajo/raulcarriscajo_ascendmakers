from pydantic import BaseModel
from typing import List

##BASES
class ProductBase(BaseModel):
    name: str
class WarehouseBase(BaseModel):
    name: str
    latitude: float
    longitude: float
class DeliveryBase(BaseModel):
    name: str
    latitude: float
    longitude: float

##CREATE
class ProductCreate(ProductBase):
    pass
class WarehouseCreate(WarehouseBase):
    pass
class DeliveryCreate(DeliveryBase):
    pass

##PRINCIPAL
class Product(ProductBase):
    id: int
    class Config:
        orm_model = True
class Warehouse(WarehouseBase):
    id: int
    products: List[Product] = []
    class Config:
        orm_model = True
class Delivery(DeliveryBase):
    id: int
    class Config:
        orm_model = True
