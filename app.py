import streamlit as st
import streamlit.components.v1 as stc
from pricestimator_app import run_pricestimator_app
import os

# ============================
# PAGE CONFIG
# ============================
st.set_page_config(page_title="AutoValue", layout="wide")

# ============================
# GLOBAL CSS (CLEAN FINAL VERSION)
# ============================
st.markdown("""
<style>

h1, h2, h3, h4 {
    color: #151c36 !important;
    font-weight: 800 !important;
}

/* MAIN CONTAINER SPACING */
.block-container {
    padding-top: 2rem !important;
}

/* Intro Card */
.intro-card {
    background-color: #ffffff;
    padding: 12px 18px;
    border-radius: 12px;
    border: 1px solid #eef1f6;
    width: 95%;
    margin: 20px auto;
    box-shadow: 0 2px 6px rgba(0,0,0,0.06);
}

/* Space between columns */
[data-testid="column"] {
    padding-left: 30px !important;
    padding-right: 30px !important;
}

/* Fix long links wrapping */
a {
    word-wrap: break-word !important;
    white-space: normal !important;
}

/* CTA Button */
.stButton > button {
    background-color: #0b1f3a !important;
    color: white !important;
    padding: 10px 22px !important;
    border-radius: 8px !important;
    border: 2px solid #0b1f3a !important;
    font-weight: 700 !important;
}

.stButton > button:hover {
    background-color: #133567 !important;
    border-color: #133567 !important;
}

/* Logo alignment */
.logo-container {
    display: flex;
    align-items: center;
    gap: 16px;
}

</style>
""", unsafe_allow_html=True)

# ============================
# SIDEBAR MENU
# ============================
menu = ['Home', 'Machine Learning']
choice = st.sidebar.selectbox("Menu", menu)

# ============================
# LOGO HANDLING
# ============================
logo_path = r"D:\Kuliah\Bootcamp\Predict.png"

if os.path.exists(logo_path):
    logo_img = logo_path
else:
    logo_img = None


# ============================
# HOME PAGE
# ============================
if choice == 'Home':

    # ===== HEADER (Logo + Title) =====
    col1, col2 = st.columns([1, 5])
    with col1:
        if logo_img:
            st.image(logo_img, width=120)
    with col2:
        st.markdown("<h1>AutoValue — Used Car Price Estimator</h1>", unsafe_allow_html=True)
        st.write(
            "Masukkan spesifikasi mobil, lalu model akan memprediksi "
            "**harga mobil bekas (USD)** menggunakan Machine Learning."
        )

    # ===== INTRO CARD =====
    st.markdown("<div class='intro-card'>", unsafe_allow_html=True)
    st.markdown("""
### What This App Does
- **Estimate resale prices** of used cars based on key specs  
- **Provide ML predictions** via Ridge Regression  
- **Explore dataset & model training** via Google Colab notebook  
    """)
    st.markdown("</div>", unsafe_allow_html=True)

    # ===== QUICK ACTION BOX =====
    st.markdown("<div class='cream-box'>", unsafe_allow_html=True)
    st.markdown("## Quick Actions")
    st.markdown("""
- Buka halaman **Machine Learning** untuk prediksi harga  
- **Link Google Colab** : https://tinyurl.com/pricestimator  
""")
    st.markdown("</div>", unsafe_allow_html=True)

    # CTA BUTTON
    st.markdown("<div style='text-align:center;'>", unsafe_allow_html=True)
    if st.button("Open Machine Learning Page"):
        run_pricestimator_app()
    st.markdown("</div>", unsafe_allow_html=True)

    # ===== DATASET & PROJECT - Two columns =====
    st.markdown("## Dataset & Project")
    col_left, col_right = st.columns([1, 1], gap="large")

    left, right = st.columns(2)

    with left:
        st.markdown("### Dataset")
        st.markdown("- Kaggle dataset : https://www.kaggle.com/datasets/therohithanand/used-car-price-prediction")
        st.markdown("- Local CSV:")

        with open("used_car_price_dataset_extended.csv", "rb") as f:
            st.download_button(
                "📥 Download Dataset CSV",
                f,
                "used_car_price_dataset_extended.csv",
                mime="text/csv"
            )

    with right:
        st.markdown("### Project")
        st.markdown("- Link Google Collab (pipeline) : https://tinyurl.com/modelpipeline")
        st.markdown("- Model artifact (pipeline):")

        with open("model_pipeline.pkl", "rb") as f:
            st.download_button(
                "📦 Download Model Pipeline",
                f,
                "model_pipeline.pkl",
                mime="application/octet-stream"
            )

    st.markdown("---")
    st.caption("Tips: tambahkan screenshot hasil model, sample predictions, dan penjelasan proses modelling di laporan atau presentasi.")


# ============================
# MACHINE LEARNING PAGE
# ============================
elif choice == "Machine Learning":
    run_pricestimator_app()




