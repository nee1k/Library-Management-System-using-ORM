# -*- coding: utf-8 -*-
"""
Student_Activity Objects
--------------------------

Module for populating StudentActivity Class
"""
import logging
from datetime import datetime
from solution.create_classes.library_schema.staff_activity import calculate_fee
from solution.create_classes import StudentActivity, Book, Student

__author__ = "neelesh.karthi@gmail.com"

LOGGER = logging.getLogger(name=__name__)


def lend_book_student(session):
    """
    Function for populating orm class

    :param session: Session object
    :type session: :class:`sqlalchemy.orm.session.Session`

    :return: None
    :rtype: None
    """
    student_activities = [
        StudentActivity(student_id=3, book_id=7, librarian_id=2,
                        issue_date=datetime.strptime("Apr 10 2008  4:15PM", "%b %d %Y %I:%M%p"),
                        due_date=datetime.strptime("May 11 2008", "%b %d %Y")),

        StudentActivity(student_id=5, book_id=12, librarian_id=6,
                        issue_date=datetime.strptime("Jun 13 2009  12:10PM", "%b %d %Y %I:%M%p"),
                        due_date=datetime.strptime("Jul 14 2009", "%b %d %Y")),

        StudentActivity(student_id=1, book_id=9, librarian_id=5,
                        issue_date=datetime.strptime("Apr 16 2007  1:33PM", "%b %d %Y %I:%M%p"),
                        due_date=datetime.strptime("May 17 2007", "%b %d %Y")),

        StudentActivity(student_id=6, book_id=11, librarian_id=4,
                        issue_date=datetime.strptime("May 19 2009  4:15PM", "%b %d %Y %I:%M%p"),
                        due_date=datetime.strptime("Jun 20 2009", "%b %d %Y")),

        StudentActivity(student_id=2, book_id=8, librarian_id=1,
                        issue_date=datetime.strptime("Apr 19 2008  12:10PM", "%b %d %Y %I:%M%p"),
                        due_date=datetime.strptime("May 20 2008", "%b %d %Y")),

        StudentActivity(student_id=1, book_id=10, librarian_id=3,
                        issue_date=datetime.strptime("Jun 22 2008  12:10PM", "%b %d %Y %I:%M%p"),
                        due_date=datetime.strptime("Jul 23 2008", "%b %d %Y")),
    ]

    for student_activity in student_activities:
        status = session.query(Book.availability_status).filter(Book.pk_id == student_activity.book_id).first()

        if status:
            session.add(student_activity)
            session.query(Book).filter(Book.pk_id == student_activity.book_id).update({Book.availability_status: 0})

            session.commit()

            LOGGER.debug("Book : %s lent by Student : %s", student_activity.book_id, student_activity.student_id)
        else:
            LOGGER.error("Book : %s is unavailable", student_activity.book_id)


def return_book_student(session, trans_id, return_date, fine_per_day):
    """
    Updates the StudentActivity and Book table while returning the book

    :param session: Session object
    :type session: :class:`sqlalchemy.orm.session.Session`

    :param trans_id: pk_id in StaffActivity table
    :type trans_id: int

    :param return_date: return date
    :type return_date: :class:`datetime.datetime`

    :param fine_per_day: fine_per_day
    :type fine_per_day: float

    :return: None
    :rtype: None
    """
    student_activity = session.query(StudentActivity).filter(StudentActivity.pk_id == trans_id).first()

    student_activity.return_date = return_date
    student_activity.fine_amt = calculate_fee(student_activity.due_date, student_activity.return_date,
                                              fine_per_day)

    LOGGER.debug("Book : %s returned by Student : %s", student_activity.book_id, student_activity.student_id)

    session.query(Student).filter(Student.pk_id == student_activity.student_id).update(
        {Student.fine_amt: Student.fine_amt + student_activity.fine_amt})

    session.query(Book).filter(Book.pk_id == student_activity.book_id).update({Book.availability_status: 1})

    session.merge(student_activity)
    session.commit()
