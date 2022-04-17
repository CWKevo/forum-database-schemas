from tests.flarum import FLARUM_ENGINE
from sqlmodel import select, Session, desc

from forum_database_schemas.schemas.flarum.discussions import FlarumDiscussion


def test_discussions_select():
    """
        Attempt to select some discussion data from the database.
    """

    with Session(FLARUM_ENGINE) as session:
        discussion = session.exec(select(FlarumDiscussion).order_by(desc(FlarumDiscussion.created_at))).first()
        print(discussion.title if discussion else 'No discussion found.')



if __name__ == '__main__':
    test_discussions_select()
