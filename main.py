import streamlit as st

# --- 1. Page Config (Sidebar Force Fix) ---
st.set_page_config(
    page_title="PakCar Elite Edition", 
    page_icon="⚖️", 
    layout="wide", 
    initial_sidebar_state="expanded"  # Sidebar hamesha khula nazar aayega
)

# --- 2. THE ULTIMATE GOLD THEME CSS ---
st.markdown("""
    <style>
    header, footer {visibility: hidden;}
    
    /* Force Sidebar Visibility even on mobile */
    [data-testid="stSidebar"][aria-expanded="false"] {
        margin-left: 0px !important;
    }

    .stApp {
        background: radial-gradient(circle, #1a1a1a 0%, #050505 100%);
        color: #ffffff;
    }

    /* --- RADIO BUTTON GOLD FIX --- */
    :root { --primary-color: #D4AF37 !important; }

    div[data-baseweb="radio__dot"] {
        border: 2px solid #555 !important;
        background-color: #222 !important;
    }

    input[checked] + div[data-baseweb="radio__dot"] {
        background-color: #D4AF37 !important;
        border-color: #D4AF37 !important;
    }

    input[checked] + div[data-baseweb="radio__dot"] > div {
        background-color: #000 !important;
    }

    /* Sidebar Background & Border */
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
        transition: 0.3s;
    }

    .car-card:hover {
        border-color: #D4AF37;
        background: rgba(212, 175, 55, 0.05);
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

# --- 3. Data (Integrated 50+ Cars Catalog) ---
CAR_CATALOG = [
    # Ultra-Budget Used Cars
    {"model": "Mazda 323 (Used 1990)", "price": 550000, "condition": "Used", "fuel_type": "Petrol", "seats": 5, "trunk_size": "Average", "type": "Sedan"},
    {"model": "Hyundai Santro (Used 2007)", "price": 650000, "condition": "Used", "fuel_type": "Petrol", "seats": 5, "trunk_size": "Limited", "type": "Hatchback"},
    {"model": "Suzuki Alto (Used 2008)", "price": 750000, "condition": "Used", "fuel_type": "Petrol", "seats": 4, "trunk_size": "Limited", "type": "Hatchback"},
    {"model": "Daihatsu Cuore (Used 2010)", "price": 800000, "condition": "Used", "fuel_type": "Petrol", "seats": 4, "trunk_size": "Limited", "type": "Hatchback"},
    {"model": "Toyota Corolla (Used 1998)", "price": 950000, "condition": "Used", "fuel_type": "Petrol", "seats": 5, "trunk_size": "Average", "type": "Sedan"},
    {"model": "Mitsubishi Lancer (Used 2006)", "price": 1000000, "condition": "Used", "fuel_type": "Petrol", "seats": 5, "trunk_size": "Average", "type": "Sedan"},
    {"model": "Suzuki Mehran VXR (Used 2017)", "price": 1100000, "condition": "Used", "fuel_type": "Petrol", "seats": 4, "trunk_size": "Limited", "type": "Hatchback"},
    {"model": "Honda Civic VTi (Used 2003)", "price": 1150000, "condition": "Used", "fuel_type": "Petrol", "seats": 5, "trunk_size": "Average", "type": "Sedan"},
    {"model": "Mitsubishi Pajero (Used 1995)", "price": 1200000, "condition": "Used", "fuel_type": "Diesel", "seats": 5, "trunk_size": "High", "type": "SUV"},
    {"model": "Suzuki Cultus VXR (Used 2012)", "price": 1250000, "condition": "Used", "fuel_type": "Petrol", "seats": 5, "trunk_size": "Limited", "type": "Hatchback"},
    {"model": "Suzuki Bolan (Used 2015)", "price": 1300000, "condition": "Used", "fuel_type": "Petrol", "seats": 7, "trunk_size": "Limited", "type": "Van"},
    {"model": "Toyota Corolla XLi (Used 2005)", "price": 1400000, "condition": "Used", "fuel_type": "Petrol", "seats": 5, "trunk_size": "Average", "type": "Sedan"},
    {"model": "Toyota Vitz (Used 2008)", "price": 1450000, "condition": "Used", "fuel_type": "Petrol", "seats": 5, "trunk_size": "Average", "type": "Hatchback"},
    {"model": "Toyota Prius (Used 2006)", "price": 1500000, "condition": "Used", "fuel_type": "Hybrid", "seats": 5, "trunk_size": "Average", "type": "Sedan"},
    # Budget Hatchbacks
    {"model": "Suzuki Alto VXL", "price": 2700000, "condition": "New", "fuel_type": "Petrol", "seats": 4, "trunk_size": "Limited", "type": "Hatchback"},
    {"model": "Suzuki Cultus VXR", "price": 3200000, "condition": "New", "fuel_type": "Petrol", "seats": 5, "trunk_size": "Limited", "type": "Hatchback"},
    {"model": "KIA Picanto AT", "price": 3500000, "condition": "New", "fuel_type": "Petrol", "seats": 5, "trunk_size": "Limited", "type": "Hatchback"},
    {"model": "Honda N-WGN (Used 2018)", "price": 2400000, "condition": "Used", "fuel_type": "Petrol", "seats": 4, "trunk_size": "Limited", "type": "Hatchback"},
    {"model": "Toyota Vitz (Used 2017)", "price": 2900000, "condition": "Used", "fuel_type": "Petrol", "seats": 5, "trunk_size": "Average", "type": "Hatchback"},
    {"model": "Suzuki Swift GLX (New)", "price": 4000000, "condition": "New", "fuel_type": "Petrol", "seats": 5, "trunk_size": "Average", "type": "Hatchback"},
    # Mid-Range Sedans/Crossovers
    {"model": "Honda City 1.2 LS", "price": 4300000, "condition": "New", "fuel_type": "Petrol", "seats": 5, "trunk_size": "Average", "type": "Sedan"},
    {"model": "Toyota Yaris ATIV X", "price": 4700000, "condition": "New", "fuel_type": "Petrol", "seats": 5, "trunk_size": "Average", "type": "Sedan"},
    {"model": "Changan Alsvin Lumiere", "price": 4100000, "condition": "New", "fuel_type": "Petrol", "seats": 5, "trunk_size": "Average", "type": "Sedan"},
    {"model": "MG ZS 1.5L", "price": 5500000, "condition": "New", "fuel_type": "Petrol", "seats": 5, "trunk_size": "Average", "type": "Crossover"},
    {"model": "Honda Vezel (Used 2018)", "price": 4500000, "condition": "Used", "fuel_type": "Hybrid", "seats": 5, "trunk_size": "Average", "type": "Crossover"},
    {"model": "Honda BR-V (New)", "price": 5100000, "condition": "New", "fuel_type": "Petrol", "seats": 7, "trunk_size": "Average", "type": "MPV"},
    # High-End SUVs/Sedans
    {"model": "Hyundai Tucson FWD", "price": 6200000, "condition": "New", "fuel_type": "Petrol", "seats": 5, "trunk_size": "High", "type": "SUV"},
    {"model": "KIA Sportage FWD", "price": 6800000, "condition": "New", "fuel_type": "Petrol", "seats": 5, "trunk_size": "High", "type": "SUV"},
    {"model": "Toyota Fortuner (Used 2018)", "price": 8500000, "condition": "Used", "fuel_type": "Diesel", "seats": 7, "trunk_size": "High", "type": "SUV"},
    {"model": "Toyota Hilux Revo (Used 2019)", "price": 6500000, "condition": "Used", "fuel_type": "Diesel", "seats": 5, "trunk_size": "High", "type": "Pickup"},
    # Luxury/Premium
    {"model": "Toyota Land Cruiser ZX (New)", "price": 45000000, "condition": "New", "fuel_type": "Diesel", "seats": 7, "trunk_size": "High", "type": "SUV"},
    {"model": "Mercedes C-Class (Used 2019)", "price": 18000000, "condition": "Used", "fuel_type": "Petrol", "seats": 5, "trunk_size": "Average", "type": "Sedan"},
    {"model": "Porsche Cayenne", "price": 30000000, "condition": "New", "fuel_type": "Petrol", "seats": 5, "trunk_size": "High", "type": "SUV"},
]

# --- 4. Sidebar Content ---
with st.sidebar:
    st.markdown("<h2 style='color: #D4AF37;'>CONSULTANT</h2>", unsafe_allow_html=True)
    
    # Input for Budget
    min_p = st.number_input("Min Budget (PKR)", value=None, placeholder="e.g. 500000")
    max_p = st.number_input("Max Budget (PKR)", value=None, placeholder="e.g. 5000000")
    
    final_min = min_p if min_p is not None else 0
    final_max = max_p if max_p is not None else 999999999

    st.divider()
    
    # Gold Styled Radio & Selectors
    cond = st.radio("Vehicle Condition", ["New", "Used"], horizontal=True)
    fuel = st.selectbox("Fuel Propulsion", ["Petrol", "Diesel", "Hybrid"])
    usage = st.selectbox("Primary Mission", ["Daily City Commuting", "Family Trips"])
    
    st.write("")
    search_btn = st.button("⚜️ FIND ELITE MATCHES")

# --- 5. Main Content Area ---
st.markdown('<h1 class="royal-header">PAK-CAR ELITE</h1>', unsafe_allow_html=True)

if search_btn:
    # Filter Logic
    filtered = [c for c in CAR_CATALOG if final_min <= c['price'] <= final_max and c['condition'].lower() == cond.lower()]
    
    scored = []
    for car in filtered:
        score = 0
        # Purpose scoring
        if usage == "Daily City Commuting" and car['type'] in ['Hatchback', 'Sedan']: score += 60
        elif usage == "Family Trips" and car['seats'] >= 7: score += 60
        # Fuel scoring
        if car['fuel_type'].lower() == fuel.lower(): score += 40
        
        scored.append({**car, "match_score": score})
    
    results = sorted(scored, key=lambda x: x['match_score'], reverse=True)

    if not results:
        st.error("No matches discovered. Please refine your elite criteria.")
    else:
        st.write(f"### Discovered {len(results)} Exclusive Matches")
        for car in results[:8]:  # Show top 8 matches
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
            <p style="color: #888;">Configure your requirements in the sidebar and initiate the selection process.</p>
        </div>
    """, unsafe_allow_html=True)
