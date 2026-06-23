import streamlit as st
import time

# Настройка страницы
st.set_page_config(page_title="Приглашение для тебя ✨", page_icon="🐱", layout="centered")

# Кастомные стили для романтической атмосферы
st.markdown("""
    <style>
    .main { background-color: #FFF5F5; }
    h1, h2, h3 { color: #D53F8C !important; text-align: center; }
    .stButton>button {
        background-color: #ED64A6; color: white; 
        border-radius: 20px; padding: 10px 25px;
        font-size: 18px; border: none; width: 100%;
    }
    .stButton>button:hover { background-color: #D53F8C; color: white; }
    div.stDateInput > div { border-radius: 15px; }
    </style>
""", unsafe_allow_html=True)

# Инициализация состояний шагов
if 'step' not in st.session_state:
    st.session_state.step = 1

# --- ШАГ 1: Главный вопрос ---
if st.session_state.step == 1:
    st.write("### 💌 Тебе пришло новое сообщение...")
    st.markdown("<h1 style='font-size: 60px;'>🐱❤️🐈</h1>", unsafe_allow_html=True)
    st.write("## Ты пойдешь со мной на свидание?")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Да! 🥰"):
            st.session_state.step = 2
            st.rerun()
    with col2:
        # Кнопка "Нет", которая при нажатии всё равно ведет на согласие, как в лучших традициях!
        if st.button("Нет... 🐾"):
            st.balloons()
            st.toast("Ошибка доступа! Кнопка 'Нет' временно недоступна. Автоматически выбрано 'ДА'! 😉")
            time.sleep(1.5)
            st.session_state.step = 2
            st.rerun()

# --- ШАГ 2: Проверка на удивление ---
elif st.session_state.step == 2:
    st.markdown("<h1 style='font-size: 60px;'>🙀💝</h1>", unsafe_allow_html=True)
    st.write("## Подожди, ты действительно сказала «ДА»?!")
    st.write("Я был уверен, что придется пускать в ход мемы с котами для уговоров... Твоё согласие официально залогировано! ✅")
    
    if st.button("Да, переходим к деталям! 🚀"):
        st.session_state.step = 3
        st.rerun()

# --- ШАГ 3: Выбор даты, времени и еды ---
elif st.session_state.step == 3:
    st.markdown("<h1 style='font-size: 60px;'>🐻🎈</h1>", unsafe_allow_html=True)
    st.write("## И тааак... Настраиваем наше свидание")
    
    # Выбор даты и времени
    date = st.date_input("Выбери удобную дату 📅")
    time_choice = st.time_input("Выбери время ⏰")
    
    # Выбор кухни (как на видео)
    st.write("### Что ты хочешь покушать? 🍕")
    food = st.selectbox(
        "Выбери то, что тебе в кайф:",
        ["🍣 Суши / Роллы", "🍕 Пицца", "🍔 Бургеры", "🍝 Паста", "🍜 Рамен", "☕️ Кофе и десерты"]
    )
    
    if st.button("Подтвердить идеальный план ✨"):
        st.session_state.date = date
        st.session_state.time = time_choice
        st.session_state.food = food
        st.session_state.step = 4
        st.rerun()

# --- ШАГ 4: Финал ---
elif st.session_state.step == 4:
    st.balloons()
    st.markdown("<h1 style='font-size: 60px;'>🍝❤️👩‍❤️‍👨</h1>", unsafe_allow_html=True)
    st.write("## Рад, что ты не отказалась!")
    
    # Форматируем красивый вывод
    formatted_date = st.session_state.date.strftime("%d.%m.%Y")
    formatted_time = st.session_state.time.strftime("%H:%M")
    
    st.info(f"""
    План перехвачен и утвержден:
    * Когда: {formatted_date} в {formatted_time}
    * Меню вечера: {st.session_state.food}
    
    Будь готова к этому времени, я заеду за тобой! Напиши мне в чат, как изучишь логи. 😘
    """)
    
    if st.button("Пройти опрос заново 🔄"):
        st.session_state.step = 1
        st.rerun()