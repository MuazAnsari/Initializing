import streamlit as st

# --- 1. Page Config (SIDEBAR FORCE FIX) ---
st.set_page_config(
    page_title="PakCar Elite Edition", 
    page_icon="⚖️", 
    layout="wide", 
    initial_sidebar_state="expanded"  # Isse sidebar hamesha nazar aayega
)

# --- 2. THE ULTIMATE GOLD THEME CSS ---
st.markdown("""
    <style>
    header, footer {visibility: hidden;}
    
    .stApp {
        background: radial-gradient(circle, #1a1a1a 0%, #050505 100%);
        color: #ffffff;
    }

    /* --- RADIO BUTTON GOLD FIX --- */
    /* Target dot circle */
    div[data-baseweb="radio__dot"] {
        border-color: #555 !important;
        background-color: #222 !important;
    }

    /* Target selected state */
    input[checked] + div[data-baseweb="radio__dot"] {
        background-color: #D4AF37 !important;
        border-color: #D4AF37 !important;
    }

    /* Target inner point of selected dot */
    input[checked] + div[data-baseweb="radio__dot"] > div {
        background-color: #000 !important;
    }

    /* Sidebar Background */
    section[data-testid="stSidebar"] {
        background-color: #0c0c0c !important;
        border-right: 1px solid #D4AF37 !important;
    }

    .royal-header {
        background: linear-gradient(90deg, #D4AF37, #FBF5B7, #D4AF37);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-family: 'Garamond', serif;
        font-size: clamp(30px, 5vw, 60px);
        font-weight: 900;
        text-align: center;
        margin: 20px 0;
    }

    .car-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(15px);
        border-radius: 15px;
        padding: 20px;
        border: 1px solid rgba(212, 175, 55, 0.2);
        margin-bottom: 15px;
    }
    
    .badge {
        background: #D4AF37;
        color: black;
        padding: 4px 12px;
        border-radius: 50px;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. Data ---
# Note: Is catalog mein aap apni 50+ gaariyan add kar sakte hain
CAR_CATALOG = [
    # 0. Ultra-Budget Used Cars (Used: ~500K to 1.5M PKR) - New Section Added
    # -------------------------------------------------------------------------------------------------------
    {"model": "Mazda 323 (Used 1990)", "price": 550000, "condition": "Used", "fuel_type": "Petrol", "seats": 5, "trunk_size": "Average", "type": "Sedan"},
    {"model": "Hyundai Santro (Used 2007)", "price": 650000, "condition": "Used", "fuel_type": "Petrol", "seats": 5, "trunk_size": "Limited", "type": "Hatchback"},
    {"model": "Suzuki Alto (Used 2008)", "price": 750000, "condition": "Used", "fuel_type": "Petrol", "seats": 4, "trunk_size": "Limited", "type": "Hatchback"},
    {"model": "Daihatsu Cuore (Used 2010)", "price": 800000, "condition": "Used", "fuel_type": "Petrol", "seats": 4, "trunk_size": "Limited", "type": "Hatchback"},
    {"model": "Toyota Corolla (Used 1998)", "price": 950000, "condition": "Used", "fuel_type": "Petrol", "seats": 5, "trunk_size": "Average", "type": "Sedan"},
    {"model": "Mitsubishi Lancer (Used 2006)", "price": 1000000, "condition": "Used", "fuel_type": "Petrol", "seats": 5, "trunk_size": "Average", "type": "Sedan"},
    {"model": "Suzuki Mehran VXR (Used 2017)", "price": 1100000, "condition": "Used", "fuel_type": "Petrol", "seats": 4, "trunk_size": "Limited", "type": "Hatchback"},
    {"model": "Honda Civic VTi (Used 2003)", "price": 1150000, "condition": "Used", "fuel_type": "Petrol", "seats": 5, "trunk_size": "Average", "type": "Sedan"},
    {"model": "Mitsubishi Pajero (Used 1995)", "price": 1200000, "condition": "Used", "fuel_type": "Diesel", "seats": 5, "trunk_size": "High", "type": "SUV"}, # Diesel option
    {"model": "Suzuki Cultus VXR (Used 2012)", "price": 1250000, "condition": "Used", "fuel_type": "Petrol", "seats": 5, "trunk_size": "Limited", "type": "Hatchback"},
    {"model": "Suzuki Bolan (Used 2015)", "price": 1300000, "condition": "Used", "fuel_type": "Petrol", "seats": 7, "trunk_size": "Limited", "type": "Van"},
    {"model": "Toyota Corolla XLi (Used 2005)", "price": 1400000, "condition": "Used", "fuel_type": "Petrol", "seats": 5, "trunk_size": "Average", "type": "Sedan"},
    {"model": "Toyota Vitz (Used 2008)", "price": 1450000, "condition": "Used", "fuel_type": "Petrol", "seats": 5, "trunk_size": "Average", "type": "Hatchback"},
    {"model": "Toyota Prius (Used 2006)", "price": 1500000, "condition": "Used", "fuel_type": "Hybrid", "seats": 5, "trunk_size": "Average", "type": "Sedan"}, # Hybrid possibility
    # -------------------------------------------------------------------------------------------------------
    # 1. Budget Hatchbacks (New/Used: ~1.6M to 3.5M PKR)
    # -------------------------------------------------------------------------------------------------------
    {"model": "Suzuki Alto VXL", "price": 2700000, "condition": "New", "fuel_type": "Petrol", "seats": 4, "trunk_size": "Limited", "type": "Hatchback"},
    {"model": "Suzuki Cultus VXR", "price": 3200000, "condition": "New", "fuel_type": "Petrol", "seats": 5, "trunk_size": "Limited", "type": "Hatchback"},
    {"model": "KIA Picanto AT", "price": 3500000, "condition": "New", "fuel_type": "Petrol", "seats": 5, "trunk_size": "Limited", "type": "Hatchback"},
    {"model": "Honda N-WGN (Used 2018)", "price": 2400000, "condition": "Used", "fuel_type": "Petrol", "seats": 4, "trunk_size": "Limited", "type": "Hatchback"},
    {"model": "Toyota Vitz (Used 2017)", "price": 2900000, "condition": "Used", "fuel_type": "Petrol", "seats": 5, "trunk_size": "Average", "type": "Hatchback"},
    {"model": "Suzuki Wagon R VXL", "price": 2850000, "condition": "New", "fuel_type": "Petrol", "seats": 5, "trunk_size": "Limited", "type": "Hatchback"},
    {"model": "Prince Pearl (Used 2021)", "price": 1800000, "condition": "Used", "fuel_type": "Petrol", "seats": 4, "trunk_size": "Limited", "type": "Hatchback"},
    {"model": "FAW V2 (Used 2019)", "price": 1600000, "condition": "Used", "fuel_type": "Petrol", "seats": 5, "trunk_size": "Average", "type": "Hatchback"},
    {"model": "Toyota Aqua (Used 2018)", "price": 3400000, "condition": "Used", "fuel_type": "Hybrid", "seats": 5, "trunk_size": "Limited", "type": "Hatchback"},
    {"model": "Daihatsu Mira (Used 2019)", "price": 1900000, "condition": "Used", "fuel_type": "Petrol", "seats": 4, "trunk_size": "Limited", "type": "Hatchback"},
    {"model": "Suzuki Swift GLX (New)", "price": 4000000, "condition": "New", "fuel_type": "Petrol", "seats": 5, "trunk_size": "Average", "type": "Hatchback"}, # Higher budget hatchback

    # -------------------------------------------------------------------------------------------------------
    # 2. Mid-Range Sedans/Crossovers (New/Used: ~3.8M to 6.0M PKR)
    # -------------------------------------------------------------------------------------------------------
    {"model": "Honda City 1.2 LS", "price": 4300000, "condition": "New", "fuel_type": "Petrol", "seats": 5, "trunk_size": "Average", "type": "Sedan"},
    {"model": "Toyota Yaris ATIV X", "price": 4700000, "condition": "New", "fuel_type": "Petrol", "seats": 5, "trunk_size": "Average", "type": "Sedan"},
    {"model": "Changan Alsvin Lumiere", "price": 4100000, "condition": "New", "fuel_type": "Petrol", "seats": 5, "trunk_size": "Average", "type": "Sedan"},
    {"model": "Honda City Aspire (Used 2020)", "price": 3950000, "condition": "Used", "fuel_type": "Petrol", "seats": 5, "trunk_size": "Average", "type": "Sedan"},
    {"model": "Toyota Corolla Altis Grande (Used 2018)", "price": 4800000, "condition": "Used", "fuel_type": "Petrol", "seats": 5, "trunk_size": "Average", "type": "Sedan"},
    {"model": "MG ZS 1.5L", "price": 5500000, "condition": "New", "fuel_type": "Petrol", "seats": 5, "trunk_size": "Average", "type": "Crossover"},
    {"model": "BAIC BJ-40 Plus", "price": 5800000, "condition": "New", "fuel_type": "Diesel", "seats": 5, "trunk_size": "Average", "type": "SUV"},
    {"model": "Honda Vezel (Used 2018)", "price": 4500000, "condition": "Used", "fuel_type": "Hybrid", "seats": 5, "trunk_size": "Average", "type": "Crossover"},
    {"model": "Toyota Prius (Used 2017)", "price": 5000000, "condition": "Used", "fuel_type": "Hybrid", "seats": 5, "trunk_size": "Average", "type": "Sedan"},
    {"model": "Nissan Juke (Used 2015)", "price": 3200000, "condition": "Used", "fuel_type": "Petrol", "seats": 5, "trunk_size": "Limited", "type": "Crossover"},
    {"model": "DFSK Glory 580 (New)", "price": 5400000, "condition": "New", "fuel_type": "Petrol", "seats": 7, "trunk_size": "Average", "type": "SUV"},
    {"model": "Toyota Rush (New)", "price": 5600000, "condition": "New", "fuel_type": "Petrol", "seats": 7, "trunk_size": "Limited", "type": "MPV"},
    {"model": "Honda BR-V (New)", "price": 5100000, "condition": "New", "fuel_type": "Petrol", "seats": 7, "trunk_size": "Average", "type": "MPV"},
    {"model": "Changan Karvaan (New)", "price": 2400000, "condition": "New", "fuel_type": "Petrol", "seats": 7, "trunk_size": "Limited", "type": "Van"},

    # -------------------------------------------------------------------------------------------------------
    # 3. High-End SUVs/Sedans (New/Used: ~6.0M to 10.0M PKR)
    # -------------------------------------------------------------------------------------------------------
    {"model": "Hyundai Tucson FWD", "price": 6200000, "condition": "New", "fuel_type": "Petrol", "seats": 5, "trunk_size": "High", "type": "SUV"},
    {"model": "KIA Sportage FWD", "price": 6800000, "condition": "New", "fuel_type": "Petrol", "seats": 5, "trunk_size": "High", "type": "SUV"},
    {"model": "Honda Civic RS Turbo", "price": 8500000, "condition": "New", "fuel_type": "Petrol", "seats": 5, "trunk_size": "Average", "type": "Sedan"},
    {"model": "Toyota Corolla Cross Hybrid", "price": 9200000, "condition": "New", "fuel_type": "Hybrid", "seats": 5, "trunk_size": "Average", "type": "SUV"},
    {"model": "MG HS 1.5T", "price": 7500000, "condition": "New", "fuel_type": "Petrol", "seats": 5, "trunk_size": "High", "type": "SUV"},
    {"model": "Changan Oshan X7 Plus", "price": 6500000, "condition": "New", "fuel_type": "Petrol", "seats": 7, "trunk_size": "Average", "type": "SUV"},
    {"model": "Audi A4 (Used 2017)", "price": 8800000, "condition": "Used", "fuel_type": "Petrol", "seats": 5, "trunk_size": "Average", "type": "Sedan"},
    {"model": "Proton X70 Executive", "price": 5900000, "condition": "New", "fuel_type": "Petrol", "seats": 5, "trunk_size": "High", "type": "SUV"},
    {"model": "Toyota Fortuner (Used 2018)", "price": 8500000, "condition": "Used", "fuel_type": "Diesel", "seats": 7, "trunk_size": "High", "type": "SUV"},
    {"model": "Honda BR-V (Used 2020)", "price": 3800000, "condition": "Used", "fuel_type": "Petrol", "seats": 7, "trunk_size": "Average", "type": "MPV"},
    {"model": "KIA Sorento", "price": 9800000, "condition": "New", "fuel_type": "Petrol", "seats": 7, "trunk_size": "High", "type": "SUV"},
    {"model": "Toyota Revo V (New)", "price": 10500000, "condition": "New", "fuel_type": "Diesel", "seats": 5, "trunk_size": "High", "type": "Pickup"},
    {"model": "Suzuki Jimny (New)", "price": 6000000, "condition": "New", "fuel_type": "Petrol", "seats": 4, "trunk_size": "Limited", "type": "Off-road"},
    {"model": "Isuzu D-Max (New)", "price": 8000000, "condition": "New", "fuel_type": "Diesel", "seats": 5, "trunk_size": "High", "type": "Pickup"},
    {"model": "Haval H6 1.5T", "price": 7000000, "condition": "New", "fuel_type": "Petrol", "seats": 5, "trunk_size": "High", "type": "SUV"},
    {"model": "Sazgar BAIC X7", "price": 7200000, "condition": "New", "fuel_type": "Petrol", "seats": 5, "trunk_size": "High", "type": "SUV"},
    {"model": "Chery Tiggo 8 Pro", "price": 8200000, "condition": "New", "fuel_type": "Petrol", "seats": 7, "trunk_size": "High", "type": "SUV"},
    {"model": "Toyota Hilux Revo (Used 2019)", "price": 6500000, "condition": "Used", "fuel_type": "Diesel", "seats": 5, "trunk_size": "High", "type": "Pickup"},
    
    # -------------------------------------------------------------------------------------------------------
    # 4. Luxury/Premium (New/Used: >10M PKR)
    # -------------------------------------------------------------------------------------------------------
    {"model": "Porsche Cayenne", "price": 30000000, "condition": "New", "fuel_type": "Petrol", "seats": 5, "trunk_size": "High", "type": "SUV"},
    {"model": "Mercedes C-Class (Used 2019)", "price": 18000000, "condition": "Used", "fuel_type": "Petrol", "seats": 5, "trunk_size": "Average", "type": "Sedan"},
    {"model": "Toyota Land Cruiser ZX (New)", "price": 45000000, "condition": "New", "fuel_type": "Diesel", "seats": 7, "trunk_size": "High", "type": "SUV"},
    {"model": "Audi Q7 (Used 2017)", "price": 21000000, "condition": "Used", "fuel_type": "Diesel", "seats": 7, "trunk_size": "High", "type": "SUV"},
    {"model": "Honda CR-V Hybrid (New)", "price": 14000000, "condition": "New", "fuel_type": "Hybrid", "seats": 5, "trunk_size": "High", "type": "SUV"},
    {"model": "Toyota Land Cruiser Prado (Used 2012)", "price": 13500000, "condition": "Used", "fuel_type": "Diesel", "seats": 7, "trunk_size": "High", "type": "SUV"},
    {"model": "BMW 3 Series (Used 2016)", "price": 11000000, "condition": "Used", "fuel_type": "Petrol", "seats": 5, "trunk_size": "Average", "type": "Sedan"},
    {"model": "BMW X1 (Used 2018)", "price": 9500000, "condition": "Used", "fuel_type": "Diesel", "seats": 5, "trunk_size": "Average", "type": "SUV"},
    {"model": "Mercedes E-Class (Used 2015)", "price": 12000000, "condition": "Used", "fuel_type": "Petrol", "seats": 5, "trunk_size": "Average", "type": "Sedan"},

]

# --- 4. Sidebar Content ---
with st.sidebar:
    st.markdown("<h2 style='color: #D4AF37;'>CONSULTANT</h2>", unsafe_allow_html=True)
    
    min_p = st.number_input("Min Budget (PKR)", value=None, placeholder="e.g. 500000")
    max_p = st.number_input("Max Budget (PKR)", value=None, placeholder="e.g. 5000000")
    
    final_min = min_p if min_p is not None else 0
    final_max = max_p if max_p is not None else 999999999

    st.divider()
    
    cond = st.radio("Vehicle Condition", ["New", "Used"], horizontal=True)
    fuel = st.selectbox("Fuel Propulsion", ["Petrol", "Diesel", "Hybrid"])
    usage = st.selectbox("Primary Mission", ["Daily City Commuting", "Family Trips"])
    
    st.write("")
    search_btn = st.button("⚜️ FIND ELITE MATCHES")

# --- 5. Main Content Area ---
st.markdown('<h1 class="royal-header">PAK-CAR ELITE</h1>', unsafe_allow_html=True)

if search_btn:
    filtered = [c for c in CAR_CATALOG if final_min <= c['price'] <= final_max and c['condition'].lower() == cond.lower()]
    
    scored = []
    for car in filtered:
        score = 0
        if usage == "Daily City Commuting" and car['type'] in ['Hatchback', 'Sedan']: score += 60
        elif usage == "Family Trips" and car['seats'] >= 7: score += 60
        if car['fuel_type'].lower() == fuel.lower(): score += 40
        scored.append({**car, "match_score": score})
    
    results = sorted(scored, key=lambda x: x['match_score'], reverse=True)

    if not results:
        st.error("No matches found. Please adjust your criteria.")
    else:
        for car in results[:5]:
            st.markdown(f"""
                <div class="car-card">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <div>
                            <span style="font-size: 26px; color: #D4AF37; font-weight: bold;">{car['model']}</span><br>
                            <span style="color: #ffffff; font-size: 18px;">Price: <b>PKR {car['price']:,}</b></span><br>
                            <p style="color: #aaa; margin-top: 5px;">Type: {car['type']} | Fuel: {car['fuel_type']} | Seats: {car['seats']}</p>
                        </div>
                        <div class="badge">{car['match_score']}% MATCH</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
else:
    st.write("---")
    st.markdown("""
        <div style="text-align: center; padding: 40px;">
            <h3 style="color: #D4AF37;">Welcome to Elite Consulting</h3>
            <p style="color: #888;">Configure your requirements in the sidebar to begin.</p>
        </div>
    """, unsafe_allow_html=True)