import typing as t
import sqlmodel as sql

from sqlalchemy import Index
from datetime import datetime

if t.TYPE_CHECKING:
    from .badge_category import FlarumBadgeCategory
    from .users import FlarumUser

from .badge_user import FlarumBadgeUser



class FlarumBadge(sql.SQLModel, table=True):
    """
        A Flarum model for badge.
    """

    __tableargs__ = (
        Index('badges_badge_category_id_foreign', 'badge_category_id'),
    )
    __tablename__ = 'badges'
    id: t.Optional[int] = sql.Field(primary_key=True)
    """The ID of the badge"""

    name: str = sql.Field(max_length=46)
    """The name of the badge"""
    icon: str = sql.Field(max_length=100)
    """The icon of the badge"""
    order: int = 0
    """The order of the badge"""

    image: t.Optional[t.Text]
    """The badge image"""
    description: t.Optional[t.Text]
    """The description of the badge"""
    is_visible: bool = True
    """Whether the badge is visible"""
    created_at: datetime = datetime.now()
    """The date and time when the badge was created"""

    badge_category: t.Optional['FlarumBadgeCategory'] = sql.Relationship(back_populates='badges')
    """The badge category"""
    badge_category_id: t.Optional[int] = sql.Field(foreign_key='badge_category.id')
    """The ID of the badge category"""

    points: int = 0
    """The points the badge gives"""
    background_color: t.Optional[str] = sql.Field(max_length=50)
    """The badge's background color"""

    icon_color: t.Optional[str] = sql.Field(max_length=50)
    """The badge's icon color"""
    label_color: t.Optional[str] = sql.Field(max_length=50)
    """The badge's label color"""

    users: t.List['FlarumUser'] = sql.Relationship(back_populates='badges', link_model=FlarumBadgeUser)
    """The users that have the badge"""
