# -*- coding: utf-8 -*-
"""
Essential libraries
----------------------

Code for creating ORM Class
"""
import logging

from sqlalchemy import Column, text, BOOLEAN
from sqlalchemy.dialects.mysql import VARCHAR, TIMESTAMP, INTEGER
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import expression
from sqlalchemy.sql.functions import now

__author__ = "neelesh.karthi@gmail.com"

LOGGER = logging.getLogger(name=__name__)

Base = declarative_base()


def create_tables(engine):
    """
    Creates tables in the schema

    :param engine: engine
    :type engine: :class:`sqlalchemy.engine`

    :return: None
    :rtype: None
    """
    Base.metadata.create_all(engine)
    LOGGER.debug("Created Tables")


class AuditAttributesMixin:
    """
    Audit Attributes Mixin

    :ivar pk_id: pk_id
    :vartype pk_id: int

    :ivar created_by: user name of creator
    :vartype created_by: str

    :ivar created_on: timestamp while creating
    :vartype created_on: :class: `datetime.datetime`

    :ivar last_updated_by: user name of updater
    :vartype last_updated_by: str

    :ivar last_updated_on: timestamp while updating
    :vartype last_updated_on: :class: `datetime.datetime`

    :ivar is_active: active status
    :vartype is_active: bool
    """

    pk_id = Column(INTEGER, primary_key=True, autoincrement=True)

    # audit attributes
    created_by = Column(VARCHAR(255), nullable=False, default="SYSTEM", server_default="SYSTEM")
    created_on = Column(TIMESTAMP, nullable=False, server_default=now())
    last_updated_by = Column(VARCHAR(255), nullable=False, default="SYSTEM", server_default="SYSTEM")
    last_updated_on = Column(TIMESTAMP, nullable=True,
                             server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    is_active = Column(BOOLEAN, nullable=False, default=True, server_default=expression.true())
