import streamlit as st
import requests
from streamlit_lottie import st_lottie
import streamlit.components.v1 as components

# =============================================================================
# 1. إعدادات الصفحة الأولية
# =============================================================================
st.set_page_config(
    page_title="Bioinformatics & MD Hub",
    page_icon="🧬",
    layout="wide"
)

# قائمة أكواد التفعيل المتاحة للطلاب (تستطيع إضافة أي أرقام/أكواد تبيعها للطلاب هنا)
VALID_CODES = ["BIO-101", "MD-2026", "STUDENT-99", "PASS-8842"]

# رقم الواتساب الخاص بك لاستلام التحويلات وإرسال الأكواد (اكتب رقمك بالرمز الدولي بدون +)
WHATSAPP_NUMBER = "201000000000" 
WA_LINK = f"https://wa.me/{WHATSAPP_NUMBER}?text=السلام%20عليكم،%20أريد%20شراء%20كود%20تفعيل%20كورس%20Bioinformatics"

# إدارة التنقل بين الصفحات عبر Session State
if "current_page" not in st.session_state:
    st.session_state.current_page = "Home"

def set_page(page_name):
    st.session_state.current_page = page_name

# دالة تحميل أنيميشن Lottie
def load_lottie_url(url: str):
    try:
        r = requests.get(url)
        if r.status_code == 200:
            return r.json()
    except:
        return None

dna_lottie = load_lottie_url("https://assets5.lottiefiles.com/packages/lf20_st45t8er.json")

# =============================================================================
# 🏠 2. الصفحة الرئيسية (واجهة الكروت والأيقونات)
# =============================================================================
if st.session_state.current_page == "Home":
    
    # Header
    col_title, col_anim = st.columns([3, 1])
    with col_title:
        st.title("🧬 Bioinformatics & MD Learning Hub")
        st.write(
            "أهلاً بك في المنصة التفاعلية لكورسات البيوانفورماتكس والمحاكاة الجزيئية. اختر الكورس أو الأداة للبدء:"
        )
    with col_anim:
        if dna_lottie:
            st_lottie(dna_lottie, height=140, key="home_dna")

    st.divider()
    st.subheader("📚 Available Modules & Courses")

    # الصف الأول من الكروت
    col1, col2, col3 = st.columns(3)

    with col1:
        with st.container(border=True):
            st.markdown("### 🟢 Intro to MD `[FREE]`")
            st.write("مقدمة مجانية بالكامل في المحاكاة الجزيئية لكافة الطلاب.")
            st.button("شاهد الدرس المجاني ➔", on_click=set_page, args=("Lesson1_Free",), use_container_width=True)

    with col2:
        with st.container(border=True):
            st.markdown("### 🔒 Advanced MD `[PREMIUM]`")
            st.write("درس متقدم في غاز Lennard-Jones وحسابات الطاقة (يحتاج كود تفعيل).")
            st.button("فتح الدرس المغلق ➔", on_click=set_page, args=("Lesson2_Locked",), use_container_width=True)

    with col3:
        with st.container(border=True):
            st.markdown("### 🧬 3D Protein Viewer")
            st.write("مستعرض تفاعلي ثلاثي الأبعاد لفحص الهياكل البروتينية (PDB).")
            st.button("فتح المستعرض ➔", on_click=set_page, args=("Viewer",), use_container_width=True)

    st.write("") # مسافة فاصبة

    # الصف الثاني من الكروت
    col4, col5, col6 = st.columns(3)

    with col4:
        with st.container(border=True):
            st.markdown("### 🔒 LAMMPS Masterclass `[PREMIUM]`")
            st.write("كورس شامل مدته ساعتان في برنامج LAMMPS (يحتاج كود تفعيل).")
            st.button("فتح الكورس ➔", on_click=set_page, args=("Lesson3_Locked",), use_container_width=True)

    with col5:
        with st.container(border=True):
            st.markdown("### 📄 Resource Downloads")
            st.write("تحميل ملفات الأكواد والـ PDB والملخصات الخاصة بالكورسات.")
            st.button("عرض الملفات ➔", on_click=set_page, args=("Downloads",), use_container_width=True)

    with col6:
        with st.container(border=True):
            st.markdown("### 🧠 Practice Quiz")
            st.write("اختبار تفاعلي سريع لتقييم مستواك في المفاهيم الأساسية.")
            st.button("ابدأ الاختبار ➔", on_click=set_page, args=("Quiz",), use_container_width=True)

# =============================================================================
# 🟢 3. صفحة الدرس الأول (مجاني 100%)
# =============================================================================
elif st.session_state.current_page == "Lesson1_Free":
    st.button("⬅️ الرجوع للرئيسية", on_click=set_page, args=("Home",))
    
    st.success("🎉 هذا الدرس مجاني بالكامل!")
    st.title("💻 Lesson 1: Introduction to Molecular Dynamics")
    
    # فيديو مجاني
    st.video("https://www.youtube.com/watch?v=ChQbBqndwIA")
    
    st.subheader("📌 الشرح والمفاهيم الأساسية")
    st.write("يتناول هذا الفيديو طريقة حل معادلات نيوتن للحركة وتطبيقها على الجسيمات والدوال الخاصة بالـ Force Fields.")
    
    st.download_button("📄 تحميل ملخص الدرس (PDF)", data="ملخص الدرس الأول", file_name="Lesson1_Notes.pdf")

# =============================================================================
# 🔒 4. صفحة الدرس الثاني (مغلق بكود)
# =============================================================================
elif st.session_state.current_page == "Lesson2_Locked":
    st.button("⬅️ الرجوع للرئيسية", on_click=set_page, args=("Home",))
    st.title("🔒 Lesson 2: Lennard-Jones Gas Simulation")

    # نظام إدخال الكود
    user_code = st.text_input("🔑 أدخل كود التفعيل الخاص بك لمشاهدة الفيديو:", type="password")
    
    if user_code in VALID_CODES:
        st.success("✅ تم تفعيل الدرس بنجاح! مشاهدة ممتعة.")
        st.video("https://www.youtube.com/watch?v=2Briqk1u44U")
        
        st.subheader("📊 Simulation Parameters")
        st.write("في هذا الدرس تم تطبيق حسابات تقليل الطاقة NVT Ensemble.")
    elif user_code != "":
        st.error("❌ كود التفعيل غير صحيح، يرجى التأكد منه أو التواصل مع الدعم.")
    else:
        st.info("💡 هذا الدرس خاص بالمشتركين فقط.")
        st.markdown(f'[💬 اضغط هنا للحصول على كود التفعيل عبر الواتساب]({WA_LINK})')

# =============================================================================
# 🔒 5. صفحة كورس LAMMPS (مغلق بكود)
# =============================================================================
elif st.session_state.current_page == "Lesson3_Locked":
    st.button("⬅️ الرجوع للرئيسية", on_click=set_page, args=("Home",))
    st.title("🔒 Lesson 3: Complete LAMMPS Masterclass")

    user_code = st.text_input("🔑 أدخل كود التفعيل الخاص بك:", type="password")
    
    if user_code in VALID_CODES:
        st.success("✅ تم التفعيل بنجاح!")
        st.video("https://www.youtube.com/watch?v=fmQpiS9kI0A")
    elif user_code != "":
        st.error("❌ كود غير صحيح.")
    else:
        st.info("💡 هذا الدرس خاص بالمشتركين فقط.")
        st.markdown(f'[💬 اضغط هنا للحصول على كود التفعيل عبر الواتساب]({WA_LINK})')

# =============================================================================
# 🧬 6. صفحة العرض ثلاثي الأبعاد (3D Viewer)
# =============================================================================
elif st.session_state.current_page == "Viewer":
    st.button("⬅️ الرجوع للرئيسية", on_click=set_page, args=("Home",))
    st.title("🧪 Interactive 3D Protein Viewer")
    st.write("يمكنك التفاعل مع شكل البروتين بالماوس (تدوير، تكبير/تصغير):")
    
    pdb_id = "1AINS" # Insulin
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
# 📄 7. صفحة التحميلات
# =============================================================================
elif st.session_state.current_page == "Downloads":
    st.button("⬅️ الرجوع للرئيسية", on_click=set_page, args=("Home",))
    st.title("📄 Course Resources & Scripts")
    
    st.write("حمل الملفات البرمجية التي تحتاجها أثناء متابعة الكورسات:")
    st.download_button("📥 Download Python MD Script", data="import numpy as np...", file_name="md_script.py")
    st.download_button("📥 Download LAMMPS Input File", data="units real...", file_name="in.lammps")

# =============================================================================
# 🧠 8. صفحة الاختبار التفاعلي
# =============================================================================
elif st.session_state.current_page == "Quiz":
    st.button("⬅️ الرجوع للرئيسية", on_click=set_page, args=("Home",))
    st.title("🧠 Quick Assessment Quiz")
    
    ans = st.radio(
        "ما هي المعادلة الأساسية المستخدمة لحساب حركة الجسيمات في الـ Classical MD؟",
        ["Schrödinger Equation", "Newton's Second Law (F=ma)", "Maxwell Equations"]
    )
    
    if st.button("إرسال الإجابة"):
        if ans == "Newton's Second Law (F=ma)":
            st.balloons() # أنيميشن احتفال
            st.success("إجابة صحيحة ممتازة! 🎉")
        else:
            st.error("إجابة خاطئة، حاول مرة أخرى!")
