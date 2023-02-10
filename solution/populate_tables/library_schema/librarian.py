# -*- coding: utf-8 -*-
"""
Librarian Objects
-----------------------

Module for populating Librarian Class
"""
import logging

from solution.create_classes import Librarian

__author__ = "neelesh.karthi@gmail.com"

LOGGER = logging.getLogger(name=__name__)


def populate_librarians(session):
    """
    Function for populating orm class

    :param session: Session object
    :type session: :class:`sqlalchemy.orm.session.Session`

    :return: None
    :rtype: None
    """
    librarians = [
        Librarian(name="Steve"),
        Librarian(name="Wilson"),
        Librarian(name="John"),
        Librarian(name="Jenna"),
        Librarian(name="Novak"),
        Librarian(name="Ed Helms"),
    ]
    # adding the list of objects to the session
    session.bulk_save_objects(librarians)

    LOGGER.info("Populated Library Table")
