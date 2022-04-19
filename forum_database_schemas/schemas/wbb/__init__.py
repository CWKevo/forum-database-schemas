import typing as t
from sqlmodel import SQLModel

from .board import WBBBoard
from .post import WBBPost
from .thread import WBBThread


ALL_WBB_MODELS: t.Type[SQLModel] = [
    WBBBoard,
    WBBPost,
    WBBThread
]
