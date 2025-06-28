
import streamlit as st
from PIL import Image
import requests
import random
from io import BytesIO
from datetime import datetime

st.set_page_config(page_title="Ancient Tarot Oracle", layout="centered")

st.markdown("""
    <style>
    html, body, [class*="css"] {
        background-color: #f4efe2;
        color: #3b2f2f;
        font-family: "Papyrus", fantasy;
    }
    .title {
        font-size: 2.5em;
        font-weight: bold;
        text-align: center;
        text-shadow: 1px 1px #b4975a;
        margin-bottom: 30px;
    }
    .card-name {
        font-size: 1.6em;
        text-align: center;
        margin-top: 10px;
        margin-bottom: 10px;
    }
    .reading-box {
        background-color: #fff8e7;
        padding: 20px;
        border: 2px solid #b4975a;
        border-radius: 10px;
        box-shadow: 2px 2px 12px #b4975a;
        font-size: 1.1em;
    }
    </style>
""", unsafe_allow_html=True)

tarot_cards = [
    {"name": "The Fool", "image_url": "https://upload.wikimedia.org/wikipedia/en/9/90/RWS_Tarot_00_Fool.jpg"},
    {"name": "The Magician", "image_url": "https://upload.wikimedia.org/wikipedia/en/d/de/RWS_Tarot_01_Magician.jpg"},
    {"name": "The High Priestess", "image_url": "https://upload.wikimedia.org/wikipedia/en/8/88/RWS_Tarot_02_High_Priestess.jpg"},
    # Add more...
]


st.markdown("<div class='title'>🕯️ Ancient Tarot Oracle 🕯️<br><i>Unearthed from the Sands of Time</i></div>", unsafe_allow_html=True)

birth_input = st.text_input("Enter your birth date (DD/MM/YYYY):")
if birth_input:
    try:
        birth_date = datetime.strptime(birth_input, "%d/%m/%Y")
        card = random.choice(tarot_cards)
        response = requests.get(card["image_url"])
        image = Image.open(BytesIO(response.content))
        st.image(image, caption=card["name"], use_column_width=True)
        st.markdown(f"<div class='card-name'>{card['name']}</div>", unsafe_allow_html=True)
        st.markdown(f"""
        <div class='reading-box'>
        <b>Reading:</b><br>
        You were born under a celestial alignment hidden in the heavens.<br><br>
        The card revealed to you — <i>{card['name']}</i> — whispers of ancient forces and forgotten truths. <br><br>
        This card, once sealed in stone, calls to your essence. Seek its lesson with heart open, and the forgotten path shall reawaken.
        </div>
        """, unsafe_allow_html=True)
    except ValueError:
        st.error("Please enter a valid date in DD/MM/YYYY format.")
