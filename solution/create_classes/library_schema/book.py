# -*- coding: utf-8 -*-
"""
Book Class
----------------------

Code for creating ORM Class
"""
import logging

from sqlalchemy import Column, VARCHAR, DATE, ForeignKey, BOOLEAN
from sqlalchemy import INTEGER
from sqlalchemy.orm import relationship

from solution.base_class import Base, AuditAttributesMixin

__author__ = "neelesh.karthi@gmail.com"

LOGGER = logging.getLogger(name=__name__)


class Book(AuditAttributesMixin, Base):
    """
    Book class docstring

    :ivar pk_id: pk_id
    :vartype pk_id: int

    :ivar name: name
    :vartype name: str

    :ivar author_id: author_id
    :vartype author_id: int

    :ivar course_id: course_id
    :vartype course_id: int

    :ivar date_of_publishing: date_of_publishing
    :vartype date_of_publishing: :class:`datetime.date`

    :ivar date_of_purchase: date_of_purchase
    :vartype date_of_purchase: :class:`datetime.date`

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
    __tablename__ = "book"

    name = Column(VARCHAR(255), nullable=False)

    author_id = Column(INTEGER, ForeignKey("author.pk_id"))
    course_id = Column(INTEGER, ForeignKey("course.pk_id"))

    date_of_publishing = Column(DATE, nullable=False)
    date_of_purchase = Column(DATE, nullable=False)
    availability_status = Column(BOOLEAN, nullable=False, default=True)

    # relationships
    author = relationship("Author", back_populates="book")
    course = relationship("Course", back_populates="book")
    student_activity = relationship("StudentActivity", back_populates="book")
    staff_activity = relationship("StaffActivity", back_populates="book")

    def __init__(self, name, author_id, course_id, date_of_publishing, date_of_purchase):
        """
        creates an instance of the class

        :param name: name
        :type name: str

        :param author_id: author_id
        :type author_id: int

        :param course_id: course_id
        :type course_id: int

        :param date_of_publishing: date_of_publishing
        :type date_of_publishing:  :class: `datetime.date`

        :param date_of_purchase: date_of_purchase
        :type date_of_purchase:  :class: `datetime.date`

        """
        self.name = name
        self.author_id = author_id
        self.course_id = course_id
        self.date_of_purchase = date_of_purchase
        self.date_of_publishing = date_of_publishing

        LOGGER.debug("Created %s (Book Object)", name)
