from sqlalchemy import Column, Integer, String, sql, Sequence, BigInteger

from utils.db_api.db_gino import TimedBaseModel



class Order(TimedBaseModel):
    __tablename__ = 'orders'
    order_id = Column(BigInteger, Sequence("user_id_seq"), primary_key=True)
    telegtam_id = Column(BigInteger, primary_key=True)
    username = Column(String(150))
    first_name = Column(String(150))
    order_set = Column(String(500))
    accepting = Column(String(50))




    query: sql.select