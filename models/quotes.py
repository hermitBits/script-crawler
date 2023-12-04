import uuid

from models.base import Base

from sqlalchemy import types
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column



class Quotes(Base):
    __tablename__ = 'quotes'

    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str]
    by: Mapped[str]
    tags: Mapped[str]
    batch: Mapped[uuid.UUID] = mapped_column(types.Uuid)