# -*- coding: utf-8 -*-
"""
Sort Operations
--------------------

"""
import logging
from sqlalchemy import desc
from solution.create_classes import Author, Librarian, Student

__author__ = "neelesh.karthi@gmail.com"

LOGGER = logging.getLogger(name=__name__)


def sort_author_desc(session):
    """
    Sorts the author name is descending order

    :param session: session object
    :type session: :class:`sqlalchemy.orm.session.Session`

    :return: items_desc
    :rtype: iterable
    """
    items_desc = session.query(Author).order_by(desc(Author.name)).all()

    LOGGER.debug("Sorted in Descending order")
    return items_desc


def sort_librarian_asc(session):
    """
    Sorts the librarian names in ascending order

    :param session: session object
    :type session: :class:`sqlalchemy.orm.session.Session`

    :return: items_asc
    :rtype: iterable
    """
    items_asc = session.query(Librarian).order_by(Librarian.name).all()

    LOGGER.debug("Sorted in Ascending order")
    return items_asc


def sort_fine_desc(session):
    """
    Sorts the student and fine amount in descending order

    :param session: session object
    :type session: :class:`sqlalchemy.orm.session.Session`

    :return: items_asc
    :rtype: iterable
    """
    items_desc = session.query(Student).order_by(desc(Student.fine_amt)).all()

    LOGGER.debug("Sorted in Descending order")
    return items_desc


def perform_sort_operations(session):
    """
    Performs the sort operations using Query API

    :param session: session object
    :type session: :class:`sqlalchemy.orm.session.Session`

    :return: None
    :rtype: None
    """
    with open("results/author_names_desc", "w") as writer:
        sort_result_1 = sort_author_desc(session)
        writer.write("\n-----------Author names in descending order-----------")
        for author in sort_result_1:
            writer.write("\n{} - {}".format(author.pk_id, author.name))

    with open("results/librarian_names_asc", "w") as writer:
        sort_result_2 = sort_librarian_asc(session)
        writer.write("\n-----------Librarian names in ascending order-----------")
        for librarian in sort_result_2:
            writer.write("\n{} - {}".format(librarian.pk_id, librarian.name))

    with open("results/student_fine_desc", "w") as writer:
        sort_result_3 = sort_fine_desc(session)
        writer.write("\n-----------Students with highest fine amount-----------")
        for student in sort_result_3:
            writer.write("\n{} - {} - {}".format(student.pk_id, student.name, student.fine_amt))
