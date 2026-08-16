import streamlit as st

# ---------------------------------------------------------
# Page Config & Custom Styling
# ---------------------------------------------------------
st.set_page_config(
    page_title="NexaBio Solutions | Your Link to What's Next",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling components matching NexaBio branding
st.markdown("""
    <style>
    /* Global Styles */
    .stApp {
        background-color: #f8fafc;
    }
    
    /* Title & Slogan styling */
    .main-title {
        color: #0d2040;
        font-size: 2.8rem;
        font-weight: 800;
        margin-bottom: 0px;
    }
    .slogan {
        color: #008080;
        font-size: 1.3rem;
        font-style: italic;
        font-weight: 500;
        margin-bottom: 25px;
    }
    
    /* Team Card Styling */
    .team-card {
        background-color: #ffffff;
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        border: 1px solid #e2e8f0;
        margin-bottom: 20px;
    }
    .team-card img {
        border-radius: 50%;
        width: 110px;
        height: 110px;
        object-fit: cover;
        margin-bottom: 12px;
        border: 3px solid #008080;
    }
    .team-name {
        color: #0d2040;
        font-weight: 700;
        font-size: 1.1rem;
        margin-bottom: 2px;
    }
    .team-role {
        color: #64748b;
        font-size: 0.9rem;
    }

    /* Portfolio Vendor Cards */
    .vendor-card {
        background-color: #ffffff;
        padding: 24px;
        border-radius: 10px;
        border-left: 5px solid #008080;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_syntax_hide=True)

# ---------------------------------------------------------
# Sidebar Navigation & Header
# ---------------------------------------------------------
with st.sidebar:
    # Attempt to load local logo file if available
    try:
        st.image("logo.png", use_container_width=True)
    except Exception:
        st.title("🧬 NexaBio Solutions")
    
    st.markdown("---")
    menu = st.radio(
        "Navigate To:",
        ["Home & About Us", "Meet The Team", "Vendor Portfolio", "Contact Us"]
    )
    st.markdown("---")
    st.caption("📍 Headquarters: Cairo, Egypt")
    st.caption("🌍 Coverage: MENA Region")
    st.caption("🗓️ Founded: 2017")

# Header Section
st.markdown('<p class="main-title">NexaBio Solutions</p>', unsafe_allow_html=True)
st.markdown('<p class="slogan">"Your Link to What\'s Next"</p>', unsafe_allow_html=True)

# ---------------------------------------------------------
# Page 1: Home & About Us
# ---------------------------------------------------------
if menu == "Home & About Us":
    st.header("About NexaBio Solutions")
    st.write(
        "Established in 2017 in Cairo, Egypt, **NexaBio Solutions** is a leading visionary distributor "
        "of cutting-edge medical and life science devices across the MENA region. We connect healthcare "
        "and research institutions with world-class technologies that drive precision diagnostics and therapeutic innovations."
    )
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🎯 Our Mission")
        st.info(
            "To empower research institutes, laboratories, and clinical facilities across the MENA region "
            "by providing seamless access to the world's most advanced biotechnology and medical solutions."
        )
        
        st.subheader("🏢 Regional Branches")
        st.markdown("""
        * **Egypt (HQ):** Cairo — Main Operations & Technical Service Center
        * **UAE:** Dubai Hub — Regional Distribution & Logistics
        * **Saudi Arabia:** Riyadh Office — Sales & Clinical Support
        """)

    with col2:
        st.subheader("👁️ Our Vision")
        st.success(
            "To be the premier partner for transformative medical technology in the Middle East & North Africa, "
            "bridging the gap between revolutionary global innovations and local healthcare advancements."
        )
        
        st.subheader("📅 Events & Exhibitions")
        st.markdown("""
        * **MedLab Middle East 2026** | Dubai, UAE — *Booth Showcase*
        * **Cairo BioTech Summit 2026** | Cairo, Egypt — *Keynote & Product Demo*
        * **MENA Genomics Conference 2025** | Riyadh, KSA — *Workshop Host*
        """)

# ---------------------------------------------------------
# Page 2: Meet The Team
# ---------------------------------------------------------
elif menu == "Meet The Team":
    st.header("Meet Our Core Team")
    st.write("The visionary experts leading NexaBio Solutions towards innovative healthcare transformation.")
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Team members data
    team = [
        {"name": "Dr. Ahmed Hassan", "role": "Chief Executive Officer", "img": "https://raw.githubusercontent.com/streamlit/streamlit/main/docs/static/favicon.png"},
        {"name": "Sarah Mansour", "role": "Head of Product Strategy", "img": "https://raw.githubusercontent.com/streamlit/streamlit/main/docs/static/favicon.png"},
        {"name": "Michael Reed", "role": "Lead Technical Specialist", "img": "https://raw.githubusercontent.com/streamlit/streamlit/main/docs/static/favicon.png"},
        {"name": "Nour El-Din", "role": "MENA Regional Operations Lead", "img": "https://raw.githubusercontent.com/streamlit/streamlit/main/docs/static/favicon.png"}
    ]
    
    cols = st.columns(len(team))
    for idx, member in enumerate(team):
        with cols[idx]:
            st.markdown(f"""
                <div class="team-card">
                    <img src="{member['img']}">
                    <div class="team-name">{member['name']}</div>
                    <div class="team-role">{member['role']}</div>
                </div>
            """, unsafe_allow_html=True)

# ---------------------------------------------------------
# Page 3: Vendor Portfolio
# ---------------------------------------------------------
elif menu == "Vendor Portfolio":
    st.header("Our Principal Partners")
    st.write("We partner with world-renowned biotechnology innovators to bring high-throughput and state-of-the-art platforms to the MENA market.")
    st.markdown("---")
    
    vendors = [
        {
            "name": "Illumina",
            "category": "Next-Generation Sequencing (NGS)",
            "desc": "Global leader in DNA sequencing and array-based technologies, serving customers in academic, government, pharmaceutical, biotechnology, and clinical settings."
        },
        {
            "name": "Quantum-Si",
            "category": "Next-Generation Protein Sequencing",
            "desc": "Pioneering single-molecule protein sequencing platform to democratize proteomics and accelerate biological discoveries."
        },
        {
            "name": "Bio-Rad Laboratories",
            "category": "Life Science Research & Clinical Diagnostics",
            "desc": "Leading global provider of life science research instruments, digital PCR systems, and clinical diagnostic products."
        },
        {
            "name": "Takara Bio",
            "category": "Reagents & Molecular Biology Technologies",
            "desc": "Specialists in gene therapy, stem cell research, enzyme technologies, and high-performance nucleic acid extraction kits."
        }
    ]
    
    for v in vendors:
        st.markdown(f"""
            <div class="vendor-card">
                <h3 style="color: #0d2040; margin-top:0;">{v['name']}</h3>
                <p><strong>Category:</strong> <span style="color: #008080;">{v['category']}</span></p>
                <p>{v['desc']}</p>
            </div>
        """, unsafe_allow_html=True)

# ---------------------------------------------------------
# Page 4: Contact Us
# ---------------------------------------------------------
elif menu == "Contact Us":
    st.header("Get In Touch")
    st.write("Connect with our sales, technical support, or regional distribution teams.")
    
    col_a, col_b = st.columns([1, 1])
    
    with col_a:
        st.subheader("📍 Contact Details")
        st.write("**Headquarters:** New Cairo, Cairo, Egypt")
        st.write("**Phone:** +20 2 1234 5678")
        st.write("**Email:** info@nexabio.com")
        st.write("**Working Hours:** Sun - Thu: 9:00 AM - 5:00 PM (EET)")
        
    with col_b:
        st.subheader("✉️ Send us a Message")
        with st.form("contact_form"):
            name = st.text_input("Full Name")
            email = st.text_input("Email Address")
            institution = st.text_input("Organization / Institution")
            vendor_interest = st.selectbox("Product Line Interest", ["General Inquiry", "Illumina", "Quantum-Si", "Bio-Rad", "Takara"])
            message = st.text_area("Message")
            
            submitted = st.form_submit_button("Submit Inquiry")
            if submitted:
                st.success(f"Thank you {name}. Your inquiry regarding {vendor_interest} has been submitted successfully.")