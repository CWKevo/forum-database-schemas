from forum_database_schemas import create_db_engine
from forum_database_schemas.schemas.flarum import ALL_FLARUM_MODELS


FLARUM_ENGINE = create_db_engine(ALL_FLARUM_MODELS, 'sqlite:///tests/flarum/test.db')
