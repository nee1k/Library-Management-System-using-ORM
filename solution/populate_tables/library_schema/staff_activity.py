# -*- coding: utf-8 -*-
"""
Staff_Activity Objects
-------------------------

Module for populating StaffActivity Class
"""
import logging
from datetime import datetime

from solution.create_classes import StaffActivity, Book, Staff
from solution.create_classes.library_schema.staff_activity import calculate_fee

__author__ = "neelesh.karthi@gmail.com"

LOGGER = logging.getLogger(name=__name__)


def lend_book_staff(session):
    """
    Function for populating orm class

    :param session: Session object
    :type session: :class:`sqlalchemy.orm.session.Session`

    :return: None
    :rtype: None
    """
    staff_activities = [
        StaffActivity(staff_id=1, book_id=1, librarian_id=2,
                      issue_date=datetime.strptime("Apr 10 2008  4:15PM", "%b %d %Y %I:%M%p"),
                      due_date=datetime.strptime("May 11 2008", "%b %d %Y")),

        StaffActivity(staff_id=2, book_id=6, librarian_id=6,
                      issue_date=datetime.strptime("Jun 13 2009  12:10PM", "%b %d %Y %I:%M%p"),
                      due_date=datetime.strptime("Jul 14 2009", "%b %d %Y")),

        StaffActivity(staff_id=3, book_id=3, librarian_id=5,
                      issue_date=datetime.strptime("Apr 16 2007  1:33PM", "%b %d %Y %I:%M%p"),
                      due_date=datetime.strptime("May 17 2007", "%b %d %Y")),

        StaffActivity(staff_id=4, book_id=5, librarian_id=4,
                      issue_date=datetime.strptime("May 19 2009  4:15PM", "%b %d %Y %I:%M%p"),
                      due_date=datetime.strptime("Jun 20 2009", "%b %d %Y")),

        StaffActivity(staff_id=6, book_id=4, librarian_id=2,
                      issue_date=datetime.strptime("Apr 02 2007  1:33PM", "%b %d %Y %I:%M%p"),
                      due_date=datetime.strptime("May 03 2007", "%b %d %Y")),

        StaffActivity(staff_id=2, book_id=2, librarian_id=1,
                      issue_date=datetime.strptime("Apr 19 2008  12:10PM", "%b %d %Y %I:%M%p"),
                      due_date=datetime.strptime("May 20 2008", "%b %d %Y")),
    ]

    for staff_activity in staff_activities:
        status = session.query(Book.availability_status).filter(Book.pk_id == staff_activity.book_id).first()

        if status:
            session.add(staff_activity)
            session.query(Book).filter(Book.pk_id == staff_activity.book_id).update({Book.availability_status: 0})
            session.commit()

            LOGGER.debug("Book : %s lent by Staff : %s", staff_activity.book_id, staff_activity.staff_id)
        else:
            LOGGER.error("Book : %s is unavailable", staff_activity.book_id)


def return_book_staff(session, trans_id, return_date, fine_per_day):
    """
    Updates the StaffActivity and Book table while returning the book

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
    staff_activity = session.query(StaffActivity).filter(StaffActivity.pk_id == trans_id).first()

    staff_activity.return_date = return_date
    staff_activity.fine_amt = calculate_fee(staff_activity.due_date, staff_activity.return_date,
                                            fine_per_day)

    LOGGER.debug("Book : %s returned by Staff : %s", staff_activity.book_id, staff_activity.staff_id)

    session.query(Staff).filter(Staff.pk_id == staff_activity.staff_id).update(
        {Staff.fine_amt: Staff.fine_amt + staff_activity.fine_amt})

    session.query(Book).filter(Book.pk_id == staff_activity.book_id).update({Book.availability_status: 1})

    session.merge(staff_activity)
    session.commit()
