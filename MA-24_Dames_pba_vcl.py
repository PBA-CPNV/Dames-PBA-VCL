#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#--------1---------2---------3---------4---------5---------6---------7---------8
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
"""
Name    : MA-24_Dames_pba_vcl.py
Authors : Pascal Benzonana and Vitor COVAL
Date    : 2024.11.03
Version : 0.01
Purpose : Jeu de dames avec la librairie pygame

# ------------------------------------------------------------------------------
# Revisions
# ------------------------------------------------------------------------------

# 2024-11-03 01 PBA & VCL
  - Version initiale
"""

import pygame


def dessine_case(case_pos):
    """Dessine la xème case du damier
    """
    global screen, case_size, cases_blanches, cases_noires, marge_gauche, marge_haut
    if case_pos % 2:
        pygame.draw.rect(screen, cases_blanches,
        (marge_gauche + case_pos*case_size,
              marge_haut,
              case_size,
              case_size),
              0)
    else:
        pygame.draw.rect(screen, cases_noires,
        (marge_gauche + case_pos*case_size,
              marge_haut,
              case_size,
              case_size),
              0)


def bouge_droite():
    """Bouge le pion à droite.
    """
    global screen, case_size, pion, pion_pos, nb_colonnes, marge_gauche, marge_haut
    if pion_pos < nb_colonnes-1:
        dessine_case(pion_pos)
        pion_pos += 1
    screen.blit(pion, (marge_gauche + pion_pos*case_size, marge_haut))


def bouge_gauche():
    """Bouge le pion à gauche
    """
    global screen, case_size, pion, pion_pos, marge_gauche, marge_haut
    if pion_pos > 0 :
        dessine_case(pion_pos)
        pion_pos -= 1
    screen.blit(pion, (marge_gauche + pion_pos*case_size, marge_haut))


# ------------
# --- MAIN ---
# ------------

plateau = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]

# Version pygame
case_size = 80
cases_blanches = (255, 255, 255)
cases_noires = (180, 180, 180)
pions_blancs = (255, 255, 255)
pions_noirs = (0, 0, 0)

# Marges autour du damier
marge_gauche = 10
marge_droite = 10
marge_haut = 10
marge_bas = 10

pion_pos = 0

path_to_images = "pictures\\"
pygame.init()

# Window size x, y
nb_colonnes = len(plateau)
window_size = (case_size*nb_colonnes
               + marge_gauche
               + marge_droite,
               case_size
               + marge_haut
               + marge_bas
               )
window_color = (89, 152, 255)
screen = pygame.display.set_mode(window_size)
icon = pygame.image.load(path_to_images+"International_draughts.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("MA-24 : Jeu de Dames")
screen.fill(window_color)

# Affiche le damier
for case in range(nb_colonnes):
    dessine_case(case)

# Charge l'image du pion
pion = pygame.image.load(path_to_images+"MA-24_pion.png")
pion = pygame.transform.scale(pion, (case_size, case_size))
screen.blit(pion, (marge_gauche, marge_haut))
pygame.display.flip()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        btn_presse = pygame.key.get_pressed()
        if btn_presse[pygame.K_RIGHT]:
            bouge_droite()
        elif btn_presse[pygame.K_LEFT]:
            bouge_gauche()
        elif btn_presse[pygame.K_q]:
            running = False
        pygame.display.update()

pygame.quit()
