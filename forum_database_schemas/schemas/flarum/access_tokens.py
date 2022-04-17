import typing as t
import sqlmodel as sql

from sqlalchemy import Column, Integer, ForeignKey
from datetime import datetime

if t.TYPE_CHECKING:
    from .users import FlarumUser



class FlarumAccessToken(sql.SQLModel, table=True):
    """
        A Flarum access token model.
    """

    __tablename__ = 'access_tokens'
    id: t.Optional[int] = sql.Field(default=None, primary_key=True)
    """ID of the access token."""

    token: str = sql.Field(max_length=40)
    """Access token."""
    user: t.Optional['FlarumUser'] = sql.Relationship(back_populates='access_tokens')
    """User associated with the access token."""
    user_id: int = sql.Field(index=True, sa_column=Column(Integer, ForeignKey('users.id', ondelete='CASCADE')))
    """ID of the user associated with the access token."""

    last_activity_at: datetime
    """Date and time when the access token was last used."""
    created_at:	datetime
    """Date and time when the access token was created."""

    type: str = sql.Field(max_length=100)
    """Type of the access token."""
    title: t.Optional[str] = sql.Field(max_length=150)
    """Title of the access token."""

    last_ip_address: t.Optional[str] = sql.Field(max_length=45)
    """IP address of the last user that used the access token."""
    last_user_agent: t.Optional[str] = sql.Field(max_length=255)
    """User agent of the last user that used the access token."""
