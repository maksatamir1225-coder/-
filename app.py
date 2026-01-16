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

# Анимация сілтемесі (Химиялық пробирка)
lottie_url = "https://assets5.lottiefiles.com/packages/lf20_072ayrre.json"
lottie_test_tube = load_lottieurl(lottie_url)

# 2. Беттің баптаулары
st.set_page_config(page_title="Химия 10", layout="wide")

# Заголовок пен Анимацияны қатар қою
col1, col2 = st.columns([1, 5])
with col1:
    if lottie_test_tube:
        st_lottie(lottie_test_tube, height=150, key="main_tube")
with col2:
    st.title("🧪 Органикалық химия - 10 сынып")
    st.subheader("19 сабақ | Әр сабақта 10 сұрақтан тест")

# 3. Сабақтар мен сұрақтар базасы (ықшамдалған нұсқа)
lessons = [
    {"id": 1, "title": "Алкандар", "topic": "Қаныққан көмірсутектер"},
    {"id": 2, "title": "Алкендер", "topic": "Қос байланыстар"},
    {"id": 3, "title": "Алкиндер", "topic": "Үш байланыстар"},
    {"id": 4, "title": "Спирттер", "topic": "Гидроксил тобы"},
]

all_questions = {
    1: [
        {"question": "1. Алкандардың жалпы формуласы:", "options": ["А) CnH2n", "В) CnH2n+2", "С) CnH2n-2", "D) CnHn"], "correct": 1},
        {"question": "2. Метан молекуласының пішіні қандай?", "options": ["А) Тетраэдр", "В) Тригоналды", "С) Сызықты", "D) Жазық"], "correct": 0},
        {"question": "3. Алкандардағы көміртек атомдары қандай гибридтенеді?", "options": ["А) sp", "В) sp²", "С) sp³", "D) sp³d"], "correct": 2},
    ],
    2: [
        {"question": "1. Алкендердің жалпы формуласы:", "options": ["А) CnH2n", "В) CnH2n+2", "С) CnH2n-2", "D) CnHn"], "correct": 0},
        {"question": "2. Этилен молекуласының пішіні қандай?", "options": ["А) Тетраэдр", "В) Тригоналды", "С) Сызықты", "D) Жазық"], "correct": 3},
    ]
}

# 4. Боковая панель (Мәзір)
st.sidebar.header("Сабақ таңдаңыз")
lesson_titles = [f"{l['id']}. {l['title']}" for l in lessons]
selected_lesson_name = st.sidebar.selectbox("Тақырыптар:", lesson_titles)
selected_id = int(selected_lesson_name.split(".")[0])

# 5. Тест интерфейсі
st.divider()
st.header(f"Тақырыбы: {selected_lesson_name}")

if selected_id in all_questions:
    questions = all_questions[selected_id]
    user_answers = []
    
    # Форма арқылы сұрақтарды шығару
    with st.form(key=f"test_form_{selected_id}"):
        for i, q in enumerate(questions):
            st.write(f"**{q['question']}**")
            ans = st.radio(f"Жауапты таңдаңыз ({i+1}):", q['options'], key=f"q_{selected_id}_{i}")
            user_answers.append(q['options'].index(ans))
        
        submit_button = st.form_submit_button(label="Нәтижені тексеру")

    if submit_button:
        score = 0
        for i, q in enumerate(questions):
            if user_answers[i] == q['correct']:
                score += 1
        
        # Нәтижені көрсету
        st.success(f"Тест аяқталды! Сіздің нәтижеңіз: {score} / {len(questions)}")
        if score == len(questions):
            st.balloons()
else:
    st.info("Бұл сабақ үшін сұрақтар әлі қосылмаған. Сұрақтар базасын толтырыңыз.")
