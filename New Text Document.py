import streamlit as st
import requests
from streamlit_lottie import st_lottie
import streamlit.components.v1 as components

# =============================================================================
# 1. إعدادات الصفحة
# =============================================================================
st.set_page_config(
    page_title="Bioinformatics & MD Hub",
    page_icon="🧬",
    layout="wide"
)

# الأكواد المتاحة ورابط الواتساب
VALID_CODES = ["BIO-101", "MD-2026", "STUDENT-99", "PASS-8842"]
WHATSAPP_NUMBER = "201000000000" 
WA_LINK = f"https://wa.me/{WHATSAPP_NUMBER}?text=السلام%20عليكم،%20أريد%20شراء%20كود%20تفعيل%20الكورس"

# إدارة التنقل عبر Session State (الصفحة الافتراضية هي Landing Page)
if "main_section" not in st.session_state:
    st.session_state.main_section = "Landing"  # الخيارات: Landing, Courses, Services

if "current_page" not in st.session_state:
    st.session_state.current_page = "Home"

def navigate_section(section):
    st.session_state.main_section = section
    st.session_state.current_page = "Home"

def set_course_page(page_name):
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
# 🌐 2. واجهة التعريف بالشركة (Landing Page)
# =============================================================================
if st.session_state.main_section == "Landing":
    
    # ─── Hero Section ───
    col_hero_text, col_hero_anim = st.columns([2, 1])
    
    with col_hero_text:
        st.title("🧬 Welcome to BioSim Solutions")
        st.subheader("تمكين الباحثين والشركات في مجالات البيوانفورماتكس والمحاكاة الجزيئية")
        st.write(
            "نحن شركة متخصصة في تقديم الحلول البرمجية والتدريب المتقدم في مجالات Bioinformatics "
            "و Molecular Dynamics (MD). نساعد الطلاب والباحثين والمؤسسات على تحليل البيانات الحيوية "
            "وبناء محاكاة جزيئية عالية الدقة باستخدام أحدث التقنيات."
        )
    
    with col_hero_anim:
        if dna_lottie:
            st_lottie(dna_lottie, height=220, key="landing_dna")

    st.divider()

    # ─── مميزات الشركة (Why Us?) ───
    st.subheader("💡 لماذا تختار منصتنا؟")
    col_a, col_b, col_c = st.columns(3)
    
    with col_a:
        with st.container(border=True):
            st.markdown("### 🎓 خبرة أكاديمية وعملية")
            st.write("محتوى تعليمي ومشاريع برمجية مشروحة بواسطة خبراء في المجال.")
    
    with col_b:
        with st.container(border=True):
            st.markdown("### 💻 أدوات تفاعلية 3D")
            st.write("استعراض ومعاينة البرشورات والبروتينات ثلاثية الأبعاد مباشرة داخل المنصة.")
            
    with col_c:
        with st.container(border=True):
            st.markdown("### 🔬 استشارات وحلول برمجية")
            st.write("تقديم خدمات تحليل البيانات وبناء المحاكاة للمشاريع والأبحاث.")

    st.divider()

    # ─── خيارات الانتقال الرئيسية (التوجيه) ───
    st.subheader("🎯 ماذا تريد أن تفعل اليوم؟")
    
    col_option1, col_option2 = st.columns(2)

    with col_option1:
        with st.container(border=True):
            st.markdown("## 📚 منصة الكورسات والتعلم")
            st.write("تصفح الدروس الفري والمدفوعة، وشاهد الفيديوهات، وحمّل المرفقات، واختبر معلوماتك.")
            st.button("الدخول لمنصة الكورسات ➔", on_click=navigate_section, args=("Courses",), use_container_width=True, type="primary")

    with col_option2:
        with st.container(border=True):
            st.markdown("## 🛠️ خدماتنا واستشاراتنا")
            st.write("تعرف على الخدمات البرمجية والاستشارية التي تقدمها الشركة للمؤسسات والباحثين.")
            st.button("استعراض الخدمات والحلول ➔", on_click=navigate_section, args=("Services",), use_container_width=True)

# =============================================================================
# 📚 3. قسم الكورسات والدروس (Courses Section)
# =============================================================================
elif st.session_state.main_section == "Courses":
    
    # زر العودة للواجهة التعريفية للشركة
    st.button("🏠 الرجوع للتعريف بالشركة", on_click=navigate_section, args=("Landing",))
    
    # ── 3.1 الصفحة الرئيسية للكورسات (واجهة الكروت) ──
    if st.session_state.current_page == "Home":
        st.title("📚 منصة الكورسات والتدريب")
        st.write("اختر الوحدات التعليمية المتاحة بالأسفل للبدء:")
        st.divider()

        # الصف الأول من الكروت
        c1, c2, c3 = st.columns(3)
        with c1:
            with st.container(border=True):
                st.markdown("### 🟢 Intro to MD `[FREE]`")
                st.write("مقدمة مجانية بالكامل في المحاكاة الجزيئية.")
                st.button("شاهد الدرس المجاني ➔", on_click=set_course_page, args=("Lesson1_Free",), use_container_width=True)

        with c2:
            with st.container(border=True):
                st.markdown("### 🔒 Advanced MD `[PREMIUM]`")
                st.write("درس متقدم في غاز Lennard-Jones وحسابات الطاقة.")
                st.button("فتح الدرس المغلق ➔", on_click=set_course_page, args=("Lesson2_Locked",), use_container_width=True)

        with c3:
            with st.container(border=True):
                st.markdown("### 🧬 3D Protein Viewer")
                st.write("مستعرض تفاعلي ثلاثي الأبعاد لفحص الهياكل (PDB).")
                st.button("فتح المستعرض ➔", on_click=set_course_page, args=("Viewer",), use_container_width=True)

        st.write("")

        # الصف الثاني من الكروت
        c4, c5, c6 = st.columns(3)
        with c4:
            with st.container(border=True):
                st.markdown("### 🔒 LAMMPS Masterclass `[PREMIUM]`")
                st.write("كورس شامل مدته ساعتان في برنامج LAMMPS.")
                st.button("فتح الكورس ➔", on_click=set_course_page, args=("Lesson3_Locked",), use_container_width=True)

        with c5:
            with st.container(border=True):
                st.markdown("### 📄 Resource Downloads")
                st.write("تحميل ملفات الأكواد والـ PDB والملخصات.")
                st.button("عرض الملفات ➔", on_click=set_course_page, args=("Downloads",), use_container_width=True)

        with c6:
            with st.container(border=True):
                st.markdown("### 🧠 Practice Quiz")
                st.write("اختبار تفاعلي سريع لتقييم مستواك.")
                st.button("ابدأ الاختبار ➔", on_click=set_course_page, args=("Quiz",), use_container_width=True)

    # ── 3.2 الدروس والصفحات الفرعية ──
    elif st.session_state.current_page == "Lesson1_Free":
        st.button("⬅️ رجوع لكروت الكورسات", on_click=set_course_page, args=("Home",))
        st.success("🎉 هذا الدرس مجاني بالكامل!")
        st.title("💻 Lesson 1: Introduction to Molecular Dynamics")
        st.video("https://www.youtube.com/watch?v=ChQbBqndwIA")
        st.download_button("📄 تحميل الملخص (PDF)", data="ملخص الدرس الأول", file_name="Lesson1_Notes.pdf")

    elif st.session_state.current_page == "Lesson2_Locked":
        st.button("⬅️ رجوع لكروت الكورسات", on_click=set_course_page, args=("Home",))
        st.title("🔒 Lesson 2: Lennard-Jones Gas Simulation")
        user_code = st.text_input("🔑 أدخل كود التفعيل الخاص بك:", type="password")
        if user_code in VALID_CODES:
            st.success("✅ تم تفعيل الدرس بنجاح!")
            st.video("https://www.youtube.com/watch?v=2Briqk1u44U")
        elif user_code != "":
            st.error("❌ كود غير صحيح.")
        else:
            st.info("💡 هذا الدرس خاص بالمشتركين فقط.")
            st.markdown(f'[💬 اضغط هنا للحصول على كود التفعيل عبر الواتساب]({WA_LINK})')

    elif st.session_state.current_page == "Lesson3_Locked":
        st.button("⬅️ رجوع لكروت الكورسات", on_click=set_course_page, args=("Home",))
        st.title("🔒 Lesson 3: Complete LAMMPS Masterclass")
        user_code = st.text_input("🔑 أدخل كود التفعيل الخاص بك:", type="password")
        if user_code in VALID_CODES:
            st.success("✅ تم تفعيل الكورس بنجاح!")
            st.video("https://www.youtube.com/watch?v=fmQpiS9kI0A")
        elif user_code != "":
            st.error("❌ كود غير صحيح.")
        else:
            st.info("💡 هذا الكورس خاص بالمشتركين فقط.")
            st.markdown(f'[💬 اضغط هنا للحصول على كود التفعيل عبر الواتساب]({WA_LINK})')

    elif st.session_state.current_page == "Viewer":
        st.button("⬅️ رجوع لكروت الكورسات", on_click=set_course_page, args=("Home",))
        st.title("🧪 Interactive 3D Protein Viewer")
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

    elif st.session_state.current_page == "Downloads":
        st.button("⬅️ رجوع لكروت الكورسات", on_click=set_course_page, args=("Home",))
        st.title("📄 Course Resources & Scripts")
        st.download_button("📥 Download Python MD Script", data="import numpy as np...", file_name="md_script.py")

    elif st.session_state.current_page == "Quiz":
        st.button("⬅️ رجوع لكروت الكورسات", on_click=set_course_page, args=("Home",))
        st.title("🧠 Quick Assessment Quiz")
        ans = st.radio("ما هي المعادلة الأساسية للحركة في الـ Classical MD؟", ["Schrödinger", "Newton (F=ma)", "Maxwell"])
        if st.button("إرسال الإجابة"):
            if ans == "Newton (F=ma)":
                st.balloons()
                st.success("إجابة صحيحة! 🎉")
            else:
                st.error("حاول مرة أخرى.")

# =============================================================================
# 🛠️ 4. قسم خدمات الشركة (Services Section)
# =============================================================================
elif st.session_state.main_section == "Services":
    
    st.button("🏠 الرجوع للتعريف بالشركة", on_click=navigate_section, args=("Landing",))
    
    st.title("🛠️ خدماتنا والحلول البرمجية")
    st.write("نقدم مجموعة واسعة من الخدمات البحثية والتقنية في مجالات Bioinformatics و Computational Chemistry:")
    st.divider()

    col_s1, col_s2 = st.columns(2)

    with col_s1:
        with st.container(border=True):
            st.markdown("### 🧪 Molecular Dynamics Simulations")
            st.write("إجراء محاكاة جزيئية كاملة للأنظمة البروتينية والمركبات الدوائية باستخدام Gromacs أو LAMMPS مع تحليل النواتج (RMSD, RMSF, Free Energy Calculation).")

        with st.container(border=True):
            st.markdown("### 🧬 Virtual Screening & Molecular Docking")
            st.write("عملية الترسيب الجزيئي واكتشاف الأدوية الحاسوبي واختيار المركبات الأقوى ارتباطاً بالـ Target Proteins.")

    with col_s2:
        with st.container(border=True):
            st.markdown("### 📊 Bioinformatics Data Analysis")
            st.write("تحليل بيانات التسلسل الجيني (NGS Data Analysis) وبناء خطوط تحليل آلي (Pipelines) باستخدام Python و R.")

        with st.container(border=True):
            st.markdown("### 💻 Custom Web Tools Development")
            st.write("تطوير أدوات ومواقع ويب مخصصة للمختبرات والأبحاث لعرض النتائج الحيوية بشكل تفاعلي.")

    st.divider()
    
    # ─── نموذج تواصل / طلب خدمة ───
    st.subheader("📬 طلب خدمة أو استشارة")
    st.write("يرجى ملء البيانات التالية وسيتواصل معك فريقنا في أقرب وقت:")
    
    with st.form("service_request_form"):
        name = st.text_input("الاسم الكامل:")
        email = st.text_input("البريد الإلكتروني:")
        service_type = st.selectbox("نوع الخدمة المطلوبة:", ["Molecular Dynamics", "Virtual Screening", "Bioinformatics Pipeline", "Custom Web App"])
        details = st.text_area("تفاصيل المشروع أو الاستفسار:")
        
        submitted = st.form_submit_button("إرسال الطلب 📤")
        if submitted:
            if name and email and details:
                st.success(f"شكراً لك يا {name}! تم استلام طلبك وسنتواصل معك عبر البريد الإلكتروني قريبًا.")
            else:
                st.warning("يرجى ملء جميع الحقول المطلوبة.")
