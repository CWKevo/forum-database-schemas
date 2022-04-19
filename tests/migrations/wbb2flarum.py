import typing as t

from sqlmodel import select, Session
from sqlalchemy.future.engine import Engine


from forum_database_schemas import create_db_engine
from forum_database_schemas.schemas.flarum import ALL_FLARUM_MODELS
from forum_database_schemas.schemas.wbb import ALL_WBB_MODELS


#from forum_database_schemas.schemas.flarum.badges import FlarumBadge
#from forum_database_schemas.schemas.flarum.banned_ips import FlarumBannedIp
from forum_database_schemas.schemas.flarum.discussions import FlarumDiscussion
from forum_database_schemas.schemas.flarum.posts import FlarumPost
from forum_database_schemas.schemas.flarum.tags import FlarumTag
from forum_database_schemas.schemas.flarum.users import FlarumUser

from forum_database_schemas.schemas.wbb.user import WCFUser



def main(from_database: Engine, to_database: Engine):
    """
        Migrates WBB -> Flarum.
    """

    with Session(to_database) as s_to:
        with Session(from_database) as s_from:
            for user in s_from.exec(select(WCFUser)):
                flarum_user = FlarumUser(
                    username=user.username,
                    email=user.email,
                    password=user.password.removeprefix('bcrypt:'),
                    nickname=user.userTitle
                )

                s_to.add(flarum_user)
                print(f"Added: {flarum_user.username}")

                for thread in user.threads:
                    flarum_discussion = FlarumDiscussion(
                        title=thread.topic,
                        tags=[FlarumTag(
                            name=thread.board.title,
                            slug=f"{thread.threadID}-{thread.board.title.replace(' ', '-').lower()}",
                            description=thread.board.description,
                            color="#000000",
                            parent=FlarumTag(
                                name=thread.board.parent.title,
                                slug=f"{thread.board.parent.boardID}-{thread.board.parent.title.replace(' ', '-').lower()}",
                                description=thread.board.parent.description,
                                color="#000000",
                            ) if thread.board.parent is not None else None
                        )],
                        posts=[FlarumPost(
                            number=post_number,
                            content=post.message,
                            ip_address=post.ipAddress,
                            user=flarum_user
                        ) for post_number, post in enumerate(thread.posts)]
                    )

                    s_to.add(flarum_discussion)
                    print(f"Added: {flarum_discussion}, {flarum_discussion.user}, {flarum_discussion.posts}")

        s_to.commit()
        print("Commited!")



if __name__ == '__main__':
    from_database = create_db_engine(ALL_WBB_MODELS, url='sqlite:///tests/wbb/test.db')
    to_database = create_db_engine(ALL_FLARUM_MODELS, url='sqlite:///tests/flarum/migrated_wbb.db')

    main(from_database, to_database)
