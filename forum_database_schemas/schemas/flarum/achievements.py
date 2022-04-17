import typing as t
import sqlmodel as sql

if t.TYPE_CHECKING:
    from .users import FlarumUser

from .achievement_user import FlarumAchievementUser



class FlarumAchievement(sql.SQLModel, table=True):
    """
        A model of Flarum achievement.

        https://discuss.flarum.org/d/26675
    """

    __tablename__ = 'achievements'
    id: t.Optional[int] = sql.Field(default=None, primary_key=True)
    """The ID of the achievement (primary key)."""

    name: str = sql.Field(max_length=200)
    """The name/title of the achievement."""
    description: t.Text = ''
    """The achievement's description"""

    computation: str = sql.Field(max_length=100, default='manual:')
    """
        `"Variable"` in achievement creation modal.
        The condition to be met for the achievement to be unlocked (example: `years:1` - user must be registered for 1 year).

        List of all variables:

        - `manual` - manual condition.
        - `posts` - user must create `X` posts.
        - `likes` - user must be given `X` likes.
        - `selflikes` - user must give `X` likes to others.
        - `discussions` - user must create `X` discussions.
        - `edits` - user must edit `X` posts.
        - `avatar` - avatars uploaded.
        - `comments` - responses received in a discussion.
        - `contains` - word or words and minimum number of posts containing it (e. g.: `contains:chicken,10`) or inclusive range (e. g.: `contains:chicken,10,19`)
        - `meanwords` - average words per post.
        - `tagposts` - slug of the tag to look for and minimum number of posts (e. g.: `tagposts:off-topic,10`) or inclusive range (e. g.: `tagposts:off-topic,10,19`)
        - `years` - amount of years registered.

        Variables can have a minimum (e. g.: `years:15`) or inclusive range/between (e. g.: `years:15,20`).

    """
    points: int = 0
    """The amount of points that this achievement gives the user."""
    image: str = sql.Field(max_length=255, default='')
    """The image URL or [FontAwesome](https://fontawesome.com/search?m=free&s=solid%2Cbrands) code of the achievement's image."""
    rectangle: str = sql.Field(max_length=100, default='0,0,,')
    """? (usually it's `0,0,,`"""

    active: bool = True
    """Whether the achievement is active/users can receive it."""
    hidden: bool = False
    """Whether the achievement is hidden from all achievements list."""

    users: t.List["FlarumUser"] = sql.Relationship(back_populates="achievements", link_model=FlarumAchievementUser)
