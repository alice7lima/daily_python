from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from sqlalchemy import create_engine
from models import Produto, Fornecedor
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

DB_CONN_URL = os.getenv("DB_CONN_URL")

# Base = declarative_base()

engine = create_engine(DB_CONN_URL, echo=True)

Session = sessionmaker(bind=engine)
session = Session()

resultado = (
    session.query(Fornecedor.nome, func.sum(Produto.preco).label("total_preco"))
    .join(Produto, Fornecedor.id == Produto.fornecedor_id)
    .group_by(Fornecedor.nome)
    .all()
)

for nome, total_preco in resultado:
    print(f"Fornecedor: {nome}, Total Preço: {total_preco}")