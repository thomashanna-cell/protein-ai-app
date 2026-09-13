import streamlit as st

st.set_page_config(page_title="Bioinformatics Hub", page_icon="🧬", layout="wide")

# إدارة التناقل بين الصفحات
if "current_page" not in st.session_state:
    st.session_state.current_page = "Home"

def set_page(page_name):
    st.session_state.current_page = page_name

# =============================================================================
# 🏠 1. الصفحة الرئيسية (عرض الكروت)
# =============================================================================
if st.session_state.current_page == "Home":
    st.title("🧬 Bioinformatics & MD Learning Hub")
    st.write("اختر من الكورسات المتاحة بالأسفل (توجد دروس مجانية وأخرى مدفوعة):")
    st.divider()

    col1, col2 = st.columns(2)

    # 🟢 كارت فيديو مجاني (Free)
    with col1:
        with st.container(border=True):
            st.markdown("### 🟢 Lesson 1: Intro to MD `[FREE]`")
            st.write("درس مقدمة مجاني بالكامل لجميع الطلاب بدون أي قيود.")
            st.button("Watch Free Video ➔", on_click=set_page, args=("Lesson1_Free",), use_container_width=True)

    # 🔒 كارت فيديو مغلق / مدفوع (Locked)
    with col2:
        with st.container(border=True):
            st.markdown("### 🔒 Lesson 2: Advanced MD `[PREMIUM]`")
            st.write("درس متقدم يحتاج لرمز دخول أو اشتراك لمشاهدته.")
            st.button("Unlock Lesson ➔", on_click=set_page, args=("Lesson2_Locked",), use_container_width=True)

# =============================================================================
# 🎬 2. صفحة الدرس المجاني (Free Lesson)
# =============================================================================
elif st.session_state.current_page == "Lesson1_Free":
    st.button("⬅️ Back to Home", on_click=set_page, args=("Home",))
    
    st.success("🎉 هذا الدرس مجاني بالكامل!")
    st.title("💻 Lesson 1: Introduction to MD (Free)")
    
    # فيديو مجاني يشتغل فوراً
    st.video("https://www.youtube.com/watch?v=ChQbBqndwIA")
    st.write("استمتع بمشاهدة الفيديو وتحميل الملفات المرفقة.")

# =============================================================================
# 🔒 3. صفحة الدرس المغلق (Locked Lesson)
# =============================================================================
elif st.session_state.current_page == "Lesson2_Locked":
    st.button("⬅️ Back to Home", on_click=set_page, args=("Home",))
    st.title("🔒 Lesson 2: Advanced MD Simulations")

    # نظام قفل بسيط باختبار كلمة سر
    passcode = st.text_input("أدخل كود الاشتراك لتشغيل الفيديو:", type="password")
    
    if passcode == "bio2026":  # كلمة السر للتجربة
        st.success("تم التفعيل بنجاح! مشاهدة ممتعة.")
        st.video("https://www.youtube.com/watch?v=2Briqk1u44U")
    elif passcode != "":
        st.error("كود الاشتراك غير صحيح، تواصل مع الدعم للحصول عليه.")
    else:
        st.warning("⚠️ هذا الفيديو خاص بالمشتركين فقط. يرجى إدخال الكود لتشغيله.")
