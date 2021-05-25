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

# Cartersian Form Visualization
st.header("1.3 Complex Plane Visualization ")
st.write("""
 As shown in graphic below, a complex number $z = a + bj$ has an intercept at $a$ along the 
real axis and $b$ along the imaginary axis. 
""")

st.write("""
Play around with the graphic below to get a better feel of complex numbers in Cartesian Form!
You can adjust the complex number plotted here with the real and
imaginary axis on the sidebar. 
""")

complex_vector_fig, real_slider, imag_slider = plot_complex_vector()
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
You can adjust the same sidebar on the left to see how changing the real and imaginary axis of the complex number
$z$ affects the phase and magnitude 
""")

polar_vector_fig = plot_polar_vector(real_slider, imag_slider)
st.pyplot(polar_vector_fig)




# real_min, real_max = 0, 10
# imaginary_min, imaginary_max = 0, 10
# real = st.sidebar.slider('Real Axis', real_min, real_max)
# imaginary = st.sidebar.slider('Imaginary Axis', imaginary_min, imaginary_max)



