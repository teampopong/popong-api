from datetime import datetime
from sqlalchemy import Column, Integer, Text, DateTime

from popong_models import Base


class ApiKey(Base):
    __tablename__ = 'api_key'

    key = Column(Text, primary_key=True)
    user_id = Column(Text, index=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

