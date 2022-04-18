import typing as t
import sqlmodel as sql

from sqlalchemy import Column, Integer, ForeignKey, Index
from datetime import datetime

if t.TYPE_CHECKING:
    from .users import FlarumUser



class FlarumBannedIp(sql.SQLModel, table=True):
    """
        A Flarum model for banned IP.
    """
	
    __tableargs__ = (
        Index('banned_ips_address_unique', 'address', unique=True),
        Index('banned_ips_user_id_foreign', 'user_id'),
    )
    __tablename__ = 'banned_ips'
    id: t.Optional[int] = sql.Field(primary_key=True)
    """The ID of the banned IP record"""

    creator: 'FlarumUser' = sql.Relationship(back_populates='given_ip_bans', sa_relationship_kwargs={"primaryjoin": "FlarumBannedIp.creator_id==FlarumUser.id", "lazy": "joined"})
    """The user who created the banned IP record"""
    creator_id: int = sql.Field(sa_column=Column(Integer, ForeignKey('users.id', ondelete='CASCADE')))
    """The ID of the user who created the banned IP record"""

    address: str = sql.Field(max_length=191)
    """The IP address that was banned."""
    reason: t.Optional[str] = sql.Field(max_length=255)
    """The reason why the IP was banned."""

    user: 'FlarumUser' = sql.Relationship(sa_relationship_kwargs={"primaryjoin": "FlarumBannedIp.user_id==FlarumUser.id", "lazy": "joined"})
    """The user who banned the IP address"""
    user_id: int = sql.Field(foreign_key='users.id')
    """The ID of the user who banned the IP address."""

    created_at: datetime = datetime.now()
    """The date and time when the banned IP record was created."""
