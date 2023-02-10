# -*- coding: utf-8 -*-
"""
Student Objects
-----------------------

Module for populating Student Class
"""
import logging
from datetime import datetime

from solution.create_classes import Student

__author__ = "neelesh.karthi@gmail.com"

LOGGER = logging.getLogger(name=__name__)


def populate_students(session):
    """
    Function for populating orm class

    :param session: Session object
    :type session: :class:`sqlalchemy.orm.session.Session`

    :return: None
    :rtype: None
    """
    students = [
        Student(name="Kevin", date_of_joining=datetime.strptime('May 1 2008  1:33PM', '%b %d %Y %I:%M%p'),
                dept_id=2, fine_amt=0),
        Student(name="Oscar", date_of_joining=datetime.strptime('Jun 12 2007  1:33PM', '%b %d %Y %I:%M%p'),
                dept_id=1, fine_amt=0),
        Student(name="Angela", date_of_joining=datetime.strptime('Jan 23 2013  1:33PM', '%b %d %Y %I:%M%p'),
                dept_id=1, fine_amt=0),
        Student(name="Kelly", date_of_joining=datetime.strptime('Nov 17 2017  1:33PM', '%b %d %Y %I:%M%p'),
                dept_id=5, fine_amt=0),
        Student(name="Ryan", date_of_joining=datetime.strptime('Mar 9 2010  1:33PM', '%b %d %Y %I:%M%p'),
                dept_id=4, fine_amt=0),
        Student(name="Meredith", date_of_joining=datetime.strptime('Dec 7 2009  1:33PM', '%b %d %Y %I:%M%p'),
                dept_id=3, fine_amt=0),
    ]
    # adding the list of objects to the session
    session.bulk_save_objects(students)

    LOGGER.info("Populated Student Table")
