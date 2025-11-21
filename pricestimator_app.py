import streamlit as st
import pandas as pd
import joblib

def run_pricestimator_app():

    # ======================================
    # SAFE CSS
    # ======================================
    st.markdown("""
    <style>

     /* --- Smooth title fonts --- */
    h1, h2, h3 {
        color: #151c36 !important;
        font-weight: 800 !important;
    }

    /* --- Wrapper Card Cream FIX --- */
    .cream-box {
        background-color: #e7dcbb; 
        border: 2px solid #ecdcab;
        padding: 8px 10px;
        border-radius: 10px;
        margin-bottom: 12px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.05);
    }

    .block-container { padding-top: 1rem !important; }

    /* NAVY BUTTON */
    div.stButton > button {
        background-color: #151c36 !important;
        color: white !important;
        padding: 0.6rem 1.2rem;
        font-size: 1.05rem;
        font-weight: 600;
        border-radius: 8px;
        border: 2px solid #151c36;
        transition: 0.2s ease-in-out;
    }

    div.stButton > button:hover {
        background-color: #133567 !important;
        border-color: #133567 !important;
        transform: translateY(-2px);
    }

    </style>
    """, unsafe_allow_html=True)


    # ======================================
    # HEADER
    # ======================================
    st.markdown("<h1>AutoValue — Used Car Price Estimator</h1>", unsafe_allow_html=True)
    st.markdown(
        "<p>Masukkan spesifikasi mobil Anda, dan sistem akan memprediksi "
        "<b>harga mobil bekas (USD)</b> menggunakan model Machine Learning.</p>",
        unsafe_allow_html=True,
    )

    # ======================================
    # FORM INPUT
    # ======================================
    def cream_card(title, widget_func):
        st.markdown(f"<div class='cream-box'><b>{title}</b>", unsafe_allow_html=True)
        value = widget_func()
        st.markdown("</div>", unsafe_allow_html=True)
        return value

    make_year = cream_card(
        "Make Year",
        lambda: st.number_input("", min_value=1990, max_value=2023, value=2015)
    )

    mileage = cream_card(
        "Mileage (km/l)",
        lambda: st.number_input("", min_value=5.0, max_value=35.0, value=18.0, step=0.1)
    )

    engine_cc = cream_card(
        "Engine Size (cc)",
        lambda: st.number_input("", min_value=600, max_value=6000, value=1500)
    )

    fuel_type = cream_card(
        "Fuel Type",
        lambda: st.selectbox("", ["Petrol", "Diesel", "Electric"])
    )

    owner_count = cream_card(
        "Number of Previous Owners",
        lambda: st.number_input("", min_value=1, max_value=5, value=1)
    )

    brand = cream_card(
        "Brand",
        lambda: st.selectbox("", ["Toyota", "Honda", "BMW", "Hyundai", "Tesla", "Ford", "Volkswagen"])
    )

    transmission = cream_card(
        "Transmission",
        lambda: st.selectbox("", ["Manual", "Automatic"])
    )

    color = cream_card(
        "Color",
        lambda: st.selectbox("", ["White", "Black", "Silver", "Blue", "Red", "Gray"])
    )

    service_history = cream_card(
        "Service History",
        lambda: st.selectbox("", ["None", "Partial", "Full", "No Service"])
    )

    accidents_reported = cream_card(
        "Accidents Reported",
        lambda: st.number_input("", min_value=0, max_value=5, value=0)
    )

    insurance_valid = cream_card(
        "Insurance Valid",
        lambda: st.selectbox("", ["Yes", "No"])
    )

    # ======================================
    # MAKE DATAFRAME
    # ======================================
    input_df = pd.DataFrame([{
        "make_year": make_year,
        "mileage_kmpl": mileage,
        "engine_cc": engine_cc,
        "fuel_type": fuel_type,
        "owner_count": owner_count,
        "brand": brand,
        "transmission": transmission,
        "color": color,
        "service_history": service_history,
        "accidents_reported": accidents_reported,
        "insurance_valid": insurance_valid
    }])

    # ======================================
    # PREDICT
    # ======================================
    st.markdown("<h2>📊 Prediction Result</h2>", unsafe_allow_html=True)

    pipeline = joblib.load("model_pipeline.pkl")

    if st.button("Predict Price"):
        prediction = pipeline.predict(input_df)[0]
        st.success(f"💰 Estimated Car Price: **${prediction:,.2f} USD**")

