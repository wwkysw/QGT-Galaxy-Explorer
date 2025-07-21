import streamlit as st

st.title("QGT Galaxy Explorer")
st.write("Welcome to the Quantum Gravity rotation curve visualizer!")

# Sidebar menu with diagram options
section = st.sidebar.radio("Choose a visualization:", [
    "Rotation Curve",
    "Model Residuals",
    "BIC Comparison",
    "Amplification Factor",
    "Stellar vs HI Density",
    "Composite Diagnostic",
    "Dark Matter Comparison"
])

# Start with IF
if section == "Rotation Curve":
    # Rotation curve plot code here

# Then continue with ELIF
elif section == "Model Residuals":
    # Residuals plot code here

elif section == "BIC Comparison":
    # BIC plot code here

elif section == "Amplification Factor":
    # Amplification plot code here

elif section == "Stellar vs HI Density":
    # Stellar + HI overlay plot code here

elif section == "Composite Diagnostic":
    # Composite breakdown plot code here

elif section == "Dark Matter Comparison":
    # New section you’re adding!

if section == "Dark Matter Comparison":

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
