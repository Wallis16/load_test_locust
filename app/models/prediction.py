from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func
from app.database import Base

class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)
    prediction = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())