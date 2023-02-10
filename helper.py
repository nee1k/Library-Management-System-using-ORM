# -*- coding: utf-8 -*-
"""
Helper file for logger and command line arguments
"""
from argparse import ArgumentParser
from json import load
import logging
import logging.config

__author__ = "neelesh.karthi@gmail.com"

LOGGER = logging.getLogger(name=__name__)


def initialize_logger():
    """
    Method to initialize and configure the logger

    :return: None
    :rtype: None
    """
    # Calling logging.json file
    log_file = "logging.json"
    with open(log_file, mode="r") as log_config_file:
        log_config_dict = load(fp=log_config_file)

    # Configuring logger
    logging.config.dictConfig(log_config_dict)

    LOGGER.info("LOGGER configuration Successful")


def initialize_command_args_amt():
    """
    Method to initializes the command line arguments

    :return: fine_amt
    :rtype: float
    """
    # Initializing parser
    parser = ArgumentParser()

    # Adding arguments

    parser.add_argument("-fine",
                        "--fine_amount",
                        type=float,
                        help="Fine amount. Example: 5.50",
                        required=True)

    args = parser.parse_args()
    fine_amt = args.fine_amount

    return fine_amt
