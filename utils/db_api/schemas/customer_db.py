from sqlalchemy import Column, String, sql, BigInteger

from utils.db_api.db_gino import TimedBaseModel


class Customer(TimedBaseModel):
    __tablename__ = 'customers'

    username = Column(String(150))
    first_name = Column(String(150))
    last_name = Column(String(150))
    telegtam_id = Column(BigInteger, primary_key=True)
    status = Column(String(50))

    query: sql.select
