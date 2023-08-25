"""
初始化数据库、表、记录
"""
from session import engine, SessionLocal
from db.base_class import Base
from models.movie import Movie


def initialize_database():
    Base.metadata.create_all(bind=engine)
    print('database created')


# 插入初始化数据
def insert_initial_data():
    movie_data = [
        {'title': 'My Neighbor Totoro', 'year': '1988'},
        {'title': 'Dead Poets Society', 'year': '1989'},
        {'title': 'A Perfect World', 'year': '1993'},
        {'title': 'Leon', 'year': '1994'},
        {'title': 'Mahjong', 'year': '1996'},
        {'title': 'Swallowtail Butterfly', 'year': '1996'},
        {'title': 'King of Comedy', 'year': '1999'},
        {'title': 'Devils on the Doorstep', 'year': '1999'},
        {'title': 'WALL-E', 'year': '2008'},
        {'title': 'The Pork of Music', 'year': '2012'},
    ]
    db = SessionLocal()
    for data in movie_data:
        movie = Movie(**data)
        db.add(movie)
    db.commit()
    print('Initial data inserted')


if __name__ == "__main__":
    initialize_database()
    insert_initial_data()
