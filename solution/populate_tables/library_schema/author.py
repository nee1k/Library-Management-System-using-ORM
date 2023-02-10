# -*- coding: utf-8 -*-
"""
Author Objects
-----------------------

Module for populating Author Class
"""
import logging

from solution.create_classes import Author

__author__ = "neelesh.karthi@gmail.com"

LOGGER = logging.getLogger(name=__name__)


def populate_authors(session):
    """
    Function for populating orm class

    :param session: Session object
    :type session: :class:`sqlalchemy.orm.session.Session`

    :return: None
    :rtype: None
    """
    authors = [
        Author(name="Jan"),
        Author(name="Creed"),
        Author(name="Darryl"),
        Author(name="Erin"),
        Author(name="Lewis"),
        Author(name="Holly"),
    ]
    # adding the list of objects to the session
    session.bulk_save_objects(authors)

    LOGGER.info("Populated Author Table")
