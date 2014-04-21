from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from popong_models import Base


def init_app(app):
    sqlalchemy_uri = app.config.get('SQLALCHEMY_URI')
    engine = create_engine(sqlalchemy_uri)
    db_session = scoped_session(sessionmaker(autocommit=False,
                                             autoflush=False,
                                             bind=engine))
    Base.query = db_session.query_property()

