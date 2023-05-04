import os

from sqlalchemy import and_, or_, not_, desc, func, distinct, text
from models.database import DATABASE_NAME, Session
import create_database as db_creator

from home.hw37.models.lesson import Lesson, association_table
from home.hw37.models.student import Student
from home.hw37.models.group import Group


if __name__ == '__main__':
    db_is_created = os.path.exists(DATABASE_NAME)
    if not db_is_created:
        db_creator.create_database()

    session = Session()

    # print(session.query(Student).first())

    # print(session.query(Student).count())

    # for it, gr in session.query(Student.surname, Group.group_name).filter(
    #         and_(association_table.c.lesson_id == Student.id, association_table.c.group_id == Group.id)):
    #     print(it, gr)

    # for it in session.query(Student).order_by(Student.surname):
    #     print(it)

    # print(session.query(Student).first())
    # print("*" * 50)

    # for it in session.query(Student).join(Group).filter(Student.address.like('г.%')):
    #     print(it)

    # for it in session.query(Student).filter(Student.age.like("16")):
    #     print(it)

    # for it in session.query(Student.address):
    #     print(it)

    # for it in session.query(Student.address).order_by(Student.address):
    #     print(it)

    # for it in session.query(Student).filter(Student.age < 20).order_by(Student.age):
    #     print(it)
