import streamlit as st
import requests
from streamlit_lottie import st_lottie

# 1. إعدادات الصفحة
st.set_page_config(
    page_title="Bioinformatics & MD Hub",
    page_icon="🧬",
    layout="wide"
)

# إدارة حالة الانتقال بين الصفحات (Session State)
if "current_page" not in st.session_state:
    st.session_state.current_page = "Home"

def set_page(page_name):
    st.session_state.current_page = page_name

# دالة لتحميل أنيميشن Lottie
def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

dna_lottie = load_lottie_url("https://assets5.lottiefiles.com/packages/lf20_st45t8er.json")

# =============================================================================
# 🏠 1. الصفحة الرئيسية (صفحة الكروت والأيقونات)
# =============================================================================
if st.session_state.current_page == "Home":
    
    # Header الصفحة
    col_title, col_anim = st.columns([3, 1])
    with col_title:
        st.title("🧬 Bioinformatics & MD Learning Hub")
        st.write(
            "Welcome to your interactive platform. Choose a course or a tool below to start learning!"
        )
    with col_anim:
        if dna_lottie:
            st_lottie(dna_lottie, height=150, key="home_dna")

    st.divider()
    st.subheader("📚 Available Courses & Modules")

    # الصف الأول من الكروت (عرض 3 كروت بجانب بعضهم)
    col1, col2, col3 = st.columns(3)

    with col1:
        with st.container(border=True):
            st.markdown("### 🧬 3D Protein Viewer")
            st.write("Explore interactive 3D protein structures (PDB format) in real-time.")
            st.button("Open Viewer ➔", on_click=set_page, args=("Viewer",), use_container_width=True)

    with col2:
        with st.container(border=True):
            st.markdown("### 💻 Lesson 1: Intro to MD")
            st.write("Learn the fundamentals of Molecular Dynamics and coding from scratch.")
            st.button("Start Lesson 1 ➔", on_click=set_page, args=("Lesson1",), use_container_width=True)

    with col3:
        with st.container(border=True):
            st.markdown("### 🧪 Lesson 2: Lennard-Jones")
            st.write("Understand gas simulations, energy minimization, and force fields.")
            st.button("Start Lesson 2 ➔", on_click=set_page, args=("Lesson2",), use_container_width=True)

    st.write("") # مسافة vertical

    # الصف الثاني من الكروت
    col4, col5, col6 = st.columns(3)

    with col4:
        with st.container(border=True):
            st.markdown("### 🎓 Lesson 3: LAMMPS Masterclass")
            st.write("A 2-hour deep dive into LAMMPS and advanced interatomic potentials.")
            st.button("Start Lesson 3 ➔", on_click=set_page, args=("Lesson3",), use_container_width=True)

    with col5:
        with st.container(border=True):
            st.markdown("### 📄 Resource Downloads")
            st.write("Access Python scripts, sample PDB files, and course slides.")
            st.button("View Downloads ➔", on_click=set_page, args=("Downloads",), use_container_width=True)

    with col6:
        with st.container(border=True):
            st.markdown("### 🧠 Practice Quizzes")
            st.write("Test your knowledge with cumulative multiple-choice questions.")
            st.button("Start Quiz ➔", on_click=set_page, args=("Quiz",), use_container_width=True)

# =============================================================================
# 🧬 2. صفحة الـ 3D Viewer
# =============================================================================
elif st.session_state.current_page == "Viewer":
    st.button("⬅️ Back to Home", on_click=set_page, args=("Home",))
    st.title("🧪 Interactive 3D Protein Viewer")
    
    import streamlit.components.v1 as components
    pdb_id = "1AINS"
    html_code = f"""
    <script src="https://3Dmol.org/build/3Dmol-min.js"></script>
    <div id="container" style="width: 100%; height: 450px; position: relative;"></div>
    <script>
      let viewer = $3Dmol.createViewer(document.getElementById('container'), {{backgroundColor: 'white'}});
      $3Dmol.download("pdb:{pdb_id}", viewer, {{}}, function() {{
        viewer.setStyle({{}}, {{cartoon: {{color: 'spectrum'}}}});
        viewer.zoomTo();
        viewer.render();
        viewer.spin('y', 1);
      }});
    </script>
    """
    components.html(html_code, height=470)

# =============================================================================
# 💻 3. صفحة الدرس الأول
# =============================================================================
elif st.session_state.current_page == "Lesson1":
    st.button("⬅️ Back to Home", on_click=set_page, args=("Home",))
    st.title("💻 Lesson 1: Introduction to MD & Coding from Scratch")
    
    st.video("https://www.youtube.com/watch?v=ChQbBqndwIA")
    
    st.subheader("📌 Lesson Overview")
    st.write("Learn Newton's equations of motion and how force fields are structured.")
    
    st.download_button("📄 Download Notes (PDF)", data="Sample notes", file_name="Lesson1.pdf")

# =============================================================================
# 🧪 4. صفحة الدرس الثاني
# =============================================================================
elif st.session_state.current_page == "Lesson2":
    st.button("⬅️ Back to Home", on_click=set_page, args=("Home",))
    st.title("🧪 Lesson 2: Lennard-Jones Gas Simulation")
    
    st.video("https://www.youtube.com/watch?v=2Briqk1u44U")
    
    if st.button("Run Simulation Step"):
        st.snow()
        st.success("Simulation calculated successfully!")

# =============================================================================
# 🎓 5. باقي الصفحات الفرعية
# =============================================================================
elif st.session_state.current_page == "Lesson3":
    st.button("⬅️ Back to Home", on_click=set_page, args=("Home",))
    st.title("🎓 Lesson 3: LAMMPS Masterclass")
    st.video("https://www.youtube.com/watch?v=fmQpiS9kI0A")

elif st.session_state.current_page == "Downloads":
    st.button("⬅️ Back to Home", on_click=set_page, args=("Home",))
    st.title("📄 Course Resources & Downloads")
    st.write("Download all repository scripts and data files below.")

elif st.session_state.current_page == "Quiz":
    st.button("⬅️ Back to Home", on_click=set_page, args=("Home",))
    st.title("🧠 Cumulative Practice Quiz")
    st.write("Quiz content goes here.")
