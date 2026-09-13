import streamlit as st
import requests
from streamlit_lottie import st_lottie

# 1. Page Configuration
st.set_page_config(
    page_title="Bioinformatics & MD Hub",
    page_icon="🧬",
    layout="wide"
)

# Function to load Lottie animations from URL
def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load a free DNA/Science animation
dna_lottie = load_lottie_url("https://assets5.lottiefiles.com/packages/lf20_st45t8er.json")

# 2. Sidebar Navigation
st.sidebar.title("📌 Navigation")
selected_page = st.sidebar.radio(
    "Go to:",
    [
        "🏠 Home / Platform Intro",
        "🧬 3D Structure Viewer Demo",
        "Lesson 1: Intro to Molecular Dynamics",
        "Lesson 2: Lennard-Jones Gas Simulation"
    ]
)

# -----------------------------------------------------------------------------
# 🏠 HOME / INTRO (With Lottie Animation)
# -----------------------------------------------------------------------------
if selected_page == "🏠 Home / Platform Intro":
    col_title, col_anim = st.columns([2, 1])
    
    with col_title:
        st.title("🧬 Bioinformatics & MD Hub")
        st.write(
            "Welcome to the ultimate interactive platform for **Bioinformatics** and "
            "**Molecular Dynamics (MD)** simulations."
        )
        st.info("👈 Use the menu on the left to navigate through lessons and 3D models!")
    
    with col_anim:
        # Display smooth vector animation if available
        if dna_lottie:
            st_lottie(dna_lottie, height=200, key="dna")
        else:
            st.text("🧬 [DNA Animation]")

    st.divider()

    # Feature Grid
    c1, c2, c3 = st.columns(3)
    c1.metric(label="Video Courses", value="12+", delta="Updated")
    c2.metric(label="Interactive 3D Models", value="PDB Ready", delta="3D Viewer")
    c3.metric(label="Active Quizzes", value="Self-Paced", delta="Instant Score")

# -----------------------------------------------------------------------------
# 🧬 3D MOLECULAR VIEWER DEMO
# -----------------------------------------------------------------------------
elif selected_page == "🧬 3D Structure Viewer Demo":
    st.title("🧪 Interactive 3D Protein Viewer")
    st.write("You can embed real-time 3D interactive molecular trajectories directly into your app.")
    
    # Embedded py3Dmol structure viewer using HTML component
    import streamlit.components.v1 as components

    # Example: Render 1AINS (Insulin PDB) in 3D
    pdb_id = "1AINS"
    html_code = f"""
    <script src="https://3Dmol.org/build/3Dmol-min.js"></script>
    <div id="container" style="width: 100%; height: 400px; position: relative;"></div>
    <script>
      let viewer = $3Dmol.createViewer(document.getElementById('container'), {{backgroundColor: 'white'}});
      $3Dmol.download("pdb:{pdb_id}", viewer, {{}}, function() {{
        viewer.setStyle({{}}, {{cartoon: {{color: 'spectrum'}}}});
        viewer.zoomTo();
        viewer.render();
        viewer.spin('y', 1); // Enables continuous 3D rotation animation
      }});
    </script>
    """
    
    components.html(html_code, height=420)
    st.caption(f"Rotating 3D structure of PDB: {pdb_id}. Users can click and drag to rotate manually.")

# -----------------------------------------------------------------------------
# LESSON 1
# -----------------------------------------------------------------------------
elif selected_page == "Lesson 1: Intro to Molecular Dynamics":
    st.title("🎓 Lesson 1: Introduction to MD")
    
    st.video("https://www.youtube.com/watch?v=ChQbBqndwIA")
    
    st.subheader("🧠 Knowledge Check")
    answer = st.radio(
        "Which law forms the foundation of classical MD?",
        ["Newton's Laws of Motion", "First Law of Thermodynamics", "Boyle's Law"],
        key="q1"
    )
    
    if st.button("Submit Answer"):
        if answer == "Newton's Laws of Motion":
            st.balloons()  # Animated confetti celebration
            st.success("Correct answer! 🎉")
        else:
            st.error("Try again!")

# -----------------------------------------------------------------------------
# LESSON 2
# -----------------------------------------------------------------------------
elif selected_page == "Lesson 2: Lennard-Jones Gas Simulation":
    st.title("🎓 Lesson 2: Lennard-Jones Gas")
    
    st.video("https://www.youtube.com/watch?v=2Briqk1u44U")
    
    st.subheader("📊 Interactive Simulation Preview")
    st.write("Click below to run a simulation check with animated progress:")
    
    if st.button("Run Simulation Step"):
        progress_bar = st.progress(0)
        for i in range(100):
            progress_bar.progress(i + 1)
        st.snow()  # Cool snow animation effect
        st.success("Simulation trajectories calculated successfully!")
