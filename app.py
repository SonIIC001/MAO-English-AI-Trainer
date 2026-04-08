import streamlit as st
import google.generativeai as genai
import datetime

# إعدادات واجهة MAO
st.set_page_config(page_title="MAO English Pilot 2.0", page_icon="🎓", layout="wide")

# القائمة الجانبية (Sidebar)
with st.sidebar:
    st.title("👨‍🏫 MAO Private Tutor")
    api_key = st.text_input("Gemini API Key:", type="password")
    st.divider()
    # نظام الـ Streaks البسيط
    st.metric(label="🔥 Daily Streak", value="5 Days")
    st.progress(60, text="Daily Goal: 3/5 Exercises")

def get_ai_response(api_key, system_prompt, user_input):
    try:
        genai.configure(api_key=api_key)
        # استخدام موديل 2.0 فلاش عشان السرعة (بناءً على اللستة بتاعتك)
        model = genai.GenerativeModel('models/gemini-2.0-flash')
        full_prompt = f"{system_prompt}\n\nUser Input: {user_input}"
        response = model.generate_content(full_prompt)
        return response.text
    except Exception as e:
        if "quota" in str(e).lower():
            return "⚠️ باقة الـ API خلصت، ارتاح شوية وارجع كمل يا بطل!"
        return f"⚠️ خطأ: {str(e)}"

if api_key:
    st.title("🚀 MAO English Pilot: Duolingo + Cake Hybrid")
    
    tab1, tab2, tab3 = st.tabs(["🎮 Challenge Zone (Duolingo Style)", "🎬 Real-Life Scenes (Cake Style)", "📊 Pro Analyst English"])

    # 1. تحدي الكلمات (تكرار وتدريب)
    with tab1:
        st.subheader("تحدي الترجمة السريع")
        word_to_test = "Data Pipeline" # ممكن نخليها تتغير عشوائياً
        user_trans = st.text_input(f"ترجم المصطلح ده في جملة من دماغك: ({word_to_test})")
        if user_trans:
            prompt = "Act like a strict but helpful English teacher. Rate my sentence out of 10 and give me a 'Golden Tip' to improve it."
            st.info(get_ai_response(api_key, prompt, user_trans))

    # 2. مواقف حقيقية (Cake)
    with tab2:
        st.subheader("موقف اليوم: الاجتماع الأسبوعي")
        st.write("كيف تقول لمديرك أن التقرير سيتأخر بسبب مشكلة في البيانات؟")
        user_scene = st.text_area("اكتب ردك هنا:")
        if st.button("تحسين الرد (Cake Style)"):
            prompt = "Convert this sentence into 3 versions: 1. Casual (Friends), 2. Professional (Work), 3. Native Speaker (Idoms)."
            st.success(get_ai_response(api_key, prompt, user_scene))

    # 3. مخصص ليك كـ Data Analyst
    with tab3:
        st.subheader("تطوير مصطلحات الداتا")
        tech_text = st.text_area("اكتب شرح تقني بسيط للي عملته النهاردة:")
        if st.button("اجعله احترافياً"):
            prompt = "Rewrite this technical explanation to be more sophisticated for a Senior Data Analyst interview."
            st.write(get_response(api_key, prompt))
else:
    st.warning("⚠️ دخل الـ API Key عشان نبدأ المذاكرة!")
