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

# Define initial parameters
init_real = 5
init_im = 5

# Create the figure and the line that we will manipulate
z=5+5j
w=10
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

arrow = plt.arrow(0, 0, x, y, head_width=w/30, head_length=w/30, fc='b', ec='b')
axcolor = 'lightgoldenrodyellow'

# adjust the main plot to make room for the sliders
plt.subplots_adjust(left=0.25, bottom=0.25)

# Make a vertically oriented slider to control the imaginary value
# ax_im = plt.axes([0.1, 0.25, 0.0225, 0.63], facecolor=axcolor)
imaginary_slider = st.sidebar.slider(
    # ax=ax_im,
    label="Imaginary axis",
    min_value=-10,
    max_value=10,
    # valinit=init_im,
    # orientation="vertical"
)

# Make a horizontal slider to control the real value.
# ax_real = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
real_slider = st.sidebar.slider(  
    # ax=ax_real,
    label='Real Axis',
    min_value=-10,
    max_value=10,
    # valinit=init_real,
)

# The function to be called anytime a slider's value changes
# def update(val):
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
print(z)
fi_a = np.angle(z)
x = z.real -abs(w)/20*np.cos(fi_a)
y = z.imag-abs(w)/20*np.sin(fi_a)
plt.arrow(0, 0, x, y, head_width=w/30, head_length=w/30, fc='b', ec='b')
fig.canvas.draw_idle()

# register the update function with each slider
# real_slider.on_changed(update)
# imaginary_slider.on_changed(update)
# plt.show()
st.pyplot(plt)
