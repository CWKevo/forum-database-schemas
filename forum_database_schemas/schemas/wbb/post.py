import typing as t
import sqlmodel as sql

from sqlalchemy import Column, Integer, ForeignKey, Index

if t.TYPE_CHECKING:
    from .thread import WBBThread
    from .user import WCFUser



class WBBPost(sql.SQLModel, table=True):
    """
        A Woltlab Burning Board post model.
    """

    __tableargs__ = (
        Index("threadID", 'threadID', 'userID'),
        Index("threadID_2", 'threadID', 'isDeleted', 'isDisabled', 'time'),
        Index("thread_3", 'threadID', 'isDisabled', 'userID', 'time'),
        Index("userToPost", 'userID', 'isDeleted', 'isDisabled', 'time'),
        Index("isDeleted", 'isDeleted'),
        Index("isDisabled", 'isDisabled'),
        Index("ipAddress", 'ipAddress'),
        Index("time", 'time'),
        Index("enableTime", 'enableTime'),
        Index("isOfficial", 'threadID', 'isOfficial'),
    )
    __tablename__ = 'wbb1_post'
    postID: t.Optional[int] = sql.Field(primary_key=True)
    """The ID of the post."""

    thread: 'WBBThread' = sql.Relationship(back_populates='posts', sa_relationship_kwargs={"primaryjoin": "WBBPost.threadID == WBBThread.threadID", "lazy": "joined"})
    """The thread the post belongs to."""
    threadID: int = sql.Field(sa_column=Column(Integer, ForeignKey('wbb1_thread.threadID', ondelete='CASCADE')))
    """ID of the thread this post was posted in."""
    user: t.Optional['WCFUser'] = sql.Relationship(back_populates='posts')
    """The user who posted this post."""
    userID: t.Optional[int] = sql.Field(foreign_key='wcf1_user.userID')
    """ID of the post author."""
    username: str = sql.Field(max_length=255, default='')
    """Username of the post author."""
    subject: str = sql.Field(max_length=255, default='')
    """Subject/title of the post."""
    message: t.Text
    """Message of the post."""
    time: int = 0
    """Time when was the post created."""

    isDeleted: bool = False
    """Whether the post is deleted."""
    isDisabled: bool = False
    """Whether the post is disabled."""
    isClosed: bool = False
    """Whether the post is closed."""
    isOfficial: bool = False
    """Whether the post is official."""

    editorID: t.Optional[int]
    """ID of the editor."""
    editor: str = sql.Field(max_length=255, default='')
    """Username of the editor."""
    lastEditTime: int = 0
    """Time of the last edit."""
    editCount: int = 0
    """Number of edits."""
    editReason: t.Optional[t.Text]
    """Reason for the last edit."""
    lastVersionTime: int = 0
    """Time of the last version(?)"""

    attachments: int = 0
    """Number of attachments."""
    pollID: t.Optional[int]
    """ID of the poll."""
    enableHtml: bool = False
    """Whether the post uses HTML."""
    ipAddress: str = sql.Field(max_length=39, default='')
    """IP address of the user that made this post."""
    cumulativeLikes: int = 0
    """Number of likes."""
    deleteTime: int = 0
    """Time of the deletion."""
    enableTime: int = 0
    """When was this post enabled(?)"""
    hasEmbeddedObjects: bool = False
    """Whether the post has embedded objects."""