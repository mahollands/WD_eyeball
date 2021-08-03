"""
Contains functions for drawing the left hand panel of the eyeball.py window.
"""
import pygame
import config as cfg
import colours as clr

# basic setup
pygame.font.init()
titlefont = pygame.font.SysFont("arial", 30)
cmdfont = pygame.font.SysFont("monospace", 24, bold=True)
genfont = pygame.font.SysFont("monospace", 17, bold=True)
errfont = pygame.font.SysFont("arial", 60, bold=True)

panel_size = panel_w, panel_h = 1500-1131-1, 800  # -1 for black line


def help_top_level(iname, N):
    side_panel = basic_panel(iname, N)
    # key commands
    strings = [
        f"'{cfg.k_wd     }' --> WD      ",
        f"'{cfg.k_wdms   }' --> WD+MS   ",
        f"'{cfg.k_cv     }' --> CV      ",
        f"'{cfg.k_star   }' --> STAR    ",
        f"'{cfg.k_nlhs   }' --> NLHS    ",
        f"'{cfg.k_qso    }' --> QSO     ",
        f"'{cfg.k_galaxy }' --> GALAXY  ",
        f"'{cfg.k_unknown}' --> UNKNOWN ",
        f"'{cfg.k_junk   }' --> JUNK    ",
        f"'{cfg.k_poor   }' --> POOR    ",
        "';' --> CANDIDATE",
    ]
    side_panel = blit_sub_cat(side_panel, "Top level:", strings)
    side_panel = blit_generic(side_panel)
    return side_panel


def help_wd(iname, N):
    side_panel = basic_panel(iname, N)
    # key commands
    strings = [
        "'RETURN' --> NONE     ",
        "'BSPACE' --> UNDO     ",
        f"'{cfg.k_da    }'      --> DA       ",
        f"'{cfg.k_db    }'      --> DB       ",
        f"'{cfg.k_dc    }'      --> DC       ",
        f"'{cfg.k_daz   }'      --> DAZ      ",
        f"'{cfg.k_dbz   }'      --> DBZ      ",
        f"'{cfg.k_dz    }'      --> DZ       ",
        f"'{cfg.k_dq    }'      --> DQ       ",
        f"'{cfg.k_do    }'      --> DO       ",
        f"'{cfg.k_dah   }'      --> DAH      ",
        f"'{cfg.k_dao   }'      --> DAO      ",
        f"'{cfg.k_dab   }'      --> DAB/DBA  ",
        f"'{cfg.k_hdq   }'      --> HDQ      ",
        f"'{cfg.k_mag   }'      --> MAG      ",
        f"'{cfg.k_wd_pec}'      --> PECULIAR ",
        f"'{cfg.k_pn    }'      --> PN       ",
        "';'      --> CANDIDATE",
    ]
    side_panel = blit_sub_cat(side_panel, "WD:", strings)
    return side_panel


def help_nlhs(iname, N):
    side_panel = basic_panel(iname, N)
    # key commands
    strings = [
        "'RETURN' --> NONE     ",
        "'BSPACE' --> UNDO     ",
        f"'{cfg.k_sdb }'      --> SDB      ",
        f"'{cfg.k_sdo }'      --> SDO      ",
        f"'{cfg.k_sdbo}'      --> SDBO     ",
        "';'      --> CANDIDATE",
    ]
    side_panel = blit_sub_cat(side_panel, "NLHS:", strings)
    return side_panel


def help_wdms(iname, N):
    side_panel = basic_panel(iname, N)
    # key commands
    strings = [
        "'RETURN' --> NONE     ",
        "'BSPACE' --> UNDO     ",
        f"'{cfg.k_dadm}'      --> DAdM     ",
        f"'{cfg.k_dbdm}'      --> DBdM     ",
        f"'{cfg.k_dcdm}'      --> DCdM     ",
        f"'{cfg.k_wddk}'      --> WDdK     ",
        f"'{cfg.k_wddm}'      --> WDdM     ",
        "';'      --> CANDIDATE",
    ]
    side_panel = blit_sub_cat(side_panel, "WDMS:", strings)
    return side_panel


def help_star(iname, N):
    side_panel = basic_panel(iname, N)
    # key commands
    strings = [
        "'RETURN' --> NONE     ",
        "'BSPACE' --> UNDO     ",
        f"'{cfg.k_carbon}'      --> CARBON   ",
        f"'{cfg.k_ms_k  }'      --> MS_K     ",
        f"'{cfg.k_ms_m  }'      --> MS_M     ",
        "';'      --> CANDIDATE"]
    side_panel = blit_sub_cat(side_panel, "STAR:", strings)
    return side_panel


def help_unknown(iname, N):
    side_panel = basic_panel(iname, N)
    # key commands
    strings = [
        "'RETURN' --> NONE     ",
        "'BSPACE' --> UNDO     ",
        f"'{cfg.k_un_pec}'      --> PECULIAR ",
        "';'      --> CANDIDATE",
    ]
    side_panel = blit_sub_cat(side_panel, "UNKNOWN:", strings)
    return side_panel


def basic_panel(iname, N):
    side_panel = pygame.Surface(panel_size)
    side_panel.fill(clr.LGREY)

    # add title
    string = "Spectral classifier"
    title = titlefont.render(string, 1, clr.BLACK)
    text_size = titlefont.size(string)
    side_panel.blit(title, ((panel_size[0]-text_size[0])/2, 50))
    if cfg.PROGRESS_BAR:
        side_panel.blit(progress_bar(iname, N), (30, 760))
    return side_panel


def blit_sub_cat(side_panel, sub_cat, strings):
    category = titlefont.render(sub_cat, 1, clr.BLACK)
    side_panel.blit(category, (30, 130))
    for i, string in enumerate(strings):
        command = cmdfont.render(string, 1, clr.BLACK)
        side_panel.blit(command, (30, 170+30*i))
    return side_panel


def blit_generic(side_panel):
    # general commands
    string = "Generic:"
    # key commands
    strings = [
        "'SPACE'  --> NEXT             ",
        "'BSPACE' --> PREV             ",
        "'TAB'    --> NEXT UNCLASSIFIED",
        "'ESC'    --> QUIT             ",
        "'i'      --> INFO             ",
        "'r'      --> RM CLASS         ",
    ]
    category = titlefont.render(string, 1, clr.BLACK)
    side_panel.blit(category, (30, 520))
    for i, string in enumerate(strings):
        command = genfont.render(string, 1, clr.BLACK)
        side_panel.blit(command, (30, 560+30*i))
    return side_panel


def progress_bar(iname, N):
    PW, PH = 308, 20

    prog_bar = pygame.Surface((PW, PH))
    prog_bar.fill(clr.WHITE)

    bar_size = (PW-2)*(iname+1)//N, PH
    progress = pygame.Surface(bar_size)
    progress.fill(clr.DBLUE)
    prog_bar.blit(progress, (1, 0))

    pygame.draw.rect(prog_bar, clr.BLACK, (0, 0, PW, PH), 1)
    return prog_bar


cls2_help_functions = {
    "WD"      : help_wd,
    "NLHS"    : help_nlhs,
    "WDMS"    : help_wdms,
    "STAR"    : help_star,
    "UNKNOWN" : help_unknown
}
