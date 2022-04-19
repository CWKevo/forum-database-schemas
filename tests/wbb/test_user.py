from tests.wbb import WBB_ENGINE
from sqlmodel import Session


from forum_database_schemas.utilities import bcrypt_hash

from forum_database_schemas.schemas.wbb.board import WBBBoard
from forum_database_schemas.schemas.wbb.post import WBBPost
from forum_database_schemas.schemas.wbb.thread import WBBThread
from forum_database_schemas.schemas.wbb.user import WCFUser



def test_user(delete: bool=True):
    """
        Creates an user.
    """

    with Session(WBB_ENGINE) as session:
        board = WBBBoard(title="Main board", children=[WBBBoard(title="Child board")])

        user = WCFUser(username='testingy', email='testingier@test.gov', password=f'bcrypt:{bcrypt_hash("test")}')

        thread = WBBThread(board=board, topic="A test thread", posts=[
            WBBPost(user=user, message="A test post"),
            WBBPost(user=user, subject="A welcome message", message="Hello everyone!", isOfficial=True)
        ])

        session.add(user)
        session.commit()
        session.refresh(user)

        print(f"User: {user}")
        print(f"Posts: {[(post.thread.topic, post.thread.board.title, post.message) for post in user.posts]}")


        if delete:
            for post in user.posts:
                session.delete(post)

            session.delete(user)
            session.delete(thread)

            for child_board in board.children:
                session.delete(child_board)
            session.delete(board)

            session.commit()
        



if __name__ == '__main__':
    test_user()
