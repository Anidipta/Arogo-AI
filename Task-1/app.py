import streamlit as st
import requests
from datetime import datetime

st.markdown("""
<style>
    /* Base theme override */
    .stApp {
        background: linear-gradient(135deg, #0f0f0f, #1a1410, #0f0f0f);
        color: #e0e0e0;
    }
    
    /* Animated gradient title */
    .title {
        position: relative;
        font-size: 3.2rem;
        font-weight: 800;
        text-align: center;
        margin: 3rem 0;
        background: linear-gradient(45deg, #c6a07c, #deb887, #e8c39e);
        -webkit-background-clip: text;
        background-clip: text;
        color: transparent;
        animation: titleGlow 8s ease infinite;
    }
    
    .title::after {
        content: '';
        position: absolute;
        bottom: -10px;
        left: 50%;
        transform: translateX(-50%);
        width: 150px;
        height: 3px;
        background: linear-gradient(90deg, transparent, #c6a07c, transparent);
    }
    
    /* Animated border container */
    .gradient-border {
        position: relative;
        padding: 2rem;
        margin: 2rem 0;
        border-radius: 12px;
        background: rgba(20, 20, 20, 0.4);
        animation: borderGlow 4s ease infinite;
    }
    
    .gradient-border::before {
        content: "";
        position: absolute;
        inset: 0;
        border-radius: 12px;
        padding: 2px;
        background: linear-gradient(
            45deg,
            rgba(198, 160, 124, 0.5),
            rgba(222, 184, 135, 0.2),
            rgba(198, 160, 124, 0.5)
        );
        mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
        -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
        mask-composite: exclude;
        -webkit-mask-composite: xor;
        pointer-events: none;
    }
    
    /* Input field styling */
    .stSelectbox > div > div {
        background-color: rgba(30, 30, 30, 0.6) !important;
        border: none !important;
        border-radius: 8px !important;
        transition: all 0.3s ease;
    }
    
    .stSelectbox > div > div:hover {
        background-color: rgba(40, 40, 40, 0.8) !important;
        box-shadow: 0 0 15px rgba(198, 160, 124, 0.2);
    }
    
    /* Floating label effect */
    .input-label {
        color: #c6a07c;
        font-size: 0.9rem;
        margin-bottom: 0.5rem;
        opacity: 0.8;
        transform: translateY(0);
        transition: all 0.3s ease;
    }
    
    /* Custom button */
    .predict-button {
        background: linear-gradient(45deg, rgba(198, 160, 124, 0.1), rgba(222, 184, 135, 0.1)) !important;
        border: 1px solid rgba(198, 160, 124, 0.3) !important;
        color: #c6a07c !important;
        padding: 1rem 2rem !important;
        border-radius: 8px !important;
        font-size: 1.1rem !important;
        font-weight: 600 !important;
        width: 100%;
        transition: all 0.3s ease !important;
        position: relative;
        overflow: hidden;
    }
    
    .predict-button:hover {
        border-color: rgba(198, 160, 124, 0.8) !important;
        box-shadow: 0 0 20px rgba(198, 160, 124, 0.2);
        transform: translateY(-2px);
    }
    
    .predict-button::after {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 60%);
        opacity: 0;
        transition: opacity 0.3s ease;
    }
    
    .predict-button:hover::after {
        opacity: 1;
    }
    
    /* Prediction result styling */
    .prediction-result {
        position: relative;
        margin-top: 2rem;
        padding: 2rem;
        border-radius: 12px;
        background: linear-gradient(135deg, rgba(198, 160, 124, 0.1), rgba(40, 30, 30, 0.2));
        border: 1px solid rgba(198, 160, 124, 0.2);
        animation: fadeIn 0.5s ease-out;
    }
    
    .prediction-result h2 {
        color: #c6a07c;
        margin-bottom: 1rem;
        font-size: 1.5rem;
    }
    
    /* Animations */
    @keyframes titleGlow {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.8; }
    }
    
    @keyframes borderGlow {
        0%, 100% { box-shadow: 0 0 20px rgba(198, 160, 124, 0.1); }
        50% { box-shadow: 0 0 30px rgba(198, 160, 124, 0.2); }
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    /* Error message */
    .stError {
        background: linear-gradient(45deg, rgba(220, 38, 38, 0.1), rgba(220, 38, 38, 0.05)) !important;
        border: 1px solid rgba(220, 38, 38, 0.2) !important;
        color: #ff8a8a !important;
        padding: 1rem;
        border-radius: 8px;
        animation: shake 0.5s ease-in-out;
    }
    
    @keyframes shake {
        0%, 100% { transform: translateX(0); }
        25% { transform: translateX(-5px); }
        75% { transform: translateX(5px); }
    }
    
</style>
""", unsafe_allow_html=True)

# App title
st.markdown('<h1 class="title">Shipment Delay Prediction</h1>', unsafe_allow_html=True)


col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="input-label">Origin</div>', unsafe_allow_html=True)
    origin = st.selectbox(
        "",
        ['Ahmedabad', 'Bangalore', 'Chennai', 'Delhi', 'Hyderabad',
         'Jaipur', 'Kolkata', 'Lucknow', 'Mumbai', 'Pune'],
        label_visibility="collapsed",
        key="origin_select"
    )
    
    
    st.markdown('<div class="input-label">Shipment Date</div>', unsafe_allow_html=True)
    shipment_date = st.date_input(
        "", 
        label_visibility="collapsed",
        key="shipment_date"
    )
    
    st.markdown('<div class="input-label">Vehicle Type</div>', unsafe_allow_html=True)
    vehicle_type = st.selectbox(
        "",
        ['Container', 'Lorry', 'Trailer', 'Truck', 'nan'],
        label_visibility="collapsed",
        key="vehicle_select"
    )
    
    st.markdown('<div class="input-label">Distance (km)</div>', unsafe_allow_html=True)
    distance = st.number_input(
        "", 
        min_value=0, 
        label_visibility="collapsed",
        key="distance_input"
    )

with col2:
    
    st.markdown('<div class="input-label">Destination</div>', unsafe_allow_html=True)
    destination = st.selectbox(
        "",
        ['Ahmedabad', 'Bangalore', 'Chennai', 'Delhi', 'Hyderabad',
         'Jaipur', 'Kolkata', 'Lucknow', 'Mumbai', 'Pune'],
        label_visibility="collapsed",
        key="destination_select"
    )
    
    st.markdown('<div class="input-label">Planned Delivery Date</div>', unsafe_allow_html=True)
    planned_delivery_date = st.date_input(
        " ", 
        label_visibility="collapsed",
        key="delivery_date"
    )

    st.markdown('<div class="input-label">Traffic Conditions</div>', unsafe_allow_html=True)
    traffic_conditions = st.selectbox(
        "",
        ['Heavy', 'Light', 'Moderate'],
        label_visibility="collapsed",
        key="traffic_select"
    )
    
    st.markdown('<div class="input-label">Weather Conditions</div>', unsafe_allow_html=True)
    weather_conditions = st.selectbox(
        "",
        ['Clear', 'Fog', 'Rain', 'Storm'],
        label_visibility="collapsed",
        key="weather_select"
    )
     
st.markdown('</div>', unsafe_allow_html=True)

# Custom styled button
if st.button("Predict Delay", key="predict_button", use_container_width=True):
    with st.spinner("Processing prediction..."):
        data = {
            "Origin": origin,
            "Destination": destination,
            "Shipment Date": str(shipment_date),
            "Planned Delivery Date": str(planned_delivery_date),
            "Vehicle Type": vehicle_type,
            "Distance": distance,
            "Weather Conditions": weather_conditions,
            "Traffic Conditions": traffic_conditions
        }

        try:
            response = requests.post("http://localhost:5000/predict", json=data)
            
            if response.status_code == 200:
                prediction = response.json()
                st.markdown(
                    f'<div class="prediction-result">'
                    f'<h2>Prediction Result</h2>'
                    f'<p>The shipment is predicted to be {prediction["Prediction"]}</p>'
                    '</div>',
                    unsafe_allow_html=True
                )
            else:
                st.error(f"Error: {response.json().get('error', 'Unknown error')}")
                
        except requests.exceptions.RequestException as e:
            st.error(f"An error occurred: {e}")
