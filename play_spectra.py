#!/usr/bin/env python2
#
# Demonstration script for "playing" a 1D spectrum using a midi output

import pyspeckit
import pygame.midi
import time
import argparse


parser = argparse.ArgumentParser(description='Play a 1D spectrum through a \
                                              midi output.')
parser.add_argument('-m', '--midi', type=int, default=0,
                    help='MIDI port to use.')
parser.add_argument('-l', '--loop', default=False, action='store_true',
                    help='Infinitely loop the spectrum?')
parser.add_argument('spec', type=str, default=False,
                    help='Spectrum to play.')
args=parser.parse_args()

print args.spec

sp = pyspeckit.Spectrum(args.spec)
pygame.midi.init()
midi_out = pygame.midi.Output(args.midi, 0)
while True:
    for a in sp.flux:
        if a > 0:
            midi_out.note_on(int(((a - min(sp.flux))/max(sp.flux)*30)+0), 1)
            time.sleep(0.15)
            midi_out.note_off(int(((a - min(sp.flux))/max(sp.flux)*30)+0))
    if not(args.loop):
        break
    time.sleep(0.5)
