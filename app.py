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

    /* Эффект падающих/летающих сердечек на фоне */
    .stApp::before {
        content: '💖';
        position: absolute;
        top: -50px;
        left: 10%;
        font-size: 24px;
        animation: airborneHearts 6s linear infinite;
        opacity: 0.6;
    }
    .stApp::after {
        content: '💝';
        position: absolute;
        top: -50px;
        left: 80%;
        font-size: 30px;
        animation: airborneHearts 8s linear infinite;
        animation-delay: 3s;
        opacity: 0.5;
    }

    @keyframes airborneHearts {
        0% { transform: translateY(0) rotate(0deg); opacity: 0; }
        10% { opacity: 0.6; }
        90% { opacity: 0.6; }
        100% { transform: translateY(105vh) rotate(360deg); opacity: 0; }
    }

    /* Пульсирующие милые кнопки */
    .stButton>button {
        background: linear-gradient(135deg, #FF69B4, #FF1493) !important;
        color: white !important; 
        border-radius: 30px !important; 
        padding: 14px 35px !important;
        font-size: 22px !important; 
        font-weight: bold !important;
        border: none !important; 
        width: 100% !important;
        box-shadow: 0 6px 20px rgba(255, 20, 147, 0.4);
        transition: all 0.3s ease-in-out !important;
        animation: heartbeat 2s infinite;
    }
    
    .stButton>button:hover {
        transform: scale(1.07) !important;
        box-shadow: 0 8px 25px rgba(255, 20, 147, 0.7);
    }

    @keyframes heartbeat {
        0% { transform: scale(1); }
        50% { transform: scale(1.04); }
        100% { transform: scale(1); }
    }

    /* Полупрозрачная матовая карточка как на видео */
    .block-container {
        background: rgba(255, 255, 255, 0.82);
        padding: 2.5rem !important;
        border-radius: 35px;
        box-shadow: 0 15px 35px rgba(255, 105, 180, 0.15);
        backdrop-filter: blur(12px);
        border: 2px solid rgba(255, 192, 203, 0.5);
        margin-top: 30px;
    }

    /* Плавное всплывание контента */
    h1, h2, h3, p, .stImage {
        color: #C71585 !important; 
        text-align: center;
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

# --- ШАГ 1: Главный вопрос ---
if st.session_state.step == 1:
    st.write("### 💌 Тебе пришло секретное послание...")
    # Котик дарит розочку (анимированный GIF)
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExM3YwZzM1ZXF0ZnV6ODZ5dzN2NzhwYW5uOHV3am96bXNreGd0YTY3NiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/G7e0gYIPscf8B0wD7R/giphy.gif", width=250)
    st.write("## Ты пойдешь со мной на свидание?")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Да! 🥰"):
            st.session_state.step = 2
            st.rerun()
    with col2:
        if st.button("Нет... 🐾"):
            st.balloons()
            st.toast("Системная ошибка: Кнопка 'Нет' сломалась под тяжестью моей любви! Перенаправление на 'ДА'... 🤭")
            time.sleep(2)
            st.session_state.step = 2
            st.rerun()

# --- ШАГ 2: Удивление ---
elif st.session_state.step == 2:
    # Котики обнимаются
    st.image("https://media.giphy.com/media/v1.
    st.write("## Подожди... Реально «ДА»?!")
    st.write("Ура! Я самый счастливый айтишник в мире! Давай подберем идеальные параметры нашей встречи 👇")
    
    if st.button("Перейти к настройкам вечера! ✨"):
        st.session_state.step = 3
        st.rerun()

# --- ШАГ 3: Настройки свидания (Календарь и Еда) ---
elif st.session_state.step == 3:
    # Мишка с розовым воздушным шариком сердечком
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbDVqbmY4MXMzdXF1ZHd3ZmUwb3VhdDV2MGg0aTUzcnloZWU5bnU1MyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/kbymazz3er6WUr08u7/giphy.gif", width=180)
    st.write("## И тааак... Когда ты свободна?")
    
    date = st.date_input("Выбери день 📅")
    time_choice = st.time_input("Удобное время ⏰")
    
    st.write("### Что ты хочешь покушать? 🍕")
    food = st.selectbox(
        "Выбери то, что тебе в кайф:",
        ["🍣 Суши / Роллы", "🍕 Горячая пицца", "🍔 Сочные бургеры", "🍝 Паста", "🍜 Пряный Рамен", "☕️ Кофе и десерты"]
    )
    
    if st.button("Залогировать идеальный план! 🚀"):
        st.session_state.date = date
        st.session_state.time = time_choice
        st.session_state.food = food
        st.session_state.step = 4
        st.rerun()

# --- ШАГ 4: Финал ---
elif st.session_state.step == 4:
    st.balloons()
    # Котик, который уплетает спагетти/пасту из видео!
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHgzajk5bThncWoxZHd3Mms2OGF3cHlsajJ1ZDJpM3FwN3A5MTZnbSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/L33yqQf8UT6FmOAzGO/giphy.gif", width=230)
    st.write("## Рад, что ты не отказалась!")
    
    formatted_date = st.session_state.date.strftime("%d.%m.%Y")
    formatted_time = st.session_state.time.strftime("%H:%M")
    
    st.success(f"""
    План свидания успешно закоммичен:
    * Когда встречаемся: {formatted_date} в {formatted_time}
    * Меню вечера: {st.session_state.food}
    
    Будь готова к этому времени, я приеду и заберу тебя! Скриншот отправлять не нужно, логи уже у меня на сервере. 😘
    """)
    
    if st.button("Пройти опрос заново 🔄"):
        st.session_state.step = 1
        st.rerun()
