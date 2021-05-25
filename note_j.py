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
# 2021/05: Streamlit

st.title("Note J Supplement: Visualizing Complex Numbers")
st.header("1.3 Complex Plane Visualization ")
st.write("""
 As shown in graphic below, a complex number $z = a + bj$ has an intercept at $a$ along the 
real axis and $b$ along the imaginary axis 
""")

st.write("""
 Play around with the graphic to get a better feel of complex numbers!
You can adjust the complex number plotted here with the real and
imaginary axis on the sidebar on the left
""")


# Define initial parameters
init_real = 5
init_im = 5

# Create the figure and the line that we will manipulate
z = 5+5j
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
print(z)
fi_a = np.angle(z)
x = z.real -abs(w)/20*np.cos(fi_a)
y = z.imag-abs(w)/20*np.sin(fi_a)
plt.arrow(0, 0, x, y, head_width=w/30, head_length=w/30, fc='b', ec='b')
st.pyplot(plt)


# real_min, real_max = 0, 10
# imaginary_min, imaginary_max = 0, 10
# real = st.sidebar.slider('Real Axis', real_min, real_max)
# imaginary = st.sidebar.slider('Imaginary Axis', imaginary_min, imaginary_max)



