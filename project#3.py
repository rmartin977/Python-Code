'''
Project #3 part 1.
Math 266 Linear Algebra
Enter your name here 
Summer 2020
'''

# import libraries

import simpleaudio as sa
import matplotlib.pyplot as pyplot
import numpy as np
from numpy import sin,pi
import os

os.system('clear')
print('\n\n\tProject #3 Audio')

sample_rate = 44100  
mid_c = 262 # frequency for middle C on the piano


def tone(freq=440, duration=2):

    ''' 
    This function generates a sine wave tone with frequency = freq
    and duration = duration. It will return a numpy array containing
    the audio sample values.
    
    Usage:

    audio = tone(262,3)

    will return "middle C note" duration 3 sec 

    '''

    dt = 1/sample_rate  # separation between samples

    # discretize the time domain for the signal
    t = np.arange(0,duration,dt)

    # need a trig review?  Go to
    # https://www.youtube.com/watch?v=OCfAEZphAzE
    note = np.sin(2*pi*freq*t)

    # normalize to 16-bit range
    note *=32767/np.max(np.abs(note))

    # convert to 16-bit data
    note = note.astype(np.int16)

    return note

def play_sound(audio):
    '''
    function will play the sound stored in array audio.

    '''

    play_obj = sa.play_buffer(audio,1,2,sample_rate=44100)
    while play_obj.is_playing():
        pass
    play_obj.wait_done
    return

# play middle c for 2 seconds 

audio = tone(262,2)

print('\n playing middle C')
play_sound(audio)

input("\n\n\t please press a key to continue:\n")



G_note = tone(392,1)
A_note = tone(440,1)
F_note = tone(349,1)
FF_note = tone(175,1)
C_note = tone(262,1)
audio = np.hstack((G_note,A_note,F_note,FF_note,C_note))
play_sound(audio)
print('\n\ndone......')



