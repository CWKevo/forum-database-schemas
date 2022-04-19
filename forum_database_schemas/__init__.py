import typing as t

from pathlib import Path

from sqlmodel import create_engine, SQLModel
from sqlalchemy.future.engine import Engine


# Overwrite __doc__ with README, so that pdoc can render it:
README_PATH = Path(__file__).parent.parent.absolute() / Path('README.md')
try:
    with open(README_PATH, 'r', encoding="UTF-8") as readme:
        __readme__ = readme.read()
except Exception:
    __readme__ = "Failed to read README.md!"

__doc__ = __readme__



def create_db_engine(database_models: t.List[t.Type[SQLModel]], *args, **kwargs) -> Engine:
    """
        Creates a database engine for migrations. This returns the standard `Engine` object from [sqlmodel](https://sqlmodel.tiangolo.com).

        But, in addition to that, it also creates all missing
        columns for tables, so it can be migrated properly
        (no 'missing column' errors).
    """

    engine = create_engine(*args, **kwargs)

    tables = [SQLModel.metadata.tables[model.__tablename__] for model in database_models]
    SQLModel.metadata.create_all(engine, tables=tables, checkfirst=True)

    return engine
