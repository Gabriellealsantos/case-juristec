from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()


class Cliente(Base):
    """Modelo ORM para a tabela de clientes."""

    __tablename__ = 'clientes'

    id_cliente = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(255), nullable=False)
    estado = Column(String(2), nullable=False)

    processos = relationship("Processo", back_populates="cliente")


class Processo(Base):
    """Modelo ORM para a tabela de processos."""

    __tablename__ = 'processos'

    id_processo = Column(Integer, primary_key=True, autoincrement=True)
    id_cliente = Column(Integer, ForeignKey('clientes.id_cliente'), nullable=False)
    assunto = Column(String(255), nullable=False)
    data_abertura = Column(Date, nullable=False)

    cliente = relationship("Cliente", back_populates="processos")


if __name__ == "__main__":
    print("Modelos 'Cliente' e 'Processo' mapeados com sucesso!")
    print("Pronto para serem instanciados ou sincronizados com o banco.")
