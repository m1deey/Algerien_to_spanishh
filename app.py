import streamlit as st
import streamlit.components.v1 as components
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
# GLOBAL CSS
# =========================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 10% 0%, rgba(34,197,94,0.08), transparent 28%),
        radial-gradient(circle at 90% 10%, rgba(239,68,68,0.07), transparent 28%),
        #080a0d;
}

/* Hide Streamlit default stuff */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

/* Main container */

.block-container {
    max-width: 1250px;
    padding-top: 1.5rem;
    padding-bottom: 3rem;
}

/* =========================================================
   HERO
   ========================================================= */

.hero {
    text-align: center;
    padding: 45px 20px 35px;
    margin-bottom: 20px;
}

.hero-badge {
    display: inline-block;
    padding: 8px 15px;
    border-radius: 999px;

    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.10);

    color: #b8bcc5;

    font-size: 11px;
    font-weight: 800;

    letter-spacing: 1.2px;

    margin-bottom: 20px;
}

.hero h1 {
    margin: 0;

    font-size: clamp(44px, 8vw, 78px);
    line-height: 0.95;

    font-weight: 900;
    letter-spacing: -4px;

    background: linear-gradient(
        90deg,
        #ffffff 0%,
        #d8dde5 45%,
        #8d949f 100%
    );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-subtitle {
    max-width: 680px;

    margin: 20px auto 0;

    color: #9ca3af;

    font-size: 17px;
    line-height: 1.65;
}

.hero-footer {
    margin-top: 25px;

    display: flex;
    justify-content: center;
    align-items: center;

    gap: 10px;
    flex-wrap: wrap;

    color: #686f7a;

    font-size: 12px;
    font-weight: 600;
}

/* =========================================================
   SEARCH
   ========================================================= */

.search-label {
    color: #777f8b;
    font-size: 12px;
    font-weight: 700;
    margin-bottom: 6px;
}

div[data-baseweb="input"] {
    background: #111419 !important;
    border: 1px solid #242932 !important;
    border-radius: 14px !important;
}

div[data-baseweb="input"] input {
    color: white !important;
}

/* Selectbox */

div[data-baseweb="select"] > div {
    background: #111419 !important;
    border: 1px solid #242932 !important;
    border-radius: 14px !important;
}

div[data-baseweb="select"] * {
    color: #f1f3f5 !important;
}

/* =========================================================
   INFO
   ========================================================= */

.results-info {
    margin-top: 20px;
    margin-bottom: 14px;

    color: #626a75;

    font-size: 12px;
    font-weight: 700;

    text-transform: uppercase;
    letter-spacing: 0.8px;
}

/* =========================================================
   FOOTER
   ========================================================= */

.site-footer {
    text-align: center;

    margin-top: 50px;
    padding-top: 25px;

    border-top: 1px solid rgba(255,255,255,0.06);

    color: #505762;

    font-size: 11px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# HERO
# =========================================================

st.markdown("""
<div class="hero">

    <div class="hero-badge">
        🇩🇿 ALGERIAN → 🇪🇸 SPANISH
    </div>

    <h1>
        Dzayer → Español
    </h1>

    <p class="hero-subtitle">
        Famous Algerian expressions translated into natural Spanish.
        <br>
        Tap any Spanish phrase to hear how it sounds.
    </p>

    <div class="hero-footer">
        <span>🗣️ 100+ expressions</span>
        <span>•</span>
        <span>🔊 Spanish pronunciation</span>
        <span>•</span>
        <span>🇩🇿 Made for Algerians</span>
    </div>

</div>
""", unsafe_allow_html=True)


# =========================================================
# EXPRESSIONS DATABASE
# =========================================================

expressions = [

# ---------------------------------------------------------
# SALUDOS
# ---------------------------------------------------------

{
    "dz": "Salam",
    "roman": "Salam",
    "es": "Hola",
    "en": "Hello",
    "cat": "👋 Saludos"
},

{
    "dz": "Saha",
    "roman": "Saha",
    "es": "Hola / ¿Qué tal?",
    "en": "Hi / How are you?",
    "cat": "👋 Saludos"
},

{
    "dz": "Saha ftorkom",
    "roman": "Saha ftorkom",
    "es": "Que aproveche",
    "en": "Enjoy your meal",
    "cat": "👋 Saludos"
},

{
    "dz": "Saha chribtek",
    "roman": "Saha chribtek",
    "es": "Salud",
    "en": "Cheers",
    "cat": "👋 Saludos"
},

{
    "dz": "Labas?",
    "roman": "Labas?",
    "es": "¿Todo bien?",
    "en": "Everything good?",
    "cat": "👋 Saludos"
},

{
    "dz": "Kach ma kayen?",
    "roman": "Kach ma kayen?",
    "es": "¿Qué tal?",
    "en": "What's up?",
    "cat": "👋 Saludos"
},

{
    "dz": "Win rak?",
    "roman": "Win rak?",
    "es": "¿Dónde estás?",
    "en": "Where are you?",
    "cat": "👋 Saludos"
},

{
    "dz": "Chbab?",
    "roman": "Chbab?",
    "es": "¿Qué tal, tío?",
    "en": "What's up, bro?",
    "cat": "👋 Saludos"
},

# ---------------------------------------------------------
# COTIDIANO
# ---------------------------------------------------------

{
    "dz": "Chnou rak dir?",
    "roman": "Chnou rak dir?",
    "es": "¿Qué estás haciendo?",
    "en": "What are you doing?",
    "cat": "🗣️ Cotidiano"
},

{
    "dz": "Win rak rayeh?",
    "roman": "Win rak rayeh?",
    "es": "¿Adónde vas?",
    "en": "Where are you going?",
    "cat": "🗣️ Cotidiano"
},

{
    "dz": "Ana jay",
    "roman": "Ana jay",
    "es": "Ya voy",
    "en": "I'm coming",
    "cat": "🗣️ Cotidiano"
},

{
    "dz": "Sani brk",
    "roman": "Sani brk",
    "es": "Espera un momento",
    "en": "Wait a moment",
    "cat": "🗣️ Cotidiano"
},

{
    "dz": "Ma fhemtch",
    "roman": "Ma fhemtch",
    "es": "No entendí",
    "en": "I didn't understand",
    "cat": "🗣️ Cotidiano"
},

{
    "dz": "Fhemt",
    "roman": "Fhemt",
    "es": "Entendido",
    "en": "Got it",
    "cat": "🗣️ Cotidiano"
},

{
    "dz": "Machi mochkil",
    "roman": "Machi mochkil",
    "es": "No pasa nada",
    "en": "No problem",
    "cat": "🗣️ Cotidiano"
},

{
    "dz": "Normal",
    "roman": "Normal",
    "es": "Normal",
    "en": "Normal",
    "cat": "🗣️ Cotidiano"
},

{
    "dz": "Ki ma hab",
    "roman": "Ki ma hab",
    "es": "Como quieras",
    "en": "As you wish",
    "cat": "🗣️ Cotidiano"
},

{
    "dz": "Dir li t7eb",
    "roman": "Dir li t7eb",
    "es": "Haz lo que quieras",
    "en": "Do whatever you want",
    "cat": "🗣️ Cotidiano"
},

{
    "dz": "Ma 3andich lwa9t",
    "roman": "Ma 3andich lwa9t",
    "es": "No tengo tiempo",
    "en": "I don't have time",
    "cat": "🗣️ Cotidiano"
},

{
    "dz": "Nchallah",
    "roman": "Nchallah",
    "es": "Si Dios quiere",
    "en": "God willing",
    "cat": "🗣️ Cotidiano"
},

{
    "dz": "Hamdoulah",
    "roman": "Hamdoulah",
    "es": "Gracias a Dios",
    "en": "Thank God",
    "cat": "🗣️ Cotidiano"
},

{
    "dz": "Allah ybarek",
    "roman": "Allah ybarek",
    "es": "Qué bonito / Qué bien",
    "en": "How nice / Great",
    "cat": "🗣️ Cotidiano"
},

# ---------------------------------------------------------
# PEOPLE
# ---------------------------------------------------------

{
    "dz": "Sahbi",
    "roman": "Sahbi",
    "es": "Mi amigo / Tío",
    "en": "My friend / Bro",
    "cat": "👥 Gente"
},

{
    "dz": "Khouya",
    "roman": "Khouya",
    "es": "Hermano / Tío",
    "en": "Brother / Bro",
    "cat": "👥 Gente"
},

{
    "dz": "Khti",
    "roman": "Khti",
    "es": "Hermana",
    "en": "Sister",
    "cat": "👥 Gente"
},

{
    "dz": "Weld",
    "roman": "Weld",
    "es": "Chaval / Chico",
    "en": "Boy / Guy",
    "cat": "👥 Gente"
},

{
    "dz": "Bent",
    "roman": "Bent",
    "es": "Chica",
    "en": "Girl",
    "cat": "👥 Gente"
},

{
    "dz": "Chbab",
    "roman": "Chbab",
    "es": "Chicos",
    "en": "Guys",
    "cat": "👥 Gente"
},

{
    "dz": "Kbir",
    "roman": "Kbir",
    "es": "Mayor",
    "en": "Older",
    "cat": "👥 Gente"
},

{
    "dz": "Sghir",
    "roman": "Sghir",
    "es": "Pequeño / Joven",
    "en": "Small / Young",
    "cat": "👥 Gente"
},

# ---------------------------------------------------------
# LOVE
# ---------------------------------------------------------

{
    "dz": "N7ebek",
    "roman": "N7ebek",
    "es": "Te quiero",
    "en": "I love you",
    "cat": "❤️ Amor"
},

{
    "dz": "Nmot 3lik",
    "roman": "Nmot 3lik",
    "es": "Me muero por ti",
    "en": "I'm crazy about you",
    "cat": "❤️ Amor"
},

{
    "dz": "Twa7achtk",
    "roman": "Twa7achtk",
    "es": "Te echo de menos",
    "en": "I miss you",
    "cat": "❤️ Amor"
},

{
    "dz": "N7ebbek bezaf",
    "roman": "N7ebbek bezaf",
    "es": "Te quiero muchísimo",
    "en": "I love you so much",
    "cat": "❤️ Amor"
},

{
    "dz": "Ya 3omri",
    "roman": "Ya 3omri",
    "es": "Mi vida",
    "en": "My life",
    "cat": "❤️ Amor"
},

{
    "dz": "Ya rou7i",
    "roman": "Ya rou7i",
    "es": "Mi alma",
    "en": "My soul",
    "cat": "❤️ Amor"
},

{
    "dz": "Zine",
    "roman": "Zine",
    "es": "Guapo / Guapa",
    "en": "Handsome / Beautiful",
    "cat": "❤️ Amor"
},

{
    "dz": "Nti zwina",
    "roman": "Nti zwina",
    "es": "Eres guapísima",
    "en": "You're beautiful",
    "cat": "❤️ Amor"
},

{
    "dz": "Rani mchtaklek",
    "roman": "Rani mchtaklek",
    "es": "Te echo mucho de menos",
    "en": "I miss you a lot",
    "cat": "❤️ Amor"
},

# ---------------------------------------------------------
# REACTIONS
# ---------------------------------------------------------

{
    "dz": "Ya latif!",
    "roman": "Ya latif!",
    "es": "¡Dios mío!",
    "en": "Oh my God!",
    "cat": "😂 Reacciones"
},

{
    "dz": "Wach had l7ala?",
    "roman": "Wach had l7ala?",
    "es": "¿Qué es esto?",
    "en": "What is this?",
    "cat": "😂 Reacciones"
},

{
    "dz": "Hadi hiya!",
    "roman": "Hadi hiya!",
    "es": "¡Eso es!",
    "en": "That's it!",
    "cat": "😂 Reacciones"
},

{
    "dz": "Saha!",
    "roman": "Saha!",
    "es": "¡Bien hecho!",
    "en": "Well done!",
    "cat": "😂 Reacciones"
},

{
    "dz": "Waaa!",
    "roman": "Waaa!",
    "es": "¡Guau!",
    "en": "Wow!",
    "cat": "😂 Reacciones"
},

{
    "dz": "Matekdebch!",
    "roman": "Matekdebch!",
    "es": "¡No mientas!",
    "en": "Don't lie!",
    "cat": "😂 Reacciones"
},

{
    "dz": "Bsa7tek!",
    "roman": "Bsa7tek!",
    "es": "¡Que lo disfrutes!",
    "en": "Enjoy it!",
    "cat": "😂 Reacciones"
},

{
    "dz": "Ya kho!",
    "roman": "Ya kho!",
    "es": "¡Venga, tío!",
    "en": "Come on, bro!",
    "cat": "😂 Reacciones"
},

# ---------------------------------------------------------
# FOOD
# ---------------------------------------------------------

{
    "dz": "Lmakla",
    "roman": "Lmakla",
    "es": "La comida",
    "en": "Food",
    "cat": "🍽️ Comida"
},

{
    "dz": "Chahiya tayba",
    "roman": "Chahiya tayba",
    "es": "Buen provecho",
    "en": "Enjoy your meal",
    "cat": "🍽️ Comida"
},

{
    "dz": "Bnin",
    "roman": "Bnin",
    "es": "Está delicioso",
    "en": "It's delicious",
    "cat": "🍽️ Comida"
},

{
    "dz": "Chba3t",
    "roman": "Chba3t",
    "es": "Estoy lleno",
    "en": "I'm full",
    "cat": "🍽️ Comida"
},

{
    "dz": "Rani ji3an",
    "roman": "Rani ji3an",
    "es": "Tengo hambre",
    "en": "I'm hungry",
    "cat": "🍽️ Comida"
},

{
    "dz": "Rani 3atchan",
    "roman": "Rani 3atchan",
    "es": "Tengo sed",
    "en": "I'm thirsty",
    "cat": "🍽️ Comida"
},

{
    "dz": "Nchrob qahwa",
    "roman": "Nchrob qahwa",
    "es": "Voy a tomar un café",
    "en": "I'm going to have coffee",
    "cat": "🍽️ Comida"
},

{
    "dz": "Nrou7o naklo",
    "roman": "Nrou7o naklo",
    "es": "Vamos a comer",
    "en": "Let's go eat",
    "cat": "🍽️ Comida"
},

# ---------------------------------------------------------
# MONEY
# ---------------------------------------------------------

{
    "dz": "Ch7al hadha?",
    "roman": "Ch7al hadha?",
    "es": "¿Cuánto cuesta?",
    "en": "How much is this?",
    "cat": "💰 Dinero"
},

{
    "dz": "Ghali",
    "roman": "Ghali",
    "es": "Es caro",
    "en": "It's expensive",
    "cat": "💰 Dinero"
},

{
    "dz": "Rkhis",
    "roman": "Rkhis",
    "es": "Es barato",
    "en": "It's cheap",
    "cat": "💰 Dinero"
},

{
    "dz": "Ma 3andich drahm",
    "roman": "Ma 3andich drahm",
    "es": "No tengo dinero",
    "en": "I don't have money",
    "cat": "💰 Dinero"
},

{
    "dz": "Sarf",
    "roman": "Sarf",
    "es": "Cambio",
    "en": "Change",
    "cat": "💰 Dinero"
},

{
    "dz": "Drahem",
    "roman": "Drahem",
    "es": "Dinero",
    "en": "Money",
    "cat": "💰 Dinero"
},

# ---------------------------------------------------------
# PLACES
# ---------------------------------------------------------

{
    "dz": "Dar",
    "roman": "Dar",
    "es": "Casa",
    "en": "House",
    "cat": "🚗 Lugares"
},

{
    "dz": "L7anout",
    "roman": "L7anout",
    "es": "Tienda",
    "en": "Shop",
    "cat": "🚗 Lugares"
},

{
    "dz": "Sou9",
    "roman": "Sou9",
    "es": "Mercado",
    "en": "Market",
    "cat": "🚗 Lugares"
},

{
    "dz": "Chari3",
    "roman": "Chari3",
    "es": "Calle",
    "en": "Street",
    "cat": "🚗 Lugares"
},

{
    "dz": "Centre ville",
    "roman": "Centre ville",
    "es": "Centro de la ciudad",
    "en": "City center",
    "cat": "🚗 Lugares"
},

{
    "dz": "Lbahri",
    "roman": "Lbahri",
    "es": "La playa",
    "en": "The beach",
    "cat": "🚗 Lugares"
},

{
    "dz": "Université",
    "roman": "Université",
    "es": "Universidad",
    "en": "University",
    "cat": "🚗 Lugares"
},

# ---------------------------------------------------------
# FAMOUS EXPRESSIONS
# ---------------------------------------------------------

{
    "dz": "Hada houwa!",
    "roman": "Hada houwa!",
    "es": "¡Así es!",
    "en": "That's how it is!",
    "cat": "🔥 Expresiones"
},

{
    "dz": "Ma fhemt walo",
    "roman": "Ma fhemt walo",
    "es": "No entendí nada",
    "en": "I understood nothing",
    "cat": "🔥 Expresiones"
},

{
    "dz": "Walo",
    "roman": "Walo",
    "es": "Nada",
    "en": "Nothing",
    "cat": "🔥 Expresiones"
},

{
    "dz": "Haka",
    "roman": "Haka",
    "es": "Así",
    "en": "Like this",
    "cat": "🔥 Expresiones"
},

{
    "dz": "Bessif",
    "roman": "Bessif",
    "es": "A la fuerza",
    "en": "By force",
    "cat": "🔥 Expresiones"
},

{
    "dz": "Dork",
    "roman": "Dork",
    "es": "Ahora",
    "en": "Now",
    "cat": "🔥 Expresiones"
},

{
    "dz": "Ba3d",
    "roman": "Ba3d",
    "es": "Después",
    "en": "Later",
    "cat": "🔥 Expresiones"
},

{
    "dz": "Hna",
    "roman": "Hna",
    "es": "Aquí",
    "en": "Here",
    "cat": "🔥 Expresiones"
},

{
    "dz": "Temma",
    "roman": "Temma",
    "es": "Allí",
    "en": "There",
    "cat": "🔥 Expresiones"
},

{
    "dz": "Hada ma kayen",
    "roman": "Hada ma kayen",
    "es": "Esto no existe",
    "en": "This doesn't exist",
    "cat": "🔥 Expresiones"
},

# ---------------------------------------------------------
# SLANG
# ---------------------------------------------------------

{
    "dz": "Sahbi",
    "roman": "Sahbi",
    "es": "Tío",
    "en": "Bro",
    "cat": "😎 Argot"
},

{
    "dz": "Kho",
    "roman": "Kho",
    "es": "Tío / Bro",
    "en": "Bro",
    "cat": "😎 Argot"
},

{
    "dz": "Mlih",
    "roman": "Mlih",
    "es": "Bien / Genial",
    "en": "Good / Great",
    "cat": "😎 Argot"
},

{
    "dz": "Yakhi",
    "roman": "Yakhi",
    "es": "¿En serio?",
    "en": "Seriously?",
    "cat": "😎 Argot"
},

{
    "dz": "Wesh",
    "roman": "Wesh",
    "es": "¿Qué?",
    "en": "What?",
    "cat": "😎 Argot"
},

{
    "dz": "Tchipa",
    "roman": "Tchipa",
    "es": "Soborno",
    "en": "Bribe",
    "cat": "😎 Argot"
},

{
    "dz": "Hawaji",
    "roman": "Hawaji",
    "es": "Cosas",
    "en": "Things",
    "cat": "😎 Argot"
},

{
    "dz": "Fikra",
    "roman": "Fikra",
    "es": "Idea",
    "en": "Idea",
    "cat": "😎 Argot"
},

# ---------------------------------------------------------
# USEFUL
# ---------------------------------------------------------

{
    "dz": "3afak",
    "roman": "3afak",
    "es": "Por favor",
    "en": "Please",
    "cat": "🧠 Útiles"
},

{
    "dz": "Smahli",
    "roman": "Smahli",
    "es": "Perdón",
    "en": "Sorry / Excuse me",
    "cat": "🧠 Útiles"
},

{
    "dz": "Merci",
    "roman": "Merci",
    "es": "Gracias",
    "en": "Thank you",
    "cat": "🧠 Útiles"
},

{
    "dz": "Mabrouk",
    "roman": "Mabrouk",
    "es": "Enhorabuena",
    "en": "Congratulations",
    "cat": "🧠 Útiles"
},

{
    "dz": "Allah yjib lkhir",
    "roman": "Allah yjib lkhir",
    "es": "Que todo salga bien",
    "en": "Hopefully everything goes well",
    "cat": "🧠 Útiles"
},

{
    "dz": "Rabbi ykhalik",
    "roman": "Rabbi ykhalik",
    "es": "Que Dios te bendiga",
    "en": "God bless you",
    "cat": "🧠 Útiles"
},

{
    "dz": "Matkhafch",
    "roman": "Matkhafch",
    "es": "No tengas miedo",
    "en": "Don't be afraid",
    "cat": "🧠 Útiles"
},

{
    "dz": "Ma tkhammemch",
    "roman": "Ma tkhammemch",
    "es": "No te preocupes",
    "en": "Don't worry",
    "cat": "🧠 Útiles"
},

{
    "dz": "T3ala",
    "roman": "T3ala",
    "es": "Ven",
    "en": "Come",
    "cat": "🧠 Útiles"
},

{
    "dz": "Roh",
    "roman": "Roh",
    "es": "Vete",
    "en": "Go",
    "cat": "🧠 Útiles"
},

{
    "dz": "Stanna",
    "roman": "Stanna",
    "es": "Espera",
    "en": "Wait",
    "cat": "🧠 Útiles"
},

{
    "dz": "Chouf",
    "roman": "Chouf",
    "es": "Mira",
    "en": "Look",
    "cat": "🧠 Útiles"
},

{
    "dz": "Esma3",
    "roman": "Esma3",
    "es": "Escucha",
    "en": "Listen",
    "cat": "🧠 Útiles"
},

{
    "dz": "Aji",
    "roman": "Aji",
    "es": "Ven aquí",
    "en": "Come here",
    "cat": "🧠 Útiles"
},

]


# =========================================================
# SEARCH + CATEGORY
# =========================================================

st.markdown('<div class="search-label">SEARCH EXPRESSIONS</div>', unsafe_allow_html=True)

col1, col2 = st.columns([2.3, 1])

with col1:
    search = st.text_input(
        "Search",
        placeholder="Try: sahbi, hola, love, food...",
        label_visibility="collapsed"
    )

with col2:

    categories = ["All"] + sorted(
        list(set(item["cat"] for item in expressions))
    )

    category = st.selectbox(
        "Category",
        categories,
        label_visibility="collapsed"
    )


# =========================================================
# FILTER
# =========================================================

search_clean = search.lower().strip()

filtered = []

for item in expressions:

    if category != "All" and item["cat"] != category:
        continue

    if search_clean:

        searchable = (
            item["dz"]
            + " "
            + item["roman"]
            + " "
            + item["es"]
            + " "
            + item["en"]
        ).lower()

        if search_clean not in searchable:
            continue

    filtered.append(item)


# =========================================================
# RESULTS COUNT
# =========================================================

st.markdown(
    f"""
    <div class="results-info">
        {len(filtered)} expressions found
    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# CARD COLORS
# =========================================================

CATEGORY_COLORS = {

    "👋 Saludos": "#22c55e",

    "🗣️ Cotidiano": "#3b82f6",

    "👥 Gente": "#a855f7",

    "❤️ Amor": "#ef4444",

    "😂 Reacciones": "#f59e0b",

    "🍽️ Comida": "#f97316",

    "💰 Dinero": "#10b981",

    "🚗 Lugares": "#06b6d4",

    "🔥 Expresiones": "#f43f5e",

    "😎 Argot": "#8b5cf6",

    "🧠 Útiles": "#64748b",
}


# =========================================================
# BUILD CARDS
# =========================================================

cards = ""

for item in filtered:

    dz = html.escape(item["dz"])
    roman = html.escape(item["roman"])
    es = html.escape(item["es"])
    en = html.escape(item["en"])
    cat = html.escape(item["cat"])

    color = CATEGORY_COLORS.get(
        item["cat"],
        "#64748b"
    )

    # Escape for JavaScript
    speech_text = (
        item["es"]
        .replace("\\", "\\\\")
        .replace("'", "\\'")
        .replace("\n", " ")
    )

    cards += f"""

    <div class="card">

        <div class="card-top">

            <div class="category"
                 style="--category-color:{color}">
                {cat}
            </div>

        </div>

        <div class="dz-text">
            {dz}
        </div>

        <div class="roman">
            {roman}
        </div>

        <div
            class="spanish"
            onclick="speakSpanish('{speech_text}')"
            title="Tap to hear Spanish pronunciation"
        >

            <span class="speaker">
                🔊
            </span>

            <span>
                {es}
            </span>

        </div>

        <div class="english">
            {en}
        </div>

    </div>

    """


# =========================================================
# EMPTY RESULT
# =========================================================

if not filtered:

    st.markdown("""
    <div style="
        text-align:center;
        padding:70px 20px;
        color:#666e79;
    ">

        <div style="
            font-size:42px;
            margin-bottom:15px;
        ">
            🔎
        </div>

        <div style="
            font-size:18px;
            font-weight:700;
            color:#9ca3af;
        ">
            Nothing found
        </div>

        <div style="
            font-size:13px;
            margin-top:7px;
        ">
            Try another word or category.
        </div>

    </div>
    """, unsafe_allow_html=True)

else:

    # =====================================================
    # RESPONSIVE HTML COMPONENT
    # =====================================================

    component_html = f"""

    <!DOCTYPE html>

    <html>

    <head>

    <meta name="viewport"
          content="width=device-width, initial-scale=1.0">

    <style>

        * {{
            box-sizing: border-box;
        }}

        html, body {{
            margin: 0;
            padding: 0;

            background: transparent;

            font-family:
                -apple-system,
                BlinkMacSystemFont,
                "Segoe UI",
                Inter,
                sans-serif;

            color: white;
        }}

        .grid {{

            display: grid;

            grid-template-columns:
                repeat(2, minmax(0, 1fr));

            gap: 14px;

            width: 100%;
        }}

        .card {{

            position: relative;

            padding: 21px;

            min-height: 225px;

            background:
                linear-gradient(
                    145deg,
                    rgba(22,25,31,0.98),
                    rgba(13,16,20,0.98)
                );

            border:
                1px solid rgba(255,255,255,0.075);

            border-radius: 20px;

            overflow: hidden;

            transition:
                transform .18s ease,
                border-color .18s ease,
                background .18s ease;

        }}

        .card:hover {{

            transform: translateY(-2px);

            border-color:
                rgba(255,255,255,0.16);

            background:
                linear-gradient(
                    145deg,
                    rgba(27,31,38,0.99),
                    rgba(15,18,23,0.99)
                );

        }}

        .card::before {{

            content: "";

            position: absolute;

            top: 0;
            left: 0;

            width: 100%;
            height: 2px;

            background:
                linear-gradient(
                    90deg,
                    var(--category-color, #64748b),
                    transparent
                );

            opacity: .8;
        }}

        .card-top {{

            display: flex;

            justify-content: flex-start;

            margin-bottom: 18px;
        }}

        .category {{

            display: inline-flex;

            align-items: center;

            padding:
                5px 9px;

            border-radius: 8px;

            background:
                color-mix(
                    in srgb,
                    var(--category-color) 12%,
                    transparent
                );

            color:
                var(--category-color);

            font-size: 10px;

            font-weight: 800;

            letter-spacing: .4px;

        }}

        .dz-text {{

            font-size: 23px;

            font-weight: 850;

            letter-spacing: -.5px;

            color: #f4f5f7;

            margin-bottom: 3px;

        }}

        .roman {{

            font-size: 12px;

            color: #656d79;

            font-style: italic;

            margin-bottom: 20px;

        }}

        .spanish {{

            display: flex;

            align-items: center;

            gap: 9px;

            width: fit-content;

            max-width: 100%;

            padding: 8px 11px;

            margin-left: -11px;

            border-radius: 10px;

            color: #e7e9ed;

            font-size: 17px;

            font-weight: 700;

            line-height: 1.35;

            cursor: pointer;

            transition:
                background .15s ease,
                transform .15s ease;

            user-select: none;

        }}

        .spanish:hover {{

            background:
                rgba(255,255,255,0.055);

        }}

        .spanish:active {{

            transform: scale(.97);

        }}

        .speaker {{

            font-size: 15px;

            opacity: .65;

            flex-shrink: 0;

        }}

        .english {{

            margin-top: 10px;

            color: #626a76;

            font-size: 12px;

            line-height: 1.45;

        }}


        @media (max-width: 700px) {{

            .grid {{

                grid-template-columns: 1fr;

                gap: 12px;

            }}

            .card {{

                min-height: 210px;

                padding: 19px;

                border-radius: 18px;

            }}

            .dz-text {{

                font-size: 21px;

            }}

            .spanish {{

                font-size: 16px;

            }}

        }}

    </style>

    </head>

    <body>

        <div class="grid">

            {cards}

        </div>


        <script>

            let voices = [];

            function loadVoices() {{

                voices =
                    window.speechSynthesis.getVoices();

            }}

            loadVoices();

            if (window.speechSynthesis) {{

                window.speechSynthesis.onvoiceschanged =
                    loadVoices;

            }}


            function speakSpanish(text) {{

                if (!window.speechSynthesis) {{

                    return;

                }}

                window.speechSynthesis.cancel();

                const utterance =
                    new SpeechSynthesisUtterance(text);

                utterance.lang = "es-ES";

                utterance.rate = 0.90;

                utterance.pitch = 1.0;

                utterance.volume = 1.0;


                let spanishVoice =
                    voices.find(
                        voice =>
                            voice.lang &&
                            voice.lang.toLowerCase()
                                .startsWith("es-es")
                    );


                if (!spanishVoice) {{

                    spanishVoice =
                        voices.find(
                            voice =>
                                voice.lang &&
                                voice.lang.toLowerCase()
                                    .startsWith("es")
                        );

                }}


                if (spanishVoice) {{

                    utterance.voice =
                        spanishVoice;

                }}


                window.speechSynthesis
                    .speak(utterance);

            }}

        </script>

    </body>

    </html>

    """

    # More than enough height for desktop/mobile.
    # scrolling=True prevents clipping if cards become taller.

    height = max(
        300,
        min(
            10000,
            len(filtered) * 250 + 100
        )
    )

    components.html(
        component_html,
        height=height,
        scrolling=True
    )


# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div class="site-footer">

    🇩🇿 Dzayer → Español

    <br><br>

    Learn the Spanish behind the expressions you already know.

    <br><br>

    MADE FOR ALGERIANS • HECHO CON ❤️

</div>
""", unsafe_allow_html=True)
