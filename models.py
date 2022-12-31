# models.py

from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, Enum
from database import Base
import enum

class RingType(str, enum.Enum):
    loud = "Loudly"
    quiet = "Quietly"

class ShowInfo(Base):
    __tablename__ = "Shows"
    id = Column(Integer, primary_key=True, index=True)
    urlname = Column(String)
    title = Column(String)
    runtimewc = Column(Float)
    runtimewoc = Column(Float)
    islive = Column(String)
    premiere = Column(String)
    season_splits = Column(String)
    distributor = Column(String)
    streamers = Column(String)