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


def plot_complex_vector(): 

    # Create the figure and the line that we will manipulate
    z = 5+5j
    w = 20 # Maximum value
    fig, axis = plt.subplots()
    plt.axis("on")
    plt.grid()
    plt.text(-0.15*w, 0.8*w, "Im", fontsize=14)
    plt.text(0.8*w,-0.15*w, "Re", fontsize=14)


    # The real and imaginary axis
    plt.xlim(-w,w)
    plt.ylim(-w,w)
    plt.arrow(0, -w, 0, 1.9*w, head_width=w/20, head_length=w/20, fc='k', ec='k')
    plt.arrow(-w, 0, 1.9*w, 0, head_width=w/20, head_length=w/20, fc='k', ec='k')

    # plot the vector
    fi_a= np.angle(z)
    x=z.real - abs(w)/20*np.cos(fi_a)
    y=z.imag - abs(w)/20*np.sin(fi_a)

    real_slider = st.sidebar.slider(  
        label='Real Axis',
        min_value=-10,
        max_value=10,
        value = 5
    )

    imaginary_slider = st.sidebar.slider(
        label="Imaginary axis",
        min_value=-10,
        max_value=10,
        value = 5
    )

    axis.clear()
    plt.axis("on")
    plt.grid()
    plt.text(-0.15*w, 0.8*w, "Im", fontsize=14)
    plt.text(0.8*w,-0.15*w, "Re", fontsize=14)

    # The real and imaginary axis
    plt.xlim(-w,w)
    plt.ylim(-w,w)
    plt.arrow(0, -w, 0, 1.9*w, head_width=w/20, head_length=w/20, fc='k', ec='k')
    plt.arrow(-w, 0, 1.9*w, 0, head_width=w/20, head_length=w/20, fc='k', ec='k')

    # plot the vector
    z = real_slider + imaginary_slider * 1j 
    fi_a = np.angle(z)
    x = z.real -abs(w)/20*np.cos(fi_a)
    y = z.imag-abs(w)/20*np.sin(fi_a)
    plt.arrow(0, 0, x, y, head_width=w/30, head_length=w/30, fc='b', ec='b', label='My label')

    return fig, real_slider, imaginary_slider


def plot_polar_vector(real_slider, imag_slider): 
    # Create the figure and the line that we will manipulate
    z = 5+5j
    w = 20 # Maximum value
    fig, axis = plt.subplots()
    plt.axis("on")
    plt.grid()
    plt.text(-0.15*w, 0.8*w, "Im", fontsize=14)
    plt.text(0.8*w,-0.15*w, "Re", fontsize=14)


    # The real and imaginary axis
    plt.xlim(-w,w)
    plt.ylim(-w,w)
    plt.arrow(0, -w, 0, 1.9*w, head_width=w/20, head_length=w/20, fc='k', ec='k')
    plt.arrow(-w, 0, 1.9*w, 0, head_width=w/20, head_length=w/20, fc='k', ec='k')

    # plot the vector
    fi_a= np.angle(z)
    x=z.real - abs(w)/20*np.cos(fi_a)
    y=z.imag - abs(w)/20*np.sin(fi_a)

    axis.clear()
    plt.axis("on") 
    plt.text(-0.15*w, 0.8*w, "Im", fontsize=14)
    plt.text(0.8*w,-0.15*w, "Re", fontsize=14)

    # The real and imaginary axis
    plt.xlim(-w,w)
    plt.ylim(-w,w)
    plt.arrow(0, -w, 0, 1.9*w, head_width=w/20, head_length=w/20, fc='k', ec='k')
    plt.arrow(-w, 0, 1.9*w, 0, head_width=w/20, head_length=w/20, fc='k', ec='k')

    # plot the vector
    z = real_slider + imag_slider * 1j 
    fi_a = np.angle(z)
    magnitude = np.around(np.abs(z), decimals=2)
    x = z.real -abs(w)/20*np.cos(fi_a)
    y = z.imag-abs(w)/20*np.sin(fi_a)
    plt.annotate("Magnitude = " + str(magnitude), (7,16))
    plt.annotate("Phase = " + str(np.around(fi_a, decimals=2)) + " radians", (7,14))

    # Uncomment if you want it in degrees
    # plt.annotate("Degrees = " + str(np.around(np.degrees(fi_a), decimals=2)), (7,12))

    plt.arrow(0, 0, x, y, head_width=w/30, head_length=w/30, fc='b', ec='b', label='My label')
    return fig