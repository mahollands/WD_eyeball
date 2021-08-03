#!/usr/bin/env python
"""
eyeball.py                       Author:(Mark Hollands)

Allows navigation and classification of spectra. A cl arg can be given to start
part way through the list.
"""
import os.path
import sys
import pygame
import config as cfg
import sdss_io
import colours as clr
from date_time import date_string
from classification import top_level_classes, get_bottom_level_class, cls1_with_cls2
from info import help_top_level, cls2_help_functions
from keyboard import wait_on_key
from misc import starting_point, goto_next_unclassified
from classes import DisplayData


def setup_data():
    print(f"Starting as USER: {cfg.USER}")
    data = sdss_io.load_data()
    if cfg.SORT_BY_CLASSIFICATION:
        data = data.sort_by("cls2")
        data = data.sort_by("cls1")
    else:
        data = data.sort_by("fnames")
    return data


def setup_display():
    pygame.display.init()
    pygame.display.set_caption("eyeball")
    size = cfg.IM_W+cfg.PANEL_W, cfg.IM_H
    screen = pygame.display.set_mode(size)
    pygame.font.init()
    myfont = pygame.font.SysFont("arial", 40)
    return DisplayData(screen, size, myfont)


def draw_frame(display, data, ispec, ispec_prev, CLS2_MODE):
    # load a picture and blit it to the screen
    fname = data.fnames[ispec]
    if ispec != ispec_prev:
        fname_full = os.path.join(cfg.FOLDER_IN, fname)
        Picture = pygame.image.load(fname_full).convert()
        print(fname)
    ispec_prev = ispec
    display.screen.blit(Picture, (display.width-cfg.IM_W, 0))

    # indicate top level classification at top left
    if data.cls1[ispec] != '':
        label = display.font.render(data.cls1[ispec], 1, clr.RED)
        text_size = display.font.size(data.cls1[ispec])
        display.screen.blit(label, (display.width-350-text_size[0], 50))

    # indicate bottom level classification (inform in blue if awaiting input)
    if CLS2_MODE:
        label = display.font.render("awaiting input", 1, clr.BLUE)
        display.screen.blit(label, (display.width-300, 50))
    elif data.cls2[ispec] != '':
        label = display.font.render(data.cls2[ispec], 1, clr.RED)
        display.screen.blit(label, (display.width-300, 50))

    # help panel
    help_fn = cls2_help_functions[data.cls1[ispec]] if CLS2_MODE else help_top_level
    display.screen.blit(help_fn(ispec, data.N), (0, 0))

    # update display
    pygame.display.flip()


def process_key_lvl1(key, data, ispec):
    CLS2_MODE = False
    if key == 'space' and ispec < data.N-1:
        ispec += 1
    elif key == 'bspace' and ispec > 0:
        ispec -= 1
    elif key == 'tab':
        ispec = goto_next_unclassified(data, ispec)
    elif key == 'i':  # print progress
        percentage = 100*(ispec+1)/data.N
        print(f"{ispec+1}/{data.N} --> ({percentage:.1f} %%)")
    elif key == 'r':  # emove all classifcations
        data.cls1[ispec], data.cls2[ispec], data.user[ispec], data.date[ispec] = \
            ('', '', '', '')
    elif key == ':':
        if data.cls2[ispec].endswith(':'):
            data.cls2[ispec] = data.cls2[ispec].rstrip(":")
        else:
            data.cls2[ispec] += ':'
        sdss_io.save_data(data, backup=True)
    elif key in top_level_classes:
        data.cls1[ispec], data.cls2[ispec], data.user[ispec], data.date[ispec] = \
            top_level_classes[key], '', cfg.USER, date_string()
        sdss_io.save_data(data, backup=True)
        if data.cls1[ispec] in cls1_with_cls2:
            CLS2_MODE = True
        if key == cfg.k_qso and cfg.AUTOJUMP and ispec < data.N-1:
            ispec = goto_next_unclassified(data, ispec)
    return data, ispec, CLS2_MODE


def process_key_lvl2(key, data, ispec):
    CLS2_MODE=True
    bottom_class = get_bottom_level_class(data.cls1[ispec], key)
    if bottom_class is not None:
        data.cls2[ispec] = bottom_class
        if key == 'return' and cfg.AUTOJUMP and ispec < data.N-1:
            ispec = goto_next_unclassified(data, ispec)
        if key == 'bspace':
            data.cls1[ispec] = ""
        sdss_io.save_data(data, backup=True)
        CLS2_MODE = False
    return data, ispec, CLS2_MODE


def shutdown(data, ispec):
    print(f"reached spectrum {ispec+1}")
    sdss_io.save_data(data)
    pygame.quit()
    sys.exit()


# Setup for program
data = setup_data()
ispec, ispec_prev, CLS2_MODE = starting_point(data), -1, False
display = setup_display()

# main loop
while True:
    draw_frame(display, data, ispec, ispec_prev, CLS2_MODE)
    key = wait_on_key()
    if key == "esc":
        shutdown(data, ispec)
    process_key_fn = process_key_lvl2 if CLS2_MODE else process_key_lvl1
    data, ispec, CLS2_MODE = process_key_fn(key, data, ispec)
