# .app.py

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import inspect
from ftcs_couette import ftcs_couette
from laasonen_couette import laasonen_couette



# =====================================================================
# =========================== main ====================================
# =====================================================================

def main():
    col1, col2 = st.columns([0.8, 0.2])
    with col1:
        st.title("Couette Flow Simulation")
        st.subheader("between Two Parallel Plates")
    with col2:
        st.image("./logoUniMasS.png", width=180)
        
    st.write("""
    This Streamlit app simulates the Couette flow of fluid between two infinite parallel plates.
    One plate is stationary, and the other moves at a constant velocity, inducing flow in the fluid.
    """)
    
    
    st.markdown('***')
    
    # =========================== INPUTS UI ===========================
    
    st.subheader("Simulation parameters")

    # Collecting inputs from the user
    h = st.number_input("Distance between the plates in meters (h)", min_value=0.1, max_value=10.0, value=1.0, step=0.1)
    u_g = st.number_input("Speed of the upper plate in m/s (u_g)", min_value=0.0, max_value=10.0, value=1.0, step=0.1)
    Ny = st.number_input("Number of grid points in y direction (Ny)", min_value=10, max_value=1000, value=100, step=10)
    dt = st.number_input("Time step in seconds (dt)", min_value=0.00001, max_value=0.01, value=0.0001, format="%.5f")
    total_time = st.number_input("Total time for the simulation in seconds (total_time)", min_value=0.1, max_value=10.0, value=2.0, step=0.1)
    Dy = st.number_input("Diffusion coefficient for the y direction (Dy)", min_value=0.0001, max_value=0.01, value=0.001, format="%.4f")
    
    
    
    st.latex(r"""
    \frac{\partial u}{\partial t} - 0.001 \frac{\partial^2 u}{\partial y^2} - 0.02 \frac{\partial u}{\partial y} = 0
    """)

    
    st.markdown('***')

    # =========================== sym ===========================
    # Call the simulation function and display the results
    
    st.subheader("FTCS method for Couette flow")
    st.write("""
    This method uses a finite-difference scheme to solve the diffusion equation governing the Couette flow.
    It discretizes the spatial and temporal derivatives to approximate the solution.
    """)
    # st.latex(r"\frac{\partial u}{\partial t} = \nu \frac{\partial^2 u}{\partial y^2}")

    # velocity_profile_ftcs_nopd = ftcs_couette()
    velocity_profile_ftcs = pd.DataFrame(ftcs_couette(h, u_g, Ny, dt, total_time, Dy))
    st.write("Final velocity profile:")
    st.dataframe(velocity_profile_ftcs.transpose())  
      
    # Display FTCS code ------------------
    # python
    ftcs_couette_code = inspect.getsource(ftcs_couette)
    with st.expander("Click to reveal Python code"):
        st.code(ftcs_couette_code, language='python')
    # matlab
    with st.expander("Show Matlab code"):
        with open('./ftcs_couette.m', 'r') as file:
            output = file.read()
            st.code(output, language='matlab')

    st.markdown("***")

    # =========================== Laasonen ====================================
    st.subheader("2. Laasonen method for Couette flow")

    # velocity_profile_laasonen = pd.DataFrame(laasonen_couette())
    st.write("Laasonen velocity profile:")
    # st.dataframe(velocity_profile_laasonen.transpose())

    # Display the source code in a streamlit code box
    laasonen_couette_code = inspect.getsource(laasonen_couette)
    with st.expander("Click to reveal Python code", expanded=True):
        st.code(laasonen_couette_code, language='python')
    
    with open('./laasonen_couette.m', 'r') as file:
        output = file.read()
        st.code(output, language='matlab')

if __name__ == "__main__":
    main()