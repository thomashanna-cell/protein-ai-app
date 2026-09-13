import streamlit as st

# Set page layout and title
st.set_page_config(
    page_title="Bioinformatics & MD Platform",
    page_icon="🧬",
    layout="wide"
)

# Sidebar for Navigation
st.sidebar.title("📌 Navigation")
selected_page = st.sidebar.radio(
    "Go to:",
    [
        "🏠 Home / Platform Intro",
        "Lesson 1: Intro & Coding MD from Scratch",
        "Lesson 2: Lennard-Jones Gas & Energy Minimization",
        "Lesson 3: Complete 2-Hour MD & LAMMPS Masterclass"
    ]
)

# -----------------------------------------------------------------------------
# 🏠 HOME / PLATFORM INTRO
# -----------------------------------------------------------------------------
if selected_page == "🏠 Home / Platform Intro":
    st.title("🧬 Welcome to the Bioinformatics & Computational Biology Hub")
    st.write(
        "Your specialized platform for interactive video courses, computational workflows, "
        "and practical training in Bioinformatics and Molecular Dynamics (MD) simulations."
    )
    
    st.divider()
    
    # Platform Highlights
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("📺 Video Courses")
        st.write("Structured video lessons ranging from fundamental concepts to advanced computational workflows.")
        
    with col2:
        st.subheader("💻 Hands-on Learning")
        st.write("Complete Python scripts, LAMMPS input files, and real-world datasets ready for download.")
        
    with col3:
        st.subheader("🧠 Interactive Quizzes")
        st.write("Test your knowledge after each lesson with instant self-assessment quizzes.")

    st.divider()

    # Introduction Video / Demo
    st.subheader("🎬 Platform Overview & Welcome Video")
    intro_video_url = "https://www.youtube.com/watch?v=ChQbBqndwIA"
    st.video(intro_video_url)

    st.info("👈 Select any lesson from the **Sidebar Menu** on the left to start learning!")

# -----------------------------------------------------------------------------
# LESSON 1
# -----------------------------------------------------------------------------
elif selected_page == "Lesson 1: Intro & Coding MD from Scratch":
    st.title("🎓 Lesson 1: Introduction to MD & Coding from Scratch")
    
    video_url_1 = "https://www.youtube.com/watch?v=ChQbBqndwIA"
    st.video(video_url_1)
    
    st.subheader("📌 Overview")
    st.write(
        "In this video, you will learn the fundamental concepts of Molecular Dynamics (MD) simulations, "
        "how Newton's equations of motion are solved numerically, and how particle interactions are modeled."
    )
    
    st.download_button(
        label="📄 Download Lesson 1 Notes (PDF)",
        data="Sample summary for Lesson 1: Newton equations, periodic boundary conditions, and Lennard-Jones potential.",
        file_name="Lesson1_Notes.pdf"
    )
    
    st.divider()
    
    # Quiz Section 1
    st.subheader("🧠 Quick Quiz")
    answer_1 = st.radio(
        "What fundamental equations are primarily solved in classical Molecular Dynamics?",
        ["Schrödinger Equation", "Newton's Equations of Motion", "Maxwell's Equations"],
        key="q1"
    )
    
    if st.button("Submit Answer", key="btn1"):
        if answer_1 == "Newton's Equations of Motion":
            st.success("Correct! Classical MD relies on Newton's second law (F = ma). 🎉")
        else:
            st.error("Incorrect. Try again!")

# -----------------------------------------------------------------------------
# LESSON 2
# -----------------------------------------------------------------------------
elif selected_page == "Lesson 2: Lennard-Jones Gas & Energy Minimization":
    st.title("🎓 Lesson 2: Lennard-Jones Gas & Energy Minimization")
    
    video_url_2 = "https://www.youtube.com/watch?v=2Briqk1u44U"
    st.video(video_url_2)
    
    st.subheader("📌 Overview")
    st.write(
        "This step-by-step tutorial covers system initialization, energy minimization, "
        "integration of motion equations, and trajectory visualization."
    )
    
    st.download_button(
        label="📄 Download Lesson 2 Notes (PDF)",
        data="Sample summary for Lesson 2: Lennard-Jones potential and NVT Ensemble setup.",
        file_name="Lesson2_Notes.pdf"
    )
    
    st.divider()
    
    # Quiz Section 2
    st.subheader("🧠 Quick Quiz")
    answer_2 = st.radio(
        "Which ensemble keeps the number of particles (N), volume (V), and temperature (T) constant?",
        ["NVE Ensemble", "NVT Ensemble", "NPT Ensemble"],
        key="q2"
    )
    
    if st.button("Submit Answer", key="btn2"):
        if answer_2 == "NVT Ensemble":
            st.success("Correct! NVT stands for constant Number of particles, Volume, and Temperature. 🎉")
        else:
            st.error("Incorrect. Try again!")

# -----------------------------------------------------------------------------
# LESSON 3
# -----------------------------------------------------------------------------
elif selected_page == "Lesson 3: Complete 2-Hour MD & LAMMPS Masterclass":
    st.title("🎓 Lesson 3: Complete 2-Hour MD & LAMMPS Masterclass")
    
    video_url_3 = "https://www.youtube.com/watch?v=fmQpiS9kI0A"
    st.video(video_url_3)
    
    st.subheader("📌 Overview")
    st.write(
        "A comprehensive deep dive into Molecular Dynamics, force fields, pair potentials (EAM, Tersoff), "
        "and running simulations using LAMMPS software."
    )
    
    st.download_button(
        label="📄 Download Lesson 3 Script & Guide (PDF)",
        data="Sample summary for Lesson 3: Interatomic potentials, boundary conditions, and software workflows.",
        file_name="Lesson3_Notes.pdf"
    )
    
    st.divider()
    
    # Quiz Section 3
    st.subheader("🧠 Quick Quiz")
    answer_3 = st.radio(
        "Which of the following is widely used for modeling metallic systems?",
        ["EAM (Embedded Atom Method) Potentials", "Simple Coulomb Potential", "Ideal Gas Law"],
        key="q3"
    )
    
    if st.button("Submit Answer", key="btn3"):
        if answer_3 == "EAM (Embedded Atom Method) Potentials":
            st.success("Correct! EAM potentials are specifically designed for metallic systems. 🎉")
        else:
            st.error("Incorrect. Try again!")
