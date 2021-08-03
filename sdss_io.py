"""
Functions for reading and writing data for eyeball.py
"""
import os.path
import glob
import sys
import numpy as np
import config as cfg
from classes import DataTuple
from date_time import date_string, time_string

folder_out = os.path.dirname(os.path.realpath(__file__))
backup_folder = os.path.join(folder_out, "backups")
BACKUP_STR = "{}_{}".format(os.path.splitext(cfg.FOUT)[0], "backup_{}_{}.csv")


def save_data(data, backup=False):
    if backup:
        backup_fout = BACKUP_STR.format(date_string(), time_string())
        destination = os.path.join(backup_folder, backup_fout)
    else:
        destination = os.path.join(folder_out, cfg.FOUT)

    if cfg.SORT_BY_CLASSIFICATION:
        data = data.sort_by("idx")

    fmt_str = ",".join(len(data)*["{}"])
    with open(destination, "w") as F:
        for row in zip(*data):
            F.write(f"{fmt_str.format(*row)}\n")


def load_data():
    if os.path.exists(cfg.FOUT):
        dtypes = "i4,U128,U16,U16,U32,U16"
        columns = np.loadtxt(cfg.FOUT, dtype=dtypes, unpack=True, delimiter=',')
        data = DataTuple(*columns)
    else:
        fnames = get_file_list()
        data = gen_blank_data(fnames)
    return data


def get_file_list():
    fname_iter = sorted(glob.iglob(os.path.join(cfg.FOLDER_IN, "SDSSJ*.gif")))
    fnames = np.fromiter(map(os.path.basename, fname_iter), dtype='U128')
    if len(fnames) == 0:
        print("could not find any SDSS gif files in the folder:")
        print(cfg.FOLDER_IN)
        sys.exit()
    return fnames


def gen_blank_data(fnames):
    cls1 = np.zeros_like(fnames, dtype="U16")
    cls2 = np.zeros_like(fnames, dtype="U16")
    user = np.zeros_like(fnames, dtype="U32")
    date = np.zeros_like(fnames, dtype="U16")

    idx = np.arange(len(fnames))
    data = DataTuple(idx, fnames, cls1, cls2, user, date)
    return data
