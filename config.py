"""
User defined variables
"""

USER = "HomerSimpson"  # username 

# path to folder of .gif spectra
FOLDER_IN = "test_spectra/"
# output file name
FOUT = f"SDSS_spectra_{USER}.csv"

# go to next spectrum if top-class is QSO or bottom class is blank
AUTOJUMP = True

# If true, the program will start at the first unclassified spectrum
GOTO_FIRST_UNCLASSIFIED = True

# progress bar for demotivational purposes
PROGRESS_BAR = True

# If True, sorts by class --- useful for checking at the end.
SORT_BY_CLASSIFICATION = False
STARTING_CLS1 = "QSO"
STARTING_CLS2 = ""       # This MUST be "" if you want to start at something without a subclassifcation.

#####################
# KEYBOARD BINDINGS #
#####################

# These can be reassigned to any letter of the alphabet (lowercase)

# TOP LEVEL
k_wd      = 'w'
k_wdms    = 'm'
k_cv      = 'c'
k_star    = 's'
k_nlhs    = 'n'
k_qso     = 'q'
k_galaxy  = 'g'
k_unknown = 'u'
k_junk    = 'j'
k_poor    = 'p'

# WD
k_da     = 'a'
k_db     = 'b'
k_dc     = 'c'
k_daz    = 'j'
k_dbz    = 'k'
k_dz     = 'z'
k_dq     = 'q'
k_do     = 'o'
k_dah    = 'h'
k_dao    = 'g'
k_dab    = 'f'
k_hdq    = 't'
k_mag    = 'm'
k_wd_pec = 'p'
k_pn     = 'x'

# WD+MS
k_dadm = 'a'
k_dbdm = 'b'
k_dcdm = 'c'
k_wddk = 'k'
k_wddm = 'm'

# STAR
k_carbon = 'c'
k_ms_k   = 'k'
k_ms_m   = 'm'

# NLHS
k_sdb  = 'b'
k_sdo  = 'o'
k_sdbo = 'p'

# UNKNOWN
k_un_pec = 'p'
