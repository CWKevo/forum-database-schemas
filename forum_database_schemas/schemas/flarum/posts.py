import typing as t
import sqlmodel as sql

from sqlalchemy import Index, Column, Integer, ForeignKey
from datetime import datetime

if t.TYPE_CHECKING:
    from .discussions import FlarumDiscussion
    from .users import FlarumUser



class FlarumPost(sql.SQLModel, table=True):
    """
        Model for Flarum post.
    """

    __tablename__ = 'posts'
    __table_args__ = (
        Index('posts_edited_user_id_foreign', "edited_user_id"),
        Index('posts_hidden_user_id_foreign', "hidden_user_id"),
        Index('posts_shadow_hidden_at_index', "shadow_hidden_at"),
        Index('posts_discussion_id_number_unique', "discussion_id", "number", unique=True),
        Index('posts_discussion_id_number_index', "discussion_id", "number"),
        Index('posts_discussion_id_created_at_index', "discussion_id", "created_at"),
        Index('posts_user_id_created_at_index', "user_id", "created_at"),
        Index('content', "content", mysql_prefix="FULLTEXT"),
    )
    id: t.Optional[int] = sql.Field(primary_key=True)
    """The ID of the post."""

    discussion: 'FlarumDiscussion' = sql.Relationship(back_populates='posts', sa_relationship_kwargs={"primaryjoin": "FlarumPost.discussion_id==FlarumDiscussion.id", "lazy": "joined", "cascade": "all, delete"})
    """The discussion the post belongs to."""
    discussion_id: int = sql.Field(sa_column=Column(Integer, ForeignKey("discussions.id", ondelete="CASCADE")))
    """The ID of the discussion the post belongs to."""
    number: t.Optional[int]
    """The number/position of the post in the discussion thread."""


    created_at: datetime = datetime.now()
    """When was this post created at?"""
    user: t.Optional['FlarumUser'] = sql.Relationship(back_populates='posts', sa_relationship_kwargs={"primaryjoin": "FlarumPost.user_id==FlarumUser.id", "lazy": "joined"})
    """The author of the post."""
    user_id: t.Optional[int] = sql.Field(foreign_key='users.id')
    """The ID of the post's author."""
    type: t.Optional[str] = sql.Field(default='comment', max_length=100)
    """The type of the post. `comment` for standard reply or `discussionLocked` for "discussion locked" messages, etc..."""
    content: t.Optional[t.Text]
    """The HTML/XML content of the post."""


    edited_at: t.Optional[datetime]
    """When was the post edited at (if it was)?"""
    edited_user: t.Optional['FlarumUser'] = sql.Relationship(sa_relationship_kwargs={"primaryjoin": "FlarumPost.edited_user_id==FlarumUser.id", "lazy": "joined"})
    """Who edited the post?"""
    edited_user_id: t.Optional[int] = sql.Field(foreign_key='users.id')
    """The ID of the user who edited the post."""

    hidden_at: t.Optional[datetime]
    """When was the post hidden at (if it was)?"""
    hidden_user: t.Optional['FlarumUser'] = sql.Relationship(sa_relationship_kwargs={"primaryjoin": "FlarumPost.hidden_user_id==FlarumUser.id", "lazy": "joined"})
    """Who hid the post?"""
    hidden_user_id: t.Optional[int] = sql.Field(foreign_key='users.id')
    """The ID of the user who hid the post."""


    ip_address: t.Optional[str] = sql.Field(max_length=45)
    """The IP address of the user who created the post."""
    is_private: bool = False
    """Whether the post is private."""
    is_approved: bool = True
    """Whether the post is approved."""

    emailed: bool = False
    """Whether the post has been emailed(?)"""
    auto_mod: bool = False
    """Whether the post was auto-moderated(?)"""

    posted_on: t.Optional[str] = sql.Field(max_length=255)
    """The date/time the post was posted on."""
    shadow_hidden_at: t.Optional[datetime]
    """When was the post shadow hidden at (if it was)?"""
