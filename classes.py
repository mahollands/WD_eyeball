"""
Contains classes for use by the eyeball.py program
"""
from collections import namedtuple
from dataclasses import dataclass
import numpy as np
import pygame

DataTuple_ = namedtuple("DataTuple_", "idx fnames cls1 cls2 user date")


class DataTuple(DataTuple_):
    """
    Named Tuple with extra features.
    Has columns: idx fnames cls1 cls2 user date
    """
    def sort_by(self, column_name):
        """
        sort all data wrt a column name
        """
        column = getattr(self, column_name)
        idx_sorted = np.argsort(column, kind='mergesort')
        return DataTuple(*(x[idx_sorted] for x in self))

    @property
    def N(self):
        return len(self.fnames)


@dataclass
class DisplayData:
    screen: pygame.Surface
    size: tuple
    font: pygame.font.Font

    @property
    def width(self):
        w, h = self.size
        return w

    @property
    def height(self):
        w, h = self.size
        return h
