import typing as t
import sqlmodel as sql

from sqlalchemy import Column, Integer, ForeignKey
from datetime import datetime

if t.TYPE_CHECKING:
    from .users import FlarumUser



class FlarumApiKey(sql.SQLModel, table=True):
    """
        A Flarum API key model.
    """
	
    __tablename__ = 'api_keys'
    id: t.Optional[int] = sql.Field(primary_key=True)
    """The ID of the API key"""
    key: str = sql.Field(max_length=100, sa_column_kwargs={'unique': True})
    """The API key"""

    allowed_ips: t.Optional[str] = sql.Field(max_length=255)
    """IPs allowed to use this key"""
    scopes: str = sql.Field(max_length=255)
    """The scopes of the API key"""

    user: 'FlarumUser' = sql.Relationship(back_populates='api_keys')
    """Do actions on behalf of this user."""
    user_id: t.Optional[int] = sql.Field(index=True, sa_column=Column(Integer, ForeignKey('users.id', ondelete='CASCADE')))
    """Do actions on behalf of this user (ID)."""

    created_at: datetime = datetime.now()
    """The date and time when the API key was created."""
    last_activity_at: t.Optional[datetime]
    """The date and time when the API key was last used."""
