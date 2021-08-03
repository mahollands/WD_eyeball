"""
Contains mapping between keyboard codes and corresponding strings as well
functions relating to the keyboard
"""
import pygame

key_map = {
    pygame.K_SPACE: 'space',
    pygame.K_BACKSPACE: 'bspace',
    pygame.K_ESCAPE: 'esc',
    pygame.K_RETURN: 'return',
    pygame.K_SEMICOLON: ':',
    pygame.K_TAB: 'tab',
    pygame.K_a: 'a',
    pygame.K_b: 'b',
    pygame.K_c: 'c',
    pygame.K_d: 'd',
    pygame.K_e: 'e',
    pygame.K_f: 'f',
    pygame.K_g: 'g',
    pygame.K_h: 'h',
    pygame.K_i: 'i',
    pygame.K_j: 'j',
    pygame.K_k: 'k',
    pygame.K_l: 'l',
    pygame.K_m: 'm',
    pygame.K_n: 'n',
    pygame.K_o: 'o',
    pygame.K_p: 'p',
    pygame.K_q: 'q',
    pygame.K_r: 'r',
    pygame.K_s: 's',
    pygame.K_t: 't',
    pygame.K_u: 'u',
    pygame.K_v: 'v',
    pygame.K_w: 'w',
    pygame.K_x: 'x',
    pygame.K_y: 'y',
    pygame.K_z: 'z',
}


def wait_on_key():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # quit if X clicked
                return "esc"
            if event.type == pygame.KEYDOWN:
                return key_map[event.key] if event.key in key_map else ''
        pygame.time.wait(10)
