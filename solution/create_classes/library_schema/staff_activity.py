# -*- coding: utf-8 -*-
"""
Staff_Activity Class
----------------------

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


def calculate_fee(due_date, return_date, fine_per_day):
    """
    Calculates the number of days between the return day and multiplies with the fine_per_day

    :param due_date: due date
    :type due_date: :class:`datetime.date`

    :param return_date: return date
    :type return_date: :class:`datetime.datetime`

    :param fine_per_day: fine amount
    :type fine_per_day: float

    :return: total_fine
    :rtype: float
    """
    if return_date.date() > due_date:
        total_fine = (return_date.date() - due_date).days * fine_per_day
    else:
        total_fine = 0

    return total_fine


class StaffActivity(AuditAttributesMixin, Base):
    """
    StaffActivity class docstring

    :ivar pk_id: pk_id
    :vartype pk_id: int

    :ivar name: name
    :vartype name: str

    :ivar staff_id: staff_id
    :vartype staff_id: int

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
    __tablename__ = "staff_activity"

    staff_id = Column(INTEGER, ForeignKey("staff.pk_id"))
    book_id = Column(INTEGER, ForeignKey("book.pk_id"))
    librarian_id = Column(INTEGER, ForeignKey("librarian.pk_id"))

    issue_date = Column(DATETIME, nullable=False)
    due_date = Column(DATE, nullable=False)
    return_date = Column(DATETIME, nullable=True)
    fine_amt = Column(FLOAT, nullable=True)

    # relationships
    staff = relationship("Staff", back_populates="staff_activity")
    book = relationship("Book", back_populates="staff_activity")
    librarian = relationship("Librarian", back_populates="staff_activity")

    def __init__(self, staff_id, book_id, librarian_id, issue_date, due_date):
        """
        creates an instance of the class

        :param staff_id: staff's pk_id
        :type staff_id: int

        :param book_id: book's pk_id
        :type book_id: int

        :param librarian_id: librarian's pk_id
        :type librarian_id: int

        :param issue_date: issue date
        :type issue_date: :class:`datetime.datetime`

        :param due_date: due date
        :type due_date: :class:`datetime.datetime.date`
        """
        self.staff_id = staff_id
        self.book_id = book_id
        self.librarian_id = librarian_id
        self.issue_date = issue_date
        self.due_date = due_date
