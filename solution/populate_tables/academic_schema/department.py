# -*- coding: utf-8 -*-
"""
Department Objects
-----------------------

Module for populating Department Class
"""
import logging
from solution.create_classes import Department

__author__ = "neelesh.karthi@gmail.com"

LOGGER = logging.getLogger(name=__name__)


def populate_departments(session):
    """
    Function for populating orm class

    :param session: Session object
    :type session: :class:`sqlalchemy.orm.session.Session`

    :return: None
    :rtype: None
    """
    departments = [
        Department(name="Mathematics"),
        Department(name="Computer Science"),
        Department(name="Physics"),
        Department(name="Chemistry"),
        Department(name="Biology"),
        Department(name="English"),
    ]
    # adding the list of objects to the session
    session.bulk_save_objects(departments)

    LOGGER.debug("Populated Department Table")
