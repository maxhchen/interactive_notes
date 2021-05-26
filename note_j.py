import streamlit as st
import streamlit.components.v1 as components
from math import log10
import numpy as np
from matplotlib.widgets import Slider, Button, RadioButtons
from note_j_utils import * 

## CHANGELOG ##
# 2021/05: Finished Note J supplement (Gavin)

st.title("Note J Supplement: Visualizing Complex Numbers")

# Cartersian Form Visualization
st.header("1. Complex Number Visualization (Cartesian Form)")
st.write("""
 As shown in graphic below, a complex number $z = a + bj$ has a value of $a$ along the 
real axis and a value of $b$ along the imaginary axis. 
""")

st.write("""
Play around with the graphic below to get a better feel of complex numbers in Cartesian Form!
You can adjust the complex number plotted here with the real and
imaginary axis on the sidebar. 
""")

complex_vector_fig = plot_complex_vector()
st.pyplot(complex_vector_fig)

# Polar form Visualization
st.header("2. Polar Form Visualization ")
st.write(""" A complex number $z = a + bj$ can also be written equivalently as:
""")
st.latex(r'''
    z = |z|e^{j\angle{z}}
''')
st.write(""" in polar form using the magnitude and the angle of $z$ to represent the complex number.
""")
st.write("""
You can adjust the magnitude and angle sidebar on the left to see how changing the real and imaginary axis of the complex number
$z$ affects the phase and magnitude of its polar representation
""")
polar_vector_fig = plot_polar_vector()
st.pyplot(polar_vector_fig)

for i in range(5):
    st.text("")


st.write("""
Created by Maxwell Chen and Gavin Liu
""")
