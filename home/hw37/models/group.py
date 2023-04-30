from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from home.hw37.models.database import Base


class Group(Base):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True)
    group_name = Column(String(250), nullable=False)
    student = relationship('Student')  # служебный элемент, позволяет устанавливать межтабличные отношения

    def __repr__(self):
        return f"Группа (ID: {self.id}, Название группы: {self.group_name})"

