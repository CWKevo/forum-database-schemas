import typing as t
import sqlmodel as sql

from sqlalchemy import Index

if t.TYPE_CHECKING:
    from .board import WBBBoard



class WBBThread(sql.SQLModel, table=True):
    """
        A Woltlab Burning Board thread model.
    """

    __tableargs__ = (
        Index("lastPostTime", 'lastPostTime'),
        Index("boardID", 'boardID', 'isAnnouncement', 'isSticky', 'lastPostTime', 'isDeleted', 'isDisabled')
    )
    __tablename__ = 'wbb1_thread'

    threadID: t.Optional[int] = sql.Field(primary_key=True)
    """The ID of the thread."""
    board: 'WBBBoard' = sql.Relationship(back_populates='threads')
    """Board this thread belongs in."""
    boardID: int = sql.Field(foreign_key='wbb1_board.boardID')
    """ID of the board this thread belongs in."""
    languageID: t.Optional[int]
    """ID of the language this thread is in."""
    topic: str = sql.Field(max_length=255)
    """Topic of the thread."""
    firstPostID: t.Optional[int]
    """ID of the first post in the thread."""
    time: int = 0
    """Time of the thread creation."""

    userID: t.Optional[int]
    """ID of the user who created the thread."""
    username: str = sql.Field(max_length=255)
    """Username of the user who created the thread."""

    lastPostID: t.Optional[int]
    """ID of the last post in the thread."""
    lastPostTime: int = 0
    """Time of the last post in the thread."""
    lastPosterID: t.Optional[int]
    """ID of the user who posted the last post in the thread."""
    lastPoster: str = sql.Field(max_length=255)
    """Username of the user who posted the last post in the thread."""

    replies: int = 0
    """Number of replies in the thread."""
    views: int = 0
    """Number of views of the thread."""
    attachments: int = 0
    """Number of attachments in the thread."""
    polls: int = 0
    """Number of polls in the thread."""

    isAnnouncement: bool = False
    """Whether the thread is an announcement."""
    isSticky: bool = False
    """Whether the thread is sticky/always on top."""
    isDisabled: bool = False
    """Whether the thread is disabled."""
    isClosed: bool = False
    """Whether the thread is closed."""
    isDeleted: bool = False
    """Whether the thread is deleted."""

    movedThreadID: t.Optional[int]
    """ID of the thread this thread was moved to."""
    movedTime: int = 0
    """Time of the thread move."""
    isDone: bool = False
    """Whether the thread is done."""

    cumulativeLikes: int = 0
    """Number of total likes of the thread."""
    hasLabels: bool = False
    """Whether the thread has labels."""
    deleteTime: int = 0
    """Time of the thread deletion."""
    bestAnswerPostID: t.Optional[int]
    """ID of the post which is the best answer."""
