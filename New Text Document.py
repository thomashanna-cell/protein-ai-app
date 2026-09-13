import streamlit as st

# Set page layout and title
st.set_page_config(
    page_title="Molecular Dynamics Course Platform",
    page_icon="🎓",
    layout="wide"
)

# Main Title
st.title("🎓 Online Learning Portal")

# Sidebar for Navigation
st.sidebar.title("📚 Course Navigation")
selected_lesson = st.sidebar.radio(
    "Select a Lesson:",
    [
        "Lesson 1: Intro to Molecular Dynamics",
        "Lesson 2: System Setup & Force Fields",
        "Lesson 3: Analyzing Trajectories"
    ]
)

# Lesson 1 Content
if selected_lesson == "Lesson 1: Intro to Molecular Dynamics":
    st.header("Lesson 1: Introduction to Molecular Dynamics")
    
    # Embedded YouTube Video (Molecular Dynamics)
    video_url = "https://www.youtube.com/watch?v=ChQbBqndwIA"
    st.video(video_url)
    
    st.subheader("📌 Overview")
    st.write(
        "In this video, you will learn the fundamental concepts of Molecular Dynamics (MD) simulations, "
        "how Newton's equations of motion are solved numerically, and how particle interactions are modeled."
    )
    
    # Downloadable Resource
    st.download_button(
        label="📄 Download Lesson Notes (PDF)",
        data="Sample course summary for Lesson 1.",
        file_name="Lesson1_Notes.pdf"
    )
    
    st.divider()
    
    # Quiz Section
    st.subheader("🧠 Quick Quiz")
    answer = st.radio(
        "What fundamental equations are primarily solved in classical Molecular Dynamics?",
        ["Schrödinger Equation", "Newton's Equations of Motion", "Maxwell's Equations"]
    )
    
    if st.button("Submit Answer"):
        if answer == "Newton's Equations of Motion":
            st.success("Correct! Classic MD relies on Newton's second law (F = ma). 🎉")
        else:
            st.error("Incorrect. Try again!")

# Lesson 2 Content
elif selected_lesson == "Lesson 2: System Setup & Force Fields":
    st.header("Lesson 2: System Setup & Force Fields")
    
    st.video("https://www.youtube.com/watch?v=ChQbBqndwIA")
    
    st.subheader("📌 Overview")
    st.write("Learn how to prepare initial atomic coordinates, define boundary conditions, and select appropriate force fields.")

# Lesson 3 Content
elif selected_lesson == "Lesson 3: Analyzing Trajectories":
    st.header("Lesson 3: Analyzing Trajectories")
    
    st.video("https://www.youtube.com/watch?v=ChQbBqndwIA")
    
    st.subheader("📌 Overview")
    st.write("Discover how to compute structural properties such as RMSD, RMSF, and Radial Distribution Functions (RDF).")
