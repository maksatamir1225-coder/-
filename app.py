import streamlit as st
import time

# Беттің реттеулері
st.set_page_config(page_title="Organic Chemistry Lab", layout="wide", page_icon="🧪")

# ---------------- CSS СТИЛЬДЕРІ ----------------
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 20px; border: 1px solid #4CAF50; }
    .stProgress > div > div > div > div { background-color: #4CAF50; }
    </style>
    """, unsafe_allow_html=True)

# ---------------- DATA (ДЕРЕКТЕР ҚОРЫ) ----------------
# Барлық 34 сабақтың базасын осы жерге толтыруға болады
lessons_db = {
    1: {
        "topic": "Алкандардың жануы",
        "theory": "Алкандар жанғанда жылу бөледі. Толық жану кезінде көмірқышқыл газы мен су түзіледі.",
        "lab": ["Парафин, оттегі", "Көгілдір жалын, CO2 бөлінуі", "Тотығу реакциясы жүрді"],
        "formula": "C_nH_{2n+2} + O_2 \\rightarrow nCO_2 + (n+1)H_2O",
        "test": [
            ("Метан жанғанда қандай газ бөлінеді?", ["O2", "CO2", "H2"], 1),
            ("Алкандардың жалпы формуласы?", ["CnH2n", "CnH2n+2", "CnH2n-2"], 1)
        ]
    },
    2: {
        "topic": "Алкандардың броммен орынбасуы",
        "theory": "Алкандар жарықтың әсерінен галогендермен орынбасу реакциясына түседі (радикалды механизм).",
        "lab": ["Гексан, Br2 ерітіндісі, УФ-жарық", "Қоңыр түстің біртіндеп жойылуы", "Орынбасу реакциясы"],
        "formula": "CH_4 + Br_2 \\xrightarrow{h\\nu} CH_3Br + HBr",
        "test": [
            ("Алкандарға тән реакция түрі?", ["Қосылу", "Орынбасу", "Полимерлену"], 1)
        ]
    },
    3: {
        "topic": "Алкендердің сапалық реакциясы",
        "theory": "Алкендер құрамында қос байланыс болғандықтан, бром суын және калий перманганатын түссіздендіреді.",
        "lab": ["Этилен, Бром суы", "Қызыл-қоңыр түссізденеді", "Қанықпағандық (қос байланыс) дәлелденді"],
        "formula": "CH_2=CH_2 + Br_2 \\rightarrow CH_2Br-CH_2Br",
        "test": [
            ("Алкендердің сапалық реактиві?", ["Бром суы", "Лакмус", "Фенолфталеин"], 0)
        ]
    }
    # 4-34 сабақтарды осы форматта жалғастыруға болады
}

# ---------------- SIDEBAR (БҮЙІРЛІК ПАНЕЛЬ) ----------------
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3022/3022588.png", width=100)
st.sidebar.title("🔬 Навигация")

# Сабақтар тізімі (1-34)
lesson_list = [f"{i}-сабақ. {lessons_db.get(i, {'topic': 'Дайындалуда...'})['topic']}" for i in range(1, 35)]
selected_idx = st.sidebar.selectbox("Сабақты таңдаңыз:", range(1, 35), format_func=lambda x: lesson_list[x-1])

st.sidebar.markdown("---")
mode = st.sidebar.segmented_control("Режим", ["Оқушы", "Мұғалім"], default="Оқушы")

# ---------------- MAIN CONTENT ----------------
data = lessons_db.get(selected_idx)

if data:
    st.title(f"🧪 {selected_idx}-зертханалық жұмыс")
    st.header(data["topic"])
    
    tab1, tab2, tab3 = st.tabs(["📚 Теория", "⚗️ Виртуалды тәжірибе", "✍️ Бақылау"])

    with tab1:
        st.subheader("Негізгі мәлімет")
        st.write(data["theory"])
        st.latex(data["formula"])
        
        
        
        with st.expander("🤖 AI Түсіндірмесі"):
            st.write("Бұл реакция органикалық химиядағы ең маңызды реакциялардың бірі. Оның механизмі...")

    with tab2:
        st.subheader("Эксперимент барысы")
        col1, col2 = st.columns(2)
        with col1:
            st.info(f"**Реактивтер:** {data['lab'][0]}")
            if st.button("Реакцияны іске қосу"):
                bar = st.progress(0)
                status = st.empty()
                for p in range(101):
                    time.sleep(0.02)
                    bar.progress(p)
                    if p < 40: status.text("🧪 Араластыру...")
                    elif p < 80: status.text("🔥 Реакция жүріп жатыр...")
                    else: status.text("✅ Аяқталды!")
                
                st.success(f"**Бақылау:** {data['lab'][1]}")
                st.balloons()
        with col2:
            st.metric("Қорытынды", data['lab'][2])

    with tab3:
        st.subheader("Білімді тексеру")
        score = 0
        for i, (q, opts, corr) in enumerate(data["test"]):
            ans = st.radio(f"{i+1}. {q}", opts, key=f"q_{selected_idx}_{i}")
            if st.button(f"Тексеру {i+1}", key=f"btn_{selected_idx}_{i}"):
                if opts.index(ans) == corr:
                    st.success("Дұрыс!")
                    score += 1
                else:
                    st.error("Қате, қайта ойлан.")

else:
    st.title(f"🧪 {selected_idx}-сабақ")
    st.info("Бұл сабақтың мазмұны жақын арада қосылады. Базаны толтыруды жалғастырыңыз.")
    st.image("https://cdn-icons-png.flaticon.com/512/2597/2597148.png", width=200)

# ---------------- FOOTER ----------------
st.markdown("---")
st.caption("© 2024 Органикалық химия оқу платформасы | Барлық құқықтар қорғалған")
