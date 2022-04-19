import typing as t
import sqlmodel as sql

if t.TYPE_CHECKING:
    from .thread import WBBThread



class WBBBoard(sql.SQLModel, table=True):
    """
        A Woltlab Burning Board board model.
    """

    __tablename__ = 'wbb1_board'
    boardID: t.Optional[int] = sql.Field(primary_key=True)
    """The ID of the board."""

    parent: t.Optional['WBBBoard'] = sql.Relationship(back_populates='children', sa_relationship_kwargs={'remote_side': "WBBBoard.boardID"})
    """Parent board."""
    parentID: t.Optional[int] = sql.Field(foreign_key='wbb1_board.boardID')
    """ID of the parent board"""

    position: int = 0
    """Position of the board."""
    boardType: bool = 0
    """Type of the board."""
    title: str = sql.Field(max_length=255, default='')
    """Board name/title."""
    description: t.Optional[t.Text]
    """Board description."""
    descriptionUseHtml: bool = False
    """Whether the board description uses HTML."""
    externalURL: str = sql.Field(max_length=255, default='')
    """External URL of the board."""
    time: int = 0
    """Time when was the board created"""
    metaDescription: str = sql.Field(max_length=255, default='')
    """Meta description of the board."""
    countUserPosts: bool = True
    """Whether the board counts user posts."""
    daysPrune: int = 0
    """Days to prune posts."""

    enableMarkingAsDone: bool = False
    """Whether the board enables marking as done."""
    ignorable: bool = True
    """Whether the board can be ignored by users."""
    isClosed: bool = False
    """Whether the board is closed."""
    isInvisible: bool = False
    """Whether the board is invisible."""
    isPrivate: bool = False
    """Whether the board is private."""

    postSortOrder: str = sql.Field(max_length=4, default='')
    """Post sort order."""
    postsPerPage: int = 0
    """Posts per page."""
    searchable: bool = True
    """Whether the board's content can be searched."""
    searchableForSimilarThreads: bool = True
    """Whether the board can be searched for similar threads."""
    showSubBoards: bool = True
    """Whether the board's subboards are shown."""
    sortField: str = sql.Field(max_length=20, default='')
    """Sort field."""
    sortOrder: str = sql.Field(max_length=4, default='')
    """Sort order."""
    styleID: t.Optional[int]
    """Style ID."""
    threadsPerPage: int = 0
    """Threads per page."""
    enableBestAnswer: bool = False
    """Whether the board enables best answer."""
    formID: t.Optional[int]
    """Form ID."""

    clicks: int = 0
    """Amount of clicks on the board."""
    posts: int = 0
    """Posts in board's threads."""
    threads: int = 0
    """Threads in the board."""
    iconData: t.Optional[t.Text]
    """Icon data."""


    threads: t.List['WBBThread'] = sql.Relationship(back_populates='board')
    """Threads in the board."""
    children: t.List['WBBBoard'] = sql.Relationship(back_populates='parent')
    """The boards that are children of the board."""
