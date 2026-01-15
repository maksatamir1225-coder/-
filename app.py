import streamlit as st

# Настройка страницы
st.set_page_config(page_title="Химия 10", layout="wide")

# Заголовок
st.title("🧪 Органикалық химия - 10 сынып")
st.subheader("19 сабақ | Әр сабақта 10 сұрақтан тест")

# 19 уроков с анимациями и формулами
lessons = [
    {"id": 1, "title": "Алкандар", "topic": "Қаныққан көмірсутектер", 
     "emoji": "⛽", "formula": "CₙH₂ₙ₊₂", "examples": "CH₄, C₂H₆, C₃H₈"},
    {"id": 2, "title": "Алкендер", "topic": "Қос байланыстар", 
     "emoji": "⚡", "formula": "CₙH₂ₙ", "examples": "C₂H₄, C₃H₆, C₄H₈"},
    {"id": 3, "title": "Алкиндер", "topic": "Үш байланыстар", 
     "emoji": "⚛️", "formula": "CₙH₂ₙ₋₂", "examples": "C₂H₂, C₃H₄, C₄H₆"},
    {"id": 4, "title": "Спирттер", "topic": "Гидроксил тобы", 
     "emoji": "🍷", "formula": "R-OH", "examples": "CH₃OH, C₂H₅OH, C₃H₇OH"},
    {"id": 5, "title": "Фенолдар", "topic": "Ароматтық спирттер", 
     "emoji": "🌺", "formula": "C₆H₅-OH", "examples": "Фенол, Крезол"},
    {"id": 6, "title": "Альдегидтер", "topic": "Карбонил тобы", 
     "emoji": "👑", "formula": "R-CHO", "examples": "HCHO, CH₃CHO, C₆H₅CHO"},
    {"id": 7, "title": "Кетондар", "topic": "Кето тобы", 
     "emoji": "🎯", "formula": "R-CO-R'", "examples": "CH₃COCH₃, C₆H₅COCH₃"},
    {"id": 8, "title": "Көмірсутектер салыстыру", "topic": "Алкан, Алкен, Алкин", 
     "emoji": "📊", "formula": "Сравнение", "examples": "Сравнительный анализ"},
    {"id": 9, "title": "Карбон қышқылдары", "topic": "Карбоксил тобы", 
     "emoji": "🍋", "formula": "R-COOH", "examples": "HCOOH, CH₃COOH, C₆H₅COOH"},
    {"id": 10, "title": "Эфирлер", "topic": "Сложный эфирлер", 
     "emoji": "🌸", "formula": "R-COO-R'", "examples": "CH₃COOC₂H₅, Этилацетат"},
    {"id": 11, "title": "Аминдар", "topic": "Амино тобы", 
     "emoji": "🐟", "formula": "R-NH₂", "examples": "CH₃NH₂, C₂H₅NH₂, C₆H₅NH₂"},
    {"id": 12, "title": "Аминқышқылдар", "topic": "Аминқышқылдар", 
     "emoji": "🧬", "formula": "H₂N-CHR-COOH", "examples": "Глицин, Аланин, Глутамин"},
    {"id": 13, "title": "Галогентуындылар", "topic": "Галогентуындылар", 
     "emoji": "☣️", "formula": "R-X", "examples": "CH₃Cl, C₂H₅Br, C₆H₅Cl"},
    {"id": 14, "title": "Нитросоединениялар", "topic": "Нитро тобы", 
     "emoji": "💥", "formula": "R-NO₂", "examples": "CH₃NO₂, C₆H₅NO₂"},
    {"id": 15, "title": "Сульфокислоталар", "topic": "Сульфо тобы", 
     "emoji": "🧪", "formula": "R-SO₃H", "examples": "C₆H₅-SO₃H, Метансульфокислота"},
    {"id": 16, "title": "Тотығу реакциялары", "topic": "Тотығу", 
     "emoji": "🔥", "formula": "[O]", "examples": "Окисление спиртов, альдегидов"},
    {"id": 17, "title": "Қосылу реакциялары", "topic": "Қосылу", 
     "emoji": "🤝", "formula": "A + B → C", "examples": "Присоединение к алкенам, алкинам"},
    {"id": 18, "title": "Ауыстыру реакциялары", "topic": "Ауыстыру", 
     "emoji": "🔄", "formula": "R-X + Nu → R-Nu + X", "examples": "SN1, SN2 реакции"},
    {"id": 19, "title": "Полимерлеу", "topic": "Полимерлер", 
     "emoji": "🧵", "formula": "nM → (M)ₙ", "examples": "Полиэтилен, Полистирол, Нейлон"},
]

# ВОПРОСЫ ДЛЯ ВСЕХ 19 УРОКОВ (остаются без изменений, как в вашем коде)
all_questions = {
    # УРОК 1: Алкандар (10 вопросов)
    1: [
        {"question": "1. Алкандардың жалпы формуласы:", 
         "options": ["А) CnH2n", "В) CnH2n+2", "С) CnH2n-2", "D) CnHn"], 
         "correct": 1},
        {"question": "2. Метан молекуласының пішіні қандай?", 
         "options": ["А) Тетраэдр", "В) Тригоналды", "С) Сызықты", "D) Жазық"], 
         "correct": 0},
        {"question": "3. Алкандардағы көміртек атомдары қандай гибридтенеді?", 
         "options": ["А) sp", "В) sp²", "С) sp³", "D) sp³d"], 
         "correct": 2},
        {"question": "4. Алкандарға тән негізгі реакция түрі:", 
         "options": ["А) Қосылу", "В) Ауыстыру", "С) Тотығу", "D) Конденсация"], 
         "correct": 1},
        {"question": "5. Метанның толық жану реакциясының өнімдері:", 
         "options": ["А) CO₂ + H₂", "В) CO + H₂O", "С) CO₂ + H₂O", "D) C + H₂O"], 
         "correct": 2},
        {"question": "6. Алкандар хлормен қандай реакцияға түседі?", 
         "options": ["А) Қосылу", "В) Тотығу", "С) Радикалды ауыстыру", "D) Ионды ауыстыру"], 
         "correct": 2},
        {"question": "7. Алкандар суда қалай ериді?", 
         "options": ["А) Жақсы ериді", "В) Нашар ериді", "С) Тек жоғары алкандар ериді", "D) Ерімейді"], 
         "correct": 1},
        {"question": "8. Пропанның формуласы:", 
         "options": ["А) CH₄", "В) C₂H₆", "С) C₃H₈", "D) C₄H₁₀"], 
         "correct": 2},
        {"question": "9. Изомерлер дегеніміз:", 
         "options": ["А) Бір формула, әртүрлі құрылым", "В) Әртүрлі формула", "С) Бір элемент", "D) Бір топ"], 
         "correct": 0},
        {"question": "10. Алкандар не үшін 'қаныққан' деп аталады?", 
         "options": ["А) Оттегі бар", "В) Қос байланыс жоқ", "С) Тотығады", "D) Галоген бар"], 
         "correct": 1}
    ],
    
    # УРОК 2: Алкендер (10 вопросов) и т.д. - все остальные вопросы как у вас
    # ... (остальные 18 уроков с вопросами остаются без изменений)
    2: [
        {"question": "1. Алкендердің жалпы формуласы:", 
         "options": ["А) CnH2n", "В) CnH2n+2", "С) CnH2n-2", "D) CnHn"], 
         "correct": 0},
        {"question": "2. Этилен молекуласының кеңістіктік құрылымы қандай?", 
         "options": ["А) Тетраэдр", "В) Тригоналды", "С) Сызықты", "D) Жазық"], 
         "correct": 3},
        {"question": "3. Қос байланыс қандай электрондардан тұрады?", 
         "options": ["А) 1 σ және 1 π", "В) 2 σ", "С) 1 σ және 2 π", "D) 2 π"], 
         "correct": 0},
        {"question": "4. Алкендердің негізгі реакция түрі:", 
         "options": ["А) Ауыстыру", "В) Қосылу", "С) Тотығу", "D) Ыдырау"], 
         "correct": 1},
        {"question": "5. Этилен бромсумен қандай реакцияға түседі?", 
         "options": ["А) Ауыстыру", "В) Қосылу", "С) Тотығу", "D) Конденсация"], 
         "correct": 1},
        {"question": "6. Марковников ережесіне сәйкес қосылу кезінде:", 
         "options": ["А) Сутек көбірек сутек бар көміртектің", "В) Галоген көбірек сутек бар көміртектің", "С) Екеуі де дұрыс", "D) Екеуі де дұрыс емес"], 
         "correct": 1},
        {"question": "7. Алкендерден қандай полимерлер алынады?", 
         "options": ["А) Полиэтилен", "В) Поливинилхлорид", "С) Полипропилен", "D) Барлығы"], 
         "correct": 3},
        {"question": "8. Этиленнің формуласы:", 
         "options": ["А) CH₄", "В) C₂H₄", "С) C₂H₂", "D) C₃H₆"], 
         "correct": 1},
        {"question": "9. KMnO₄ ерітіндісі алкендердің қасиетін қалай өзгертеді?", 
         "options": ["А) Түсін өзгертеді", "В) Түсін өзгертпейді", "С) Тұнба түзееді", "D) Газ бөледі"], 
         "correct": 0},
        {"question": "10. Циклоалкандардың жалпы формуласы:", 
         "options": ["А) CnH2n", "В) CnH2n+2", "С) CnH2n-2", "D) CnHn"], 
         "correct": 0}
    ],
    
    # Добавьте остальные уроки как у вас...
    # 3-19 уроки...
}

# Инициализация состояния
if "current_lesson" not in st.session_state:
    st.session_state.current_lesson = None
if "answers" not in st.session_state:
    st.session_state.answers = {}
if "test_completed" not in st.session_state:
    st.session_state.test_completed = {}

# Главное меню с улучшенным дизайном
st.write("### 📚 19 сабақты таңдаңыз:")

# Создаем контейнеры для уроков с использованием columns
for i in range(0, len(lessons), 3):
    cols = st.columns(3)
    for j in range(3):
        if i + j < len(lessons):
            lesson = lessons[i + j]
            lesson_id = lesson["id"]
            
            with cols[j]:
                # Стилизованная карточка урока
                container = st.container(border=True)
                
                with container:
                    # Заголовок с эмодзи
                    st.markdown(f"### {lesson['emoji']} **Сабақ {lesson_id}: {lesson['title']}**")
                    
                    # Формула
                    st.markdown(f"**Формула:** `{lesson['formula']}`")
                    
                    # Примеры
                    st.markdown(f"**Мысалдар:** {lesson['examples']}")
                    
                    # Статус теста
                    if lesson_id in st.session_state.test_completed:
                        score = st.session_state.test_completed[lesson_id]
                        st.success(f"✅ **Нәтиже: {score}/10**", icon="✅")
                    else:
                        st.info("📝 **Тест берілмеген**", icon="📝")
                    
                    # Кнопка для выбора урока
                    if st.button(f"Сабақты бастау", 
                                 key=f"btn_{lesson_id}",
                                 use_container_width=True,
                                 type="primary"):
                        st.session_state.current_lesson = lesson_id
                        st.rerun()

# Если урок выбран
if st.session_state.current_lesson:
    lesson_id = st.session_state.current_lesson
    lesson = lessons[lesson_id-1]
    
    st.markdown("---")
    
    # Заголовок урока с анимацией
    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        st.markdown(f"<h1 style='text-align: center;'>{lesson['emoji']} Сабақ {lesson_id}: {lesson['title']}</h1>", 
                   unsafe_allow_html=True)
    
    # Информация о классе соединений
    st.markdown(f"""
    <div style='background-color: #f0f2f6; padding: 20px; border-radius: 10px;'>
        <h3>📋 Сабақ туралы ақпарат:</h3>
        <p><strong>Тақырып:</strong> {lesson['topic']}</p>
        <p><strong>Жалпы формула:</strong> <code>{lesson['formula']}</code></p>
        <p><strong>Негізгі мысалдар:</strong> {lesson['examples']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Тест
    st.write("### ✅ Тест (10 сұрақ)")
    
    if lesson_id in all_questions:
        questions = all_questions[lesson_id]
        
        # Проверяем, завершен ли тест
        if lesson_id in st.session_state.test_completed:
            score = st.session_state.test_completed[lesson_id]
            
            # Показываем результат
            if score >= 8:
                st.balloons()
                st.success(f"## 🎉 Керемет! Нәтиже: {score}/10")
            elif score >= 5:
                st.success(f"## 👍 Жақсы! Нәтиже: {score}/10")
            else:
                st.warning(f"## 📚 Қайталау керек! Нәтиже: {score}/10")
            
            # Прогресс бар
            st.progress(score/10)
            
            # Показываем правильные ответы
            with st.expander("📖 Тест жауаптарын көру"):
                for i, q in enumerate(questions):
                    st.write(f"**{i+1}. {q['question']}**")
                    correct_answer = q['options'][q['correct']]
                    st.info(f"✅ **Дұрыс жауап:** {correct_answer}")
            
            # Кнопки управления
            col1, col2 = st.columns(2)
            with col1:
                if st.button("🔄 Тестті қайта тапсыру", use_container_width=True):
                    st.session_state.test_completed.pop(lesson_id, None)
                    st.session_state.answers.pop(lesson_id, None)
                    st.rerun()
            with col2:
                if st.button("🏠 Басты бетке қайту", use_container_width=True):
                    st.session_state.current_lesson = None
                    st.rerun()
                    
        else:
            # Тестирование
            user_answers = st.session_state.answers.get(lesson_id, {})
            score = 0
            
            # Прогресс тестирования
            progress = len(user_answers) / len(questions)
            st.progress(progress)
            st.caption(f"Өткізілді: {len(user_answers)}/{len(questions)} сұрақ")
            
            for i, q in enumerate(questions):
                st.write(f"**{q['question']}**")
                
                # Если уже отвечали
                if i in user_answers:
                    user_answer_index = user_answers[i]
                    user_answer = q['options'][user_answer_index]
                    is_correct = (user_answer_index == q['correct'])
                    
                    if is_correct:
                        st.success(f"✓ Сіздің жауабыңыз: **{user_answer}**")
                        score += 1
                    else:
                        st.error(f"✗ Сіздің жауабыңыз: {user_answer}")
                        correct_answer = q['options'][q['correct']]
                        st.info(f"✅ Дұрыс жауап: **{correct_answer}**")
                else:
                    # Выбор ответа с улучшенным дизайном
                    cols = st.columns(4)
                    for idx, option in enumerate(q["options"]):
                        with cols[idx % 4]:
                            if st.button(option, 
                                       key=f"option_{lesson_id}_{i}_{idx}",
                                       use_container_width=True,
                                       type="secondary"):
                                if lesson_id not in st.session_state.answers:
                                    st.session_state.answers[lesson_id] = {}
                                st.session_state.answers[lesson_id][i] = idx
                                st.rerun()
                
                st.write("---")
            
            # Кнопка завершения теста
            if len(user_answers) == len(questions):
                percentage = (score / len(questions)) * 100
                
                st.markdown(f"""
                <div style='background-color: #e8f4fd; padding: 15px; border-radius: 10px; border-left: 5px solid #2196F3;'>
                    <h4>📊 Тест аяқталды!</h4>
                    <p><strong>Сіздің ұпайыңыз:</strong> {score}/{len(questions)}</p>
                    <p><strong>Процент:</strong> {percentage:.1f}%</p>
                </div>
                """, unsafe_allow_html=True)
                
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("✅ Тестті аяқтау", 
                               type="primary", 
                               use_container_width=True,
                               icon="✅"):
                        st.session_state.test_completed[lesson_id] = score
                        st.rerun()
                
                with col2:
                    if st.button("🔄 Жауаптарды өзгерту", 
                               type="secondary", 
                               use_container_width=True,
                               icon="🔄"):
                        st.session_state.answers[lesson_id] = {}
                        st.rerun()
    
    # Кнопка назад всегда видна
    if st.button("← Басты бетке қайту", icon="🏠"):
        st.session_state.current_lesson = None
        st.rerun()

# Общая статистика в сайдбаре
with st.sidebar:
    st.markdown("## 📊 Жалпы статистика")
    
    completed_count = len(st.session_state.test_completed)
    total_score = sum(st.session_state.test_completed.values()) if st.session_state.test_completed else 0
    max_score = completed_count * 10
    total_possible = 190  # 19 уроков × 10 вопросов
    
    # Прогресс всех тестов
    overall_progress = completed_count / 19
    st.progress(overall_progress)
    
    # Показатели
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Өтілген сабақтар", f"{completed_count}/19")
    with col2:
        st.metric("Жалпы ұпай", f"{total_score}/{max_score}")
    
    # Дополнительная статистика
    st.markdown("---")
    st.markdown("### 🏆 Ең жақсы нәтижелер")
    
    if st.session_state.test_completed:
        sorted_scores = sorted(st.session_state.test_completed.items(), 
                              key=lambda x: x[1], 
                              reverse=True)[:5]
        
        for lesson_id, score in sorted_scores:
            lesson = lessons[lesson_id-1]
            st.write(f"{lesson['emoji']} **Сабақ {lesson_id}:** {score}/10")
    else:
        st.info("Әлі тест берілмеген")
    
    # Общая информация
    st.markdown("---")
    st.markdown("### ℹ️ Ақпарат")
    st.write(f"**Барлығы:** 19 сабақ")
    st.write(f"**Барлық сұрақтар:** 190")
    st.write(f"**Тақырыптар:** органикалық химияның негізгі бөлімдері")
    
    # Контактная информация
    st.markdown("---")
    st.markdown("### 👨‍🔬 Автор")
    st.write("Химия пәнінің мұғалімі")
    st.write("10 сынып, органикалық химия")
    st.write("Барлық құқықтар қорғалған © 2024")

# Футер
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray;'>
    <p>🏫 <strong>Химия 10 сынып - Органикалық химия курсы</strong></p>
    <p>Барлық 19 сабақ органикалық химияның негізгі тақырыптарын қамтиды</p>
</div>
""", unsafe_allow_html=True)
