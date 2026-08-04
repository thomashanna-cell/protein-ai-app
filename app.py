import streamlit as st
import requests

# الرابط الكامل المدمج بين Ngrok والـ Path الموضح في الصورة
WEBHOOK_URL = "https://rename-chastity-chamber.ngrok-free.dev/webhook/f2ba8546-d338-4836-b7ff-4faae74b38f9"

st.set_page_config(page_title="Protein AI Assistant", page_icon="🧬")
st.title("🧬 Protein AI Assistant")
st.caption("مساعد الذكاء الاصطناعي للبحث في قواعد بيانات البروتينات")

# تهيئة سجل المحادثة
if "messages" not in st.session_state:
    st.session_state.messages = []

# عرض المحادثات السابقة
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# استقبال مدخلات المستخدم
if prompt := st.chat_input("اكتب اسم البروتين أو سؤالك هنا..."):
    # إضافة سؤال المستخدم للواجهة
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # إرسال الطلب إلى n8n وعرض استجابة الذكاء الاصطناعي
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        message_placeholder.markdown("جاري البحث في قاعدة البيانات...")
        
        try:
            response = requests.post(WEBHOOK_URL, json={"message": prompt})
            if response.status_code == 200:
                try:
                    res_data = response.json()
                    if isinstance(res_data, list) and len(res_data) > 0:
                        output_text = res_data[0].get("output", res_data[0].get("text", str(res_data[0])))
                    elif isinstance(res_data, dict):
                        output_text = res_data.get("output", res_data.get("text", str(res_data)))
                    else:
                        output_text = str(res_data)
                except Exception:
                    output_text = response.text

                message_placeholder.markdown(output_text)
                st.session_state.messages.append({"role": "assistant", "content": output_text})
            else:
                error_msg = f"حدث خطأ في الاتصال بالسيرفر ({response.status_code})"
                message_placeholder.error(error_msg)
        except Exception as e:
            message_placeholder.error(f"فشل الاتصال: {e}")