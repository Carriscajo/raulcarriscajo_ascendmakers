from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from app.database import Base

class Producto(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

class Warehouse(Base):
    __tablename__ = "warehouses"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    latitud = Column(Float)
    longitud = Column(Float)
    productos = relationship("Products", secondary="warehouse_products")
class Delivery(Base):
    __tablename__ = "deliveries"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    latitud = Column(Float)
    longitud = Column(Float)

almacen_producto = Table(
    "warehouse_products",
    Base.metadata,
    Column("warehouse_id", Integer, ForeignKey("warehouse.id")),
    Column("product_id", Integer, ForeignKey("product.id"))
)