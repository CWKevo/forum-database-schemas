import typing as t
from sqlmodel import SQLModel

from .access_tokens import FlarumAccessToken
from .achievement_user import FlarumAchievementUser
from .achievements import FlarumAchievement
from .api_keys import FlarumApiKey
from .badges import FlarumBadge
from .badge_category import FlarumBadgeCategory
from .badge_user import FlarumBadgeUser
from .banned_ips import FlarumBannedIp
from .blog_meta import FlarumBlogMeta
from .discussions import FlarumDiscussion
from .posts import FlarumPost
from .users import FlarumUser


ALL_FLARUM_MODELS: t.Type[SQLModel] = [
    FlarumAccessToken,
    FlarumAchievementUser,
    FlarumAchievement,
    FlarumApiKey,
    FlarumBadge,
    FlarumBadgeCategory,
    FlarumBadgeUser,
    FlarumBannedIp,
    FlarumBlogMeta,
    FlarumDiscussion,
    FlarumPost,
    FlarumUser,
]
