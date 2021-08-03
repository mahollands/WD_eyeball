"""
Contains functions and dictionaries defining relationships
between keybindings and classifications.
"""
from collections import defaultdict
import config as cfg

top_level_classes = {
    cfg.k_wd      : "WD",
    cfg.k_cv      : "CV",
    cfg.k_wdms    : "WDMS",
    cfg.k_nlhs    : "NLHS",
    cfg.k_qso     : "QSO",
    cfg.k_star    : "STAR",
    cfg.k_galaxy  : "GALAXY",
    cfg.k_junk    : "JUNK",
    cfg.k_poor    : "POOR",
    cfg.k_unknown : "UNKNOWN",
}

WD_classes = defaultdict(lambda : None, {
    cfg.k_da     : "DA",
    cfg.k_db     : "DB",
    cfg.k_dc     : "DC",
    cfg.k_daz    : "DAZ",
    cfg.k_dbz    : "DBZ",
    cfg.k_dz     : "DZ",
    cfg.k_dq     : "DQ",
    cfg.k_do     : "DO",
    cfg.k_dah    : "DAH",
    cfg.k_dao    : "DAO",
    cfg.k_dab    : "DBA",
    cfg.k_hdq    : "HDQ",
    cfg.k_mag    : "MAG",
    cfg.k_wd_pec : "PEC",
    cfg.k_pn     : "PN",
})

NLHS_classes = defaultdict(lambda : None, {
    cfg.k_sdb : "SDB",
    cfg.k_sdo : "SDO",
    cfg.k_sdbo: "SDBO",
})

WDMS_classes = defaultdict(lambda : None, {
    cfg.k_dadm: "DAdM",
    cfg.k_dbdm: "DBdM",
    cfg.k_dcdm: "DCdM",
    cfg.k_wddk: "WDdK",
    cfg.k_wddm: "WDdM",
})

STAR_classes = defaultdict(lambda : None, {
    cfg.k_carbon: "CARBON",
    cfg.k_ms_k  : "MS_K",
    cfg.k_ms_m  : "MS_M",
})

UNKNOWN_classes = defaultdict(lambda : None, {
    cfg.k_un_pec: "PEC",
})

cls1_with_cls2 = {
    'WD': WD_classes,
    'NLHS': NLHS_classes,
    'WDMS': WDMS_classes,
    'STAR': STAR_classes,
    'UNKNOWN': UNKNOWN_classes,
}

def get_bottom_level_class(cls1, key):
    if key == ':':
        return key
    if key in {"return", "bspace"}:
        return ''
    return cls1_with_cls2[cls1][key]
