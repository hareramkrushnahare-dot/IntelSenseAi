from sqlalchemy import Column, Integer, String, DateTime, func
from app.database.base import Base


class AuditLog(Base):
    __tablename__ = "audit_logs"
    id = Column(Integer, primary_key=True)
    action = Column(String(255))
    detail = Column(String(2000))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
