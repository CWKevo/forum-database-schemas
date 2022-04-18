import typing as t
import sqlmodel as sql

from sqlalchemy import Index
from datetime import datetime, date

if t.TYPE_CHECKING:
    from .access_tokens import FlarumAccessToken
    from .achievements import FlarumAchievement
    from .api_keys import FlarumApiKey
    from .discussions import FlarumDiscussion
    from .posts import FlarumPost

from .achievement_user import FlarumAchievementUser


class FlarumUser(sql.SQLModel, table=True):
    """
        A Flarum user model.
    """

    __tableargs__ = (
        Index('users_username_unique', "username", unique=True),
        Index('users_email_unique', "email", unique=True),
        Index('users_joined_at_index', "joined_at"),
        Index('users_last_seen_at_index', "last_seen_at"),
        Index('users_discussion_count_index', "discussion_count"),
        Index('users_comment_count_index', "comment_count"),
        Index('users_nickname_index', "nickname"),
        Index('users_blocks_byobu_pd_index', "blocks_byobu_pd"),
        Index('users_staffbadge_index', "staffBadge"),
        Index('users_taglist_index', "tagList"),
        Index('users_shadow_banned_until_index', "shadow_banned_until"),
    )
    __tablename__ = 'users'
    id: t.Optional[int] = sql.Field(default=None, primary_key=True)
    """ID of the user."""

    username: str = sql.Field(max_length=100, sa_column_kwargs={'unique': True})
    """Username of the user."""
    nickname: t.Optional[str] = sql.Field(max_length=255)
    """User's nickname."""

    email: str = sql.Field(max_length=150, sa_column_kwargs={'unique': True})
    """User's email address."""
    is_email_confirmed: bool = False
    """Whether the user's email address has been confirmed."""

    password: str = sql.Field(max_length=100)
    """User's password (`bcrypt` hashed)."""

    bio: t.Optional[t.Text]
    """User's bio."""
    avatar_url: t.Optional[str] = sql.Field(max_length=100)
    """User's avatar URL."""

    preferences: str = '{}'
    """User's preferences data (for notifications, and other settings such as draft autosave interval)."""

    joined_at: t.Optional[datetime]
    """Date and time when the user joined the forum."""
    last_seen_at: t.Optional[datetime]
    """Date and time when the user was last seen on the forum."""
    marked_all_as_read_at: t.Optional[datetime]
    """Date and time when the user marked all discussions as read."""
    read_notifications_at: t.Optional[datetime]
    """Date and time when the user read their notifications."""

    new_achievements: str = '[]'
    """JSON-encoded list of new achievements earned by the user."""

    read_flags_at: t.Optional[datetime]
    """Date and time when the user read flagged posts."""
    suspended_until: t.Optional[datetime]
    """Date and time when the user's suspension expires."""
    suspend_reason: t.Optional[t.Text]
    """Reason for the user's suspension."""
    suspend_message: t.Optional[t.Text]
    """Message for user's suspension."""

    discussion_count: int = sql.Field(default=0)
    """Number of discussions the user has created."""
    comment_count: int = sql.Field(default=0)
    """Number of posts the user has created."""

    first_post_approval_count: int = 0
    """Number of posts requiring approval."""
    first_discussion_approval_count: int = 0
    """Number of discussions requiring approval."""

    birthday: t.Optional[date]
    """Date of user's birthday."""
    showDobDate: bool = True
    """Whether the user's birthday should be shown."""
    showDobYear: bool = True
    """Whether the user's birthday's year should be shown."""

    tagList: t.Optional[str] = sql.Field(max_length=150)
    staffBadge: t.Optional[str] = sql.Field(max_length=150)

    blocks_byobu_pd: bool = False
    """Whether the user has blocked private discussions."""
    cover: t.Optional[str] = sql.Field(max_length=150)
    """URL to user's cover image."""
    minotar: t.Optional[str] = sql.Field(max_length=36)
    """URL to user's minotar avatar."""
    username_history: str = '{}'
    """Username history."""
    social_buttons: t.Optional[t.Text]
    """JSON-encoded list of social buttons."""
    signature: t.Text = ''
    """User's signature."""
    location: t.Text = ''
    """User's location."""

    twofa_secret: str = sql.Field(max_length=120, default='')
    """User's two-factor authentication secret."""
    twofa_active: bool = False
    """Whether the user has enabled two-factor authentication."""
    twofa_codes: str = sql.Field(max_length=200, default='')
    """JSON-encoded list of two-factor authentication codes."""

    unread_messages: int = 0
    """Number of unread messages."""

    invite_code: t.Optional[str] = sql.Field(max_length=128)
    """The invite code of the user."""
    votes: int = 0
    """Number of votes the user has cast."""
    last_vote_time: t.Optional[datetime]
    """Date and time when the user last voted."""
    rank: t.Optional[str] = sql.Field(max_length=255)
    """User's rank."""
    money: float = 0
    """User's money."""

    disclose_posted_on: bool = True
    """Whether the user's `'posted on <device>'` header should be shown above posts."""
    shadow_banned_until: t.Optional[datetime]
    """Date and time when the user's shadow ban expires."""


    access_tokens: t.List['FlarumAccessToken'] = sql.Relationship(back_populates='user')
    """List of access tokens for the user."""
    achievements: t.List['FlarumAchievement'] = sql.Relationship(back_populates="users", link_model=FlarumAchievementUser)
    """List of achievements the user has."""
    api_keys: t.List['FlarumApiKey'] = sql.Relationship(back_populates='user')
    """List of API keys belonging to the user."""
    best_answer_discussions: t.List['FlarumDiscussion'] = sql.Relationship(sa_relationship_kwargs={"primaryjoin": "FlarumUser.id==FlarumDiscussion.best_answer_user_id", "lazy": "joined"})
    """List of discussions in which the user has posted the best answer."""
    discussions: t.List['FlarumDiscussion'] = sql.Relationship(sa_relationship_kwargs={"primaryjoin": "FlarumUser.id==FlarumDiscussion.user_id", "lazy": "joined"})
    """List of discussions the user has created."""
    hid_discussions: t.List['FlarumDiscussion'] = sql.Relationship(sa_relationship_kwargs={"primaryjoin": "FlarumUser.id==FlarumDiscussion.hidden_user_id", "lazy": "joined"})
    """List of discussions that the user hid."""
    last_posted_in_discussions: t.List['FlarumDiscussion'] = sql.Relationship(sa_relationship_kwargs={"primaryjoin": "FlarumUser.id==FlarumDiscussion.last_posted_user_id", "lazy": "joined"})
    """List of discussions in which the user created last post."""
    posts: t.List['FlarumPost'] = sql.Relationship(sa_relationship_kwargs={"primaryjoin": "FlarumPost.user_id==FlarumUser.id", "lazy": "joined"})
    """List of all posts the user made."""
