import streamlit as st
import time

st.set_page_config(page_title="Органикалық химия: Сапалық реакциялар", layout="wide")

# ---------------- SIDEBAR ----------------
st.sidebar.title("📘 34 САБАҚ")
lessons = [f"{i}-сабақ" for i in range(1, 35)]
lesson_selected = st.sidebar.selectbox("Сабақты таңдаңыз", lessons)
st.sidebar.markdown("---")
mode = st.sidebar.radio("Режим", ["Оқушы", "Мұғалім"])

st.title("🧪 Органикалық функционалдық топтардың сапалық реакциялары")
st.caption(f"Таңдалған: {lesson_selected} | Режим: {mode}")

# ---------------- DATA ----------------
import streamlit as st
import time

# Беттің баптаулары
st.set_page_config(page_title="Chemistry AI Lab", layout="wide", page_icon="🧪")

# ------------------- МӘЛІМЕТТЕР ҚОРЫ (DATA) -------------------
# Осында барлық 34 сабақтың мазмұнын қосуға болады
chemistry_data = {
    1: {
        "topic": "Алкандардың жануы",
        "theory": "Алкандар оттегінде жанғанда CO₂ және H₂O түзеді. Бұл процесс экзотермиялық (жылу бөледі).",
        "lab": {
            "reagents": "Метан (CH₄), Оттегі (O₂), Лай су (Ca(OH)₂)",
            "observation": "Көгілдір жалын, лай судың лайлануы",
            "conclusion": "Жану нәтижесінде көмірқышқыл газы түзілді."
        },
        "tests": [
            ("Жану реакциясының негізгі белгісі:", ["тұнба", "түс өзгеруі", "жылу мен жарық бөлінуі", "иіс"], 2),
            ("Алкан жанғанда түзілетін газ:", ["H₂", "O₂", "CO₂", "N₂"], 2),
            ("Жану – бұл:", ["физикалық", "химиялық", "изомерлену", "еріту"], 1),
            ("Жану типі:", ["қосылу", "орынбасу", "тотығу", "айырылу"], 2),
            ("CO₂ дәлелдеу реактиві:", ["лакмус", "лай су", "NaOH", "HCl"], 1),
            ("Алкан жануы экзотермиялық па?", ["жоқ", "кейде", "иә", "белгісіз"], 2),
            ("Жану үшін қажет зат:", ["CO₂", "O₂", "H₂O", "NaCl"], 1),
            ("Жану кезінде байланыс:", ["үзіледі ғана", "түзіледі ғана", "үзіліп-түзіледі", "өзгермейді"], 2),
            ("Жану жылдамдығы тәуелді:", ["масса", "температура", "түс", "иіс"], 1),
            ("Қорытынды белгі:", ["газ жоқ", "энергия жұтылады", "энергия бөлінеді", "тұнба түзіледі"], 2)
        ]
    },
    2: {
        "topic": "Алкандардың броммен орынбасуы",
        "theory": "Алкандар жарық түскенде галогендермен орынбасу реакциясына түседі (SR механизмі).",
        "lab": {
            "reagents": "Гексан, Бром (Br₂), УФ-жарық",
            "observation": "Бром суының біртіндеп түссізденуі",
            "conclusion": "Радикалды орынбасу реакциясы жүрді."
        },
        "tests": [
            ("Реакция типі:", ["қосылу", "орынбасу", "айырылу", "гидролиз"], 1),
            ("Қандай шарт керек?", ["су", "жарық", "суық", "қысым"], 1),
            ("Бақылау:", ["тұнба", "газ", "бром түссізденуі", "көк түс"], 2),
            ("Реакция механизмі:", ["иондық", "радикалдық", "кешен", "электрофильді"], 1),
            ("Br₂ рөлі:", ["катализатор", "реагент", "еріткіш", "индикатор"], 1),
            ("Алкан белсенділігі:", ["жоғары", "орташа", "төмен", "өте жоғары"], 2),
            ("Өнімдердің бірі:", ["спирт", "қышқыл", "галогеналкан", "альдегид"], 2),
            ("Реакция қайда жүреді?", ["қараңғыда", "жарықта", "суда", "ауада"], 1),
            ("Қауіпсіздік:", ["ашық от", "иіскеу", "қорғаныш көзілдірік", "қолмен ұстау"], 2),
            ("Қорытынды белгі:", ["түс өзгермейді", "түссіздену", "газ", "тұнба"], 1)
        ]
    },
    3: {
        "topic": "Алкендердің бром суын түссіздендіруі",
        "theory": "Қанықпаған көмірсутектер (алкендер) еселі байланыстың үзілуі есебінен бромды тез қосып алады.",
        "lab": {
            "reagents": "Этилен (C₂H₄), Бром суы (Br₂)",
            "observation": "Қызыл-қоңыр түстің лезде жойылуы",
            "conclusion": "Заттың құрамында қос байланыс (C=C) бар."
        },
        "tests": [
            ("Сапалық реакция белгісі:", ["газ", "тұнба", "түссіздену", "иіс"], 2),
            ("Қандай байланыс үзіледі?", ["σ", "π", "иондық", "сутектік"], 1),
            ("Реакция типі:", ["орынбасу", "қосылу", "тотығу", "айырылу"], 1),
            ("Br₂ рөлі:", ["катализатор", "индикатор", "реагент", "еріткіш"], 2),
            ("Алкендердің қасиеті:", ["қаныққан", "қанықпаған", "ароматты", "инертті"], 1),
            ("Бақылау түсі:", ["көк", "қоңыр", "түссіз", "сары"], 2),
            ("Сапалық реакция мақсаты:", ["масса өлшеу", "анықтау", "еріту", "салқындату"], 1),
            ("Реакция жылдамдығы:", ["баяу", "орташа", "тез", "жүрмейді"], 2),
            ("Орта:", ["қышқыл", "негіздік", "бейтарап", "тұзды"], 2),
            ("Қорытынды:", ["алкан", "алкен бар", "алкин", "спирт"], 1)
        ]
    }
}

# ------------------- SIDEBAR -------------------
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3655/3655580.png", width=100)
st.sidebar.title("🧪 Chemistry AI Lab")
lesson_num = st.sidebar.selectbox("Сабақты таңдаңыз:", options=list(range(1, 35)))
mode = st.sidebar.radio("Режим:", ["Оқу", "Зертхана", "Тест"])

# ------------------- MAIN INTERFACE -------------------
if lesson_num in chemistry_data:
    data = chemistry_data[lesson_num]
    st.header(f"№{lesson_num} сабақ: {data['topic']}")

    if mode == "Оқу":
        st.subheader("📖 Теориялық мәлімет")
        st.info(data['theory'])
        
        st.markdown("""
        ### Қауіпсіздік ережесі:
        * Реактивтермен жұмыс кезінде қолғап киіңіз.
        * Тез тұтанатын заттарды оттан алыс ұстаңыз.
        """)

    elif mode == "Зертхана":
        st.subheader("🔬 Виртуалды зертханалық жұмыс")
        st.write(f"**Реактивтер:** {data['lab']['reagents']}")
        
        if st.button("Тәжірибені бастау"):
            progress = st.progress(0)
            status = st.empty()
            
            for i in range(1, 101):
                time.sleep(0.02)
                progress.progress(i)
                if i < 40: status.text("🧪 Реактивтер қосылуда...")
                elif i < 80: status.text(f"👀 Бақылау: {data['lab']['observation']}")
                else: status.text("✅ Тәжірибе аяқталды!")
            
            st.success(f"**Қорытынды:** {data['lab']['conclusion']}")
            

    elif mode == "Тест":
        st.subheader("📝 Білімді тексеру (10 сұрақ)")
        score = 0
        user_answers = []

        for i, (q, opts, correct) in enumerate(data['tests']):
            ans = st.radio(f"**{i+1}. {q}**", opts, key=f"q_{lesson_num}_{i}")
            user_answers.append(ans == opts[correct])

        if st.button("Нәтижені есептеу"):
            score = sum(user_answers)
            if score >= 8:
                st.balloons()
                st.success(f"Керемет! Сіздің нәтижеңіз: {score}/10")
            elif score >= 5:
                st.warning(f"Жақсы, бірақ толықтыру керек: {score}/10")
            else:
                st.error(f"Қайта оқуды ұсынамыз: {score}/10")

else:
    st.warning(f"№{lesson_num} сабақтың мазмұны жақын арада қосылады. Әзірге алғашқы 3 сабақ қолжетімді.")

# ------------------- FOOTER -------------------
st.markdown("---")
st.caption("©️ 2024 Органикалық химия: Цифрлық зертхана")
      
# ---------------- UI FUNCTIONS ----------------
def show_theory(text):
    st.subheader("📖 Теория")
    st.info(text)

def show_lab(reagents, observation, conclusion):
    st.subheader("🔬 Виртуалды зертхана")
    st.write(f"**Реактивтер:** {reagents}")
    
    if st.button("Реакцияны бастау"):
        progress_bar = st.progress(0)
        status_text = st.empty()
        for i in range(1, 101):
            time.sleep(0.01)
            progress_bar.progress(i)
            if i < 30: status_text.text("🧪 Реактивтер араласуда...")
            elif i < 70: status_text.text(f"👀 Бақылау: {observation}")
            else: status_text.text(f"✅ Қорытынды: {conclusion}")

def show_ai(task):
    st.subheader("🤖 AI Тапсырма")
    st.write(task)
    user_answer = st.text_input("Жауабыңызды жазыңыз:", key=f"ai_in_{lesson_selected}")
    if st.button("AI-дан көмек"):
        st.success("Бұл топтың қасиеті оның құрамындағы электрондардың тығыздығына байланысты...")

def show_test(test_items):
    st.subheader("📝 Тест")
    user_selections = []
    
    # Сұрақтарды шығару
    for idx, (q, opts, correct) in enumerate(test_items):
        # index=None пайдаланушы таңдау жасағанша бос тұрады
        ans = st.radio(f"{idx+1}. {q}", opts, index=None, key=f"test_{lesson_selected}_{idx}")
        user_selections.append(ans)

    st.markdown("---")
    if st.button("Нәтижені тексеру"):
        score = 0
        for i, ans in enumerate(user_selections):
            if ans is not None:
                correct_idx = test_items[i][2]
                if ans == test_items[i][1][correct_idx]:
                    score += 1
        
        if score == len(test_items):
            st.balloons()
            st.success(f"Керемет! Ұпай: {score} / {len(test_items)}")
        else:
            st.warning(f"Нәтиже: {score} / {len(test_items)}. Қателерді қайталаңыз.")
    else:
        st.info(f"Ағымдағы ұпай: 0 / {len(test_items)}")

# ---------------- MAIN CONTENT ----------------
lesson_num = int(lesson_selected.split("-")[0])
data = lesson_data.get(lesson_num)

if data:
    st.header(f"{lesson_num}-сабақ. {data['topic']}")
    tab1, tab2, tab3 = st.tabs(["📚 Оқу", "🧪 Тәжірибе", "✍️ Тест"])
    
    with tab1:
        show_theory(data["theory"])
        show_ai(data["ai"])
    
    with tab2:
        show_lab(*data["lab"])
        
    with tab3:
        show_test(data["test"])
else:
    st.warning("Бұл сабақтың мазмұны әзірленуде...")

st.markdown("---")
st.caption("©️ Chemistry + AI | Streamlit оқу платформасы")
