import streamlit as st
import time

# Настройка страницы
st.set_page_config(page_title="Приглашение для тебя ✨", page_icon="🐱", layout="centered")

# --- МЕГА-СТИЛИ С АНИМАЦИЯМИ (CSS) ---
st.markdown("""
    <style>
    /* Анимированный градиентный фон */
    .stApp {
        background: linear-gradient(-45deg, #FFF5F5, #FED7E2, #FBB6CE, #FFF5F5);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
    }
    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Стилизация и анимация кнопок */
    .stButton>button {
        background-color: #ED64A6 !important; 
        color: white !important; 
        border-radius: 25px !important; 
        padding: 12px 30px !important;
        font-size: 20px !important; 
        font-weight: bold !important;
        border: none !important; 
        width: 100% !important;
        box-shadow: 0 4px 15px rgba(237, 100, 166, 0.4);
        transition: all 0.3s ease-in-out !important;
        animation: pulse 2s infinite; /* Эффект пульсации */
    }
    
    /* Эффект при наведении на кнопку */
    .stButton>button:hover {
        transform: scale(1.05) !important;
        background-color: #D53F8C !important;
        box-shadow: 0 6px 20px rgba(213, 63, 140, 0.6);
    }

    /* Анимация пульсации для кнопок */
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.03); }
        100% { transform: scale(1); }
    }

    /* Красивый контейнер для контента */
    .block-container {
        background: rgba(255, 255, 255, 0.75);
        padding: 2rem !important;
        border-radius: 30px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.05);
        backdrop-filter: blur(10px); /* Эффект размытия стекла */
        margin-top: 20px;
    }

    /* Анимация появления текста */
    h1, h2, h3, p {
        color: #B83280 !important; 
        text-align: center;
        animation: fadeIn 1.2s ease-in-out;
    }
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    </style>
""", unsafe_allow_html=True)

# Инициализация состояний шагов
if 'step' not in st.session_state:
    st.session_state.step = 1

# --- ШАГ 1: Главный вопрос ---
if st.session_state.step == 1:
    st.write("### 💌 Тебе пришло интерактивное сообщение...")
    st.markdown("<h1 style='font-size: 70px; text-align: center; animation: pulse 1.5s infinite;'>🐱❤️🐈</h1>", unsafe_allow_html=True)
    st.write("## Ты пойдешь со мной на свидание?")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Да! 🥰"):
            st.session_state.step = 2
            st.rerun()
    with col2:
        if st.button("Нет... 🐾"):
            st.balloons()
            st.toast("Ошибка 404: Вариант 'Нет' заблокирован купидоном! Автоматический выбор: ДА! 🤭")
            time.sleep(1.5)
            st.session_state.step = 2
            st.rerun()

# --- ШАГ 2: Удивление ---
elif st.session_state.step == 2:
    st.markdown("<h1 style='font-size: 70px; text-align: center;'>🙀💝</h1>", unsafe_allow_html=True)
    st.write("## Подожди... Ты действительно сказала «ДА»?!")
    st.write("Мой мимиметр только что взорвался! Переходим к калибровке деталей встречи. ⚙️")
    
    if st.button("Выбрать время и еду! 🚀"):
        st.session_state.step = 3
        st.rerun()

# --- ШАГ 3: Выбор параметров ---
elif st.session_state.step == 3:
    st.markdown("<h1 style='font-size: 70px; text-align: center;'>🐻🎈</h1>", unsafe_allow_html=True)
    st.write("## Настраиваем идеальный вечер")
    
    # Инпуты
    date = st.date_input("Выбери день для свидания 📅")
    time_choice = st.time_input("Удобное время ⏰")
    
    st.write("### Что будем кушать? 🍕")
    food = st.selectbox(
        "Выбери то, что тебе в кайф:",
        ["🍣 Суши / Роллы", "🍕 Горячая пицца", "🍔 Сочные бургеры", "🍝 Паста", "🍜 Пряный Рамен", "☕ Кофе и десерты"]
    )
    
    if st.button("Утвердить план свидания ✨"):
        st.session_state.date = date
        st.session_state.time = time_choice
        st.session_state.food = food
        st.session_state.step = 4
        st.rerun()

# --- ШАГ 4: Финал ---
elif st.session_state.step == 4:
    st.balloons() # Запуск анимации шаров на весь экран
    st.markdown("<h1 style='font-size: 70px; text-align: center;'>🍝❤️👩‍❤️‍👨</h1>", unsafe_allow_html=True)
    st.write("## Логи приняты, свидание назначено!")
    
    formatted_date = st.session_state.date.strftime("%d.%m.%Y")
    formatted_time = st.session_state.time.strftime("%H:%M")
    
    st.success(f"""
    Твой персональный айтишник всё забронировал:
    * Дата: {formatted_date}
    * Время: {formatted_time}
    * В меню вечера: {st.session_state.food}
    
    Будь готова к этому времени, я приеду за тобой! Напиши мне, как закроешь вкладку. 😘
    """)
    
    if st.button("Пройти заново 🔄"):
        st.session_state.step = 1
        st.rerun()
