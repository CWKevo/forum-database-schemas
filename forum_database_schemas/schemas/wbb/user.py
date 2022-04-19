import typing as t
import sqlmodel as sql

from sqlalchemy import Index

if t.TYPE_CHECKING:
    from .post import WBBPost
    from .thread import WBBThread



class WCFUser(sql.SQLModel, table=True):
    """
        A Woltlab Burning Board user model.
    """

    __tableargs__ = (
        Index("username", 'username', unique=True),
        Index("email", 'email'),
        Index("registrationDate", 'registrationDate'),
        Index("styleID", 'styleID'),
        Index("activationCode", 'activationCode'),
        Index("registrationData", 'registrationIpAddress', 'registrationDate'),
        Index("activityPoints", 'activityPoints'),
        Index("likesReceived", 'likesReceived'),
        Index("authData", 'authData'),
        Index("trophyPoints", 'trophyPoints'),
        Index("wbbPosts", 'wbbPosts'),
    )
    __tablename__ = 'wcf1_user'
    userID: t.Optional[int] = sql.Field(primary_key=True)
    """The ID of the user."""

    username: str = sql.Field(max_length=100, default='', sa_column_kwargs={'unique': True})
    """Username of the user."""
    email: str = sql.Field(max_length=191, default='')
    """Email of the user."""
    password: str = sql.Field(max_length=255, default='invalid:')
    """Password of the user."""
    accessToken: str = sql.Field(max_length=40, default='')
    """Access token of the user."""
    multifactorActive: bool = False
    """Whether the user has activated multifactor authentication."""
    languageID: int = 0
    """ID of the user's preferred language."""
    registrationDate: int = 0
    """Time of the user's registration."""
    styleID: int = 0
    """ID of the style the user is using."""

    banned: bool = False
    """Whether the user is banned or not."""
    banReason: t.Optional[t.Text]
    """The ban reason."""
    banExpires: int = 0
    """The time when the ban expires."""

    activationCode: int = 0
    """The activation code for the user."""
    emailConfirmed: t.Optional[str] = sql.Field(max_length=40)
    """The email confirmation code for the user. If `None`, then the user has confirmed their email(?)"""
    lastLostPasswordRequestTime: int = 0
    """The time when the user last requested a password reset."""
    lostPasswordKey: t.Optional[str] = sql.Field(max_length=40)
    """The lost password key for the user."""
    lastUsernameChange: int = 0
    """The time when the user last changed their username."""

    newEmail: str = sql.Field(max_length=255, default='')
    """The new email address for the user."""
    oldUsername: str = sql.Field(max_length=255, default='')
    """The old username for the user."""
    quitStarted: int = 0
    """?"""

    reactivationCode: int = 0
    """The reactivation code for the user."""
    registrationIpAddress: str = sql.Field(max_length=39, default='')
    """The IP address of the user when they registered."""

    avatarID: t.Optional[int]
    """The ID of the avatar for the user."""
    disableAvatar: bool = False
    """Whether the user has a disabled avatar or not."""
    disableAvatarReason: t.Optional[t.Text]
    """The reason why the user has a disabled avatar."""
    disableAvatarExpires: bool = False
    """The time when the user's avatar will be enabled again."""
    enableGravatar: bool = False
    """Whether the user has enabled Gravatar or not."""
    gravatarFileExtension: str = sql.Field(max_length=3, default='')
    """The file extension of the user's Gravatar."""

    signature: t.Optional[t.Text]
    """The signature for the user."""
    signatureEnableHtml: bool = False
    """Whether the user can use HTML in their signature or not."""
    disableSignature: bool = False
    """Whether the user has disabled their signature or not."""
    disableSignatureReason: t.Optional[t.Text]
    """The reason why the user has a disabled signature."""
    disableSignatureExpires: int = 0
    """The time when the user's signature will be enabled again."""

    lastActivityTime: int = 0
    """The time when the user was last active."""
    profileHits: int = 0
    """The number of profile views the user has had."""
    rankID: t.Optional[int]
    """The ID of the user's rank."""
    userTitle: str = sql.Field(max_length=255, default='')
    """The user's title."""
    userOnlineGroupID: t.Optional[int]
    """The ID of the user's online group."""
    activityPoints: int = 0
    """The number of activity points the user has."""
    notificationMailToken: str = sql.Field(max_length=20, default='')
    """The notification mail token for the user."""
    authData: str = sql.Field(max_length=191, default='')
    """The authentication data for the user."""
    likesReceived: int = 0
    """The number of likes the user has received."""
    trophyPoints: int = 0
    """The number of trophy points the user has."""

    coverPhotoHash: t.Optional[str] = sql.Field(max_length=40)
    """The cover photo hash for the user."""
    coverPhotoExtension: str = sql.Field(max_length=4, default='')
    """The cover photo extension for the user."""
    coverPhotoHasWebP: bool = False
    """Whether the cover photo has a WebP version or not."""
    disableCoverPhoto: bool = False
    """Whether the user has a disabled cover photo or not."""
    disableCoverPhotoReason: t.Optional[t.Text]
    """The reason why the user has a disabled cover photo."""
    disableCoverPhotoExpires: int = 0
    """The time when the user's cover photo will be enabled again."""

    articles: int = 0
    """The number of articles the user has written."""
    blacklistMatches: str = sql.Field(max_length=255, default='')
    """The blacklist matches for the user."""

    wbbPosts: int = 0
    """The number of posts the user has made."""
    wbbBestAnswers: int = 0
    """The number of best answers the user has."""


    posts: t.List['WBBPost'] = sql.Relationship(back_populates='user')
    """The posts the user has made."""
    threads: t.List['WBBThread'] = sql.Relationship(back_populates='user')
    """The threads the user has started."""
