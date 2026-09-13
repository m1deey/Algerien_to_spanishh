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
# DATA
# Algerian Darija → Natural Spanish
# =========================================================

WORDS = [

    # -----------------------------------------------------
    # GREETINGS & POLITENESS
    # -----------------------------------------------------

    {
        "category": "👋 Greetings",
        "dz": "السلام عليكم",
        "roman": "Salam 3likom",
        "es": "Hola",
        "meaning": "Hello"
    },
    {
        "category": "👋 Greetings",
        "dz": "وعليكم السلام",
        "roman": "Wa 3likom salam",
        "es": "Hola",
        "meaning": "Hello / reply to greeting"
    },
    {
        "category": "👋 Greetings",
        "dz": "واش راك؟",
        "roman": "Wach rak?",
        "es": "¿Cómo estás?",
        "meaning": "How are you?"
    },
    {
        "category": "👋 Greetings",
        "dz": "واش راكي؟",
        "roman": "Wach raki?",
        "es": "¿Cómo estás?",
        "meaning": "How are you? (to a woman)"
    },
    {
        "category": "👋 Greetings",
        "dz": "لاباس؟",
        "roman": "Labas?",
        "es": "¿Todo bien?",
        "meaning": "Everything good?"
    },
    {
        "category": "👋 Greetings",
        "dz": "صباح الخير",
        "roman": "Sbah el-khir",
        "es": "Buenos días",
        "meaning": "Good morning"
    },
    {
        "category": "👋 Greetings",
        "dz": "مساء الخير",
        "roman": "Msa el-khir",
        "es": "Buenas tardes",
        "meaning": "Good afternoon / evening"
    },
    {
        "category": "👋 Greetings",
        "dz": "أهلا",
        "roman": "Ahlan",
        "es": "Hola",
        "meaning": "Hi"
    },
    {
        "category": "👋 Greetings",
        "dz": "بسلامة",
        "roman": "Bslama",
        "es": "Adiós",
        "meaning": "Goodbye"
    },
    {
        "category": "👋 Greetings",
        "dz": "صحا",
        "roman": "Saha",
        "es": "¡Que vaya bien!",
        "meaning": "Take care / good health"
    },


    # -----------------------------------------------------
    # EVERYDAY EXPRESSIONS
    # -----------------------------------------------------

    {
        "category": "🗣️ Everyday",
        "dz": "مليح",
        "roman": "Mlih",
        "es": "Bien",
        "meaning": "Good / fine"
    },
    {
        "category": "🗣️ Everyday",
        "dz": "لاباس الحمد لله",
        "roman": "Labas, hamdullah",
        "es": "Estoy bien, gracias a Dios",
        "meaning": "I'm fine, thank God"
    },
    {
        "category": "🗣️ Everyday",
        "dz": "كولشي مليح",
        "roman": "Kolchi mlih",
        "es": "Todo bien",
        "meaning": "Everything is good"
    },
    {
        "category": "🗣️ Everyday",
        "dz": "ماشي مشكل",
        "roman": "Machi mochkil",
        "es": "No pasa nada",
        "meaning": "No problem"
    },
    {
        "category": "🗣️ Everyday",
        "dz": "ماعلاباليش",
        "roman": "Ma 3labalich",
        "es": "No lo sé",
        "meaning": "I don't know"
    },
    {
        "category": "🗣️ Everyday",
        "dz": "ما فهمتش",
        "roman": "Ma fhemtch",
        "es": "No entiendo",
        "meaning": "I don't understand"
    },
    {
        "category": "🗣️ Everyday",
        "dz": "فهمت",
        "roman": "Fhemt",
        "es": "Entiendo",
        "meaning": "I understand"
    },
    {
        "category": "🗣️ Everyday",
        "dz": "واش ندير؟",
        "roman": "Wach ndir?",
        "es": "¿Qué hago?",
        "meaning": "What should I do?"
    },
    {
        "category": "🗣️ Everyday",
        "dz": "واش درت؟",
        "roman": "Wach dert?",
        "es": "¿Qué hiciste?",
        "meaning": "What did you do?"
    },
    {
        "category": "🗣️ Everyday",
        "dz": "واش كاين؟",
        "roman": "Wach kayen?",
        "es": "¿Qué pasa?",
        "meaning": "What's going on?"
    },
    {
        "category": "🗣️ Everyday",
        "dz": "كاين",
        "roman": "Kayen",
        "es": "Hay",
        "meaning": "There is / there are"
    },
    {
        "category": "🗣️ Everyday",
        "dz": "ما كاينش",
        "roman": "Ma kayench",
        "es": "No hay",
        "meaning": "There isn't / there aren't"
    },
    {
        "category": "🗣️ Everyday",
        "dz": "درك",
        "roman": "Dork",
        "es": "Ahora",
        "meaning": "Now"
    },
    {
        "category": "🗣️ Everyday",
        "dz": "غدوة",
        "roman": "Ghodwa",
        "es": "Mañana",
        "meaning": "Tomorrow"
    },
    {
        "category": "🗣️ Everyday",
        "dz": "البارح",
        "roman": "El-bareh",
        "es": "Ayer",
        "meaning": "Yesterday"
    },
    {
        "category": "🗣️ Everyday",
        "dz": "مازال",
        "roman": "Mazal",
        "es": "Todavía",
        "meaning": "Still / not yet"
    },


    # -----------------------------------------------------
    # FRIENDS & PEOPLE
    # -----------------------------------------------------

    {
        "category": "👥 People",
        "dz": "صحبي",
        "roman": "Sahbi",
        "es": "Mi amigo",
        "meaning": "My friend"
    },
    {
        "category": "👥 People",
        "dz": "صحبتي",
        "roman": "Sahbti",
        "es": "Mi amiga",
        "meaning": "My female friend"
    },
    {
        "category": "👥 People",
        "dz": "خويا",
        "roman": "Khoya",
        "es": "Mi hermano",
        "meaning": "My brother / bro"
    },
    {
        "category": "👥 People",
        "dz": "ختي",
        "roman": "Khti",
        "es": "Mi hermana",
        "meaning": "My sister"
    },
    {
        "category": "👥 People",
        "dz": "صاحبي العزيز",
        "roman": "Sahbi l-3ziz",
        "es": "Mi querido amigo",
        "meaning": "My dear friend"
    },
    {
        "category": "👥 People",
        "dz": "العائلة",
        "roman": "L3ayla",
        "es": "La familia",
        "meaning": "The family"
    },
    {
        "category": "👥 People",
        "dz": "الوالدين",
        "roman": "Lwalidin",
        "es": "Mis padres",
        "meaning": "My parents"
    },
    {
        "category": "👥 People",
        "dz": "يمّا",
        "roman": "Yemma",
        "es": "Mamá",
        "meaning": "Mom"
    },
    {
        "category": "👥 People",
        "dz": "بابا",
        "roman": "Baba",
        "es": "Papá",
        "meaning": "Dad"
    },


    # -----------------------------------------------------
    # LOVE & RELATIONSHIPS
    # -----------------------------------------------------

    {
        "category": "❤️ Love",
        "dz": "نحبك",
        "roman": "N7abek",
        "es": "Te quiero",
        "meaning": "I love you"
    },
    {
        "category": "❤️ Love",
        "dz": "نموت عليك",
        "roman": "Nmout 3lik",
        "es": "Me muero por ti",
        "meaning": "I'm crazy about you"
    },
    {
        "category": "❤️ Love",
        "dz": "توحشتك",
        "roman": "Twa7achtek",
        "es": "Te echo de menos",
        "meaning": "I miss you"
    },
    {
        "category": "❤️ Love",
        "dz": "حبيبي",
        "roman": "Habibi",
        "es": "Cariño",
        "meaning": "My love"
    },
    {
        "category": "❤️ Love",
        "dz": "حبيبتي",
        "roman": "Habibti",
        "es": "Cariño",
        "meaning": "My love"
    },
    {
        "category": "❤️ Love",
        "dz": "يا عمري",
        "roman": "Ya 3omri",
        "es": "Mi vida",
        "meaning": "My life / darling"
    },
    {
        "category": "❤️ Love",
        "dz": "قلبي",
        "roman": "Galbi",
        "es": "Mi corazón",
        "meaning": "My heart"
    },


    # -----------------------------------------------------
    # EMOTIONS / REACTIONS
    # -----------------------------------------------------

    {
        "category": "😂 Reactions",
        "dz": "يا لطيف!",
        "roman": "Ya latif!",
        "es": "¡Dios mío!",
        "meaning": "Oh my God!"
    },
    {
        "category": "😂 Reactions",
        "dz": "واااااا",
        "roman": "Waaaa",
        "es": "¡Vaya!",
        "meaning": "Wow!"
    },
    {
        "category": "😂 Reactions",
        "dz": "بالاك",
        "roman": "Balak",
        "es": "Quizás",
        "meaning": "Maybe"
    },
    {
        "category": "😂 Reactions",
        "dz": "بزاف",
        "roman": "Bezaf",
        "es": "Mucho",
        "meaning": "A lot"
    },
    {
        "category": "😂 Reactions",
        "dz": "شوية",
        "roman": "Chwiya",
        "es": "Un poco",
        "meaning": "A little"
    },
    {
        "category": "😂 Reactions",
        "dz": "والو",
        "roman": "Walou",
        "es": "Nada",
        "meaning": "Nothing"
    },
    {
        "category": "😂 Reactions",
        "dz": "صح؟",
        "roman": "Sah?",
        "es": "¿De verdad?",
        "meaning": "Really?"
    },
    {
        "category": "😂 Reactions",
        "dz": "واش بيك؟",
        "roman": "Wach bik?",
        "es": "¿Qué te pasa?",
        "meaning": "What's wrong with you?"
    },
    {
        "category": "😂 Reactions",
        "dz": "ربي يستر",
        "roman": "Rabbi yestor",
        "es": "Dios nos proteja",
        "meaning": "God protect us"
    },
    {
        "category": "😂 Reactions",
        "dz": "إن شاء الله",
        "roman": "Inchallah",
        "es": "Si Dios quiere",
        "meaning": "God willing"
    },


    # -----------------------------------------------------
    # FOOD
    # -----------------------------------------------------

    {
        "category": "🍽️ Food",
        "dz": "بصحتك",
        "roman": "Bsa7tek",
        "es": "Que aproveche",
        "meaning": "Enjoy your meal"
    },
    {
        "category": "🍽️ Food",
        "dz": "شهية طيبة",
        "roman": "Chahia tayba",
        "es": "Buen provecho",
        "meaning": "Enjoy your meal"
    },
    {
        "category": "🍽️ Food",
        "dz": "بنينة",
        "roman": "Bnina",
        "es": "Delicioso",
        "meaning": "Delicious"
    },
    {
        "category": "🍽️ Food",
        "dz": "جعت",
        "roman": "J3et",
        "es": "Tengo hambre",
        "meaning": "I'm hungry"
    },
    {
        "category": "🍽️ Food",
        "dz": "عطشت",
        "roman": "3techt",
        "es": "Tengo sed",
        "meaning": "I'm thirsty"
    },
    {
        "category": "🍽️ Food",
        "dz": "الما",
        "roman": "El-ma",
        "es": "Agua",
        "meaning": "Water"
    },


    # -----------------------------------------------------
    # SHOPPING / MONEY
    # -----------------------------------------------------

    {
        "category": "💰 Money",
        "dz": "بقداش هذا؟",
        "roman": "Bqaddach hada?",
        "es": "¿Cuánto cuesta esto?",
        "meaning": "How much does this cost?"
    },
    {
        "category": "💰 Money",
        "dz": "غالي",
        "roman": "Ghali",
        "es": "Caro",
        "meaning": "Expensive"
    },
    {
        "category": "💰 Money",
        "dz": "رخيص",
        "roman": "Rkhis",
        "es": "Barato",
        "meaning": "Cheap"
    },
    {
        "category": "💰 Money",
        "dz": "دراهم",
        "roman": "Drahem",
        "es": "Dinero",
        "meaning": "Money"
    },
    {
        "category": "💰 Money",
        "dz": "ما عنديش دراهم",
        "roman": "Ma 3andich drahem",
        "es": "No tengo dinero",
        "meaning": "I don't have money"
    },


    # -----------------------------------------------------
    # PLACES / MOVEMENT
    # -----------------------------------------------------

    {
        "category": "🚗 Places",
        "dz": "وين؟",
        "roman": "Win?",
        "es": "¿Dónde?",
        "meaning": "Where?"
    },
    {
        "category": "🚗 Places",
        "dz": "وين راك؟",
        "roman": "Win rak?",
        "es": "¿Dónde estás?",
        "meaning": "Where are you?"
    },
    {
        "category": "🚗 Places",
        "dz": "روح",
        "roman": "Rouh",
        "es": "Ve",
        "meaning": "Go"
    },
    {
        "category": "🚗 Places",
        "dz": "أرواح",
        "roman": "Arwah",
        "es": "Ven",
        "meaning": "Come"
    },
    {
        "category": "🚗 Places",
        "dz": "استنى",
        "roman": "Stenna",
        "es": "Espera",
        "meaning": "Wait"
    },
    {
        "category": "🚗 Places",
        "dz": "هنا",
        "roman": "Hna",
        "es": "Aquí",
        "meaning": "Here"
    },
    {
        "category": "🚗 Places",
        "dz": "لهيه",
        "roman": "Lihih",
        "es": "Allí",
        "meaning": "There"
    },


    # -----------------------------------------------------
    # FAMOUS ALGERIAN-STYLE EXPRESSIONS
    # -----------------------------------------------------

    {
        "category": "🔥 Famous",
        "dz": "كاش جديد؟",
        "roman": "Kach jdid?",
        "es": "¿Qué hay de nuevo?",
        "meaning": "What's new?"
    },
    {
        "category": "🔥 Famous",
        "dz": "ماكانش",
        "roman": "Makanche",
        "es": "No hay",
        "meaning": "There isn't any"
    },
    {
        "category": "🔥 Famous",
        "dz": "غير هاني",
        "roman": "Ghir hani",
        "es": "Estoy bien",
        "meaning": "I'm good / I'm fine"
    },
    {
        "category": "🔥 Famous",
        "dz": "ربي يسهل",
        "roman": "Rabbi ysahel",
        "es": "Que Dios lo facilite",
        "meaning": "May God make it easy"
    },
    {
        "category": "🔥 Famous",
        "dz": "الله يبارك",
        "roman": "Allah ybarek",
        "es": "Que Dios te bendiga",
        "meaning": "God bless"
    },
    {
        "category": "🔥 Famous",
        "dz": "يعطيك الصحة",
        "roman": "Y3atik essa7a",
        "es": "Muchas gracias",
        "meaning": "Thank you / may you have health"
    },
    {
        "category": "🔥 Famous",
        "dz": "صحا فطورك",
        "roman": "Saha ftorek",
        "es": "Buen provecho",
        "meaning": "Enjoy your meal"
    },
    {
        "category": "🔥 Famous",
        "dz": "على حساب",
        "roman": "3la hsab",
        "es": "Depende",
        "meaning": "It depends"
    },
    {
        "category": "🔥 Famous",
        "dz": "كفاش؟",
        "roman": "Kifach?",
        "es": "¿Cómo?",
        "meaning": "How?"
    },
    {
        "category": "🔥 Famous",
        "dz": "علاش؟",
        "roman": "3lach?",
        "es": "¿Por qué?",
        "meaning": "Why?"
    },
]


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 10% 10%, rgba(16, 185, 129, 0.07), transparent 30%),
        radial-gradient(circle at 90% 20%, rgba(239, 68, 68, 0.06), transparent 30%),
        #f8faf9;
}

/* Hide Streamlit chrome */
#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

/* Main width */
.block-container {
    max-width: 1150px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}

/* Hero */
.hero {
    position: relative;
    overflow: hidden;
    padding: 42px 35px;
    border-radius: 28px;
    background: linear-gradient(
        135deg,
        #063f2e 0%,
        #087653 55%,
        #0c9369 100%
    );
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

.hero h1 {
    font-size: clamp(30px, 5vw, 50px);
    font-weight: 800;
    margin: 0;
    letter-spacing: -1.5px;
}

.hero p {
    font-size: 17px;
    margin-top: 12px;
    max-width: 650px;
    opacity: .88;
    line-height: 1.6;
}

.badge {
    display: inline-block;
    background: rgba(255,255,255,.13);
    border: 1px solid rgba(255,255,255,.2);
    padding: 7px 12px;
    border-radius: 999px;
    font-size: 12px;
    margin-bottom: 15px;
}

/* Search */
div[data-testid="stTextInput"] input {
    border-radius: 14px;
    border: 1px solid #dfe7e3;
    padding: 13px 16px;
    font-size: 15px;
}

/* Select */
div[data-baseweb="select"] > div {
    border-radius: 14px;
    border: 1px solid #dfe7e3;
}

/* Mobile */
@media (max-width: 700px) {

    .block-container {
        padding: 1rem;
    }

    .hero {
        padding: 30px 23px;
        border-radius: 22px;
    }

    .hero h1 {
        font-size: 32px;
    }

    .hero p {
        font-size: 15px;
    }

    .hero::after {
        font-size: 70px;
        right: 15px;
    }
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# HERO
# =========================================================

st.markdown("""
<div class="hero">

    <div class="badge">🇩🇿 Algerian Darija → 🇪🇸 Spanish</div>

    <h1>Dzayer → Español</h1>

    <p>
        Famous Algerian words, expressions and everyday phrases
        translated into natural Spanish.
        Tap 🔊 and hear the Spanish pronunciation.
    </p>

</div>
""", unsafe_allow_html=True)


# =========================================================
# SEARCH + CATEGORY
# =========================================================

col1, col2 = st.columns([2.2, 1])

with col1:
    search = st.text_input(
        "Search",
        placeholder="🔎  Search in Algerian, Spanish or English...",
        label_visibility="collapsed"
    )

with col2:
    categories = ["All"] + sorted(set(item["category"] for item in WORDS))

    selected_category = st.selectbox(
        "Category",
        categories,
        label_visibility="collapsed"
    )


# =========================================================
# FILTER
# =========================================================

filtered = WORDS.copy()

if selected_category != "All":
    filtered = [
        item for item in filtered
        if item["category"] == selected_category
    ]

if search:
    query = search.lower().strip()

    filtered = [
        item for item in filtered
        if (
            query in item["dz"].lower()
            or query in item["roman"].lower()
            or query in item["es"].lower()
            or query in item["meaning"].lower()
        )
    ]


# =========================================================
# RESULT COUNT
# =========================================================

st.markdown(
    f"""
    <div style="
        color:#66756e;
        font-size:14px;
        margin:18px 2px 10px 2px;
    ">
        Showing <strong>{len(filtered)}</strong> expressions
    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# BUILD CARD HTML
# =========================================================

cards = []

for index, item in enumerate(filtered):

    dz = html.escape(item["dz"])
    roman = html.escape(item["roman"])
    spanish = html.escape(item["es"])
    meaning = html.escape(item["meaning"])
    category = html.escape(item["category"])

    # JSON-safe text for JavaScript
    js_text = json.dumps(item["es"])

    card = f"""
    <div class="card">

        <div class="category">
            {category}
        </div>

        <div class="dz">
            {dz}
        </div>

        <div class="roman">
            {roman}
        </div>

        <div class="divider"></div>

        <button
            class="spanish-button"
            onclick='speakSpanish({js_text}, this)'
            title="Listen to Spanish pronunciation"
        >
            <span class="spanish">
                🇪🇸 {spanish}
            </span>

            <span class="speaker">
                🔊
            </span>
        </button>

        <div class="meaning">
            {meaning}
        </div>

    </div>
    """

    cards.append(card)


cards_html = "\n".join(cards)


# =========================================================
# PRONUNCIATION COMPONENT
# =========================================================

component_html = f"""

<!DOCTYPE html>

<html>

<head>

<meta charset="UTF-8">

<style>

* {{
    box-sizing: border-box;
}}

body {{
    margin: 0;
    background: transparent;
    font-family:
        Inter,
        -apple-system,
        BlinkMacSystemFont,
        "Segoe UI",
        sans-serif;
}}

.grid {{
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 14px;
}}

.card {{
    background: #ffffff;
    border: 1px solid #e4ebe7;
    border-radius: 18px;
    padding: 18px;
    box-shadow: 0 5px 18px rgba(0,0,0,.035);
    transition: transform .15s ease, box-shadow .15s ease;
}}

.card:hover {{
    transform: translateY(-2px);
    box-shadow: 0 10px 28px rgba(0,0,0,.07);
}}

.category {{
    color: #75847d;
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: .5px;
    margin-bottom: 12px;
}}

.dz {{
    color: #202825;
    font-size: 23px;
    font-weight: 700;
    direction: rtl;
    text-align: right;
    line-height: 1.4;
}}

.roman {{
    color: #84918c;
    font-size: 13px;
    margin-top: 4px;
    font-style: italic;
}}

.divider {{
    height: 1px;
    background: #edf1ef;
    margin: 14px 0;
}}

.spanish-button {{
    width: 100%;
    border: 0;
    background: #eef9f4;
    border-radius: 13px;
    padding: 12px 13px;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: space-between;
    text-align: left;
    transition: all .15s ease;
}}

.spanish-button:hover {{
    background: #dff4eb;
    transform: scale(1.01);
}}

.spanish-button:active {{
    transform: scale(.98);
}}

.spanish {{
    color: #087653;
    font-size: 19px;
    font-weight: 750;
}}

.speaker {{
    font-size: 18px;
}}

.meaning {{
    color: #707b76;
    font-size: 13px;
    margin-top: 9px;
}}

@media (max-width: 700px) {{

    .grid {{
        grid-template-columns: 1fr;
        gap: 11px;
    }}

    .card {{
        padding: 16px;
        border-radius: 16px;
    }}

    .dz {{
        font-size: 21px;
    }}

    .spanish {{
        font-size: 18px;
    }}
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

    // Prefer Spain Spanish
    let voice = voices.find(v =>
        v.lang.toLowerCase() === "es-es"
    );

    // Then any Spanish voice
    if (!voice) {{
        voice = voices.find(v =>
            v.lang.toLowerCase().startsWith("es")
        );
    }}

    return voice;
}}


function speakSpanish(text, button) {{

    // Stop previous speech
    window.speechSynthesis.cancel();

    const utterance =
        new SpeechSynthesisUtterance(text);

    utterance.lang = "es-ES";

    // Natural-ish learning speed
    utterance.rate = 0.88;

    utterance.pitch = 1.0;

    const voice = getSpanishVoice();

    if (voice) {{
        utterance.voice = voice;
    }}

    // Visual feedback
    const oldText = button.innerHTML;

    button.style.transform = "scale(.98)";

    button.querySelector(".speaker").textContent = "🔊";

    utterance.onend = function() {{
        button.style.transform = "";
    }};

    utterance.onerror = function() {{
        button.style.transform = "";
    }};

    window.speechSynthesis.speak(utterance);
}}


// Some browsers load voices asynchronously
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

    # Calculate approximate height
    rows = (len(filtered) + 1) // 2

    height = max(200, rows * 175)

    components.html(
        component_html,
        height=height,
        scrolling=False
    )

else:

    st.markdown(
        """
        <div style="
            text-align:center;
            padding:50px 20px;
            color:#7b8782;
        ">
            <div style="font-size:45px;">🔎</div>
            <h3>No expressions found</h3>
            <p>Try another word or category.</p>
        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div style="
    text-align:center;
    color:#8a9691;
    font-size:12px;
    margin-top:30px;
">
    🇩🇿 Made for Algerian Spanish learners 🇪🇸
    <br>
    Spanish audio uses your device's built-in speech voice.
</div>
""", unsafe_allow_html=True)
