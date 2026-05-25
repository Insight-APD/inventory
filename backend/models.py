from sqlalchemy import Column, Integer, String, Text
from database import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    sku = Column(String)
    category = Column(String)
    quantity = Column(Integer)
    description = Column(Text)