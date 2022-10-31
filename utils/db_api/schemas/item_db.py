from sqlalchemy import Column, Integer, String, sql, Sequence

from utils.db_api.db_gino import TimedBaseModel


class Item(TimedBaseModel):
    __tablename__ = 'items'

    id = Column(Integer, Sequence("user_id_seq"), primary_key=True)
    category_name = Column(String(50))
    name = Column(String(50))
    type = Column(String(50))
    dops = Column(String(50))
    price = Column(Integer)


    query: sql.select
