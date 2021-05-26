import streamlit as st
import streamlit.components.v1 as components
import numpy as np
from math import log10
import numpy as np
import matplotlib.pyplot as plt

# Purpose: The purpose of this utils file is to not clutter the main note.py file and have all the plotting 
# things here all in 1 place

## CHANGELOG ##
# 2021/05: Finished utils.py for Note J (Gavin)


def plot_complex_vector(): 

    # Create the figure and the line that we will manipulate
    z = 5+5j
    w = 20 # Maximum value
    fig, axis = plt.subplots()

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

    return fig


def plot_polar_vector(): 
    # Create the figure and the line that we will manipulate
    z = 5+5j
    w = 20 # Maximum value
    fig, axis = plt.subplots()


    # The real and imaginary axis
    plt.xlim(-w,w)
    plt.ylim(-w,w)
    plt.arrow(0, -w, 0, 1.9*w, head_width=w/20, head_length=w/20, fc='k', ec='k')
    plt.arrow(-w, 0, 1.9*w, 0, head_width=w/20, head_length=w/20, fc='k', ec='k')

    mag_slider = st.sidebar.slider(  
        label='Magnitude',
        min_value=0.0,
        max_value=10.0,
        value = 5.0
    )

    angle_slider = st.sidebar.slider(
        label="Angle (radians)",
        min_value = 0.0,
        max_value= 2*np.pi,
        value = 5.0
    )

    # plot the vector
    z = mag_slider * np.cos(angle_slider) + (mag_slider * np.sin(angle_slider)) * 1j 
    fi_a= np.angle(z)
    x_val = z.real - abs(w)/20*np.cos(fi_a)
    y_val = z.imag - abs(w)/20*np.sin(fi_a)
    txt = "z = {x}+ {y}i".format(x = np.around(x_val, decimals=2), y = np.around(y_val, decimals=2))
    plt.annotate(txt, (5,16), size=12)
    plt.arrow(0, 0, x_val, y_val, head_width=w/30, head_length=w/30, fc='b', ec='b', label='My label')
    return fig


def pol2cart(rho, phi):
    x = rho * np.cos(phi)
    y = rho * np.sin(phi)
    return(x, y)