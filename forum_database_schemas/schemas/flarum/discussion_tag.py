import typing as t
import sqlmodel as sql

from sqlalchemy import Index
from datetime import datetime



class FlarumDiscussionTag(sql.SQLModel, table=True):
    """
        A Flarum Discussion <-> Tag relationship
    """

    __tableargs__ = (
        Index('discussion_tag_tag_id_foreign', 'tag_id'),
    )
    __tablename__ = 'discussion_tag'

    discussion_id: int = sql.Field(foreign_key='discussions.id', primary_key=True)
    """The ID of the discussion that has the tag."""
    tag_id: int = sql.Field(foreign_key='tags.id', primary_key=True)
    """The tag's ID."""

    marked_as_read_at: t.Optional[datetime]
    """When the user has marked all discussions under this tag as read."""
    is_hidden: bool = False
    """Whether the tag is hidden for the user(?)"""
