from datetime import datetime
from uuid import UUID, uuid4

from pgvector.sqlalchemy import Vector
from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Text,
)
from sqlalchemy.dialects.postgresql import JSONB, UUID as PG_UUID
from sqlalchemy.orm import relationship

from app.database.connection import Base


# ==========================================
# Embedding Configuration
# ==========================================

# all-MiniLM-L6-v2 produces 384 dimensions
EMBEDDING_DIMENSION = 384


# ==========================================
# Documents Table
# ==========================================

class Document(Base):
    """
    Stores uploaded document information.
    """

    __tablename__ = "documents"

    id = Column(
        PG_UUID(as_uuid=True),
        primary_key=True,
        default=uuid4,
        index=True,
    )

    filename = Column(
        String(255),
        nullable=False,
        index=True,
    )

    file_type = Column(
        String(50),
        nullable=False,
    )

    file_size = Column(
        Integer,
        nullable=True,
    )

    metadata_ = Column(
        "metadata",
        JSONB,
        nullable=True,
        default=dict,
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )

    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False,
    )

    # Relationship
    chunks = relationship(
        "DocumentChunk",
        back_populates="document",
        cascade="all, delete-orphan",
    )

    def __repr__(self):
        return (
            f"<Document "
            f"id={self.id} "
            f"filename={self.filename}>"
        )


# ==========================================
# Document Chunks Table
# ==========================================

class DocumentChunk(Base):
    """
    Stores chunks extracted from documents
    along with vector embeddings.
    """

    __tablename__ = "document_chunks"

    id = Column(
        PG_UUID(as_uuid=True),
        primary_key=True,
        default=uuid4,
        index=True,
    )

    document_id = Column(
        PG_UUID(as_uuid=True),
        ForeignKey(
            "documents.id",
            ondelete="CASCADE",
        ),
        nullable=False,
        index=True,
    )

    chunk_index = Column(
        Integer,
        nullable=False,
    )

    content = Column(
        Text,
        nullable=False,
    )

    embedding = Column(
        Vector(EMBEDDING_DIMENSION),
        nullable=True,
    )

    metadata_ = Column(
        "metadata",
        JSONB,
        nullable=True,
        default=dict,
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )

    # Relationship
    document = relationship(
        "Document",
        back_populates="chunks",
    )

    def __repr__(self):
        return (
            f"<DocumentChunk "
            f"id={self.id} "
            f"document_id={self.document_id} "
            f"chunk_index={self.chunk_index}>"
        )