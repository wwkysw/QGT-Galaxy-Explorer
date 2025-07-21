import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(layout="wide")

# Title
st.title("🌌 Exploring Quantum Gravity Theory through NGC 2403")

st.markdown("""
Dive into how gravity behaves across NGC 2403—from classical models to Quantum Gravity Theory (QGT). Use the sidebar to explore each visualization.
""")

# Sidebar selector
section = st.sidebar.radio("Choose a visualization:", [
    "Rotation Curve",
    "Model Residuals",
    "BIC Comparison",
    "Amplification Factor",
    "Stellar vs HI Density",
    "Composite Diagnostic",
    "Dark Matter Comparison"
])

# Shared data
radius = [0.2, 0.8, 1.5, 2.3, 2.9, 3.5, 4.2, 4.55, 5.0, 6.0, 7.5, 9.0, 11.0, 13.0, 15.0]
observed_velocity = [28.5, 52.1, 78.3, 102.6, 121.4, 128.7, 130.1, 130.3, 130.0, 129.2, 127.8, 126.1, 124.3, 122.5, 120.8]
observed_error = [1.0, 1.8, 2.7, 3.6, 4.2, 4.5, 4.6, 4.6, 4.6, 4.5, 4.5, 4.4, 4.4, 4.3, 4.2]
newtonian_velocity = [28.5, 52.1, 78.3, 102.6, 121.4, 116.2, 98.3, 84.7, 71.5, 54.8, 39.2, 28.6, 19.3, 13.2, 9.1]
qgt_velocity = [28.4, 52.0, 78.2, 102.5, 121.4, 128.7, 130.1, 130.2, 130.0, 129.2, 127.7, 126.1, 124.2, 122.4, 120.6]
velocity_residual = [((o - n)/o)*100 for o, n in zip(observed_velocity, newtonian_velocity)]
amplification = [(q**2 / n**2 - 1) for q, n in zip(qgt_velocity, newtonian_velocity)]
stellar_density = [125.3, 89.7, 64.2, 42.5, 28.7, 18.9, 12.4, 9.2, 7.5, 4.8, 2.9, 1.8, 0.9, 0.4, 0.2]
hi_density = [0.8, 1.2, 2.1, 2.9, 3.5, 4.2, 4.6, 5.0, 4.6, 4.5, 4.0, 2.8, 1.9, 1.2, 1.2]
scaled_stellar = np.array(stellar_density) * 130 / max(stellar_density)
scaled_hi = np.array(hi_density) * 130 / max(stellar_density)

# Visualization blocks
if section == "Rotation Curve":
    st.subheader("📈 Rotation Curve")
    fig, ax = plt.subplots()
    ax.errorbar(radius, observed_velocity, yerr=observed_error, label="Observed", color='black')
    ax.plot(radius, newtonian_velocity, 'r:', label="Newtonian")
    ax.plot(radius, qgt_velocity, 'b-', label="QGT")
    ax.axvline(x=4.55, color='gray', linestyle='--', label='R₀ = 4.55 kpc')
    ax.set_xlabel("Radius (kpc)")
    ax.set_ylabel("Velocity (km/s)")
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

elif section == "Model Residuals":
    st.subheader("📉 Velocity Residuals vs Radius")
    fig, ax = plt.subplots()
    ax.plot(radius, velocity_residual, 'r--', marker='x', label="Newtonian Residuals (%)")
    ax.axvline(x=4.55, color='gray', linestyle='--', label='R₀')
    ax.set_xlabel("Radius (kpc)")
    ax.set_ylabel("Residual (%)")
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

elif section == "BIC Comparison":
    st.subheader("📊 Bayesian Information Criterion")
    models = ['QGT', 'MOND', 'NFW', 'Newtonian']
    bic_scores = [15.2, 147.9, 327.2, 941.6]
    fig, ax = plt.subplots()
    bars = ax.bar(models, bic_scores, color=['blue', 'green', 'orange', 'red'])
    for bar, score in zip(bars, bic_scores):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 10, f'{score}', ha='center')
    ax.set_ylabel("BIC Score")
    ax.set_title("Model Preference")
    ax.grid(axis='y')
    st.pyplot(fig)

elif section == "Amplification Factor":
    st.subheader("🚀 Mass Amplification")
    fig, ax = plt.subplots()
    ax.plot(radius, amplification, 'm-o', label="QGT Amplification")
    ax.axvline(x=4.55, color='gray', linestyle='--', label='R₀')
    ax.set_xlabel("Radius (kpc)")
    ax.set_ylabel("Amplification (×)")
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

elif section == "Stellar vs HI Density":
    st.subheader("🌠 Density Profiles")
    fig, ax = plt.subplots()
    ax.plot(radius, scaled_stellar, 'darkred', marker='o', linestyle='--', label="Stellar Density (scaled)")
    ax.plot(radius, scaled_hi, 'dodgerblue', marker='s', linestyle='-.', label="HI Density (scaled)")
    ax.axvline(x=4.55, color='gray', linestyle='--', label='R₀')
    ax.set_xlabel("Radius (kpc)")
    ax.set_ylabel("Scaled Surface Density")
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

elif section == "Composite Diagnostic":
    st.subheader("🧭 Composite Breakdown Diagnostic")
    scaled_density = np.array(stellar_density) * 100 / max(stellar_density)
    fig, ax = plt.subplots()
    ax.plot(radius, velocity_residual, 'r--', marker='x', label='Velocity Residual (%)')
    ax.plot(radius, amplification, 'b-', marker='o', label='Amplification (×)')
    ax.plot(radius, scaled_density, 'g-.', marker='s', label='Stellar Density (scaled)')
    for i, r in enumerate(radius):
        if velocity_residual[i] > 15 and amplification[i] > 10 and scaled_density[i] < 10:
            ax.axvline(x=r, color='gray', linestyle=':', alpha=0.5)
            ax.text(r, 120, '⚠', ha='center', fontsize=12)
    ax.axvline(x=4.55, color='gray', linestyle='--', label='R₀')
    ax.set_xlabel("Radius (kpc)")
    ax.set_ylabel("Diagnostic Value")
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

elif section == "Dark Matter Comparison":
    st.subheader("🌌 Dark Matter vs QGT")
    fig, ax = plt.subplots()
    # Example stub data for visualization
    dark_matter_velocity = [28.5, 52.1, 78.3, 102.6, 121.4, 125.0, 127.0, 127.5, 128.0, 128.2, 128.5, 128.7, 129.0, 129.2, 129.5]
    ax.plot(radius, qgt_velocity, label='QGT', color='blue', linewidth=2)
    ax.plot(radius, dark_matter_velocity, label='Dark Matter Model', color='purple', linestyle='--')
    ax.plot(radius, observed_velocity, label='Observed', color='black', linestyle=':')
    ax.axvline(x=4.55, color='gray', linestyle='--', label='R₀')
    ax.set_xlabel("Radius (kpc)")
    ax.set_ylabel("Velocity (km/s)")
    ax.set_title("QGT vs Dark Matter Predictions")
    ax.legend()
