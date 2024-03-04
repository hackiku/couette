# .app.py

import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import inspect
import pandas as pd

import streamlit as st
import pandas as pd
# Import your computational functions
from ftcs_couette import ftcs_couette
from laasonen_couette import laasonen_couette


# =====================================================================
# =========================== main ====================================
# =====================================================================

def main():
    st.title("Couette Flow Simulation between Two Parallel Plates")\
        
    st.write("""
    This Streamlit app simulates the Couette flow of fluid between two infinite parallel plates.
    One plate is stationary, and the other moves at a constant velocity, inducing flow in the fluid.
    """)
    
    st.latex(r"""
    \frac{\partial u}{\partial t} - 0.001 \frac{\partial^2 u}{\partial y^2} - 0.02 \frac{\partial u}{\partial y} = 0
    """)
    
    st.markdown('***')
    
    # =========================== INPUTS UI ===========================
    
    st.subheader("Simulation parameters")
    
    st.write("The simulation parameters are the same for both the FTCS and Laasonen methods.")
    
    st.code("interactive element")
    
    st.markdown('***')

    # =========================== sym ===========================
    # Call the simulation function and display the results
    
    st.subheader("FTCS method for Couette flow")
    st.write("""
    This method uses a finite-difference scheme to solve the diffusion equation governing the Couette flow.
    It discretizes the spatial and temporal derivatives to approximate the solution.
    """)
    st.latex(r"\frac{\partial u}{\partial t} = \nu \frac{\partial^2 u}{\partial y^2}")

    # velocity_profile_ftcs_nopd = ftcs_couette()
    velocity_profile_ftcs = pd.DataFrame(ftcs_couette())
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