# -*- coding: utf-8 -*-
"""
Student_Activity Class
-------------------------

Code for creating ORM Class
"""
import logging

from sqlalchemy import Column, DATE, ForeignKey
from sqlalchemy import INTEGER
from sqlalchemy.dialects.mysql import DATETIME, FLOAT
from sqlalchemy.orm import relationship
from solution.base_class import AuditAttributesMixin, Base

__author__ = "neelesh.karthi@gmail.com"

LOGGER = logging.getLogger(name=__name__)


class StudentActivity(AuditAttributesMixin, Base):
    """
    StudentActivity class docstring

    :ivar pk_id: pk_id
    :vartype pk_id: int

    :ivar name: name
    :vartype name: str

    :ivar student_id: student_id
    :vartype student_id: int

    :ivar book_id: book_id
    :vartype book_id: int

    :ivar librarian_id: librarian_id
    :vartype librarian_id: int

    :ivar created_by: user name of creator
    :vartype created_by: str

    :ivar created_on: timestamp while creating
    :vartype created_on: :class:`datetime.datetime`

    :ivar last_updated_by: user name of updater
    :vartype last_updated_by: str

    :ivar last_updated_on: timestamp while updating
    :vartype last_updated_on: :class:`datetime.datetime`

    :ivar is_active: active status
    :vartype is_active: bool

    """
    __tablename__ = "student_activity"

    student_id = Column(INTEGER, ForeignKey("student.pk_id"))
    book_id = Column(INTEGER, ForeignKey("book.pk_id"))
    librarian_id = Column(INTEGER, ForeignKey("librarian.pk_id"))

    issue_date = Column(DATETIME, nullable=False)
    due_date = Column(DATE, nullable=False)
    return_date = Column(DATE, nullable=True)
    fine_amt = Column(FLOAT, nullable=True)

    # relationships
    student = relationship("Student", back_populates="student_activity")
    book = relationship("Book", back_populates="student_activity")
    librarian = relationship("Librarian", back_populates="student_activity")

    def __init__(self, student_id, book_id, librarian_id, issue_date, due_date):
        """
        creates an instance of the class

        :param student_id: student's pk_id
        :type student_id: int

        :param book_id: book's pk_id
        :type book_id: int

        :param librarian_id: librarian's pk_id
        :type librarian_id: int

        :param issue_date: issue_date
        :type issue_date:  :class:`datetime.datetime`

        :param due_date: due_date
        :type due_date:  :class: `datetime.date`

        """
        self.student_id = student_id
        self.book_id = book_id
        self.librarian_id = librarian_id
        self.issue_date = issue_date
        self.due_date = due_date
