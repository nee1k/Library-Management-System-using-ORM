# -*- coding: utf-8 -*-
"""
Update Operations
--------------------

"""
import logging

from solution.create_classes import Book, Staff

__author__ = "neelesh.karthi@gmail.com"

LOGGER = logging.getLogger(name=__name__)


def update_book_name(queried_name, new_name, session):
    """
    Updates the items in Book

    :param queried_name: queried name
    :type queried_name: str

    :param new_name: new name
    :type new_name: str

    :param session: session object
    :type session: :class:`sqlalchemy.orm.session.Session`

    :return: None
    :rtype: None
    """
    books_to_update = session.query(Book).filter(Book.name == queried_name).all()

    if books_to_update:

        for book_to_update in books_to_update:
            book_to_update.name = new_name

            session.merge(book_to_update)
        LOGGER.debug("Changed from %s to %s", queried_name, new_name)

    else:
        LOGGER.error("Book name not found : %s", queried_name)


def update_staff_name(queried_name, new_name, session):
    """
    Updates the items in Staff

    :param queried_name: queried name
    :type queried_name: str

    :param new_name: new name
    :type new_name: str

    :param session: session object
    :type session: :class:`sqlalchemy.orm.session.Session`

    :return: None
    :rtype: None
    """
    staffs_to_update = session.query(Staff).filter(Staff.name == queried_name).all()

    if staffs_to_update:
        for staff_to_update in staffs_to_update:
            staff_to_update.name = new_name

            session.merge(staff_to_update)
        LOGGER.debug("Changed from %s to %s", queried_name, new_name)

    else:
        LOGGER.error("Author name not found : %s", queried_name)


def perform_update_operations(session):
    """
    Performs the update operations using Query API and Textual API

    :param session: session object
    :type session: :class:`sqlalchemy.orm.session.Session`

    :return: None
    :rtype: None
    """
    with open("results/updated_books", "w") as writer:
        update_book_name("Python", "Python 3.9", session)
        update_book_result = session.query(Book).all()
        writer.write("\n-----------Update book names-----------")
        for book in update_book_result:
            writer.write("\n{} - {}".format(book.pk_id, book.name))

    with open("results/updated_staffs", "w") as writer:
        update_staff_name("Andrew", "Andy", session)
        update_staff_result = session.query(Staff).all()
        writer.write("\n-----------Update staff names-----------")
        for staff in update_staff_result:
            writer.write("\n{} - {}".format(staff.pk_id, staff.name))
