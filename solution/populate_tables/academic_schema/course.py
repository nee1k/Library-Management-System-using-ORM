# -*- coding: utf-8 -*-
"""
Course Objects
-----------------

Module for populating Course Class
"""
import logging

from solution.create_classes import Course

__author__ = "neelesh.karthi@gmail.com"

LOGGER = logging.getLogger(name=__name__)


def populate_courses(session):
    """
    Function for populating orm class

    :param session: Session object
    :type session: :class:`sqlalchemy.orm.session.Session`

    :return: None
    :rtype: None
    """
    courses = [
        Course(name="Introduction to Computer Science", staff_id=1, dept_id=2),
        Course(name="English", staff_id=6, dept_id=6),
        Course(name="Introduction to Physics", staff_id=3, dept_id=1),
        Course(name="Organic Chemistry", staff_id=4, dept_id=4),
        Course(name="Human Anatomy", staff_id=5, dept_id=5),
        Course(name="Force and Motion", staff_id=2, dept_id=3),
    ]
    # adding the list of objects to the session
    session.bulk_save_objects(courses)

    LOGGER.info("Populated Course Table")
