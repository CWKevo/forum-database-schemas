from tests.flarum import FLARUM_ENGINE
from sqlmodel import select, Session

from forum_database_schemas.utilities import bcrypt_hash
from forum_database_schemas.schemas.flarum.badges import FlarumBadge
from forum_database_schemas.schemas.flarum.banned_ips import FlarumBannedIp
from forum_database_schemas.schemas.flarum.discussions import FlarumDiscussion
from forum_database_schemas.schemas.flarum.posts import FlarumPost
from forum_database_schemas.schemas.flarum.tags import FlarumTag
from forum_database_schemas.schemas.flarum.users import FlarumUser


def test_user_select():
    """
        Attempt to select some user from the database.
    """

    with Session(FLARUM_ENGINE) as session:
        user = session.exec(select(FlarumUser)).first()

        if user:
            print(user.username)
            print(f"Achievements: {[achievement.name for achievement in user.achievements]}")

        else:
            print('No user found.')



def test_user_create_and_delete(delete: bool=True):
    """
        Creates an user.
    """

    with Session(FLARUM_ENGINE) as session:
        discussions = [
            FlarumDiscussion(title='Test Discussion 1', slug='test-discussion-1', tags=[
                FlarumTag(name='amazing test tag', slug='test-tag', children=[
                    FlarumTag(name='children test tag', slug='test-tag-children')
                ])
            ]),
            FlarumDiscussion(title='Test Discussion 2', slug='test-discussion-2'),
        ]

        user = FlarumUser(username='testingier', email='testingier@test.gov', password=bcrypt_hash('test'), discussions=discussions)
        user.badges = [
            FlarumBadge(name='Awesome badge', description='A test badge that is awesome.', icon='fas fa-award'),
        ]
        user.given_ip_bans = [
            FlarumBannedIp(user=user, address='127.0.0.1'),
        ]

        session.add(user)
        session.commit()
        session.refresh(user)

        print(user.id, user.username)
        print(f"Badges: {[badge.name for badge in user.badges]}")
        print(f"Given IP bans: {[(ban.user.username, ban.address) for ban in user.given_ip_bans]}")

        for discussion in user.discussions:
            user.posts = [
                FlarumPost(discussion=discussion, content=f'Test post 1 in "{discussion.title}"'),
                FlarumPost(discussion=discussion, content=f'Test post 2 in "{discussion.title}"'),
            ]
            session.commit()
            session.refresh(user)
            session.refresh(discussion)

            print(discussion.id, discussion.title)
            print(f'First post: "{discussion.posts[0].content}"')
            print(f"Tags: {[(tag.name, [child_tag.name for child_tag in tag.children]) for tag in discussion.tags]}")


        if delete:
            session.delete(user)

            for discussion in discussions:
                session.delete(discussion)

            session.commit()

        print("OK")



if __name__ == '__main__':
    test_user_select()
    test_user_create_and_delete()
