# -*- coding: utf-8 -*-
"""
Enrollment Class
----------------------

Code for creating ORM Class
"""
import logging

from sqlalchemy import Column, ForeignKey
from sqlalchemy import INTEGER
from sqlalchemy.orm import relationship

from solution.base_class import AuditAttributesMixin, Base

__author__ = "neelesh.karthi@gmail.com"

LOGGER = logging.getLogger(name=__name__)


class Enrollment(AuditAttributesMixin, Base):
    """
    Enrollment class docstring

    :ivar pk_id: pk_id
    :vartype pk_id: int

    :ivar name: name
    :vartype name: str

    :ivar date_of_joining: date_of_joining
    :vartype date_of_joining: :class:`datetime.date`

    :ivar dept_id: dept_id
    :vartype dept_id: int

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
    __tablename__ = "enrollment"

    student_id = Column(INTEGER, ForeignKey("student.pk_id"))
    course_id = Column(INTEGER, ForeignKey("course.pk_id"))

    # relationships
    student = relationship("Student", back_populates="enrollment")
    course = relationship("Course", back_populates="enrollment")

    def __init__(self, student_id, course_id):
        """
        creates an instance of the class

        :param student_id: student's pk_id
        :type student_id: int

        :param course_id: course's pk_id
        :type course_id: int

        """
        self.student_id = student_id
        self.course_id = course_id

        LOGGER.debug("Created Enrollment Object")
