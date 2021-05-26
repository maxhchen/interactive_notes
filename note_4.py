import streamlit as st
import streamlit.components.v1 as components
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
from note_4_utils import * 

## CHANGELOG ##
# 2021/05: Streamlit
st.set_option('deprecation.showPyplotGlobalUse', False)

amp_slider = st.sidebar.slider(  
    label='Signal Amplitude',
    min_value=0.0,
    max_value=10.0,
    value = 5.0
)

phase_slider = st.sidebar.slider(
    label="Signal Phase (radians)",
    min_value = 0.0,
    max_value= 2*np.pi,
    value = 5.0
)

w_slider = st.sidebar.slider(
    label="Signal Frequency (w)",
    min_value = 0.0,
    max_value= 10.0,
    value = 5.0
)

r_lp_slider = st.sidebar.slider(  
        label='R_LP (ohms)',
        min_value=0.0,
        max_value=4.0,
        value = 1.0
    )

c_lp_slider = st.sidebar.slider(
    label="C_LP (farads)",
    min_value = 0.0,
    max_value= 4.0,
    value = 1.0
)

r_hp_slider = st.sidebar.slider(  
        label='R_HP (ohms)',
        min_value=0.0,
        max_value=4.0,
        value = 1.0
    )

c_hp_slider = st.sidebar.slider(
    label="C_HP (farads)",
    min_value = 0.0,
    max_value= 4.0,
    value = 1.0
)

st.title("Note 4 Supplement: Visualizing Filters")

# LP Filter Visualization
st.header("1. Low Pass Filters")
st.write("""
    This visualization is intended to help understand low-pass filters better for any given sinusoidal input. 
    Recall that any sinusoidal input signal can be represented with the form: 
""")
st.latex(r'''
    V(t) = V_o cos(wt + \theta)
''')
st.write("""
    Play around with the graphic below to get a better feel of how the input signal is affected by the filter 
    by adjusting $w$, $R$, and $C$ values of the basic RC low pass filter. 
    You can adjust low-pass frequency, $R$, and $C$ values on the sidebar. 
    The input signal can also be adjusted on the left by changing its amplitude, phase, and frequency
""")

fig1, axis1 = plt.subplots()
t = np.linspace(0, 1, 1000)
axis1.plot(t, signal(t, amp_slider, phase_slider, w_slider), lw=2)
axis1.set_xlabel("Time (seconds)")
axis1.set_ylabel("Voltage (V) ")

lp_filter_fig = plot_lp_filter(t, axis1, amp_slider, phase_slider, w_slider, r_lp_slider, c_lp_slider)
st.pyplot(lp_filter_fig)



# HP Filter Visualization
st.header("2. High Pass Filters")
st.write("""
    Similar to the RC low-pass filter above, play around with the graphic below to get a better feel of how the input signal is 
    affected by the high-pass RC filter now.
""")

fig2, axis2 = plt.subplots()
t = np.linspace(0, 1, 1000)
axis2.plot(t, signal(t, amp_slider, phase_slider, w_slider), lw=2)
axis2.set_xlabel("Time (seconds)")
axis2.set_ylabel("Voltage (V) ")
hp_filter_fig = plot_hp_filter(t, axis2, amp_slider, phase_slider, w_slider, r_hp_slider, c_hp_slider)
st.pyplot(hp_filter_fig)

st.header("3. Band Pass Filters")
st.write("""
    Similar to the low-pass and high-pass filters above, play around with the graphic below to get a better feel of how the input signal is 
    affected by the bandpass filter now. Recall that a bandpass filter is just a low-pass filter cascaded with a high-pass filter.
""")
fig3, axis3 = plt.subplots()
t = np.linspace(0, 1, 1000)
axis3.plot(t, signal(t, amp_slider, phase_slider, w_slider), lw=2)
axis3.set_xlabel("Time (seconds)")
axis3.set_ylabel("Voltage (V) ")
bp_filter_fig = plot_bp_filter(t, axis3, amp_slider, phase_slider, w_slider, r_hp_slider, c_hp_slider)
st.pyplot(bp_filter_fig)


for i in range(5):
    st.text("")


st.write("""
Created by Maxwell Chen and Gavin Liu
""")

