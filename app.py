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

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

.stApp {
    background:
        radial-gradient(circle at 10% 0%, rgba(34,197,94,0.10), transparent 28%),
        radial-gradient(circle at 90% 10%, rgba(59,130,246,0.10), transparent 28%),
        #080b10;
    color: #f8fafc;
    font-family: 'Inter', sans-serif;
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

.block-container {
    max-width: 1250px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* HERO */

.hero {
    text-align: center;
    padding: 48px 20px 40px;
    margin-bottom: 25px;
    border-radius: 28px;
    border: 1px solid rgba(255,255,255,0.07);
    background:
        radial-gradient(circle at 50% 0%, rgba(34,197,94,0.12), transparent 45%),
        linear-gradient(145deg, rgba(255,255,255,0.035), rgba(255,255,255,0.01));
    box-shadow: 0 25px 80px rgba(0,0,0,0.25);
}

.hero-badge {
    display: inline-block;
    padding: 8px 15px;
    border-radius: 999px;
    background: rgba(34,197,94,0.10);
    border: 1px solid rgba(34,197,94,0.25);
    color: #4ade80;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 1.5px;
    margin-bottom: 18px;
}

.hero h1 {
    margin: 0;
    font-size: clamp(38px, 6vw, 68px);
    font-weight: 800;
    letter-spacing: -3px;
    line-height: 1;
    background: linear-gradient(90deg, #ffffff, #d1fae5);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-subtitle {
    margin: 20px auto 0;
    max-width: 650px;
    color: #94a3b8;
    font-size: 15px;
    line-height: 1.7;
}

.hero-footer {
    margin-top: 25px;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-wrap: wrap;
    gap: 12px;
    color: #64748b;
    font-size: 11px;
    font-weight: 600;
}

/* SEARCH */

.search-label {
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 1.5px;
    color: #64748b;
    margin-bottom: 7px;
}

div[data-baseweb="input"] {
    background: #10151d !important;
    border: 1px solid #1e293b !important;
    border-radius: 12px !important;
}

div[data-baseweb="input"]:focus-within {
    border-color: rgba(34,197,94,0.55) !important;
    box-shadow: 0 0 0 1px rgba(34,197,94,0.15) !important;
}

div[data-baseweb="select"] > div {
    background: #10151d !important;
    border: 1px solid #1e293b !important;
    border-radius: 12px !important;
}

input {
    color: #f8fafc !important;
}

.results-info {
    margin: 18px 0 13px;
    color: #64748b;
    font-size: 12px;
    font-weight: 600;
}

/* FOOTER */

.site-footer {
    text-align: center;
    padding: 55px 20px 20px;
    color: #475569;
    font-size: 11px;
    line-height: 1.6;
}

/* MOBILE */

@media (max-width: 700px) {

    .block-container {
        padding-left: 12px;
        padding-right: 12px;
        padding-top: 1rem;
    }

    .hero {
        padding: 38px 15px 32px;
        border-radius: 22px;
    }

    .hero h1 {
        font-size: 42px;
        letter-spacing: -2px;
    }

    .hero-subtitle {
        font-size: 13px;
    }

    .hero-footer {
        gap: 8px;
        font-size: 10px;
    }
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# HERO
# =========================================================

st.markdown("""
<div class="hero">
    <div class="hero-badge">🇩🇿 ALGERIAN → 🇪🇸 SPANISH</div>

    <h1>Dzayer → Español</h1>

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
# EXPRESSIONS
# =========================================================

expressions = [

    # -----------------------------------------------------
    # SALUDOS
    # -----------------------------------------------------

    {
        "cat": "👋 Saludos",
        "dz": "Salam",
        "roman": "Salam",
        "es": "Hola",
        "en": "Hello"
    },
    {
        "cat": "👋 Saludos",
        "dz": "Saha",
        "roman": "Saha",
        "es": "Hola / ¿Qué tal?",
        "en": "Hi / How are you?"
    },
    {
        "cat": "👋 Saludos",
        "dz": "Saha ftorkom",
        "roman": "Saha ftorkom",
        "es": "Que aproveche",
        "en": "Enjoy your meal"
    },
    {
        "cat": "👋 Saludos",
        "dz": "Saha chribtek",
        "roman": "Saha chribtek",
        "es": "¡Salud!",
        "en": "Cheers"
    },
    {
        "cat": "👋 Saludos",
        "dz": "Labas?",
        "roman": "Labas?",
        "es": "¿Todo bien?",
        "en": "Everything good?"
    },
    {
        "cat": "👋 Saludos",
        "dz": "Kach ma kayen?",
        "roman": "Kach ma kayen?",
        "es": "¿Qué tal?",
        "en": "What's up?"
    },
    {
        "cat": "👋 Saludos",
        "dz": "Win rak?",
        "roman": "Win rak?",
        "es": "¿Dónde estás?",
        "en": "Where are you?"
    },
    {
        "cat": "👋 Saludos",
        "dz": "Chbab?",
        "roman": "Chbab?",
        "es": "¿Qué tal, tío?",
        "en": "What's up, bro?"
    },
    {
        "cat": "👋 Saludos",
        "dz": "Sbah el khir",
        "roman": "Sbah el khir",
        "es": "Buenos días",
        "en": "Good morning"
    },
    {
        "cat": "👋 Saludos",
        "dz": "Msa el khir",
        "roman": "Msa el khir",
        "es": "Buenas tardes",
        "en": "Good afternoon"
    },
    {
        "cat": "👋 Saludos",
        "dz": "Tsba7 3la khir",
        "roman": "Tsba7 3la khir",
        "es": "Buenas noches",
        "en": "Good night"
    },

    # -----------------------------------------------------
    # COTIDIANO
    # -----------------------------------------------------

    {
        "cat": "🗣️ Cotidiano",
        "dz": "Chnou rak dir?",
        "roman": "Chnou rak dir?",
        "es": "¿Qué estás haciendo?",
        "en": "What are you doing?"
    },
    {
        "cat": "🗣️ Cotidiano",
        "dz": "Win rak rayeh?",
        "roman": "Win rak rayeh?",
        "es": "¿Adónde vas?",
        "en": "Where are you going?"
    },
    {
        "cat": "🗣️ Cotidiano",
        "dz": "Ana jay",
        "roman": "Ana jay",
        "es": "Ya voy",
        "en": "I'm coming"
    },
    {
        "cat": "🗣️ Cotidiano",
        "dz": "Sani brk",
        "roman": "Sani brk",
        "es": "Espera un momento",
        "en": "Wait a moment"
    },
    {
        "cat": "🗣️ Cotidiano",
        "dz": "Ma fhemtch",
        "roman": "Ma fhemtch",
        "es": "No entendí",
        "en": "I didn't understand"
    },
    {
        "cat": "🗣️ Cotidiano",
        "dz": "Fhemt",
        "roman": "Fhemt",
        "es": "Entendido",
        "en": "Got it"
    },
    {
        "cat": "🗣️ Cotidiano",
        "dz": "Machi mochkil",
        "roman": "Machi mochkil",
        "es": "No pasa nada",
        "en": "No problem"
    },
    {
        "cat": "🗣️ Cotidiano",
        "dz": "Normal",
        "roman": "Normal",
        "es": "Normal",
        "en": "Normal"
    },
    {
        "cat": "🗣️ Cotidiano",
        "dz": "Ki ma hab",
        "roman": "Ki ma hab",
        "es": "Como quieras",
        "en": "As you want"
    },
    {
        "cat": "🗣️ Cotidiano",
        "dz": "Dir li t7eb",
        "roman": "Dir li t7eb",
        "es": "Haz lo que quieras",
        "en": "Do whatever you want"
    },
    {
        "cat": "🗣️ Cotidiano",
        "dz": "Ma 3andich lwa9t",
        "roman": "Ma 3andich lwa9t",
        "es": "No tengo tiempo",
        "en": "I don't have time"
    },
    {
        "cat": "🗣️ Cotidiano",
        "dz": "Nchallah",
        "roman": "Nchallah",
        "es": "Si Dios quiere",
        "en": "God willing"
    },
    {
        "cat": "🗣️ Cotidiano",
        "dz": "Hamdoulah",
        "roman": "Hamdoulah",
        "es": "Gracias a Dios",
        "en": "Thank God"
    },
    {
        "cat": "🗣️ Cotidiano",
        "dz": "Allah ybarek",
        "roman": "Allah ybarek",
        "es": "Qué bonito / Qué bien",
        "en": "How nice / How good"
    },
    {
        "cat": "🗣️ Cotidiano",
        "dz": "Dork",
        "roman": "Dork",
        "es": "Ahora",
        "en": "Now"
    },
    {
        "cat": "🗣️ Cotidiano",
        "dz": "Ba3d",
        "roman": "Ba3d",
        "es": "Después",
        "en": "Later"
    },
    {
        "cat": "🗣️ Cotidiano",
        "dz": "Hna",
        "roman": "Hna",
        "es": "Aquí",
        "en": "Here"
    },
    {
        "cat": "🗣️ Cotidiano",
        "dz": "Temma",
        "roman": "Temma",
        "es": "Allí",
        "en": "There"
    },

    # -----------------------------------------------------
    # GENTE
    # -----------------------------------------------------

    {
        "cat": "👥 Gente",
        "dz": "Sahbi",
        "roman": "Sahbi",
        "es": "Mi amigo / Tío",
        "en": "My friend / Bro"
    },
    {
        "cat": "👥 Gente",
        "dz": "Khouya",
        "roman": "Khouya",
        "es": "Hermano / Tío",
        "en": "Brother / Bro"
    },
    {
        "cat": "👥 Gente",
        "dz": "Khti",
        "roman": "Khti",
        "es": "Hermana",
        "en": "Sister"
    },
    {
        "cat": "👥 Gente",
        "dz": "Weld",
        "roman": "Weld",
        "es": "Chaval / Chico",
        "en": "Boy / Guy"
    },
    {
        "cat": "👥 Gente",
        "dz": "Bent",
        "roman": "Bent",
        "es": "Chica",
        "en": "Girl"
    },
    {
        "cat": "👥 Gente",
        "dz": "Chbab",
        "roman": "Chbab",
        "es": "Chicos",
        "en": "Guys"
    },
    {
        "cat": "👥 Gente",
        "dz": "Kbir",
        "roman": "Kbir",
        "es": "Mayor",
        "en": "Older"
    },
    {
        "cat": "👥 Gente",
        "dz": "Sghir",
        "roman": "Sghir",
        "es": "Pequeño / Joven",
        "en": "Small / Young"
    },
    {
        "cat": "👥 Gente",
        "dz": "Lweld",
        "roman": "Lweld",
        "es": "El chico",
        "en": "The boy"
    },
    {
        "cat": "👥 Gente",
        "dz": "Lbnat",
        "roman": "Lbnat",
        "es": "Las chicas",
        "en": "The girls"
    },

    # -----------------------------------------------------
    # AMOR
    # -----------------------------------------------------

    {
        "cat": "❤️ Amor",
        "dz": "N7ebek",
        "roman": "N7ebek",
        "es": "Te quiero",
        "en": "I love you"
    },
    {
        "cat": "❤️ Amor",
        "dz": "Nmot 3lik",
        "roman": "Nmot 3lik",
        "es": "Me muero por ti",
        "en": "I'm crazy about you"
    },
    {
        "cat": "❤️ Amor",
        "dz": "Twa7achtk",
        "roman": "Twa7achtk",
        "es": "Te echo de menos",
        "en": "I miss you"
    },
    {
        "cat": "❤️ Amor",
        "dz": "N7ebbek bezaf",
        "roman": "N7ebbek bezaf",
        "es": "Te quiero muchísimo",
        "en": "I love you so much"
    },
    {
        "cat": "❤️ Amor",
        "dz": "Ya 3omri",
        "roman": "Ya 3omri",
        "es": "Mi vida",
        "en": "My love / My life"
    },
    {
        "cat": "❤️ Amor",
        "dz": "Ya rou7i",
        "roman": "Ya rou7i",
        "es": "Mi alma",
        "en": "My soul"
    },
    {
        "cat": "❤️ Amor",
        "dz": "Zine",
        "roman": "Zine",
        "es": "Guapo / Guapa",
        "en": "Handsome / Beautiful"
    },
    {
        "cat": "❤️ Amor",
        "dz": "Nti zwina",
        "roman": "Nti zwina",
        "es": "Eres guapísima",
        "en": "You're beautiful"
    },
    {
        "cat": "❤️ Amor",
        "dz": "Rani mchtaklek",
        "roman": "Rani mchtaklek",
        "es": "Te echo mucho de menos",
        "en": "I miss you a lot"
    },
    {
        "cat": "❤️ Amor",
        "dz": "N7eb nchofo",
        "roman": "N7eb nchofo",
        "es": "Quiero verte",
        "en": "I want to see you"
    },

    # -----------------------------------------------------
    # REACCIONES
    # -----------------------------------------------------

    {
        "cat": "😂 Reacciones",
        "dz": "Ya latif!",
        "roman": "Ya latif!",
        "es": "¡Dios mío!",
        "en": "Oh my God!"
    },
    {
        "cat": "😂 Reacciones",
        "dz": "Wach had l7ala?",
        "roman": "Wach had l7ala?",
        "es": "¿Qué es esto?",
        "en": "What is this?"
    },
    {
        "cat": "😂 Reacciones",
        "dz": "Hadi hiya!",
        "roman": "Hadi hiya!",
        "es": "¡Eso es!",
        "en": "That's it!"
    },
    {
        "cat": "😂 Reacciones",
        "dz": "Saha!",
        "roman": "Saha!",
        "es": "¡Bien hecho!",
        "en": "Well done!"
    },
    {
        "cat": "😂 Reacciones",
        "dz": "Waaa!",
        "roman": "Waaa!",
        "es": "¡Guau!",
        "en": "Wow!"
    },
    {
        "cat": "😂 Reacciones",
        "dz": "Matekdebch!",
        "roman": "Matekdebch!",
        "es": "¡No mientas!",
        "en": "Don't lie!"
    },
    {
        "cat": "😂 Reacciones",
        "dz": "Bsa7tek!",
        "roman": "Bsa7tek!",
        "es": "¡Que lo disfrutes!",
        "en": "Enjoy it!"
    },
    {
        "cat": "😂 Reacciones",
        "dz": "Ya kho!",
        "roman": "Ya kho!",
        "es": "¡Venga, tío!",
        "en": "Come on, bro!"
    },
    {
        "cat": "😂 Reacciones",
        "dz": "Wesh?",
        "roman": "Wesh?",
        "es": "¿Qué?",
        "en": "What?"
    },
    {
        "cat": "😂 Reacciones",
        "dz": "Serieux?",
        "roman": "Serieux?",
        "es": "¿En serio?",
        "en": "Seriously?"
    },

    # -----------------------------------------------------
    # COMIDA
    # -----------------------------------------------------

    {
        "cat": "🍽️ Comida",
        "dz": "Lmakla",
        "roman": "Lmakla",
        "es": "La comida",
        "en": "Food"
    },
    {
        "cat": "🍽️ Comida",
        "dz": "Chahiya tayba",
        "roman": "Chahiya tayba",
        "es": "Buen provecho",
        "en": "Enjoy your meal"
    },
    {
        "cat": "🍽️ Comida",
        "dz": "Bnin",
        "roman": "Bnin",
        "es": "Está delicioso",
        "en": "It's delicious"
    },
    {
        "cat": "🍽️ Comida",
        "dz": "Chba3t",
        "roman": "Chba3t",
        "es": "Estoy lleno",
        "en": "I'm full"
    },
    {
        "cat": "🍽️ Comida",
        "dz": "Rani ji3an",
        "roman": "Rani ji3an",
        "es": "Tengo hambre",
        "en": "I'm hungry"
    },
    {
        "cat": "🍽️ Comida",
        "dz": "Rani 3atchan",
        "roman": "Rani 3atchan",
        "es": "Tengo sed",
        "en": "I'm thirsty"
    },
    {
        "cat": "🍽️ Comida",
        "dz": "Nchrob qahwa",
        "roman": "Nchrob qahwa",
        "es": "Voy a tomar un café",
        "en": "I'm going to have coffee"
    },
    {
        "cat": "🍽️ Comida",
        "dz": "Nrou7o naklo",
        "roman": "Nrou7o naklo",
        "es": "Vamos a comer",
        "en": "Let's go eat"
    },
    {
        "cat": "🍽️ Comida",
        "dz": "Ndirou l3cha",
        "roman": "Ndirou l3cha",
        "es": "Vamos a cenar",
        "en": "Let's have dinner"
    },
    {
        "cat": "🍽️ Comida",
        "dz": "Jib lmakla",
        "roman": "Jib lmakla",
        "es": "Trae la comida",
        "en": "Bring the food"
    },

    # -----------------------------------------------------
    # DINERO
    # -----------------------------------------------------

    {
        "cat": "💰 Dinero",
        "dz": "Ch7al hadha?",
        "roman": "Ch7al hadha?",
        "es": "¿Cuánto cuesta?",
        "en": "How much is this?"
    },
    {
        "cat": "💰 Dinero",
        "dz": "Ghali",
        "roman": "Ghali",
        "es": "Es caro",
        "en": "It's expensive"
    },
    {
        "cat": "💰 Dinero",
        "dz": "Rkhis",
        "roman": "Rkhis",
        "es": "Es barato",
        "en": "It's cheap"
    },
    {
        "cat": "💰 Dinero",
        "dz": "Ma 3andich drahm",
        "roman": "Ma 3andich drahm",
        "es": "No tengo dinero",
        "en": "I don't have money"
    },
    {
        "cat": "💰 Dinero",
        "dz": "Sarf",
        "roman": "Sarf",
        "es": "Cambio",
        "en": "Change"
    },
    {
        "cat": "💰 Dinero",
        "dz": "Drahem",
        "roman": "Drahem",
        "es": "Dinero",
        "en": "Money"
    },
    {
        "cat": "💰 Dinero",
        "dz": "3tini drahem",
        "roman": "3tini drahem",
        "es": "Dame dinero",
        "en": "Give me money"
    },
    {
        "cat": "💰 Dinero",
        "dz": "Ma ykafich",
        "roman": "Ma ykafich",
        "es": "No es suficiente",
        "en": "It's not enough"
    },

    # -----------------------------------------------------
    # LUGARES
    # -----------------------------------------------------

    {
        "cat": "🚗 Lugares",
        "dz": "Dar",
        "roman": "Dar",
        "es": "Casa",
        "en": "House"
    },
    {
        "cat": "🚗 Lugares",
        "dz": "L7anout",
        "roman": "L7anout",
        "es": "Tienda",
        "en": "Shop"
    },
    {
        "cat": "🚗 Lugares",
        "dz": "Sou9",
        "roman": "Sou9",
        "es": "Mercado",
        "en": "Market"
    },
    {
        "cat": "🚗 Lugares",
        "dz": "Chari3",
        "roman": "Chari3",
        "es": "Calle",
        "en": "Street"
    },
    {
        "cat": "🚗 Lugares",
        "dz": "Centre ville",
        "roman": "Centre ville",
        "es": "Centro de la ciudad",
        "en": "City center"
    },
    {
        "cat": "🚗 Lugares",
        "dz": "Lbahri",
        "roman": "Lbahri",
        "es": "La playa",
        "en": "The beach"
    },
    {
        "cat": "🚗 Lugares",
        "dz": "Université",
        "roman": "Université",
        "es": "Universidad",
        "en": "University"
    },
    {
        "cat": "🚗 Lugares",
        "dz": "L'aéroport",
        "roman": "L'aéroport",
        "es": "El aeropuerto",
        "en": "Airport"
    },
    {
        "cat": "🚗 Lugares",
        "dz": "Win rah?",
        "roman": "Win rah?",
        "es": "¿Dónde está?",
        "en": "Where is it?"
    },
    {
        "cat": "🚗 Lugares",
        "dz": "Nrou7 lcentre",
        "roman": "Nrou7 lcentre",
        "es": "Voy al centro",
        "en": "I'm going downtown"
    },

    # -----------------------------------------------------
    # EXPRESSIONS
    # -----------------------------------------------------

    {
        "cat": "🔥 Expresiones",
        "dz": "Hada houwa!",
        "roman": "Hada houwa!",
        "es": "¡Así es!",
        "en": "That's right!"
    },
    {
        "cat": "🔥 Expresiones",
        "dz": "Ma fhemt walo",
        "roman": "Ma fhemt walo",
        "es": "No entendí nada",
        "en": "I understood nothing"
    },
    {
        "cat": "🔥 Expresiones",
        "dz": "Walo",
        "roman": "Walo",
        "es": "Nada",
        "en": "Nothing"
    },
    {
        "cat": "🔥 Expresiones",
        "dz": "Haka",
        "roman": "Haka",
        "es": "Así",
        "en": "Like this"
    },
    {
        "cat": "🔥 Expresiones",
        "dz": "Bessif",
        "roman": "Bessif",
        "es": "A la fuerza",
        "en": "By force"
    },
    {
        "cat": "🔥 Expresiones",
        "dz": "Hada ma kayen",
        "roman": "Hada ma kayen",
        "es": "Esto no existe",
        "en": "This doesn't exist"
    },
    {
        "cat": "🔥 Expresiones",
        "dz": "Machi mouchkil",
        "roman": "Machi mouchkil",
        "es": "No hay problema",
        "en": "No problem"
    },
    {
        "cat": "🔥 Expresiones",
        "dz": "Ma 3labalich",
        "roman": "Ma 3labalich",
        "es": "No lo sé",
        "en": "I don't know"
    },
    {
        "cat": "🔥 Expresiones",
        "dz": "3labali",
        "roman": "3labali",
        "es": "Lo sé",
        "en": "I know"
    },
    {
        "cat": "🔥 Expresiones",
        "dz": "Smahli",
        "roman": "Smahli",
        "es": "Perdona",
        "en": "Sorry"
    },

    # -----------------------------------------------------
    # ARGOT
    # -----------------------------------------------------

    {
        "cat": "😎 Argot",
        "dz": "Sahbi",
        "roman": "Sahbi",
        "es": "Tío",
        "en": "Bro"
    },
    {
        "cat": "😎 Argot",
        "dz": "Kho",
        "roman": "Kho",
        "es": "Tío / Bro",
        "en": "Bro"
    },
    {
        "cat": "😎 Argot",
        "dz": "Mlih",
        "roman": "Mlih",
        "es": "Bien / Genial",
        "en": "Good / Great"
    },
    {
        "cat": "😎 Argot",
        "dz": "Yakhi",
        "roman": "Yakhi",
        "es": "¿En serio?",
        "en": "Seriously?"
    },
    {
        "cat": "😎 Argot",
        "dz": "Wesh",
        "roman": "Wesh",
        "es": "¿Qué?",
        "en": "What?"
    },
    {
        "cat": "😎 Argot",
        "dz": "Tchipa",
        "roman": "Tchipa",
        "es": "Soborno",
        "en": "Bribe"
    },
    {
        "cat": "😎 Argot",
        "dz": "Hawaji",
        "roman": "Hawaji",
        "es": "Cosas",
        "en": "Things"
    },
    {
        "cat": "😎 Argot",
        "dz": "Fikra",
        "roman": "Fikra",
        "es": "Idea",
        "en": "Idea"
    },
    {
        "cat": "😎 Argot",
        "dz": "Mrigel",
        "roman": "Mrigel",
        "es": "Todo bien",
        "en": "All good"
    },
    {
        "cat": "😎 Argot",
        "dz": "Fhamt?",
        "roman": "Fhamt?",
        "es": "¿Entiendes?",
        "en": "Do you understand?"
    },

    # -----------------------------------------------------
    # ÚTILES
    # -----------------------------------------------------

    {
        "cat": "🧠 Útiles",
        "dz": "3afak",
        "roman": "3afak",
        "es": "Por favor",
        "en": "Please"
    },
    {
        "cat": "🧠 Útiles",
        "dz": "Smahli",
        "roman": "Smahli",
        "es": "Perdón",
        "en": "Sorry / Excuse me"
    },
    {
        "cat": "🧠 Útiles",
        "dz": "Merci",
        "roman": "Merci",
        "es": "Gracias",
        "en": "Thank you"
    },
    {
        "cat": "🧠 Útiles",
        "dz": "Mabrouk",
        "roman": "Mabrouk",
        "es": "Enhorabuena",
        "en": "Congratulations"
    },
    {
        "cat": "🧠 Útiles",
        "dz": "Allah yjib lkhir",
        "roman": "Allah yjib lkhir",
        "es": "Que todo salga bien",
        "en": "May everything go well"
    },
    {
        "cat": "🧠 Útiles",
        "dz": "Rabbi ykhalik",
        "roman": "Rabbi ykhalik",
        "es": "Que Dios te bendiga",
        "en": "God bless you"
    },
    {
        "cat": "🧠 Útiles",
        "dz": "Matkhafch",
        "roman": "Matkhafch",
        "es": "No tengas miedo",
        "en": "Don't be afraid"
    },
    {
        "cat": "🧠 Útiles",
        "dz": "Ma tkhammemch",
        "roman": "Ma tkhammemch",
        "es": "No te preocupes",
        "en": "Don't worry"
    },
    {
        "cat": "🧠 Útiles",
        "dz": "T3ala",
        "roman": "T3ala",
        "es": "Ven",
        "en": "Come"
    },
    {
        "cat": "🧠 Útiles",
        "dz": "Roh",
        "roman": "Roh",
        "es": "Vete",
        "en": "Go"
    },
    {
        "cat": "🧠 Útiles",
        "dz": "Stanna",
        "roman": "Stanna",
        "es": "Espera",
        "en": "Wait"
    },
    {
        "cat": "🧠 Útiles",
        "dz": "Chouf",
        "roman": "Chouf",
        "es": "Mira",
        "en": "Look"
    },
    {
        "cat": "🧠 Útiles",
        "dz": "Esma3",
        "roman": "Esma3",
        "es": "Escucha",
        "en": "Listen"
    },
    {
        "cat": "🧠 Útiles",
        "dz": "Aji",
        "roman": "Aji",
        "es": "Ven aquí",
        "en": "Come here"
    },
    {
        "cat": "🧠 Útiles",
        "dz": "Khalli",
        "roman": "Khalli",
        "es": "Déjalo",
        "en": "Leave it"
    },
    {
        "cat": "🧠 Útiles",
        "dz": "Dour",
        "roman": "Dour",
        "es": "Date la vuelta",
        "en": "Turn around"
    },

    # -----------------------------------------------------
    # EXTRA EXPRESSIONS
    # -----------------------------------------------------

    {
        "cat": "🔥 Expresiones",
        "dz": "Rani jay",
        "roman": "Rani jay",
        "es": "Ya voy",
        "en": "I'm coming"
    },
    {
        "cat": "🔥 Expresiones",
        "dz": "Rani hna",
        "roman": "Rani hna",
        "es": "Estoy aquí",
        "en": "I'm here"
    },
    {
        "cat": "🔥 Expresiones",
        "dz": "Nchallah khir",
        "roman": "Nchallah khir",
        "es": "Ojalá salga bien",
        "en": "Hopefully it goes well"
    },
    {
        "cat": "🔥 Expresiones",
        "dz": "Ma t9ala9ch",
        "roman": "Ma t9ala9ch",
        "es": "No te preocupes",
        "en": "Don't worry"
    },
    {
        "cat": "🔥 Expresiones",
        "dz": "Rani m3ak",
        "roman": "Rani m3ak",
        "es": "Estoy contigo",
        "en": "I'm with you"
    },
    {
        "cat": "🔥 Expresiones",
        "dz": "Smahli kho",
        "roman": "Smahli kho",
        "es": "Perdona, tío",
        "en": "Sorry, bro"
    },
    {
        "cat": "🔥 Expresiones",
        "dz": "Khalliha 3la Rabbi",
        "roman": "Khalliha 3la Rabbi",
        "es": "Déjalo en manos de Dios",
        "en": "Leave it to God"
    },
    {
        "cat": "🔥 Expresiones",
        "dz": "Yakhi normal",
        "roman": "Yakhi normal",
        "es": "Es normal, ¿no?",
        "en": "It's normal, right?"
    },
    {
        "cat": "🔥 Expresiones",
        "dz": "Ma 3andekch l7a9",
        "roman": "Ma 3andekch l7a9",
        "es": "No tienes razón",
        "en": "You're wrong"
    },
    {
        "cat": "🔥 Expresiones",
        "dz": "3andek l7a9",
        "roman": "3andek l7a9",
        "es": "Tienes razón",
        "en": "You're right"
    },

]


# =========================================================
# SEARCH + CATEGORY
# =========================================================

st.markdown(
    '<div class="search-label">SEARCH EXPRESSIONS</div>',
    unsafe_allow_html=True
)

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


st.markdown(
    f'<div class="results-info">{len(filtered)} expressions found</div>',
    unsafe_allow_html=True
)


# =========================================================
# CATEGORY COLORS
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

if filtered:

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

        # Safely prepare text for JavaScript
        speech_text = (
            item["es"]
            .replace("\\", "\\\\")
            .replace("'", "\\'")
            .replace("\n", " ")
        )

        cards += f"""
        <div class="card">

            <div class="category"
                 style="
                    color:{color};
                    border-color:{color}55;
                    background:{color}12;
                 ">
                {cat}
            </div>

            <div class="darija">
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
                <span class="speaker">🔊</span>
                <span>{es}</span>
            </div>

            <div class="english">
                {en}
            </div>

        </div>
        """

    # =====================================================
    # COMPONENT HTML
    # =====================================================

    component_html = f"""
    <style>

        * {{
            box-sizing: border-box;
        }}

        body {{
            margin: 0;
            background: transparent;
            font-family: Inter, Arial, sans-serif;
            color: #f8fafc;
        }}

        .grid {{
            display: grid;
            grid-template-columns: repeat(2, minmax(0, 1fr));
            gap: 14px;
            padding: 3px 1px 15px;
        }}

        .card {{
            min-height: 225px;
            padding: 22px;
            border-radius: 20px;

            background:
                radial-gradient(
                    circle at 100% 0%,
                    rgba(255,255,255,0.035),
                    transparent 35%
                ),
                linear-gradient(
                    145deg,
                    #111720,
                    #0c1118
                );

            border: 1px solid rgba(255,255,255,0.065);

            box-shadow:
                0 10px 30px rgba(0,0,0,0.18);

            transition:
                transform 0.18s ease,
                border-color 0.18s ease,
                box-shadow 0.18s ease;
        }}

        .card:hover {{
            transform: translateY(-2px);
            border-color: rgba(255,255,255,0.13);
            box-shadow:
                0 15px 40px rgba(0,0,0,0.28);
        }}

        .category {{
            display: inline-block;
            padding: 6px 9px;
            border-radius: 999px;

            border: 1px solid;

            font-size: 9px;
            font-weight: 800;
            letter-spacing: 0.6px;

            margin-bottom: 18px;
        }}

        .darija {{
            color: #f8fafc;
            font-size: 23px;
            line-height: 1.2;
            font-weight: 800;
            letter-spacing: -0.5px;
        }}

        .roman {{
            margin-top: 7px;
            color: #64748b;
            font-size: 12px;
            font-style: italic;
        }}

        .spanish {{
            display: flex;
            align-items: center;
            gap: 9px;

            margin-top: 25px;

            color: #4ade80;
            font-size: 17px;
            line-height: 1.35;
            font-weight: 700;

            cursor: pointer;

            width: fit-content;

            transition:
                color 0.15s ease,
                transform 0.15s ease;
        }}

        .spanish:hover {{
            color: #86efac;
            transform: translateX(2px);
        }}

        .speaker {{
            font-size: 15px;
            opacity: 0.8;
        }}

        .english {{
            margin-top: 10px;

            color: #64748b;

            font-size: 11px;
            line-height: 1.4;
        }}

        @media (max-width: 700px) {{

            .grid {{
                grid-template-columns: 1fr;
                gap: 12px;
            }}

            .card {{
                min-height: 210px;
                padding: 20px;
            }}

            .darija {{
                font-size: 21px;
            }}

            .spanish {{
                font-size: 16px;
            }}

        }}

    </style>


    <div class="grid">
        {cards}
    </div>


    <script>

        let voices = [];

        function loadVoices() {{
            voices = window.speechSynthesis.getVoices();
        }}

        loadVoices();

        if (window.speechSynthesis) {{
            window.speechSynthesis.onvoiceschanged = loadVoices;
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
                        voice.lang
                            .toLowerCase()
                            .startsWith("es-es")
                );


            if (!spanishVoice) {{

                spanishVoice =
                    voices.find(
                        voice =>
                            voice.lang &&
                            voice.lang
                                .toLowerCase()
                                .startsWith("es")
                    );

            }}


            if (spanishVoice) {{
                utterance.voice = spanishVoice;
            }}


            window.speechSynthesis.speak(
                utterance
            );

        }}

    </script>
    """


    # Height adapts to number of cards
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
# NO RESULTS
# =========================================================

else:

    st.markdown("""
    <div style="
        text-align:center;
        padding:70px 20px;
        border:1px solid rgba(255,255,255,0.06);
        border-radius:20px;
        background:#0d1219;
    ">

        <div style="
            font-size:40px;
            margin-bottom:15px;
        ">
            🔎
        </div>

        <div style="
            font-size:18px;
            font-weight:700;
            color:#f8fafc;
        ">
            No expressions found
        </div>

        <div style="
            margin-top:8px;
            font-size:12px;
            color:#64748b;
        ">
            Try another word or choose a different category.
        </div>

    </div>
    """, unsafe_allow_html=True)


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
