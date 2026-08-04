import streamlit as st
import requests
import uuid

# الرابط الخاص بـ Ngrok للـ Webhook
WEBHOOK_URL = "https://rename-chastity-chamber.ngrok-free.dev/webhook/f2ba8546-d338-4836-b7ff-4faae74b38f9"

st.set_page_config(page_title="Multi-Database Protein AI", page_icon="🧬", layout="wide")
st.title("🧬 Protein & Genomics AI Assistant")
st.caption("مساعد بحثي متكامل متصل بـ UniProt, PDB, و NCBI")

# إنشاء Session ID فريد للفيو الحالي عشان n8n يحفظ سياق المحادثة
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

# تهيئة سجل المحادثة على الشاشة
if "messages" not in st.session_state:
    st.session_state.messages = []

# زر لإعادة بدء محادثة جديدة
with st.sidebar:
    st.header("إعدادات الجلسة")
    if st.button("🗑️ مسح المحادثة وبدء جلسة جديدة"):
        st.session_state.messages = []
        st.session_state.session_id = str(uuid.uuid4())
        st.rerun()

# عرض المحادثات السابقة
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# استقبال مدخلات المستخدم
if prompt := st.chat_input("اسأل عن بروتين، تركيب PDB، أو تتابع جيني في NCBI..."):
    # إضافة سؤال المستخدم للواجهة
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # إرسال الطلب مع الـ session_id للحفاظ على التتابع
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        message_placeholder.markdown("🔍 جاري البحث والاستعلام من القواعد..." )
        
        payload = {
            "message": prompt,
            "sessionId": st.session_state.session_id
        }
        
        try:
            response = requests.post(WEBHOOK_URL, json=payload)
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
