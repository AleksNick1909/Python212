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

