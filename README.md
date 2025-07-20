# QGT-Galaxy-Explorer
Streamlit-based app to visualize galaxy curves using Qunatum Grvity Theory
# 🌌 QGT Galaxy Explorer

**Explore the rotation curves of galaxies through the lens of Quantum Gravity Theory.**  
An interactive Streamlit app that visualizes observed and predicted galactic dynamics using QGT, MOND, and NFW models.

---

## 🚀 Overview

QGT Galaxy Explorer is an educational interface designed for students, researchers, and astro-curious minds to investigate how theoretical models fit real-world galactic rotation data.

Using sliders and dropdowns, you can:

- Input physical parameters for a selected galaxy
- Generate plots comparing observed rotation curves to theoretical predictions
- Explore residuals via interactive heatmaps
- Receive contextual commentary from a virtual assistant named **Qubit**
- Deepen your understanding of QGT through optional explainer modules and mini challenges

---

## 🛠️ How It Works

The app runs on **Streamlit**, using simulated data and basic rotation curve equations to visualize:

- **Observed velocities**
- Predictions from:
  - QGT (Quantum Gravity Theory)
  - MOND (Modified Newtonian Dynamics)
  - NFW (Cold Dark Matter Halo Model)

It calculates residuals between observations and predictions, and uses heatmaps and graphs for clear comparison.

> 💡 Future versions may include real datasets from SPARC or THINGS, and curve-fitting optimizers using Scipy or PyMC.

---

## 📸 Screenshots

*(Optional: add image links here once you have mockups)*  
- Galaxy Dashboard Interface  
- Rotation Curve Viewer  
- Residual Heatmap with Commentary  

---

## 📦 Installation & Usage

### Clone and Run Locally:

```bash
git clone https://github.com/your-username/QGT-Galaxy-Explorer.git
cd QGT-Galaxy-Explorer
pip install -r requirements.txt
streamlit run qgt_explorer.py
