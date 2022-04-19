from forum_database_schemas import create_db_engine
from forum_database_schemas.schemas.wbb import ALL_WBB_MODELS


WBB_ENGINE = create_db_engine(ALL_WBB_MODELS, 'sqlite:///tests/wbb/test.db')
