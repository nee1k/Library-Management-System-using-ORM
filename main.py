# -*- coding: utf-8 -*-
"""
Alpha University is a reputed institution with more than 5000 students and 300 teaching staff.
Recent survey results indicate that their library facilities are not up to standards. To counter
the issue, the management decides to have an online portal where users (students and staff)
can borrow books from the library and pay fine online, in case of late return. Users can also
search for books to get to know the current status of the book (borrowed or available). The
students have volunteered and designed a database schema for the portal.
"""
import logging
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from helper import initialize_logger, initialize_command_args_amt

from solution.base_class import create_tables
from solution.populate_tables import populate_authors, populate_books, populate_courses, populate_departments, \
    populate_enrollments, \
    populate_librarians, lend_book_staff, populate_staffs, lend_book_student, populate_students
from solution.populate_tables.library_schema.staff_activity import return_book_staff
from solution.populate_tables.library_schema.student_activity import return_book_student
from solution.query_tables.querying import perform_query_operations, perform_join_operations
from solution.query_tables.sorting import perform_sort_operations
from solution.query_tables.updating import perform_update_operations

__author__ = "neelesh.karthi@gmail.com"

LOGGER = logging.getLogger(name=__name__)


def populate_tables(session):
    """
    Creates and Populates ORM create_classes

    :param session: session object for creation
    :type session: :class:`sqlalchemy.orm.session.Session`

    :return: None
    :rtype: None
    """
    # create orm classes and populate the tables
    populate_departments(session)
    populate_students(session)
    populate_staffs(session)
    populate_courses(session)
    populate_enrollments(session)
    populate_authors(session)
    populate_books(session)
    populate_librarians(session)


def lend_books(session):
    """
    Creates and populates the StudentActivity and StaffActivity table

    :param session: session object for library_session
    :type session: :class:`sqlalchemy.orm.session.Session`

    :return: None
    :rtype: None
    """
    # populate student_activity and staff_activity tables with return_date and fine_amt as Null
    lend_book_staff(session)
    lend_book_student(session)


def return_books(session, fine_per_day):
    """
    Updates the StudentActivity and StaffActivity table

    :param session: session object for library_session
    :type session: :class:`sqlalchemy.orm.session.Session`

    :param fine_per_day: fine per day
    :type fine_per_day: float

    :return: None
    :rtype: None
    """
    try:
        return_book_staff(session, 1, datetime.strptime("May 17 2008  1:33PM", "%b %d %Y %I:%M%p"), fine_per_day)
        return_book_staff(session, 2, datetime.strptime("Jul 25 2009  4:15PM", "%b %d %Y %I:%M%p"), fine_per_day)
        return_book_staff(session, 3, datetime.strptime("Jul 28 2007  12:10PM", "%b %d %Y %I:%M%p"), fine_per_day)
        return_book_staff(session, 4, datetime.strptime("Aug 14 2009  1:33PM", "%b %d %Y %I:%M%p"), fine_per_day)
        return_book_staff(session, 5, datetime.strptime("Jun 24 2007  4:15PM", "%b %d %Y %I:%M%p"), fine_per_day)
        return_book_staff(session, 6, datetime.strptime("Aug 27 2008  1:33PM", "%b %d %Y %I:%M%p"), fine_per_day)

    except AttributeError:
        LOGGER.error("Lend operation was not successful")
        raise

    try:
        return_book_student(session, 1, datetime.strptime("May 27 2008  1:33PM", "%b %d %Y %I:%M%p"), fine_per_day)
        return_book_student(session, 2, datetime.strptime("Jun 25 2009  4:15PM", "%b %d %Y %I:%M%p"), fine_per_day)
        return_book_student(session, 3, datetime.strptime("Jul 28 2007  12:10PM", "%b %d %Y %I:%M%p"), fine_per_day)
        return_book_student(session, 4, datetime.strptime("Aug 24 2009  1:33PM", "%b %d %Y %I:%M%p"), fine_per_day)
        return_book_student(session, 5, datetime.strptime("Sep 14 2008  4:15PM", "%b %d %Y %I:%M%p"), fine_per_day)
        return_book_student(session, 6, datetime.strptime("May 24 2007  1:33PM", "%b %d %Y %I:%M%p"), fine_per_day)

    except AttributeError:
        LOGGER.error("Lend operation was not successful")
        raise


def query_tables(session):
    """
    Performs join, sort and update operations on the database

    :param session: session object for querying
    :type session: Session

    :return: None
    :rtype: None
    """
    # query operations
    perform_query_operations(session)

    # join operations
    perform_join_operations(session)

    # sort operations
    perform_sort_operations(session)

    # update operations
    perform_update_operations(session)


def open_library(fine_amt):
    """
    Main function for open_library

    :param fine_amt: fine_amount
    :type fine_amt: float

    :return: None
    :rtype: None
    """
    # connection
    connection_string = "mysql+pymysql://root:qawsedrf@localhost:3306/assignment_5"
    engine = create_engine(connection_string, echo=False)
    connection = engine.connect()

    # Session
    Session = sessionmaker(bind=connection)

    # create orm classes and populate tables
    creation_session = Session()
    create_tables(engine)
    populate_tables(creation_session)
    creation_session.commit()
    creation_session.close()

    # create and update student_activity and staff_activity tables while lending and returning the books
    library_session = Session()
    lend_books(library_session)
    return_books(library_session, fine_amt)
    library_session.commit()
    library_session.close()

    # query the populated tables
    query_session = Session()
    query_tables(query_session)
    query_session.commit()
    query_session.close()


if __name__ == "__main__":
    # initialize logger
    initialize_logger()

    # initialize fine amount per day
    fine_amount = initialize_command_args_amt()

    # call open_library function
    open_library(fine_amount)
