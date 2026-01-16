import streamlit as st
import requests
from streamlit_lottie import st_lottie

# 1. Анимацияны жүктеу функциясы
def load_lottieurl(url: str):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except:
        return None

# Пробирка анимациясының сілтемесі
lottie_url = "https://assets5.lottiefiles.com/packages/lf20_072ayrre.json"
lottie_ani = load_lottieurl(lottie_url)

# 2. Беттің баптаулары
st.set_page_config(page_title="Химия 10", layout="wide")

# Анимация мен тақырыпты қатар шығару
col1, col2 = st.columns([1, 6])
with col1:
    if lottie_ani:
        st_lottie(lottie_ani, height=150, key="tube_animation")
with col2:
    st.title("🧪 Органикалық химия - 10 сынып")
    st.subheader("19 сабақ | Әр сабақта 10 сұрақтан тест")

# 3. Сабақтар тізімі (Сенің тізімің)
lessons = [
    {"id": 1, "title": "Алкандар", "topic": "Қаныққан көмірсутектер"},
    {"id": 2, "title": "Алкендер", "topic": "Қос байланыстар"},
    {"id": 3, "title": "Алкиндер", "topic": "Үш байланыстар"},
    {"id": 4, "title": "Спирттер", "topic": "Гидроксил тобы"},
    {"id": 5, "title": "Фенолдар", "topic": "Ароматтық спирттер"},
    {"id": 6, "title": "Альдегидтер", "topic": "Карбонил тобы"},
    {"id": 7, "title": "Кетондар", "topic": "Кето тобы"},
    {"id": 8, "title": "Көмірсутектер салыстыру", "topic": "Алкан, Алкен, Алкин"},
    {"id": 9, "title": "Карбон қышқылдары", "topic": "Карбоксил тобы"},
    {"id": 10, "title": "Эфирлер", "topic": "Сложный эфирлер"},
    {"id": 11, "title": "Аминдар", "topic": "Амино тобы"},
    {"id": 12, "title": "Аминқышқылдар", "topic": "Аминқышқылдар"},
    {"id": 13, "title": "Галогентуындылар", "topic": "Галогентуындылар"},
    {"id": 14, "title": "Нитросоединениялар", "topic": "Нитро тобы"},
    {"id": 15, "title": "Сульфокислоталар", "topic": "Сульфо тобы"},
    {"id": 16, "title": "Тотығу реакциялары", "topic": "Тотығу"},
    {"id": 17, "title": "Қосылу реакциялары", "topic": "Қосылу"},
    {"id": 18, "title": "Ауыстыру реакциялары", "topic": "Ауыстыру"},
    {"id": 19, "title": "Полимерлеу", "topic": "Полимерлер"},
]

# 4. Сұрақтар базасы (Сенің сұрақтарың)
all_questions = {
    1: [
        {"question": "1. Алкандардың жалпы формуласы:", "options": ["А) CnH2n", "В) CnH2n+2", "С) CnH2n-2", "D) CnHn"], "correct": 1},
        {"question": "2. Метан молекуласының пішіні қандай?", "options": ["А) Тетраэдр", "В) Тригоналды", "С) Сызықты", "D) Жазық"], "correct": 0},
        {"question": "3. Алкандардағы көміртек атомдары қандай гибридтенеді?", "options": ["А) sp", "В) sp²", "С) sp³", "D) sp³d"], "correct": 2},
        {"question": "4. Алкандарға тән негізгі реакция түрі:", "options": ["А) Қосылу", "В) Ауыстыру", "С) Тотығу", "D) Конденсация"], "correct": 1},
        {"question": "5. Метанның толық жану реакциясының өнімдері:", "options": ["А) CO₂ + H₂", "В) CO + H₂O", "С) CO₂ + H₂O", "D) C + H₂O"], "correct": 2},
        {"question": "6. Алкандар хлормен қандай реакцияға түседі?", "options": ["А) Қосылу", "В) Тотығу", "С) Радикалды ауыстыру", "D) Ионды ауыстыру"], "correct": 2},
        {"question": "7. Алкандар суда қалай ериді?", "options": ["А) Жақсы ериді", "В) Нашар ериді", "С) Тек жоғары алкандар ериді", "D) Ерімейді"], "correct": 1},
        {"question": "8. Пропанның формуласы:", "options": ["А) CH₄", "В) C₂H₆", "С) C₃H₈", "D) C₄H₁₀"], "correct": 2},
        {"question": "9. Изомерлер дегеніміз:", "options": ["А) Бір формула, әртүрлі құрылым", "В) Әртүрлі формула", "С) Бір элемент", "D) Бір топ"], "correct": 0},
        {"question": "10. Алкандар не үшін 'қаныққан' деп аталады?", "options": ["А) Оттегі бар", "В) Қос байланыс жоқ", "С) Тотығады", "D) Галоген бар"], "correct": 1}
    ],
    2: [
        {"question": "1. Алкендердің жалпы формуласы:", "options": ["А) CnH2n", "В) CnH2n+2", "С) CnH2n-2", "D) CnHn"], "correct": 0},
        {"question": "2. Этилен молекуласының кеңістіктік құрылымы қандай?", "options": ["А) Тетраэдр", "В) Тригоналды", "С) Сызықты", "D) Жазық"], "correct": 3},
        {"question": "3. Қос байланыс қандай электрондардан тұрады?", "options": ["А) 1 σ және 1 π", "В) 2 σ", "С) 1 σ және 2 π", "D) 2 π"], "correct": 0},
        {"question": "4. Алкендердің негізгі реакция түрі:", "options": ["А) Ауыстыру", "В) Қосылу", "С) Тотығу", "D) Ыдырау"], "correct": 1},
        {"question": "5. Этилен бромсумен қандай реакцияға түседі?", "options": ["А) Ауыстыру", "В) Қосылу", "С) Тотығу", "D) Конденсация"], "correct": 1},
        {"question": "6. Марковников ережесіне сәйкес қосылу кезінде:", "options": ["А) Сутек көбірек сутек бар көміртектің", "В) Галоген көбірек сутек бар көміртектің", "С) Екеуі де дұрыс", "D) Екеуі де дұрыс емес"], "correct": 1},
        {"question": "7. Алкендерден қандай полимерлер алынады?", "options": ["А) Полиэтилен", "В) Поливинилхлорид", "С) Полипропилен", "D) Барлығы"], "correct": 3},
        {"question": "8. Этиленның формуласы:", "options": ["А) CH₄", "В) C₂H₄", "С) C₂H₂", "D) C₃H₆"], "correct": 1},
        {"question": "9. KMnO₄ ерітіндісі алкендердің қасиетін қалай өзгертеді?", "options": ["А) Түсін өзгертеді", "В) Түсін өзгертпейді", "С) Тұнба түзееді", "D) Газ бөледі"], "correct": 0},
        {"question": "10. Циклоалкандардың жалпы формуласы:", "options": ["А) CnH2n", "В) CnH2n+2", "С) CnH2n-2", "D) CnHn"], "correct": 0}
    ]
    # Қалған сұрақтарды (3-19) осылай қосуға болады...
}

# 5. Боковая панель (Сабақ таңдау)
st.sidebar.header("📚 Сабақтар")
lesson_titles = [f"{l['id']}. {l['title']}" for l in lessons]
selected_lesson = st.sidebar.selectbox("Сабақты таңдаңыз:", lesson_titles)
selected_id = int(selected_lesson.split(".")[0])

# 6. Тест бөлімі
st.divider()
st.header(f"Тақырыбы: {selected_lesson}")

if selected_id in all_questions:
    questions = all_questions[selected_id]
    
    with st.form(key=f"test_form_{selected_id}"):
        user_answers = []
        for i, q in enumerate(questions):
            st.write(f"**{q['question']}**")
            ans = st.radio("Жауап:", q['options'], key=f"q_{selected_id}_{i}")
            user_answers.append(q['options'].index(ans))
        
        submit = st.form_submit_button("Нәтижені тексеру")
        
    if submit:
        score = sum(1 for i, q in enumerate(questions) if user_answers[i] == q['correct'])
        st.success(f"Нәтиже: {score} / {len(questions)}")
        if score == len(questions):
            st.balloons()
else:
    st.warning("Бұл сабақ үшін сұрақтар әлі дайын емес.")
