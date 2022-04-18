import typing as t
import sqlmodel as sql

from sqlalchemy import Index
from datetime import datetime

if t.TYPE_CHECKING:
    from .blog_meta import FlarumBlogMeta
    from .posts import FlarumPost
    from .users import FlarumUser



class FlarumDiscussion(sql.SQLModel, table=True):
    """
        Model for Flarum discussion.
    """

    __tablename__ = 'discussions'
    __table_args__ = (
        Index('discussions_hidden_user_id_foreign', "hidden_user_id"),
        Index('discussions_first_post_id_foreign', "first_post_id"),
        Index('discussions_last_post_id_foreign', "last_post_id"),
        Index('discussions_last_posted_at_index', "last_posted_at"),
        Index('discussions_last_posted_user_id_index', "last_posted_user_id"),
        Index('discussions_created_at_index', "created_at"),
        Index('discussions_user_id_index', "user_id"),
        Index('discussions_comment_count_index', "comment_count"),
        Index('discussions_participant_count_index', "participant_count"),
        Index('discussions_hidden_at_index', "hidden_at"),
        Index('discussions_is_locked_index', "is_locked"),
        Index('discussions_best_answer_post_id_foreign', "best_answer_post_id"),
        Index('discussions_best_answer_user_id_foreign', "best_answer_user_id"),
        Index('discussions_best_answer_set_at_index', "best_answer_set_at"),
        Index('discussions_language_id_foreign', "language_id"),
        Index('discussions_votes_index', "votes"),
        Index('discussions_shadow_hidden_at_index', "shadow_hidden_at"),
        Index('title', "title", mysql_prefix='FULLTEXT'),

        Index('discussions_is_sticky_created_at_index', "is_sticky", "created_at"),
        Index('discussions_is_sticky_last_posted_at_index', "is_sticky", "last_posted_at"),
        Index('discussions_is_stickiest_last_posted_at_index', "is_stickiest", "last_posted_at"),
        Index('discussions_is_tagSticky_last_posted_at_index', "is_tagSticky", "last_posted_at"),
        Index('discussions_is_stickiest_created_at_index', "is_stickiest", "created_at"),
        Index('discussions_is_tagSticky_created_at_index', "is_tagSticky", "created_at")
    )
    id: t.Optional[int] = sql.Field(primary_key=True)
    """ID of the discussion."""

    title: str = sql.Field(max_length=200)
    """Title of the discussion."""
    slug: str = sql.Field(max_length=255)
    """Slug of the discussion, used in the URL (format: `<discussion.id>-<discussion.title>`, discussion title is converted to an URL safe string)."""

    comment_count: int = sql.Field(default=1)
    """Number of comments (posts) in the discussion."""
    participant_count: int = sql.Field(default=0)
    """How many users have participated in the discussion?"""
    post_number_index: int = 0
    """Index of the last post in the discussion."""

    created_at: datetime = sql.Field(default=datetime.now())
    """Date and time when the discussion was created."""
    user: t.Optional['FlarumUser'] = sql.Relationship(back_populates='discussions', sa_relationship_kwargs={"primaryjoin": "FlarumDiscussion.user_id==FlarumUser.id", "lazy": "joined"})
    """User who created the discussion."""
    user_id: t.Optional[int] = sql.Field(foreign_key='users.id')
    """ID of the discussion's author."""
    first_post: t.Optional['FlarumPost'] = sql.Relationship(sa_relationship_kwargs={"primaryjoin": "FlarumDiscussion.first_post_id==FlarumPost.id"})
    """First post in the discussion."""
    first_post_id: t.Optional[int] = sql.Field(foreign_key='posts.id')
    """ID of the first post in the discussion."""

    last_posted_at: t.Optional[datetime]
    """Date and time when the last post was created."""
    last_posted_user: t.Optional['FlarumUser'] = sql.Relationship(back_populates='last_posted_in_discussions', sa_relationship_kwargs={"primaryjoin": "FlarumDiscussion.last_posted_user_id==FlarumUser.id", "lazy": "joined"})
    """User who created the last post in the discussion."""
    last_posted_user_id: t.Optional[int] = sql.Field(foreign_key='users.id')
    """ID of the user who created the last post."""
    last_post: t.Optional['FlarumPost'] = sql.Relationship(sa_relationship_kwargs={"primaryjoin": "FlarumDiscussion.last_post_id==FlarumPost.id", "lazy": "joined"})
    """Last post in the discussion."""
    last_post_id: t.Optional[int] = sql.Field(foreign_key='posts.id')
    """ID of the last post in the discussion."""
    last_post_number: t.Optional[int]
    """Number of the last post in the discussion."""

    hidden_at: t.Optional[datetime]
    """Date and time when the discussion was hidden."""
    hidden_user: t.Optional['FlarumUser'] = sql.Relationship(back_populates='hid_discussions', sa_relationship_kwargs={"primaryjoin": "FlarumDiscussion.hidden_user_id==FlarumUser.id", "lazy": "joined"})
    """User who hid the discussion."""
    hidden_user_id: t.Optional[int] = sql.Field(foreign_key='users.id')
    """ID of the user who hid the discussion."""

    is_private: bool = False
    """Whether the discussion is private."""
    is_approved: bool = True
    """Whether the discussion is approved."""
    is_locked: bool = sql.Field(default=False)
    """Whether the discussion is locked."""
    is_sticky: bool = False
    """Whether the discussion is sticky."""

    best_answer_post_id: t.Optional[int]
    """ID of the post that is the best answer."""
    best_answer_user: t.Optional['FlarumUser'] = sql.Relationship(back_populates='best_answer_discussions', sa_relationship_kwargs={"primaryjoin": "FlarumDiscussion.best_answer_user_id==FlarumUser.id", "lazy": "joined"})
    """User who posted the best answer in the discussion."""
    best_answer_user_id: t.Optional[int] = sql.Field(foreign_key='users.id')
    """ID of the user who posted the best answer in the discussion."""
    best_answer_notified: bool = True
    """Whether the author was notified of best answer."""
    best_answer_set_at: t.Optional[datetime]
    """Date and time when the best answer was set."""

    view_count: int = 0
    """Number of times the discussion was viewed."""
    replyTemplate: t.Text = ''
    """Template for the reply form."""
    language_id: t.Optional[int] # TODO: foreign key
    """ID of the language used for the discussion."""

    is_stickiest: bool = False
    """Whether the discussion is stickiest."""
    is_tagSticky: bool = False
    is_first_moved: bool = False

    votes: int = sql.Field(default=0)
    """Number of votes for the discussion."""
    hotness: float = 0.0
    """Hotness of the discussion."""
    shadow_hidden_at: t.Optional[datetime]
    """Date and time when the discussion was hidden."""
    show_to_all: bool = False
    """Whether the discussion is visible to everyone."""


    blog_metas: t.List['FlarumBlogMeta'] = sql.Relationship(back_populates='discussion')
    """List of blog metas of this discussion."""
    posts: t.List['FlarumPost'] = sql.Relationship(sa_relationship_kwargs={"primaryjoin": "FlarumPost.discussion_id==FlarumDiscussion.id", "lazy": "joined"})
    """List of all posts in the discussion."""
