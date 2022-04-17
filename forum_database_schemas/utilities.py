from sqlmodel import Session, Column, SQLModel

import bcrypt

from sqlalchemy.future.engine import Engine
from sqlalchemy.exc import OperationalError
from sqlalchemy.sql import text



def add_column(engine: Engine, table_name: str, column: Column):
    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        with session.begin():
            try:
                return session.exec(text(rf'ALTER TABLE `{table_name}` ADD COLUMN `{column.name}` `{column.type}`;'))

            except OperationalError as oe:
                if 'duplicate column name' not in str(oe):
                    session.rollback()
                    raise oe



def flarum_hash_password(string: str) -> str:
    """
        Hashes a string with bcrypt for Flarum.
        
        See [this](https://github.com/illuminate/hashing/blob/master/BcryptHasher.php) for PHP implementation that Flarum uses.
    """

    return bcrypt.hashpw(string.encode('utf-8'), bcrypt.gensalt(rounds=10)).decode('utf-8')
