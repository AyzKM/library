from sqlalchemy import create_engine, Column, Integer, VARCHAR, Sequence
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("postgresql://postgres:postgres@localhost:5432/rarity_db")
Base = declarative_base()

class Book(Base):

    __tablename__ = "Book"

    id = Column('id', Integer, primary_key = True)
    name = Column(VARCHAR(255), nullable = False)
    author = Column(VARCHAR(255), nullable = False)
    image = Column(VARCHAR(255))
    number_of_composition = Column(Integer)

Base.metadata.create_all(bind=engine)  