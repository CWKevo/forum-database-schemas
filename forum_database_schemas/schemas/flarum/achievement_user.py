import typing as t
import sqlmodel as sql

from datetime import datetime



class FlarumAchievementUser(sql.SQLModel, table=True):
    """
        Model for achievement <-> user relationship.

        https://discuss.flarum.org/d/26675
    """

    __tablename__ = 'achievement_user'
    id: t.Optional[int] = sql.Field(default=None, primary_key=True)
    """ID of the `achievement_user` row."""

    user_id: t.Optional[int] = sql.Field(default=None, foreign_key="users.id", primary_key=True, index=True)
    """The ID of the user who has the achievement."""
    achievement_id: t.Optional[int] = sql.Field(default=None, foreign_key="achievements.id", primary_key=True, index=True)
    """The ID of the achievement that belongs to the user."""

    created_at: t.Optional[datetime]
    """The date and time when the user got the achievement."""
    updated_at: t.Optional[datetime]
    """The date and time when the achievement was updated."""

    new: bool = False
    """Whether the achievement is new."""

