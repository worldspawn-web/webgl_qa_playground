# -*- encoding=utf8 -*-
__author__ = "worldspawn"

from airtest.core.api import *
import logging

# # Logger Setup
# logger = logging.getLogger("airtest")
# # logger.setLevel(logging.ERROR)

auto_setup(__file__)

def random_touch():
    touch((0.5, 0.5))

__all__ = ['random_touch']


