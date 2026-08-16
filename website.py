import streamlit as st
import os

# ---------------------------------------------------------
# Page Config & Custom Styling
# ---------------------------------------------------------
st.set_page_config(
    page_title="NexaBio Solutions | Your Link to What's Next",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for primary colors (Navy & Teal Palette)
st.markdown("""
    <style>
    /* Palette definition */
    :root {
        --navy-dark: #0A1128;
        --navy-main: #1C2541;
        --teal-main: #2A9D8F;
        --teal-light: #52B788;
        --bg-light: #F8FAF9;
    }

    .stApp {
        background-color: var(--bg-light);
    }
    
    /* Main Headers */
    .main-title {
        color: #0A1128;
        font-size: 2.8rem;
        font-weight: 800;
        margin-bottom: 0px;
    }
    .slogan {
        color: #2A9D8F;
        font-size: 1.3rem;
        font-style: italic;
        font-weight: 600;
        margin-bottom: 25px;
    }
    
    /* Cards (Vision / Mission) */
    .info-box {
        background-color: #FFFFFF;
        border-radius: 10px;
        padding: 22px;
        border-left: 5px solid #2A9D8F;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        margin-bottom: 20px;
    }
    .info-box-title {
        color: #0A1128;
        font-weight: 700;
        font-size: 1.2rem;
        margin-bottom: 8px;
    }
    
    /* Team Member Border Cards */
    .team-box {
        border: 2px solid #2A9D8F;
        border-radius: 15px;
        padding: 15px;
        text-align: center;
        background-color: #FFFFFF;
        box-shadow: 0 4px 8px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }
    .team-box:hover {
        border-color: #0A1128;
        box-shadow: 0 6px 12px rgba(0,0,0,0.1);
        transition: all 0.3s ease-in-out;
    }

    /* Timeline Section */
    .timeline-item {
        background: #FFFFFF;
        padding: 15px 20px;
        border-radius: 8px;
        border-left: 4px solid #0A1128;
        margin-bottom: 12px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.04);
    }
    .timeline-year {
        color: #2A9D8F;
        font-weight: 800;
        font-size: 1.1rem;
    }

    /* Vendor Card Styling */
    .vendor-card {
        background-color: #FFFFFF;
        padding: 22px;
        border-radius: 10px;
        border-top: 4px solid #2A9D8F;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Sidebar Navigation
# ---------------------------------------------------------
with st.sidebar:
    if os.path.exists("logo.png"):
        st.image("logo.png", use_container_width=True)
    else:
        st.title("🧬 NexaBio Solutions")
    
    st.markdown("---")
    menu = st.sidebar.radio(
        "Navigation",
        ["About Us", "Meet The Team", "Vendor Portfolio", "Contact Us"]
    )
    st.markdown("---")
    st.caption("📍 **Headquarters:** Cairo, Egypt")
    st.caption("🌍 **Coverage:** MENA Region")
    st.caption("🗓️ **Founded:** 2017")

# Header Title Block
st.markdown('<p class="main-title">NexaBio Solutions</p>', unsafe_allow_html=True)
st.markdown('<p class="slogan">"Your Link to What\'s Next"</p>', unsafe_allow_html=True)

# ---------------------------------------------------------
# Page 1: About Us (Mission, Vision, Our Reach)
# ---------------------------------------------------------
if menu == "About Us":
    st.header("About NexaBio Solutions")
    st.write(
        "Founded in 2017 in Cairo, Egypt, **NexaBio Solutions** is a distributor "
        "of medical devices and life science technologies dedicated to serving the MENA region."
    )
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
            <div class="info-box">
                <div class="info-box-title">👁️ Vision</div>
                To become a trusted link to the future of healthcare, connecting the MENA region 
                with innovative technologies that advance scientific discovery, improve diagnostic capabilities, 
                and enable better healthcare outcomes.
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div class="info-box">
                <div class="info-box-title">🎯 Mission</div>
                To connect healthcare providers, laboratories, and research institutions with trusted medical 
                and life-science technologies, delivering reliable products, responsive support, and practical expertise 
                throughout the customer journey. We are committed to building strong partnerships with global technology 
                innovators while making advanced solutions more accessible to the markets we serve.
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("🌍 Our Reach & Expansion Timeline")
    st.write(
        "Our regional network enables us to support healthcare and life-science institutions "
        "across key MENA markets while maintaining close relationships with both customers and technology partners."
    )

    reach_data = [
        {"year": "2017 | Cairo, Egypt", "desc": "Headquarters and initial operations"},
        {"year": "2020 | Riyadh, Saudi Arabia", "desc": "First regional expansion into the GCC"},
        {"year": "2022 | Dubai, UAE", "desc": "Regional commercial and logistics hub"},
        {"year": "2024 | Amman, Jordan", "desc": "Expansion into Levant markets"},
        {"year": "2026 | MENA Network", "desc": "Distribution coverage through strategic partners across North Africa, GCC, and Levant"}
    ]

    for item in reach_data:
        st.markdown(f"""
            <div class="timeline-item">
                <span class="timeline-year">{item['year']}</span><br>
                <span>{item['desc']}</span>
            </div>
        """, unsafe_allow_html=True)

# ---------------------------------------------------------
# Page 2: Meet The Team
# ---------------------------------------------------------
elif menu == "Meet The Team":
    st.header("Meet Our Core Team")
    st.write("The professionals driving innovation and operational excellence across the MENA region.")
    st.markdown("<br>", unsafe_allow_html=True)
    
    team_members = [
        {"name": "Mariam Morgan", "role": "Business Development Specialist", "img": "team_mariam.jpg"},
        {"name": "Rahma Abdelslam", "role": "Compliance Specialist", "img": "team_rahma.jpg"},
        {"name": "Abdelrahman Mohamed", "role": "Product Specialist", "img": "team_abdelrahman.jpg"},
        {"name": "Kareem Elsayed", "role": "Application Support Specialist", "img": "team_kareem.jpg"},
        {"name": "Nour Hisham", "role": "Application Support Specialist", "img": "team_nour.jpg"},
        {"name": "Youssef Ahmed", "role": "Product Specialist", "img": "team_youssef.jpg"}
    ]
    
    # الصف الأول (3 أعضاء)
    row1_cols = st.columns(3)
    for idx in range(3):
        member = team_members[idx]
        with row1_cols[idx]:
            img_path = member["img"] if os.path.exists(member["img"]) else "https://via.placeholder.com/300x350.png?text=" + member['name'].replace(' ', '+')
            
            st.markdown(f"""
                <div class="team-box">
                    <img src="{img_path}" style="width:100%; border-radius: 10px; margin-bottom: 12px;">
                    <div style="color: #0A1128; font-weight: 700; font-size: 1.1rem;">{member['name']}</div>
                    <div style="color: #2A9D8F; font-size: 0.9rem; font-weight: 600;">{member['role']}</div>
                </div>
            """, unsafe_allow_html=True)

    # الصف الثاني (3 أعضاء)
    row2_cols = st.columns(3)
    for idx in range(3, 6):
        member = team_members[idx]
        with row2_cols[idx - 3]:
            img_path = member["img"] if os.path.exists(member["img"]) else "https://via.placeholder.com/300x350.png?text=" + member['name'].replace(' ', '+')
            
            st.markdown(f"""
                <div class="team-box">
                    <img src="{img_path}" style="width:100%; border-radius: 10px; margin-bottom: 12px;">
                    <div style="color: #0A1128; font-weight: 700; font-size: 1.1rem;">{member['name']}</div>
                    <div style="color: #2A9D8F; font-size: 0.9rem; font-weight: 600;">{member['role']}</div>
                </div>
            """, unsafe_allow_html=True)

# ---------------------------------------------------------
# Page 3: Vendor Portfolio
# ---------------------------------------------------------
elif menu == "Vendor Portfolio":
    st.header("Vendor Portfolio")
    st.write("Explore our strategic partnerships and healthcare solutions.")

# ---------------------------------------------------------
# Page 4: Contact Us
# ---------------------------------------------------------
elif menu == "Contact Us":
    st.header("Contact Us")
    st.write("Get in touch with our team.")
