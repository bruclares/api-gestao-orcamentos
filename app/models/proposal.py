import uuid
from sqlalchemy import Column, String, ForeignKey, DateTime, Float
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import enum
from app.db.base_class import Base

class ProposalStatus(str, enum.Enum):
    DRAFT = "draft" # rascunho
    SENT = "sent" # enviada
    ACCEPTED = "accepted" # aceita
    REJECTED = "rejected" # recusada

class Proposal(Base):
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)

    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    client_id = Column(UUID(as_uuid=True), ForeignKey("client.id"), nullable=False)

    title = Column(String, nullable=False)
    description = Column(String)
    total_value = Column(Float, nullable=False)
    status = Column(String, default=ProposalStatus.DRAFT, nullable=False)

    pdf_path = Column(String)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    deleted_at = Column(DateTime(timezone=True), nullable=True)

    client = relationship("Client", back_populates="proposals")
    user = relationship("User", back_populates="proposals")