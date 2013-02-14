import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine(os.environ.get('DATABASE_URL',
                                      'sqlite:///detour_app.db'))
db = scoped_session(sessionmaker(autocommit=False, autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db.query_property()


def init_db():
    # Import all modules here that might define models so that they will be
    # registered properly on the metadata.  Otherwise you will have to import
    # them first before calling init_db().
    from detour.apps.message.models import Message
    from detour.apps.user.models import User
    Base.metadata.create_all(bind=engine)
