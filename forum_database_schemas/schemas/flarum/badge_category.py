import typing as t
import sqlmodel as sql

from datetime import datetime

if t.TYPE_CHECKING:
    from .badges import FlarumBadge



class FlarumBadgeCategory(sql.SQLModel, table=True):
    """
        A Flarum model for badge.
    """
	
    __tablename__ = 'badge_category'
    id: t.Optional[int] = sql.Field(primary_key=True)
    """The ID of the badge category"""

    name: str = sql.Field(max_length=46)
    """The name of the badge category"""
    order: int = 0
    """The order of the badge category"""
    created_at: datetime = datetime.now()
    """The date and time when the badge category was created"""

    is_enabled: bool = True
    """Whether the badge category is enabled"""
    is_table: bool = True
    """Whether the badge category is table(?)"""

    badges: t.List['FlarumBadge'] = sql.Relationship(back_populates='badge_category')
    """A list of badges in this category."""
