# -*- coding: utf-8 -*-
"""
Query and Join Operations
---------------------------

"""
import logging

from sqlalchemy import func, desc

from solution.create_classes import Book, Student, Department, Staff, StudentActivity, Course, Enrollment

__author__ = "neelesh.karthi@gmail.com"

LOGGER = logging.getLogger(name=__name__)


def query_available_books(session):
    """
    Returns the books that are available in the library

    :param session: session object
    :type session: :class:`sqlalchemy.orm.session.Session`

    :return: books
    :rtype: list
    """
    books = session.query(Book).filter(Book.availability_status == 1).all()
    return books


def query_popular_course(session):
    """
    Returns the courses that had the highest enrollments

    :param session: session object
    :type session: :class:`sqlalchemy.orm.session.Session`

    :return: course
    :rtype: list
    """
    courses = session. \
        query(Enrollment.course_id, Course.name, func.count(Enrollment.student_id)). \
        join(Course, Course.pk_id == Enrollment.course_id). \
        group_by(Enrollment.course_id). \
        order_by(desc(func.count(Enrollment.student_id))).all()

    return courses


def query_popular_student(session):
    """
    Returns the courses that had the highest enrollments

    :param session: session object
    :type session: :class:`sqlalchemy.orm.session.Session`

    :return: student
    :rtype: list
    """
    courses = session. \
        query(Enrollment.student_id, Student.name, func.count(Enrollment.course_id)). \
        join(Student, Student.pk_id == Enrollment.student_id). \
        group_by(Enrollment.student_id). \
        order_by(desc(func.count(Enrollment.course_id))).all()

    return courses


def perform_query_operations(session):
    """
    Performs the query operations using Query API

    :param session: session object
    :type session: :class:`sqlalchemy.orm.session.Session`

    :return: None
    :rtype: None
    """
    with open("results/available_books", "w") as writer:
        writer.write("\n-----------Available books-----------")
        result = query_available_books(session)
        for row in result:
            writer.write("\n{} - {}".format(row.pk_id, row.name))

    with open("results/popular_courses", "w") as writer:
        writer.write("\n-----------Popular courses-----------")
        result = query_popular_course(session)
        for row in result:
            writer.write("\n{} - {} - {}".format(row[0], row[1], row[2]))

    with open("results/students_with_most_courses", "w") as writer:
        writer.write("\n-----------Popular students-----------")
        result = query_popular_student(session)
        for row in result:
            writer.write("\n{} - {} - {}".format(row[0], row[1], row[2]))


def join_dept_student(session):
    """
    Joins the department table and student table with dept_id

    :param session: session object
    :type session: :class:`sqlalchemy.orm.session.Session`

    :return: result
    :rtype: iterable
    """
    join_query = session.query(Student.pk_id, Student.name, Department.name) \
        .join(Department, Department.pk_id == Student.dept_id)

    LOGGER.debug("Join Operation Successful")
    return join_query


def join_dept_staff(session):
    """
    Joins the department table and staff table with dept_id

    :param session: session object
    :type session: :class:`sqlalchemy.orm.session.Session`

    :return: result
    :rtype: iterable
    """
    join_query = session.query(Staff.pk_id, Staff.name, Department.name) \
        .join(Department, Department.pk_id == Staff.dept_id)

    LOGGER.debug("Join Operation Successful")
    return join_query


def join_student_book(session):
    """
    Returns the students who took books from other departments

    :param session: session object
    :type session: :class:`sqlalchemy.orm.session.Session`

    :return: result
    :rtype: iterable
    """
    join_query = session.query(Student.pk_id, Student.name, Department.name, Book.name) \
        .join(Department, Department.pk_id == Student.dept_id) \
        .join(StudentActivity, StudentActivity.student_id == Student.pk_id) \
        .join(Book, Book.pk_id == StudentActivity.book_id) \
        .join(Course, Course.pk_id == Book.course_id) \
        .where(Student.dept_id != Course.dept_id)

    LOGGER.debug("Join Operation Successful")
    return join_query


def perform_join_operations(session):
    """
    Performs the join operations using Query API

    :param session: session object
    :type session: :class:`sqlalchemy.orm.session.Session`

    :return: None
    :rtype: None
    """
    with open("results/student_dept_names", "w") as writer:
        join_result_1 = join_dept_student(session)
        writer.write("\n-----------Student and Department-----------")
        for student_id, student_name, department_name in join_result_1:
            writer.write("\n{} - {} - {}".format(student_id, student_name, department_name))

    with open("results/staff_dept_names", "w") as writer:
        join_result_2 = join_dept_staff(session)
        writer.write("\n-----------Staff and Department-----------")
        for staff_id, staff_name, department_name in join_result_2:
            writer.write("\n{} - {} - {}".format(staff_id, staff_name, department_name))

    with open("results/students_other-dept_books", "w") as writer:
        join_result_3 = join_student_book(session)
        writer.write("\n-----------Students who borrowed books from other departments-----------")
        for student_id, student_name, department_name, book_name in join_result_3:
            writer.write("\n{} - {} - {} - {}".format(student_id, student_name, department_name, book_name))
