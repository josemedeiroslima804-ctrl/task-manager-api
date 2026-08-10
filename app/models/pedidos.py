from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base

class Pedido(Base):

    __tablename__ = "pedidos"
    
    id = Column(Integer, primary_key=True)

    cliente_id = Column(
        Integer,
         ForeignKey("clientes.id"),
            nullable=False
            )
    
    produto_id = Column(
        Integer, 
        ForeignKey("produtos.id"),
          nullable=False
          )
    
    quantidade = Column(Integer, nullable=False)


    cliente = relationship("Cliente", back_populates="pedidos")


    produto = relationship("Produto", back_populates="pedidos")