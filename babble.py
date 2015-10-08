#!/usr/bin/env python

'''
babble - a numbers station in less than 100 lines

Copyright 2015 zachwick <zach@zachwick.com>

babble is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

babble is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with babble.  If not, see <http://www.gnu.org/licenses/>.

'''

import random
import pygame
import time

ONE_UNIT       = 0.5
THREE_UNITS    = 3 * ONE_UNIT
SEVEN_UNITS    = 7 * ONE_UNIT
FOURTEEN_UNITS = 14 * ONE_UNIT

MORSE = {'A': '.-',     'B': '-...',   'C': '-.-.', 
         'D': '-..',    'E': '.',      'F': '..-.',
         'G': '--.',    'H': '....',   'I': '..',
         'J': '.---',   'K': '-.-',    'L': '.-..',
         'M': '--',     'N': '-.',     'O': '---',
         'P': '.--.',   'Q': '--.-',   'R': '.-.',
     	 'S': '...',    'T': '-',      'U': '..-',
         'V': '...-',   'W': '.--',    'X': '-..-',
         'Y': '-.--',   'Z': '--..',
         
         '0': '-----',  '1': '.----',  '2': '..---',
         '3': '...--',  '4': '....-',  '5': '.....',
         '6': '-....',  '7': '--...',  '8': '---..',
         '9': '----.' 
}
SOUND_PATH = 'morse_sound_files/'

def main():
    # Get our word corpus read into a Python list
    word_file = open('/usr/share/dict/words','r')
    words = word_file.readlines()
    word_count = len(words)

    # Construct a 'sentence' of five random words from our corpus
    sentence = ""
    for x in range(0, 6):
        sentence += words[random.randint(0,word_count)].replace("\n"," ")
    print(sentence)

    # Print out the morse code encoded message for informational purposes
    morse_sentence = ""
    for char in sentence:
        if char == " ":
            morse_sentence += " " * 7
        elif char == "'":
            morse_sentence += ""
        else:
            morse_sentence += MORSE[char.upper()] + " "
    print(morse_sentence+"\n\n")
    
    # Play the audio of dots and dashes that make up our sentence
    play(sentence)

    # Wait fourteen time units, then generate new random message and play it
    time.sleep(FOURTEEN_UNITS)
    
def play(msg):
    pygame.init()
    for char in msg:
        if char == " ":
            time.sleep(SEVEN_UNITS)
        else:
            if char != "'":
                pygame.mixer.music.load(SOUND_PATH + char.upper() + '_morse_code.ogg')
                pygame.mixer.music.play()
                time.sleep(THREE_UNITS)
    
if __name__ == "__main__":
    while True:
        main()
