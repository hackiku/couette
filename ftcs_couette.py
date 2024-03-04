import streamlit as st
import numpy as np
import matplotlib.pyplot as plt


def ftcs_couette(h, u_g, Ny, dt, total_time, Dy):

    # Discretization parameters
    dy = h / (Ny - 1)  # Grid spacing in y direction
    num_steps = int(total_time / dt)  # Number of time steps

    # Prepare the array for u(y,t) with initial condition u(y,0) = 0
    u = np.zeros(Ny)

    # Boundary conditions
    u[0] = 0      # u(0,t) = 0 for the lower stationary plate
    u[-1] = u_g   # u(h,t) = u_g for the upper moving plate

    # FTCS scheme to update u for each time step
    for n in range(num_steps):
        u_new = u.copy()  # Copy the current velocity profile
        for i in range(1, Ny-1):  # Update all points except the boundaries
            # Include the term for the first derivative with respect to y
            u_new[i] = u[i] + (Dy * dt / dy**2) * (u[i+1] - 2*u[i] + u[i-1]) \
                    + (0.02 * dt / (2 * dy)) * (u[i+1] - u[i-1])
        u = u_new  # Set the new profile as the current profile

    # Visualize the final velocity profile
    fig, ax = plt.subplots()
    ax.plot(np.linspace(0, h, Ny), u, label=f'Time = {num_steps*dt} seconds')
    ax.set_xlabel('Position between the plates (m)')
    ax.set_ylabel('Fluid velocity (m/s)')
    ax.set_title('Velocity profile of fluid between two parallel plates')
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

    # Return the final velocity profile
    return u

