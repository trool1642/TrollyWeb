import streamlit as st
import time

# Настройка страницы
st.set_page_config(page_title="Приглашение для тебя ✨", page_icon="🐱", layout="centered")

# --- МЕГА-СТИЛИ С АНИМАЦИЕЙ ЛЕТАЮЩИХ СЕРДЕЧЕК (CSS) ---
st.markdown("""
    <style>
    /* Анимированный нежный фон */
    .stApp {
        background: linear-gradient(-45deg, #FFF0F5, #FFE4E1, #FFC0CB, #FFF0F5);
        background-size: 400% 400%;
        animation: gradient 12s ease infinite;
        overflow: hidden;
    }
    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Эффект падающих сердечек на фоне */
    .stApp::before {
        content: '💖'; position: absolute; top: -50px; left: 10%;
        font-size: 30px; animation: airborneHearts 6s linear infinite; opacity: 0.6;
    }
    .stApp::after {
        content: '💝'; position: absolute; top: -50px; left: 85%;
        font-size: 35px; animation: airborneHearts 8s linear infinite;
        animation-delay: 3s; opacity: 0.5;
    }

    @keyframes airborneHearts {
        0% { transform: translateY(0) rotate(0deg); opacity: 0; }
        10% { opacity: 0.6; }
        90% { opacity: 0.6; }
        100% { transform: translateY(105vh) rotate(360deg); opacity: 0; }
    }

    /* Пульсирующие кнопки */
    .stButton>button {
        background: linear-gradient(135deg, #FF69B4, #FF1493) !important;
        color: white !important; border-radius: 30px !important; 
        padding: 14px 35px !important; font-size: 22px !important; 
        font-weight: bold !important; border: none !important; 
        width: 100% !important; box-shadow: 0 6px 20px rgba(255, 20, 147, 0.4);
        transition: all 0.3s ease-in-out !important; animation: heartbeat 2s infinite;
    }
    .stButton>button:hover {
        transform: scale(1.07) !important; box-shadow: 0 8px 25px rgba(255, 20, 147, 0.7);
    }
    @keyframes heartbeat {
        0% { transform: scale(1); }
        50% { transform: scale(1.04); }
        100% { transform: scale(1); }
    }

    /* Анимированные крупные эмодзи вместо картинок */
    .big-cat {
        font-size: 100px;
        text-align: center;
        margin: 20px 0;
        animation: float 3s ease-in-out infinite;
    }
    @keyframes float {
        0% { transform: translateY(0px) rotate(0deg); }
        50% { transform: translateY(-15px) rotate(3deg); }
        100% { transform: translateY(0px) rotate(0deg); }
    }

    /* Полупрозрачная матовая карточка */
    .block-container {
        background: rgba(255, 255, 255, 0.85); padding: 2.5rem !important;
        border-radius: 35px; box-shadow: 0 15px 35px rgba(255, 105, 180, 0.15);
        backdrop-filter: blur(12px); border: 2px solid rgba(255, 192, 203, 0.5);
        margin-top: 30px;
    }

    h1, h2, h3, p {
        color: #C71585 !important; text-align: center;
        animation: popUp 1s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }
    @keyframes popUp {
        from { opacity: 0; transform: scale(0.8) translateY(20px); }
        to { opacity: 1; transform: scale(1) translateY(0); }
    }
    </style>
""", unsafe_allow_html=True)

# Инициализация состояний шагов
if 'step' not in st.session_state:
    st.session_state.step = 1

# --- ШАГ 1 ---
if st.session_state.step == 1:
    st.write("### 💌 Тебе пришло секретное послание...")
    st.markdown('<div class="big-cat">🐱🌹</div>', unsafe_allow_html=True)
    st.write("## Ты пойдешь со мной на свидание?")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Да! 🥰"):
            st.session_state.step = 2
            st.rerun()
    with col2:
        if st.button("Нет... 🐾"):
            st.balloons()
            st.toast("Кнопка 'Нет' временно сломалась от любви! Автовыбор: ДА! 🤭")
            time.sleep(1.5)
            st.session_state.step = 2
            st.rerun()

# --- ШАГ 2 ---
elif st.session_state.step == 2:
    st.markdown('<div class="big-cat">🐱❤️🐈</div>', unsafe_allow_html=True)
    st.write("## Подожди... Реально «ДА»?!")
    st.write("Ура! Я самый счастливый человек! Давай настроим нашу встречу 👇")
    
    if st.button("Выбрать время и еду! ✨"):
        st.session_state.step = 3
        st.rerun()

# --- ШАГ 3 ---
elif st.session_state.step == 3:
    st.markdown('<div class="big-cat">🧸🎈</div>', unsafe_allow_html=True)
    st.write("## Когда ты свободна?")
    
    date = st.date_input("Выбери день 📅")
    time_choice = st.time_input("Удобное время ⏰")
    
    st.write("### Что ты хочешь покушать? 🍕")
    food = st.selectbox(
        "Выбери то, что тебе в кайф:",
        ["🍣 Суши / Роллы", "🍕 Горячая пицца", "🍔 Сочные бургеры", "🍝 Итальянская паста", "🍜 Пряный Рамен", "☕️ Кофе и десерты"]
    )
    
    if st.button("Зафиксировать идеальный план! 🚀"):
        st.session_state.date = date
        st.session_state.time = time_choice
        st.session_state.food = food
        st.session_state.step = 4
        st.rerun()

# --- ШАГ 4 ---
elif st.session_state.step == 4:
    st.balloons()
    st.markdown('<div class="big-cat">🐈🍝🤵</div>', unsafe_allow_html=True)
    st.write("## Рад, что ты не отказалась!")
    
    formatted_date = st.session_state.date.strftime("%d.%m.%Y")
    formatted_time = st.session_state.time.strftime("%H:%M")
    
    st.success(f"""
    План свидания успешно утвержден:
    * Дата встречи: {formatted_date}
    * Время: {formatted_time}
    * В меню вечера: {st.session_state.food}
    
    Будь готова к этому времени, я приеду за тобой! Логи сохранены на сервере. 😘
    """)
    
    if st.button("Пройти опрос заново 🔄"):
        st.session_state.step = 1
        st.rerun()
