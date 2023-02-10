# -*- coding: utf-8 -*-
"""
Book Objects
-----------------------

Module for populating Book Class
"""
import logging
from datetime import datetime

from solution.create_classes import Book

__author__ = "neelesh.karthi@gmail.com"

LOGGER = logging.getLogger(name=__name__)


def populate_books(session):
    """
    Function for populating orm class

    :param session: Session object
    :type session: :class:`sqlalchemy.orm.session.Session`

    :return: None
    :rtype: None
    """
    books = [
        Book(
            name="Harry Potter",
            author_id=6,
            course_id=2,
            date_of_purchase=datetime.strptime("2021-10-10", "%Y-%m-%d"),
            date_of_publishing=datetime.strptime("2011-04-11", "%Y-%m-%d")),

        Book(
            name="Algorithms",
            author_id=2,
            course_id=3,
            date_of_purchase=datetime.strptime("2021-09-06", "%Y-%m-%d"),
            date_of_publishing=datetime.strptime("2005-03-12", "%Y-%m-%d")),

        Book(
            name="Laws of Motion",
            author_id=4,
            course_id=3,
            date_of_purchase=datetime.strptime("2011-04-03", "%Y-%m-%d"),
            date_of_publishing=datetime.strptime("2000-05-19", "%Y-%m-%d")),

        Book(
            name="Human Anatomy by Tata McGraw Hill",
            author_id=3,
            course_id=5,
            date_of_purchase=datetime.strptime("2017-08-19", "%Y-%m-%d"),
            date_of_publishing=datetime.strptime("2015-06-03", "%Y-%m-%d")),

        Book(
            name="Properties of Carbon",
            author_id=3,
            course_id=4,
            date_of_purchase=datetime.strptime("2021-08-17", "%Y-%m-%d"),
            date_of_publishing=datetime.strptime("1996-12-29", "%Y-%m-%d")),

        Book(
            name="Python",
            author_id=1,
            course_id=1,
            date_of_purchase=datetime.strptime("2021-10-10", "%Y-%m-%d"),
            date_of_publishing=datetime.strptime("1991-08-03", "%Y-%m-%d")),

        Book(
            name="Song of Ice and Fire",
            author_id=6,
            course_id=2,
            date_of_purchase=datetime.strptime("2021-10-10", "%Y-%m-%d"),
            date_of_publishing=datetime.strptime("2011-04-11", "%Y-%m-%d")),

        Book(
            name="Data Structures",
            author_id=2,
            course_id=1,
            date_of_purchase=datetime.strptime("2021-09-06", "%Y-%m-%d"),
            date_of_publishing=datetime.strptime("2005-03-12", "%Y-%m-%d")),

        Book(
            name="Fundamentals of Gravity",
            author_id=4,
            course_id=3,
            date_of_purchase=datetime.strptime("2011-04-03", "%Y-%m-%d"),
            date_of_publishing=datetime.strptime("2000-05-19", "%Y-%m-%d")),

        Book(
            name="Microorganisms",
            author_id=3,
            course_id=5,
            date_of_purchase=datetime.strptime("2017-08-19", "%Y-%m-%d"),
            date_of_publishing=datetime.strptime("2015-06-03", "%Y-%m-%d")),

        Book(
            name="Organic Chemistry",
            author_id=3,
            course_id=4,
            date_of_purchase=datetime.strptime("2021-08-17", "%Y-%m-%d"),
            date_of_publishing=datetime.strptime("1996-12-29", "%Y-%m-%d")),

        Book(
            name="SQL",
            author_id=1,
            course_id=1,
            date_of_purchase=datetime.strptime("2021-10-10", "%Y-%m-%d"),
            date_of_publishing=datetime.strptime("1991-08-03", "%Y-%m-%d"))
    ]
    # adding the list of objects to the session
    session.bulk_save_objects(books)

    LOGGER.info("Populated Book Table")
