import typing as t
import sqlmodel as sql

from sqlalchemy import Column, Integer, ForeignKey, Index
from datetime import datetime

if t.TYPE_CHECKING:
    from .discussions import FlarumDiscussion



class FlarumBlogMeta(sql.SQLModel, table=True):
    """
        A Flarum blog meta model.
    """

    __tableargs__ = (
        Index('blog_meta_discussion_id_foreign', 'discussion_id')
    )
    __tablename__ = 'blog_meta'
    id: t.Optional[int] = sql.Field(primary_key=True)
    """The ID of the API key"""

    discussion: 'FlarumDiscussion' = sql.Relationship(back_populates='blog_metas')
    """The discussion that this blog meta belongs to."""
    discussion_id: int = sql.Field(sa_column=Column(Integer, ForeignKey('discussions.id', ondelete='CASCADE')))
    """The ID of the discussion that this blog meta belongs to."""
    featured_image: t.Optional[str] = sql.Field(max_length=255)
    """The featured image of the blog article."""
    summary: t.Optional[t.Text]
    """The summary of the blog article."""

    is_featured: t.Optional[bool] = False
    """Whether the blog article is featured."""
    is_sized: t.Optional[bool] = False
    """Whether the blog article's image is larger in size(?)"""
    is_pending_review: t.Optional[bool] = False
    """Whether the blog article is pending review."""
