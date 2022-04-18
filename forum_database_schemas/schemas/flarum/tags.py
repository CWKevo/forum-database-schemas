import typing as t
import sqlmodel as sql

from sqlalchemy import Index
from sqlalchemy.orm import backref
from datetime import datetime

if t.TYPE_CHECKING:
    from .discussions import FlarumDiscussion
    from .users import FlarumUser

from .discussion_tag import FlarumDiscussionTag



class FlarumTag(sql.SQLModel, table=True):
    """
        A Flarum tag model.
    """

    __tableargs__ = (
        Index('tags_slug_unique', 'slug', unique=True),
        Index('tags_parent_id_foreign', 'parent_id'),
        Index('tags_last_posted_user_id_foreign', 'last_posted_user_id'),
        Index('tags_last_posted_discussion_id_foreign', 'last_posted_discussion_id'),
    )
    __tablename__ = 'tags'
    id: t.Optional[int] = sql.Field(default=None, primary_key=True)
    """ID of the tag."""

    name: str = sql.Field(max_length=100)
    """Name of the tag."""
    slug: str = sql.Field(max_length=100)
    """Slug of the tag."""
    description: t.Optional[t.Text]
    """Description of the tag."""

    color: t.Optional[str] = sql.Field(max_length=50)
    """Color of the tag."""
    background_path: t.Optional[str] = sql.Field(max_length=100)
    """Background path of the tag."""
    background_mode: t.Optional[str] = sql.Field(max_length=100)
    """Background mode of the tag."""
    position: t.Optional[int]
    """Position/order of the tag."""

    parent_id: t.Optional[int] = sql.Field(foreign_key='tags.id')
    """ID of the parent tag."""
    parent: t.Optional['FlarumTag'] = sql.Relationship(back_populates='children', sa_relationship_kwargs={'remote_side': "FlarumTag.id"})
    """Parent tag."""

    default_sort: t.Optional[str] = sql.Field(max_length=50)
    """Default sorting of the tag."""
    is_restricted: bool = False
    """Whether the tag is restricted."""
    is_hidden: bool = False
    """Whether the tag is hidden."""
    discussion_count: int = 0
    """Number of discussions in the tag."""

    last_posted_at: t.Optional[datetime]
    """Date and time of the last post in the tag."""
    last_posted_discussion: t.Optional['FlarumDiscussion'] = sql.Relationship()
    """Discussion of the last post in the tag."""
    last_posted_discussion_id: t.Optional[int] = sql.Field(foreign_key='discussions.id')
    """ID of the discussion of the last post in the tag."""
    last_posted_user: t.Optional['FlarumUser'] = sql.Relationship()
    """User that last posted in the tag."""
    last_posted_user_id: t.Optional[int] = sql.Field(foreign_key='users.id')
    """ID of the user that last posted in the tag."""

    icon: t.Optional[str] = sql.Field(max_length=100)
    """The FontAwesome icon of the tag."""
    is_qna: bool = False
    """Whether the tag is a QnA tag."""
    qna_reminders: bool = False
    """?"""

    template: t.Text = ''
    """Template of the tag."""
    localised_last_discussion: t.Text = '{}'
    """JSON encoded string of last localised data(?)."""
    excerpt_length: t.Optional[int]
    """Length of the excerpt of the tag."""
    rich_excerpts: t.Optional[bool]
    """Whether the tag has rich excerpts enabled (e. g.: HTML excerpts)."""
    post_count: int = 0
    """Number of posts in the tag."""

    discussions: t.List['FlarumDiscussion'] = sql.Relationship(back_populates='tags', link_model=FlarumDiscussionTag)
    """The discussions tagged with this tag."""
    children: t.List['FlarumTag'] = sql.Relationship(back_populates='parent')
    """The tags that are children of this tag."""
