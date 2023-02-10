# -*- coding: utf-8 -*-
"""
Staff Objects
-----------------------

Module for populating Staff Class
"""
import logging
from datetime import datetime

from solution.create_classes import Staff

__author__ = "neelesh.karthi@gmail.com"

LOGGER = logging.getLogger(name=__name__)


def populate_staffs(session):
    """
    Function for populating orm class

    :param session: Session object
    :type session: :class:`sqlalchemy.orm.session.Session`

    :return: None
    :rtype: None
    """
    staffs = [
        Staff(name="Micheal", date_of_joining=datetime.strptime('May 1 2008', '%b %d %Y'), dept_id=2),
        Staff(name="Dwight", date_of_joining=datetime.strptime('Jun 12 2007', '%b %d %Y'), dept_id=1),
        Staff(name="Jim", date_of_joining=datetime.strptime('Jan 23 2013', '%b %d %Y'), dept_id=1),
        Staff(name="Andrew", date_of_joining=datetime.strptime('Nov 17 2017', '%b %d %Y'), dept_id=5),
        Staff(name="Stanley", date_of_joining=datetime.strptime('Mar 9 2010', '%b %d %Y'), dept_id=4),
        Staff(name="Phyllis", date_of_joining=datetime.strptime('Dec 7 2009', '%b %d %Y'), dept_id=3),
    ]
    # adding the list of objects to the session
    session.bulk_save_objects(staffs)

    LOGGER.info("Populated Staff Table")
