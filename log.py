# -*- coding: utf-8 -*-
# @Author: JinHua
# @Date:   2019-11-08 10:47:36
# @Last Modified by:   JinHua
# @Last Modified time: 2019-11-08 10:48:28

import sys
import logging


def get_logger(name, level=logging.INFO, stream=None, filePath=None, fmtStr=None, dateStr=None):
    if fmtStr is None:
        fmtStr = "<%(asctime)s> [%(name)s] [%(levelname)s] %(message)s"
    if dateStr is None:
        dateStr = '%Y-%m-%d %H:%M:%S'

    log = logging.getLogger(name)
    log.setLevel(level)

    logFmt = logging.Formatter(fmtStr, datefmt=dateStr)

    if stream is None:
        stream = sys.__stdout__

    handler1 = logging.StreamHandler(stream)
    handler1.setFormatter(logFmt)
    log.addHandler(handler1)

    if filePath:
        handler2 = logging.FileHandler(filePath, 'wt')
        handler2.setFormatter(logFmt)
        log.addHandler(handler2)

    return log