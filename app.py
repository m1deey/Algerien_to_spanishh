import streamlit as st
import streamlit.components.v1 as components
import json
import html


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Dzayer → Español",
    page_icon="🇩🇿",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# =========================================================
# DATA — Algerian Darija → Natural Spanish
# Translations are equivalence-based, not word-for-word,
# and deliberately varied so similar phrases don't collapse
# into the same Spanish output.
# =========================================================

WORDS = [

    # ---------------- GREETINGS ----------------
    {"category": "👋 Saludos", "dz": "السلام عليكم", "roman": "Salam 3likom",
     "es": "Hola, ¿qué tal?", "meaning": "Hello (formal greeting)"},
    {"category": "👋 Saludos", "dz": "وعليكم السلام", "roman": "Wa 3likom salam",
     "es": "¡Hola, igualmente!", "meaning": "Hello / reply to greeting"},
    {"category": "👋 Saludos", "dz": "واش راك؟", "roman": "Wach rak?",
     "es": "¿Qué tal estás?", "meaning": "How are you? (to a man)"},
    {"category": "👋 Saludos", "dz": "واش راكي؟", "roman": "Wach raki?",
     "es": "¿Cómo te va?", "meaning": "How are you? (to a woman)"},
    {"category": "👋 Saludos", "dz": "لاباس؟", "roman": "Labas?",
     "es": "¿Todo en orden?", "meaning": "Everything good?"},
    {"category": "👋 Saludos", "dz": "صباح الخير", "roman": "Sbah el-khir",
     "es": "Buenos días", "meaning": "Good morning"},
    {"category": "👋 Saludos", "dz": "مساء الخير", "roman": "Msa el-khir",
     "es": "Buenas tardes", "meaning": "Good afternoon / evening"},
    {"category": "👋 Saludos", "dz": "أهلا", "roman": "Ahlan",
     "es": "¡Bienvenido!", "meaning": "Hi / welcome"},
    {"category": "👋 Saludos", "dz": "بسلامة", "roman": "Bslama",
     "es": "Nos vemos", "meaning": "Goodbye"},
    {"category": "👋 Saludos", "dz": "صحا", "roman": "Saha",
     "es": "¡Cuídate!", "meaning": "Take care / good health"},

    # ---------------- EVERYDAY ----------------
    {"category": "🗣️ Cotidiano", "dz": "مليح", "roman": "Mlih",
     "es": "Bien", "meaning": "Good / fine"},
    {"category": "🗣️ Cotidiano", "dz": "لاباس الحمد لله", "roman": "Labas, hamdullah",
     "es": "Bien, gracias a Dios", "meaning": "I'm fine, thank God"},
    {"category": "🗣️ Cotidiano", "dz": "كولشي مليح", "roman": "Kolchi mlih",
     "es": "Todo marcha bien", "meaning": "Everything is good"},
    {"category": "🗣️ Cotidiano", "dz": "ماشي مشكل", "roman": "Machi mochkil",
     "es": "No pasa nada", "meaning": "No problem"},
    {"category": "🗣️ Cotidiano", "dz": "ماعلاباليش", "roman": "Ma 3labalich",
     "es": "Ni idea", "meaning": "I don't know"},
    {"category": "🗣️ Cotidiano", "dz": "ما فهمتش", "roman": "Ma fhemtch",
     "es": "No te entiendo", "meaning": "I don't understand"},
    {"category": "🗣️ Cotidiano", "dz": "فهمت", "roman": "Fhemt",
     "es": "Ya capté", "meaning": "I understand / got it"},
    {"category": "🗣️ Cotidiano", "dz": "واش ندير؟", "roman": "Wach ndir?",
     "es": "¿Y ahora qué hago?", "meaning": "What should I do?"},
    {"category": "🗣️ Cotidiano", "dz": "واش درت؟", "roman": "Wach dert?",
     "es": "¿Qué has hecho?", "meaning": "What did you do?"},
    {"category": "🗣️ Cotidiano", "dz": "واش كاين؟", "roman": "Wach kayen?",
     "es": "¿Qué onda?", "meaning": "What's going on?"},
    {"category": "🗣️ Cotidiano", "dz": "كاين", "roman": "Kayen",
     "es": "Sí hay", "meaning": "There is / there are"},
    {"category": "🗣️ Cotidiano", "dz": "ما كاينش", "roman": "Ma kayench",
     "es": "No queda", "meaning": "There isn't / there aren't"},
    {"category": "🗣️ Cotidiano", "dz": "درك", "roman": "Dork",
     "es": "Ahora mismo", "meaning": "Now"},
    {"category": "🗣️ Cotidiano", "dz": "غدوة", "roman": "Ghodwa",
     "es": "Mañana", "meaning": "Tomorrow"},
    {"category": "🗣️ Cotidiano", "dz": "البارح", "roman": "El-bareh",
     "es": "Ayer", "meaning": "Yesterday"},
    {"category": "🗣️ Cotidiano", "dz": "مازال", "roman": "Mazal",
     "es": "Aún no", "meaning": "Still / not yet"},

    # ---------------- PEOPLE ----------------
    {"category": "👥 Gente", "dz": "صحبي", "roman": "Sahbi",
     "es": "Mi colega", "meaning": "My friend (male)"},
    {"category": "👥 Gente", "dz": "صحبتي", "roman": "Sahbti",
     "es": "Mi amiga", "meaning": "My friend (female)"},
    {"category": "👥 Gente", "dz": "خويا", "roman": "Khoya",
     "es": "Tío / hermano", "meaning": "My brother / bro"},
    {"category": "👥 Gente", "dz": "ختي", "roman": "Khti",
     "es": "Mi hermana", "meaning": "My sister"},
    {"category": "👥 Gente", "dz": "صاحبي العزيز", "roman": "Sahbi l-3ziz",
     "es": "Mi gran amigo", "meaning": "My dear friend"},
    {"category": "👥 Gente", "dz": "العائلة", "roman": "L3ayla",
     "es": "La familia", "meaning": "The family"},
    {"category": "👥 Gente", "dz": "الوالدين", "roman": "Lwalidin",
     "es": "Mis padres", "meaning": "My parents"},
    {"category": "👥 Gente", "dz": "يمّا", "roman": "Yemma",
     "es": "Mamá", "meaning": "Mom"},
    {"category": "👥 Gente", "dz": "بابا", "roman": "Baba",
     "es": "Papá", "meaning": "Dad"},

    # ---------------- LOVE ----------------
    {"category": "❤️ Amor", "dz": "نحبك", "roman": "N7abek",
     "es": "Te quiero", "meaning": "I love you"},
    {"category": "❤️ Amor", "dz": "نموت عليك", "roman": "Nmout 3lik",
     "es": "Estoy loco por ti", "meaning": "I'm crazy about you"},
    {"category": "❤️ Amor", "dz": "توحشتك", "roman": "Twa7achtek",
     "es": "Te extraño", "meaning": "I miss you"},
    {"category": "❤️ Amor", "dz": "حبيبي", "roman": "Habibi",
     "es": "Mi amor", "meaning": "My love (to a man)"},
    {"category": "❤️ Amor", "dz": "حبيبتي", "roman": "Habibti",
     "es": "Cariño mío", "meaning": "My love (to a woman)"},
    {"category": "❤️ Amor", "dz": "يا عمري", "roman": "Ya 3omri",
     "es": "Mi vida", "meaning": "My life / darling"},
    {"category": "❤️ Amor", "dz": "قلبي", "roman": "Galbi",
     "es": "Mi corazón", "meaning": "My heart"},

    # ---------------- REACTIONS ----------------
    {"category": "😂 Reacciones", "dz": "يا لطيف!", "roman": "Ya latif!",
     "es": "¡Dios mío!", "meaning": "Oh my God!"},
    {"category": "😂 Reacciones", "dz": "واااااا", "roman": "Waaaa",
     "es": "¡Anda ya!", "meaning": "Wow!"},
    {"category": "😂 Reacciones", "dz": "بالاك", "roman": "Balak",
     "es": "A lo mejor", "meaning": "Maybe"},
    {"category": "😂 Reacciones", "dz": "بزاف", "roman": "Bezaf",
     "es": "Un montón", "meaning": "A lot"},
    {"category": "😂 Reacciones", "dz": "شوية", "roman": "Chwiya",
     "es": "Un poquito", "meaning": "A little"},
    {"category": "😂 Reacciones", "dz": "والو", "roman": "Walou",
     "es": "Nada de nada", "meaning": "Nothing"},
    {"category": "😂 Reacciones", "dz": "صح؟", "roman": "Sah?",
     "es": "¿En serio?", "meaning": "Really?"},
    {"category": "😂 Reacciones", "dz": "واش بيك؟", "roman": "Wach bik?",
     "es": "¿Qué te pasa?", "meaning": "What's wrong with you?"},
    {"category": "😂 Reacciones", "dz": "ربي يستر", "roman": "Rabbi yestor",
     "es": "Que Dios nos ampare", "meaning": "God protect us"},
    {"category": "😂 Reacciones", "dz": "إن شاء الله", "roman": "Inchallah",
     "es": "Si Dios quiere", "meaning": "God willing"},

    # ---------------- FOOD ----------------
    {"category": "🍽️ Comida", "dz": "بصحتك", "roman": "Bsa7tek",
     "es": "Que aproveche", "meaning": "Enjoy your meal"},
    {"category": "🍽️ Comida", "dz": "شهية طيبة", "roman": "Chahia tayba",
     "es": "Buen provecho", "meaning": "Enjoy your meal"},
    {"category": "🍽️ Comida", "dz": "بنينة", "roman": "Bnina",
     "es": "Está buenísimo", "meaning": "Delicious"},
    {"category": "🍽️ Comida", "dz": "جعت", "roman": "J3et",
     "es": "Tengo hambre", "meaning": "I'm hungry"},
    {"category": "🍽️ Comida", "dz": "عطشت", "roman": "3techt",
     "es": "Tengo sed", "meaning": "I'm thirsty"},
    {"category": "🍽️ Comida", "dz": "الما", "roman": "El-ma",
     "es": "Agua", "meaning": "Water"},

    # ---------------- MONEY ----------------
    {"category": "💰 Dinero", "dz": "بقداش هذا؟", "roman": "Bqaddach hada?",
     "es": "¿Cuánto vale esto?", "meaning": "How much does this cost?"},
    {"category": "💰 Dinero", "dz": "غالي", "roman": "Ghali",
     "es": "Está caro", "meaning": "Expensive"},
    {"category": "💰 Dinero", "dz": "رخيص", "roman": "Rkhis",
     "es": "Sale barato", "meaning": "Cheap"},
    {"category": "💰 Dinero", "dz": "دراهم", "roman": "Drahem",
     "es": "Plata", "meaning": "Money"},
    {"category": "💰 Dinero", "dz": "ما عنديش دراهم", "roman": "Ma 3andich drahem",
     "es": "No me queda dinero", "meaning": "I don't have money"},

    # ---------------- PLACES ----------------
    {"category": "🚗 Lugares", "dz": "وين؟", "roman": "Win?",
     "es": "¿Dónde?", "meaning": "Where?"},
    {"category": "🚗 Lugares", "dz": "وين راك؟", "roman": "Win rak?",
     "es": "¿Dónde andas?", "meaning": "Where are you?"},
    {"category": "🚗 Lugares", "dz": "روح", "roman": "Rouh",
     "es": "Vete", "meaning": "Go"},
    {"category": "🚗 Lugares", "dz": "أرواح", "roman": "Arwah",
     "es": "Ven aquí", "meaning": "Come"},
    {"category": "🚗 Lugares", "dz": "استنى", "roman": "Stenna",
     "es": "Espera un momento", "meaning": "Wait"},
    {"category": "🚗 Lugares", "dz": "هنا", "roman": "Hna",
     "es": "Aquí mismo", "meaning": "Here"},
    {"category": "🚗 Lugares", "dz": "لهيه", "roman": "Lihih",
     "es": "Por allí", "meaning": "There"},

    # ---------------- FAMOUS EXPRESSIONS ----------------
    {"category": "🔥 Expresiones", "dz": "كاش جديد؟", "roman": "Kach jdid?",
     "es": "¿Alguna novedad?", "meaning": "What's new?"},
    {"category": "🔥 Expresiones", "dz": "ماكانش", "roman": "Makanche",
     "es": "No quedó nada", "meaning": "There isn't any left"},
    {"category": "🔥 Expresiones", "dz": "غير هاني", "roman": "Ghir hani",
     "es": "Aquí ando, tirando", "meaning": "I'm good / getting by"},
    {"category": "🔥 Expresiones", "dz": "ربي يسهل", "roman": "Rabbi ysahel",
     "es": "Que Dios lo facilite", "meaning": "May God make it easy"},
    {"category": "🔥 Expresiones", "dz": "الله يبارك", "roman": "Allah ybarek",
     "es": "Bendito seas", "meaning": "God bless"},
    {"category": "🔥 Expresiones", "dz": "يعطيك الصحة", "roman": "Y3atik essa7a",
     "es": "Un millón de gracias", "meaning": "Thank you / may you have health"},
    {"category": "🔥 Expresiones", "dz": "صحا فطورك", "roman": "Saha ftorek",
     "es": "Que te siente bien", "meaning": "Enjoy your meal (breakfast)"},
    {"category": "🔥 Expresiones", "dz": "على حساب", "roman": "3la hsab",
     "es": "Según se mire", "meaning": "It depends"},
    {"category": "🔥 Expresiones", "dz": "كفاش؟", "roman": "Kifach?",
     "es": "¿De qué manera?", "meaning": "How?"},
    {"category": "🔥 Expresiones", "dz": "علاش؟", "roman": "3lach?",
     "es": "¿Por qué motivo?", "meaning": "Why?"},
]


# Distinct accent color per category, used for the category chip
CATEGORY_COLORS = {
    "👋 Saludos": "#0c9369",
    "🗣️ Cotidiano": "#2563eb",
    "👥 Gente": "#7c3aed",
    "❤️ Amor": "#e11d48",
    "😂 Reacciones": "#d97706",
    "🍽️ Comida": "#ea580c",
    "💰 Dinero": "#059669",
    "🚗 Lugares": "#0891b2",
    "🔥 Expresiones": "#dc2626",
}


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

.stApp {
    background:
        radial-gradient(circle at 10% 10%, rgba(16, 185, 129, 0.07), transparent 30%),
        radial-gradient(circle at 90% 20%, rgba(239, 68, 68, 0.06), transparent 30%),
        #f8faf9;
}

#MainMenu { visibility: hidden; }
footer { visibility: hidden; }
header { visibility: hidden; }

.block-container { max-width: 1150px; padding-top: 2rem; padding-bottom: 4rem; }

.hero {
    position: relative;
    overflow: hidden;
    padding: 42px 35px;
    border-radius: 28px;
    background: linear-gradient(135deg, #063f2e 0%, #087653 55%, #0c9369 100%);
    color: white;
    margin-bottom: 25px;
    box-shadow: 0 18px 50px rgba(5, 90, 65, .18);
}
.hero::after {
    content: "🇩🇿";
    position: absolute;
    right: 35px;
    top: 10px;
    font-size: 110px;
    opacity: .10;
}
.hero h1 { font-size: clamp(30px, 5vw, 50px); font-weight: 800; margin: 0; letter-spacing: -1.5px; }
.hero p { font-size: 17px; margin-top: 12px; max-width: 650px; opacity: .88; line-height: 1.6; }
.badge {
    display: inline-block;
    background: rgba(255,255,255,.13);
    border: 1px solid rgba(255,255,255,.2);
    padding: 7px 12px;
    border-radius: 999px;
    font-size: 12px;
    margin-bottom: 15px;
}

div[data-testid="stTextInput"] input { border-radius: 14px; border: 1px solid #dfe7e3; padding: 13px 16px; font-size: 15px; }
div[data-baseweb="select"] > div { border-radius: 14px; border: 1px solid #dfe7e3; }

@media (max-width: 700px) {
    .block-container { padding: 1rem; }
    .hero { padding: 30px 23px; border-radius: 22px; }
    .hero h1 { font-size: 32px; }
    .hero p { font-size: 15px; }
    .hero::after { font-size: 70px; right: 15px; }
}
</style>
""", unsafe_allow_html=True)


# =========================================================
# HERO — flush-left HTML so Streamlit's markdown parser
# doesn't treat indented lines as a code block.
# =========================================================

hero_html = (
'<div class="hero">'
'<div class="badge">🇩🇿 Darija Argelina → 🇪🇸 Español</div>'
'<h1>Dzayer → Español</h1>'
'<p>Palabras y expresiones argelinas traducidas a un español '
'natural y cotidiano — no traducciones literales. '
'Toca 🔊 para escuchar la pronunciación en español.</p>'
'</div>'
)
st.markdown(hero_html, unsafe_allow_html=True)


# =========================================================
# SEARCH + CATEGORY
# =========================================================

col1, col2 = st.columns([2.2, 1])

with col1:
    search = st.text_input(
        "Search",
        placeholder="🔎  Busca en darija, español o inglés...",
        label_visibility="collapsed"
    )

with col2:
    categories = ["Todas"] + sorted(set(item["category"] for item in WORDS))
    selected_category = st.selectbox("Category", categories, label_visibility="collapsed")


# =========================================================
# FILTER
# =========================================================

filtered = WORDS.copy()

if selected_category != "Todas":
    filtered = [item for item in filtered if item["category"] == selected_category]

if search:
    query = search.lower().strip()
    filtered = [
        item for item in filtered
        if query in item["dz"].lower()
        or query in item["roman"].lower()
        or query in item["es"].lower()
        or query in item["meaning"].lower()
    ]


# =========================================================
# RESULT COUNT
# =========================================================

st.markdown(
    f'<div style="color:#66756e;font-size:14px;margin:18px 2px 10px 2px;">'
    f'Mostrando <strong>{len(filtered)}</strong> expresiones</div>',
    unsafe_allow_html=True
)


# =========================================================
# BUILD CARD HTML
# =========================================================

cards = []

for item in filtered:
    dz = html.escape(item["dz"])
    roman = html.escape(item["roman"])
    spanish = html.escape(item["es"])
    meaning = html.escape(item["meaning"])
    category = html.escape(item["category"])
    accent = CATEGORY_COLORS.get(item["category"], "#087653")
    js_text = json.dumps(item["es"])

    card = (
        f'<div class="card">'
        f'<div class="category" style="color:{accent};">{category}</div>'
        f'<div class="dz">{dz}</div>'
        f'<div class="roman">{roman}</div>'
        f'<div class="divider"></div>'
        f'<button class="spanish-button" onclick=\'speakSpanish({js_text}, this)\' '
        f'title="Escuchar pronunciación" style="background:{accent}14;">'
        f'<span class="spanish" style="color:{accent};">🇪🇸 {spanish}</span>'
        f'<span class="speaker">🔊</span>'
        f'</button>'
        f'<div class="meaning">{meaning}</div>'
        f'</div>'
    )
    cards.append(card)

cards_html = "".join(cards)


# =========================================================
# PRONUNCIATION COMPONENT
# =========================================================

component_html = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
* {{ box-sizing: border-box; }}
body {{ margin: 0; background: transparent; font-family: Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; }}

.grid {{ display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 14px; }}

.card {{
    background: #ffffff;
    border: 1px solid #e4ebe7;
    border-radius: 18px;
    padding: 18px;
    box-shadow: 0 5px 18px rgba(0,0,0,.035);
    transition: transform .15s ease, box-shadow .15s ease;
}}
.card:hover {{ transform: translateY(-3px); box-shadow: 0 12px 30px rgba(0,0,0,.09); }}

.category {{ font-size: 11px; font-weight: 800; text-transform: uppercase; letter-spacing: .5px; margin-bottom: 12px; }}

.dz {{ color: #202825; font-size: 23px; font-weight: 700; direction: rtl; text-align: right; line-height: 1.4; }}
.roman {{ color: #84918c; font-size: 13px; margin-top: 4px; font-style: italic; }}

.divider {{ height: 1px; background: #edf1ef; margin: 14px 0; }}

.spanish-button {{
    width: 100%;
    border: 0;
    border-radius: 13px;
    padding: 12px 13px;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: space-between;
    text-align: left;
    transition: all .15s ease;
}}
.spanish-button:hover {{ filter: brightness(0.97); transform: scale(1.01); }}
.spanish-button:active {{ transform: scale(.98); }}

.spanish {{ font-size: 19px; font-weight: 750; }}
.speaker {{ font-size: 18px; }}

.meaning {{ color: #707b76; font-size: 13px; margin-top: 9px; }}

@media (max-width: 700px) {{
    .grid {{ grid-template-columns: 1fr; gap: 11px; }}
    .card {{ padding: 16px; border-radius: 16px; }}
    .dz {{ font-size: 21px; }}
    .spanish {{ font-size: 18px; }}
}}
</style>
</head>
<body>

<div class="grid">
{cards_html}
</div>

<script>
function getSpanishVoice() {{
    const voices = window.speechSynthesis.getVoices();
    let voice = voices.find(v => v.lang.toLowerCase() === "es-es");
    if (!voice) voice = voices.find(v => v.lang.toLowerCase().startsWith("es"));
    return voice;
}}

function speakSpanish(text, button) {{
    window.speechSynthesis.cancel();
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = "es-ES";
    utterance.rate = 0.88;
    utterance.pitch = 1.0;
    const voice = getSpanishVoice();
    if (voice) utterance.voice = voice;

    button.style.transform = "scale(.98)";
    utterance.onend = function() {{ button.style.transform = ""; }};
    utterance.onerror = function() {{ button.style.transform = ""; }};

    window.speechSynthesis.speak(utterance);
}}

window.speechSynthesis.onvoiceschanged = function() {{
    window.speechSynthesis.getVoices();
}};
</script>

</body>
</html>
"""


# =========================================================
# SHOW CARDS
# =========================================================

if filtered:
    rows = (len(filtered) + 1) // 2
    height = max(200, rows * 175)
    components.html(component_html, height=height, scrolling=False)
else:
    st.markdown(
        '<div style="text-align:center;padding:50px 20px;color:#7b8782;">'
        '<div style="font-size:45px;">🔎</div>'
        '<h3>No se encontraron expresiones</h3>'
        '<p>Prueba con otra palabra o categoría.</p>'
        '</div>',
        unsafe_allow_html=True
    )


# =========================================================
# FOOTER
# =========================================================

footer_html = (
'<div style="text-align:center;color:#8a9691;font-size:12px;margin-top:30px;">'
'🇩🇿 Hecho para quienes aprenden español desde Argelia 🇪🇸'
'<br>El audio en español usa la voz integrada de tu dispositivo.'
'</div>'
)
st.markdown(footer_html, unsafe_allow_html=True)

