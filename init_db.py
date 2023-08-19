from db import Base,engine


def craete_tables():
    Base.metadata.create_all(engine,checkfirst=True)


