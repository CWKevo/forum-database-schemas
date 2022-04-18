import typing as t
import sqlmodel as sql

from sqlalchemy import Index, Column, Integer, ForeignKey
from datetime import datetime



class FlarumBadgeUser(sql.SQLModel, table=True):
    """
        Model for Flarum badge user.
    """

    __tablename__ = 'badge_user'
    __table_args__ = (
        Index('badge_user_user_id_foreign', "user_id"),
        Index('badge_user_badge_id_foreign', "badge_id"),
    )
    id: t.Optional[int] = sql.Field(primary_key=True)
    """The ID of the badge <-> user relationship."""

    user_id: int = sql.Field(sa_column=Column(Integer, ForeignKey('users.id', ondelete='CASCADE')))
    """The ID of the user."""
    badge_id: int = sql.Field(sa_column=Column(Integer, ForeignKey('badges.id', ondelete='CASCADE')))
    """The ID of the badge."""

    description: t.Optional[t.Text]
    """The description of the user's badge."""
    is_primary: bool = False
    """Whether the badge is the primary badge for the user."""
    assigned_at: datetime = datetime.now()
    """When was the badge assigned to the user?"""
