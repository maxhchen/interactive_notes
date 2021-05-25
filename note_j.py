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
$\mathbf{real}$ $\mathbf{axis}$ and $b$ along the $\mathbf{imaginary}$ $\mathbf{axis}$. 
""")

fig = complex_plane2([20+10j,15,-10-10j,5+15j], 1)
st.pyplot(fig)
st.markdown("<h4 style='text-align: center;'>Play around with the graphic to get a better feel of complex numbers! \
You can adjust the complex number plotted here with the real and \
imaginary axis on the sidebar on the left </h1>", unsafe_allow_html=True)

# real_min, real_max = 0, 10
# imaginary_min, imaginary_max = 0, 10
# real = st.sidebar.slider('Real Axis', real_min, real_max)
# imaginary = st.sidebar.slider('Imaginary Axis', imaginary_min, imaginary_max)



