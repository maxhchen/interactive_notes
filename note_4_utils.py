import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import altair as alt
from math import log10
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
from note_j_utils import * 

## CHANGELOG ##
# 2021/05: Finished utils.py for Note J (Gavin)




def plot_lp_filter(t, axis, orig_sig_amp, orig_sig_phase, w, R, C):
    transfer_function = 1/(1+ (w*R*C*1j))
    tf_mag = np.abs(transfer_function)
    tf_phase = np.angle(transfer_function)

    new_amp = orig_sig_amp * tf_mag
    new_phase = orig_sig_phase + tf_phase
    axis.plot(t, signal(t, new_amp, new_phase, w), lw=3)
    axis.legend(['Original Signal', 'Filtered Signal'])
    



def plot_hp_filter(t, axis, orig_sig_amp, orig_sig_phase, w, R, C):
    transfer_function = (w*R*C*1j)/(1+ (w*R*C*1j))
    tf_mag = np.abs(transfer_function)
    tf_phase = np.angle(transfer_function)

    new_amp = orig_sig_amp * tf_mag
    new_phase = orig_sig_phase + tf_phase
    axis.plot(t, signal(t, new_amp, new_phase, w), lw=3)
    axis.legend(['Original Signal', 'Filtered Signal'])

def plot_bp_filter(t, axis, orig_sig_amp, orig_sig_phase, w, R, C):
    transfer_function = (1/(1+ (w*R*C*1j))) * ((w*R*C*1j)/(1+ (w*R*C*1j))) # LP * HP transfer function
    tf_mag = np.abs(transfer_function)
    tf_phase = np.angle(transfer_function)

    new_amp = orig_sig_amp * tf_mag
    new_phase = orig_sig_phase + tf_phase
    axis.plot(t, signal(t, new_amp, new_phase, w), lw=3)
    axis.legend(['Original Signal', 'Filtered Signal'])




# The parametrized function to be plotted
def signal(t, amplitude, phase, frequency):
    return amplitude * np.sin(2 * np.pi * frequency * t + phase)