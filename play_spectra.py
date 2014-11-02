#!/usr/bin/env python2
#
# Demonstration script for "playing" a 1D spectrum using a midi output

import pyspeckit
import pygame.midi
import time
import argparse


parser = argparse.ArgumentParser(description='Play a 1D spectrum through a \
                                              midi output.')
parser.add_argument('-m', '--midi', type=int, nargs=1, default=0,
                    help='MIDI port to use.')
parser.add_argument('spec', type=str, nargs=1, default=False,
                    help='Spectrum to play.')
args=parser.parse_args()

sp = pyspeckit.Spectrum(args.spec)
pygame.midi.init()
midi_out = pygame.midi.Output(args.m, 0)
for a in sp.flux:
    if a > 0:
        midi_out.note_on(int(((a - min(sp.flux))/max(sp.flux)*24)+50), 1)
        time.sleep(0.1)
        midi_out.note_off(int(((a - min(sp.flux))/max(sp.flux)*24)+50))
