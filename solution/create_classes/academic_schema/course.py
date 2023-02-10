# -*- coding: utf-8 -*-
"""
Course Class
----------------------

Code for creating ORM Class
"""
import logging

from sqlalchemy import Column, VARCHAR, ForeignKey
from sqlalchemy import INTEGER
from sqlalchemy.orm import relationship

from solution.base_class import AuditAttributesMixin, Base

__author__ = "neelesh.karthi@gmail.com"

LOGGER = logging.getLogger(name=__name__)


class Course(AuditAttributesMixin, Base):
    """
    Course class docstring

    :ivar pk_id: pk_id
    :vartype pk_id: int

    :ivar name: name
    :vartype name: str

    :ivar dept_id: dept_id
    :vartype dept_id: int

    :ivar dept_id: dept_id
    :vartype dept_id: int

    :ivar created_by: user name of creator
    :vartype created_by: str

    :ivar created_on: timestamp while creating
    :vartype created_on: :class:`datetime.date`

    :ivar last_updated_by: user name of updater
    :vartype last_updated_by: str

    :ivar last_updated_on: timestamp while updating
    :vartype last_updated_on: :class:`datetime.date`

    :ivar is_active: active status
    :vartype is_active: bool

    """
    __tablename__ = "course"

    name = Column(VARCHAR(255), nullable=False)

    dept_id = Column(INTEGER, ForeignKey("department.pk_id"))
    staff_id = Column(INTEGER, ForeignKey("staff.pk_id"))

    # relationships
    department = relationship("Department", back_populates="course")
    staff = relationship("Staff", back_populates="course")
    enrollment = relationship("Enrollment", back_populates="course")
    book = relationship("Book", back_populates="course")

    def __init__(self, name, dept_id, staff_id):
        """
        creates an instance of the class

        :param name: name
        :type name: str

        :param dept_id: department's pk_id
        :type dept_id: int

        :param staff_id: staff's pk_id
        :type staff_id: int

        """
        self.name = name
        self.dept_id = dept_id
        self.staff_id = staff_id

        LOGGER.debug("Created %s (Course Object)", name)
