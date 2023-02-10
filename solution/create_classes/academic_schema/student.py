# -*- coding: utf-8 -*-
"""
Student Class
----------------------

Code for creating ORM Class
"""
import logging

from sqlalchemy import Column, VARCHAR, DATE, ForeignKey
from sqlalchemy import INTEGER
from sqlalchemy.dialects.mysql import FLOAT
from sqlalchemy.orm import relationship

from solution.base_class import AuditAttributesMixin, Base

__author__ = "neelesh.karthi@gmail.com"

LOGGER = logging.getLogger(name=__name__)


class Student(AuditAttributesMixin, Base):
    """
    Student class docstring

    :ivar pk_id: pk_id
    :vartype pk_id: int

    :ivar name: name
    :vartype name: str

    :ivar date_of_joining: date_of_joining
    :vartype date_of_joining: :class:`datetime.date`

    :ivar dept_id: dept_id
    :vartype dept_id: int

    :ivar fine_amt: fine amount
    :vartype fine_amt: float

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
    __tablename__ = "student"

    name = Column(VARCHAR(255), nullable=False)
    date_of_joining = Column(DATE, nullable=False)
    dept_id = Column(INTEGER, ForeignKey("department.pk_id"), nullable=False)
    fine_amt = Column(FLOAT, default=0, nullable=False)

    # relationship
    department = relationship("Department", back_populates="student")
    enrollment = relationship("Enrollment", back_populates="student")
    student_activity = relationship("StudentActivity", back_populates="student")

    def __init__(self, name, dept_id, date_of_joining, fine_amt):
        """
        creates an instance of the class

        :param name: name
        :type name: str

        :param dept_id: department's pk_id
        :type dept_id: int

        :param fine_amt: fine amount
        :type fine_amt: float

        :param date_of_joining: date_of_joining
        :type date_of_joining:  :class: `datetime.date`
        """
        self.name = name
        self.dept_id = dept_id
        self.date_of_joining = date_of_joining
        self.fine_amt = fine_amt

        LOGGER.debug("Created %s (Student Object)", name)
