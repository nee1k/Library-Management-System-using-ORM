# -*- coding: utf-8 -*-
"""
Enrollment Objects
-----------------------

Module for populating Enrollment Class
"""
import logging

from solution.create_classes import Enrollment

__author__ = "neelesh.karthi@gmail.com"

LOGGER = logging.getLogger(name=__name__)


def populate_enrollments(session):
    """
    Function for populating orm class

    :param session: Session object
    :type session: :class:`sqlalchemy.orm.session.Session`

    :return: None
    :rtype: None
    """
    enrollments = [
        Enrollment(student_id=1, course_id=2),
        Enrollment(student_id=6, course_id=1),
        Enrollment(student_id=2, course_id=1),
        Enrollment(student_id=3, course_id=5),
        Enrollment(student_id=4, course_id=4),
        Enrollment(student_id=6, course_id=3),
        Enrollment(student_id=1, course_id=6),
        Enrollment(student_id=5, course_id=5),
        Enrollment(student_id=3, course_id=4),
        Enrollment(student_id=4, course_id=3),
        Enrollment(student_id=5, course_id=2),
        Enrollment(student_id=6, course_id=1),
        Enrollment(student_id=1, course_id=1),
        Enrollment(student_id=6, course_id=5),
        Enrollment(student_id=3, course_id=6),
        Enrollment(student_id=3, course_id=4),
        Enrollment(student_id=3, course_id=2),
        Enrollment(student_id=2, course_id=1),
        Enrollment(student_id=6, course_id=2),
        Enrollment(student_id=3, course_id=1),
        Enrollment(student_id=2, course_id=1),
        Enrollment(student_id=3, course_id=5),
        Enrollment(student_id=2, course_id=4),
        Enrollment(student_id=1, course_id=3),
    ]
    # adding the list of objects to the session
    session.bulk_save_objects(enrollments)

    LOGGER.info("Populated Enrollment Table")
