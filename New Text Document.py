import streamlit as st

# ضبط عنوان الصفحة
st.set_page_config(page_title="منصة الكورسات التعليمية", layout="wide")

# الشريط الجانبي (قائمة الدروس)
st.sidebar.title("📚 محتوى الكورس")
lesson = st.sidebar.radio(
    "اختر الدرس:",
    ["الدرس الأول: مقدمة", "الدرس الثاني: الأساسيات", "الدرس الثالث: التطبيق العملي"]
)

# محتوى الصفحة الرئيسي بناءً على الدرس المختار
if lesson == "الدرس الأول: مقدمة":
    st.header("الدرس الأول: مقدمة في المجال")
    # عرض فيديو من يوتيوب كمثال
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ") 
    
    st.subheader("تفاصيل الدرس:")
    st.write("في هذا الفيديو سنتعرف على الأساسيات والمفاهيم الأولى...")
    
    # أزرار تحميل المرفقات
    st.download_button("تحميل ملخص الدرس (PDF)", data="محتوى الملف", file_name="lesson1.pdf")

elif lesson == "الدرس الثاني: الأساسيات":
    st.header("الدرس الثاني: الأساسيات")
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    
    # اختبار سريع
    st.subheader("🧠 اختبار سريع:")
    answer = st.radio("ما هي اللغة المستخدمة في Streamlit؟", ["Java", "Python", "C++"])
    if st.button("إرسال الإجابة"):
        if answer == "Python":
            st.success("إجابة صحيحة! 🎉")
        else:
            st.error("إجابة خاطئة، حاول مرة أخرى.")