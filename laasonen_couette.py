import streamlit as st
import numpy as np

def laasonen_couette():
    # Parameters are the same as in the ftcs_couette function
    h = 1.0
    u_g = 1.0
    Ny = 100
    dy = h / (Ny - 1)
    dt = 0.0001
    total_time = 2.0
    num_steps = int(total_time / dt)
    Dy = 0.001

    # Initialize the velocity profile
    u = np.zeros(Ny)
    u[0] = 0
    u[-1] = u_g

    # Coefficient matrix and right-hand side vector
    A = np.zeros((Ny, Ny))
    b = np.zeros(Ny)

    # Populate the matrix A
    for i in range(1, Ny - 1):
        A[i, i-1] = -Dy * dt / dy**2
        A[i, i] = 1 + 2 * Dy * dt / dy**2
        A[i, i+1] = -Dy * dt / dy**2

    # Boundary conditions
    A[0, 0] = A[-1, -1] = 1

    # Time-stepping loop
    for n in range(num_steps):
        # Update the right-hand side vector
        b = u.copy()
        b[0] = 0
        b[-1] = u_g

        # Solve the linear system
        u = np.linalg.solve(A, b)

    # Plotting the final velocity profile
    fig, ax = plt.subplots()
    ax.plot(np.linspace(0, h, Ny), u, label=f'Time = {num_steps*dt} seconds')
    ax.set_xlabel('Position between the plates (m)')
    ax.set_ylabel('Fluid velocity (m/s)')
    ax.set_title('Laasonen method: Velocity profile of fluid between two parallel plates')
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

    return u
