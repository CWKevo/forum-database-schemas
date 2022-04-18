import typing as t
import sqlmodel as sql

from sqlalchemy import Index
from datetime import datetime



class FlarumTagUser(sql.SQLModel, table=True):
    """
        A Flarum Tag <-> User relationship
    """

    __tableargs__ = (
        Index('tag_user_tag_id_foreign', 'tag_id'),
    )
    __tablename__ = 'tag_user'

    user_id: int = sql.Field(foreign_key='users.id', primary_key=True)
    """The user's ID."""
    tag_id: int = sql.Field(foreign_key='tags.id', primary_key=True)
    """The tag's ID."""

    marked_as_read_at: t.Optional[datetime]
    """When the user has marked all discussions under this tag as read."""
    is_hidden: bool = False
    """Whether the tag is hidden for the user(?)"""
