from tests.flarum import FLARUM_ENGINE
from sqlmodel import select, Session

from forum_database_schemas.schemas.flarum.access_tokens import FlarumAccessToken


def test_access_token_select():
    """
        Attempt to select some access token data from the database.
    """

    with Session(FLARUM_ENGINE) as session:
        access_token = session.exec(select(FlarumAccessToken)).first()
        print(access_token.id if access_token else 'No access token found.')



if __name__ == '__main__':
    test_access_token_select()
