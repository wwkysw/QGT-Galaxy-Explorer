import streamlit as st

st.title("QGT Galaxy Explorer")
st.write("Welcome to the Quantum Gravity rotation curve visualizer!")

section = st.sidebar.radio("Choose a visualization:", [
    "Rotation Curve", "Model Residuals", "BIC Comparison",
    "Amplification Factor", "Stellar vs HI Density",
    "Composite Diagnostic", "Dark Matter Comparison"
])
elif section == "Dark Matter Comparison":
    st.subheader("🌌 Dark Matter vs QGT")
    fig, ax = plt.subplots()
    # Plot your data here
    ax.plot(...)
    ax.set_title("Model Comparison")
    st.pyplot(fig)
    st.markdown("Explanation of how QGT differs from dark matter models...")
r0_value = st.slider("Choose critical radius R₀ (kpc):", 2.0, 10.0, 4.55)
tab1, tab2 = st.tabs(["Plot", "Explanation"])
with tab1:
    st.pyplot(fig)
with tab2:
    st.markdown("Here’s how the physics works...")
streamlit run qgt_explorer.py
git add qgt_explorer.py
git commit -m "Added new plot and improved layout"
git push
streamlit run qgt_explorer.py
