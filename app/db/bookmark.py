from sqlalchemy import enum
from sqlalchemy import Column, String ,Integer,  Text, DateTime , func, ForeignKey
from sqlalchemy.dialects.postgresql import UUID ,ARRAY , JSONB
from app.db.database import Base

class BookmarkType(enum.Enum):
    twitter = "twitter"
    article = "article"
    weblink = "weblink"
    newsletter = "newsletter"
    saved_email = "saved_email"
    important_email = "important_email"
    pdf = "pdf"
    
class Bookmark(Base):
    __tablename__ = "bookmarks"
    
    id = Column(
        UUID(as_uuid = True),
        primary_key=True,
        index = True,
        server_default=func.gen_random_uuid()
    )
    
    name = Column(String, nullable=False)
    link = Column(Text, nullable=False, unique=True)
    tags = Column(ARRAY(String), nullable=False)
    bookmark_type = Column(Enum(BookmarkType), nullable=False)
    
    created_at = Column(
        
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now()
    )
    
    updated_at = Column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        onupdate=func.now()
    )
    
    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id" , ondelete="CASCADE" ),
        nullable=False
    )

__table_args__ = (
        UniqueConstraint("link", "user_id", name="uq_user_bookmark"),
    )