# -*- coding: utf-8 -*-
"""
Module for Populating ORM Classes
"""
from solution.populate_tables.academic_schema.course import populate_courses
from solution.populate_tables.academic_schema.department import populate_departments
from solution.populate_tables.academic_schema.enrollment import populate_enrollments
from solution.populate_tables.academic_schema.staff import populate_staffs
from solution.populate_tables.academic_schema.student import populate_students

from solution.populate_tables.library_schema.author import populate_authors
from solution.populate_tables.library_schema.book import populate_books
from solution.populate_tables.library_schema.librarian import populate_librarians
from solution.populate_tables.library_schema.staff_activity import lend_book_staff
from solution.populate_tables.library_schema.student_activity import lend_book_student

