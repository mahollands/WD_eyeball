"""
Miscallaneous functions for eyeball.py
"""
import sys
import numpy as np
import config as cfg


def starting_point(data):
    if cfg.SORT_BY_CLASSIFICATION:
        starting_cls = (data.cls1 == cfg.STARTING_CLS1) & (data.cls2 == cfg.STARTING_CLS2)
        if not starting_cls.any():
            print("nothing classified as {STARTING_TOP_CLS} {STARTING_BOTTOM_CLS}")
            sys.exit()
        return np.argmax(starting_cls)
    elif len(sys.argv) == 1:
        unclassified = (data.cls1 == '')
        if cfg.GOTO_FIRST_UNCLASSIFIED and unclassified.any():
            ispec = np.argmax(unclassified)
            print(f"Skipped to first unclassified spectrum ({ispec+1}/{data.N})")
            return ispec
        else:
            print("No unclassified spectra. Starting at the beginning")
            return 0
    else:
        try:
            ispec = int(sys.argv[1]) - 1
            if not 0 <= ispec < data.N:
                print(f"Specified starting index outside of valid range (1-{data.N})")
                sys.exit(1)
            print(f"Skipped to specified spectrum ({ispec+1}/{data.N})")
            return ispec
        except ValueError:
            print("Argument must be an integer.")
            sys.exit(1)


def goto_next_unclassified(data, ispec):
    if ispec == data.N-1:
        return ispec
    unclassified = data.cls1[ispec+1:] == ''
    if unclassified.any():
        return ispec+1 + np.argmax(unclassified)
    return ispec
