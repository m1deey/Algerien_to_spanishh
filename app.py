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
# DATA — 70+ ALGERIAN EXPRESSIONS
# =========================================================

WORDS = [

    # =====================================================
    # 👋 GREETINGS
    # =====================================================

    {
        "category": "👋 Saludos",
        "dz": "السلام عليكم",
        "roman": "Salam 3likom",
        "es": "Hola, ¿qué tal?",
        "meaning": "Hello / formal greeting"
    },
    {
        "category": "👋 Saludos",
        "dz": "وعليكم السلام",
        "roman": "Wa 3likom salam",
        "es": "¡Hola, igualmente!",
        "meaning": "Reply to a greeting"
    },
    {
        "category": "👋 Saludos",
        "dz": "واش راك؟",
        "roman": "Wach rak?",
        "es": "¿Qué tal estás?",
        "meaning": "How are you? — to a man"
    },
    {
        "category": "👋 Saludos",
        "dz": "واش راكي؟",
        "roman": "Wach raki?",
        "es": "¿Cómo estás?",
        "meaning": "How are you? — to a woman"
    },
    {
        "category": "👋 Saludos",
        "dz": "لاباس؟",
        "roman": "Labas?",
        "es": "¿Todo bien?",
        "meaning": "Everything good?"
    },
    {
        "category": "👋 Saludos",
        "dz": "صباح الخير",
        "roman": "Sbah el-khir",
        "es": "Buenos días",
        "meaning": "Good morning"
    },
    {
        "category": "👋 Saludos",
        "dz": "مساء الخير",
        "roman": "Msa el-khir",
        "es": "Buenas tardes",
        "meaning": "Good afternoon / evening"
    },
    {
        "category": "👋 Saludos",
        "dz": "أهلا",
        "roman": "Ahlan",
        "es": "¡Hola!",
        "meaning": "Hi / hello"
    },
    {
        "category": "👋 Saludos",
        "dz": "بسلامة",
        "roman": "Bslama",
        "es": "Nos vemos",
        "meaning": "Goodbye / see you"
    },
    {
        "category": "👋 Saludos",
        "dz": "صحا",
        "roman": "Saha",
        "es": "¡Cuídate!",
        "meaning": "Take care"
    },

    # =====================================================
    # 🗣️ EVERYDAY
    # =====================================================

    {
        "category": "🗣️ Cotidiano",
        "dz": "مليح",
        "roman": "Mlih",
        "es": "Bien",
        "meaning": "Good / fine"
    },
    {
        "category": "🗣️ Cotidiano",
        "dz": "لاباس الحمد لله",
        "roman": "Labas, hamdullah",
        "es": "Bien, gracias a Dios",
        "meaning": "I'm fine, thank God"
    },
    {
        "category": "🗣️ Cotidiano",
        "dz": "كولشي مليح",
        "roman": "Kolchi mlih",
        "es": "Todo va bien",
        "meaning": "Everything is going well"
    },
    {
        "category": "🗣️ Cotidiano",
        "dz": "ماشي مشكل",
        "roman": "Machi mochkil",
        "es": "No pasa nada",
        "meaning": "No problem"
    },
    {
        "category": "🗣️ Cotidiano",
        "dz": "ماعلاباليش",
        "roman": "Ma 3labalich",
        "es": "No tengo ni idea",
        "meaning": "I have no idea"
    },
    {
        "category": "🗣️ Cotidiano",
        "dz": "ما فهمتش",
        "roman": "Ma fhemtch",
        "es": "No entiendo",
        "meaning": "I don't understand"
    },
    {
        "category": "🗣️ Cotidiano",
        "dz": "فهمت",
        "roman": "Fhemt",
        "es": "Ya entendí",
        "meaning": "I understood / got it"
    },
    {
        "category": "🗣️ Cotidiano",
        "dz": "واش ندير؟",
        "roman": "Wach ndir?",
        "es": "¿Qué hago?",
        "meaning": "What should I do?"
    },
    {
        "category": "🗣️ Cotidiano",
        "dz": "واش درت؟",
        "roman": "Wach dert?",
        "es": "¿Qué has hecho?",
        "meaning": "What did you do?"
    },
    {
        "category": "🗣️ Cotidiano",
        "dz": "واش كاين؟",
        "roman": "Wach kayen?",
        "es": "¿Qué pasa?",
        "meaning": "What's going on?"
    },
    {
        "category": "🗣️ Cotidiano",
        "dz": "كاين",
        "roman": "Kayen",
        "es": "Sí, hay",
        "meaning": "There is / there are"
    },
    {
        "category": "🗣️ Cotidiano",
        "dz": "ما كاينش",
        "roman": "Ma kayench",
        "es": "No hay",
        "meaning": "There isn't / there aren't"
    },
    {
        "category": "🗣️ Cotidiano",
        "dz": "درك",
        "roman": "Dork",
        "es": "Ahora mismo",
        "meaning": "Right now"
    },
    {
        "category": "🗣️ Cotidiano",
        "dz": "غدوة",
        "roman": "Ghodwa",
        "es": "Mañana",
        "meaning": "Tomorrow"
    },
    {
        "category": "🗣️ Cotidiano",
        "dz": "البارح",
        "roman": "El-bareh",
        "es": "Ayer",
        "meaning": "Yesterday"
    },
    {
        "category": "🗣️ Cotidiano",
        "dz": "مازال",
        "roman": "Mazal",
        "es": "Todavía",
        "meaning": "Still / yet"
    },
    {
        "category": "🗣️ Cotidiano",
        "dz": "بالاك",
        "roman": "Balak",
        "es": "Quizás",
        "meaning": "Maybe"
    },
    {
        "category": "🗣️ Cotidiano",
        "dz": "أكيد",
        "roman": "Akid",
        "es": "Claro",
        "meaning": "Of course / definitely"
    },

    # =====================================================
    # 👥 PEOPLE
    # =====================================================

    {
        "category": "👥 Gente",
        "dz": "صحبي",
        "roman": "Sahbi",
        "es": "Mi amigo",
        "meaning": "My male friend"
    },
    {
        "category": "👥 Gente",
        "dz": "صحبتي",
        "roman": "Sahbti",
        "es": "Mi amiga",
        "meaning": "My female friend"
    },
    {
        "category": "👥 Gente",
        "dz": "خويا",
        "roman": "Khoya",
        "es": "Mi hermano",
        "meaning": "My brother / bro"
    },
    {
        "category": "👥 Gente",
        "dz": "ختي",
        "roman": "Khti",
        "es": "Mi hermana",
        "meaning": "My sister"
    },
    {
        "category": "👥 Gente",
        "dz": "صاحبي العزيز",
        "roman": "Sahbi l-3ziz",
        "es": "Mi gran amigo",
        "meaning": "My dear friend"
    },
    {
        "category": "👥 Gente",
        "dz": "العائلة",
        "roman": "L3ayla",
        "es": "La familia",
        "meaning": "The family"
    },
    {
        "category": "👥 Gente",
        "dz": "الوالدين",
        "roman": "Lwalidin",
        "es": "Mis padres",
        "meaning": "My parents"
    },
    {
        "category": "👥 Gente",
        "dz": "يمّا",
        "roman": "Yemma",
        "es": "Mamá",
        "meaning": "Mom"
    },
    {
        "category": "👥 Gente",
        "dz": "بابا",
        "roman": "Baba",
        "es": "Papá",
        "meaning": "Dad"
    },
    {
        "category": "👥 Gente",
        "dz": "الناس",
        "roman": "En-nas",
        "es": "La gente",
        "meaning": "People"
    },

    # =====================================================
    # ❤️ LOVE
    # =====================================================

    {
        "category": "❤️ Amor",
        "dz": "نحبك",
        "roman": "N7abek",
        "es": "Te quiero",
        "meaning": "I love you"
    },
    {
        "category": "❤️ Amor",
        "dz": "نموت عليك",
        "roman": "Nmout 3lik",
        "es": "Estoy loco por ti",
        "meaning": "I'm crazy about you"
    },
    {
        "category": "❤️ Amor",
        "dz": "توحشتك",
        "roman": "Twa7achtek",
        "es": "Te extraño",
        "meaning": "I miss you"
    },
    {
        "category": "❤️ Amor",
        "dz": "حبيبي",
        "roman": "Habibi",
        "es": "Mi amor",
        "meaning": "My love — male"
    },
    {
        "category": "❤️ Amor",
        "dz": "حبيبتي",
        "roman": "Habibti",
        "es": "Mi amor",
        "meaning": "My love — female"
    },
    {
        "category": "❤️ Amor",
        "dz": "يا عمري",
        "roman": "Ya 3omri",
        "es": "Mi vida",
        "meaning": "My life / darling"
    },
    {
        "category": "❤️ Amor",
        "dz": "قلبي",
        "roman": "Galbi",
        "es": "Mi corazón",
        "meaning": "My heart"
    },
    {
        "category": "❤️ Amor",
        "dz": "نحتاجك",
        "roman": "N7tajek",
        "es": "Te necesito",
        "meaning": "I need you"
    },

    # =====================================================
    # 😂 REACTIONS
    # =====================================================

    {
        "category": "😂 Reacciones",
        "dz": "يا لطيف!",
        "roman": "Ya latif!",
        "es": "¡Dios mío!",
        "meaning": "Oh my God!"
    },
    {
        "category": "😂 Reacciones",
        "dz": "واااااا",
        "roman": "Waaaa",
        "es": "¡Madre mía!",
        "meaning": "Wow / oh my God"
    },
    {
        "category": "😂 Reacciones",
        "dz": "بزاف",
        "roman": "Bezaf",
        "es": "Muchísimo",
        "meaning": "A lot / very much"
    },
    {
        "category": "😂 Reacciones",
        "dz": "شوية",
        "roman": "Chwiya",
        "es": "Un poquito",
        "meaning": "A little"
    },
    {
        "category": "😂 Reacciones",
        "dz": "والو",
        "roman": "Walou",
        "es": "Nada de nada",
        "meaning": "Absolutely nothing"
    },
    {
        "category": "😂 Reacciones",
        "dz": "صح؟",
        "roman": "Sah?",
        "es": "¿En serio?",
        "meaning": "Really?"
    },
    {
        "category": "😂 Reacciones",
        "dz": "واش بيك؟",
        "roman": "Wach bik?",
        "es": "¿Qué te pasa?",
        "meaning": "What's wrong with you?"
    },
    {
        "category": "😂 Reacciones",
        "dz": "ربي يستر",
        "roman": "Rabbi yestor",
        "es": "Que Dios nos proteja",
        "meaning": "May God protect us"
    },
    {
        "category": "😂 Reacciones",
        "dz": "إن شاء الله",
        "roman": "Inchallah",
        "es": "Si Dios quiere",
        "meaning": "God willing"
    },
    {
        "category": "😂 Reacciones",
        "dz": "واش هذا؟",
        "roman": "Wach hada?",
        "es": "¿Qué es esto?",
        "meaning": "What is this?"
    },

    # =====================================================
    # 🍽️ FOOD
    # =====================================================

    {
        "category": "🍽️ Comida",
        "dz": "بصحتك",
        "roman": "Bsa7tek",
        "es": "Que aproveche",
        "meaning": "Enjoy your meal"
    },
    {
        "category": "🍽️ Comida",
        "dz": "شهية طيبة",
        "roman": "Chahia tayba",
        "es": "Buen provecho",
        "meaning": "Enjoy your meal"
    },
    {
        "category": "🍽️ Comida",
        "dz": "بنينة",
        "roman": "Bnina",
        "es": "Está buenísimo",
        "meaning": "It's delicious"
    },
    {
        "category": "🍽️ Comida",
        "dz": "جعت",
        "roman": "J3et",
        "es": "Tengo hambre",
        "meaning": "I'm hungry"
    },
    {
        "category": "🍽️ Comida",
        "dz": "عطشت",
        "roman": "3techt",
        "es": "Tengo sed",
        "meaning": "I'm thirsty"
    },
    {
        "category": "🍽️ Comida",
        "dz": "الما",
        "roman": "El-ma",
        "es": "Agua",
        "meaning": "Water"
    },
    {
        "category": "🍽️ Comida",
        "dz": "ناكلو",
        "roman": "Naklou",
        "es": "Vamos a comer",
        "meaning": "Let's eat"
    },
    {
        "category": "🍽️ Comida",
        "dz": "راني شبعان",
        "roman": "Rani chba3an",
        "es": "Estoy lleno",
        "meaning": "I'm full"
    },

    # =====================================================
    # 💰 MONEY
    # =====================================================

    {
        "category": "💰 Dinero",
        "dz": "بقداش هذا؟",
        "roman": "Bqaddach hada?",
        "es": "¿Cuánto cuesta esto?",
        "meaning": "How much does this cost?"
    },
    {
        "category": "💰 Dinero",
        "dz": "غالي",
        "roman": "Ghali",
        "es": "Es caro",
        "meaning": "It's expensive"
    },
    {
        "category": "💰 Dinero",
        "dz": "رخيص",
        "roman": "Rkhis",
        "es": "Es barato",
        "meaning": "It's cheap"
    },
    {
        "category": "💰 Dinero",
        "dz": "دراهم",
        "roman": "Drahem",
        "es": "Dinero",
        "meaning": "Money"
    },
    {
        "category": "💰 Dinero",
        "dz": "ما عنديش دراهم",
        "roman": "Ma 3andich drahem",
        "es": "No tengo dinero",
        "meaning": "I don't have money"
    },
    {
        "category": "💰 Dinero",
        "dz": "عندي",
        "roman": "3andi",
        "es": "Tengo",
        "meaning": "I have"
    },
    {
        "category": "💰 Dinero",
        "dz": "ما عنديش",
        "roman": "Ma 3andich",
        "es": "No tengo",
        "meaning": "I don't have"
    },

    # =====================================================
    # 🚗 PLACES & MOVEMENT
    # =====================================================

    {
        "category": "🚗 Lugares",
        "dz": "وين؟",
        "roman": "Win?",
        "es": "¿Dónde?",
        "meaning": "Where?"
    },
    {
        "category": "🚗 Lugares",
        "dz": "وين راك؟",
        "roman": "Win rak?",
        "es": "¿Dónde andas?",
        "meaning": "Where are you?"
    },
    {
        "category": "🚗 Lugares",
        "dz": "وين راكي؟",
        "roman": "Win raki?",
        "es": "¿Dónde estás?",
        "meaning": "Where are you? — female"
    },
    {
        "category": "🚗 Lugares",
        "dz": "روح",
        "roman": "Rouh",
        "es": "Vete",
        "meaning": "Go / leave"
    },
    {
        "category": "🚗 Lugares",
        "dz": "أرواح",
        "roman": "Arwah",
        "es": "Ven aquí",
        "meaning": "Come here"
    },
    {
        "category": "🚗 Lugares",
        "dz": "استنى",
        "roman": "Stenna",
        "es": "Espera",
        "meaning": "Wait"
    },
    {
        "category": "🚗 Lugares",
        "dz": "هنا",
        "roman": "Hna",
        "es": "Aquí",
        "meaning": "Here"
    },
    {
        "category": "🚗 Lugares",
        "dz": "لهيه",
        "roman": "Lihih",
        "es": "Por allí",
        "meaning": "Over there"
    },
    {
        "category": "🚗 Lugares",
        "dz": "بعيد",
        "roman": "B3id",
        "es": "Lejos",
        "meaning": "Far"
    },
    {
        "category": "🚗 Lugares",
        "dz": "قريب",
        "roman": "Gريب / Grib",
        "es": "Cerca",
        "meaning": "Near"
    },

    # =====================================================
    # 🔥 FAMOUS ALGERIAN EXPRESSIONS
    # =====================================================

    {
        "category": "🔥 Expresiones",
        "dz": "كاش جديد؟",
        "roman": "Kach jdid?",
        "es": "¿Alguna novedad?",
        "meaning": "What's new?"
    },
    {
        "category": "🔥 Expresiones",
        "dz": "ماكانش",
        "roman": "Makanche",
        "es": "No hay",
        "meaning": "There isn't any"
    },
    {
        "category": "🔥 Expresiones",
        "dz": "غير هاني",
        "roman": "Ghir hani",
        "es": "Aquí ando, tirando",
        "meaning": "I'm good / getting by"
    },
    {
        "category": "🔥 Expresiones",
        "dz": "ربي يسهل",
        "roman": "Rabbi ysahel",
        "es": "Que Dios lo facilite",
        "meaning": "May God make it easy"
    },
    {
        "category": "🔥 Expresiones",
        "dz": "الله يبارك",
        "roman": "Allah ybarek",
        "es": "Dios te bendiga",
        "meaning": "God bless"
    },
    {
        "category": "🔥 Expresiones",
        "dz": "يعطيك الصحة",
        "roman": "Y3atik essa7a",
        "es": "Muchas gracias",
        "meaning": "Thank you / may God give you health"
    },
    {
        "category": "🔥 Expresiones",
        "dz": "صحا فطورك",
        "roman": "Saha ftorek",
        "es": "Que aproveche",
        "meaning": "Enjoy your meal"
    },
    {
        "category": "🔥 Expresiones",
        "dz": "على حساب",
        "roman": "3la hsab",
        "es": "Depende",
        "meaning": "It depends"
    },
    {
        "category": "🔥 Expresiones",
        "dz": "كفاش؟",
        "roman": "Kifach?",
        "es": "¿Cómo?",
        "meaning": "How?"
    },
    {
        "category": "🔥 Expresiones",
        "dz": "علاش؟",
        "roman": "3lach?",
        "es": "¿Por qué?",
        "meaning": "Why?"
    },
    {
        "category": "🔥 Expresiones",
        "dz": "واش من؟",
        "roman": "Wach men?",
        "es": "¿Cuál?",
        "meaning": "Which one?"
    },
    {
        "category": "🔥 Expresiones",
        "dz": "صحيت",
        "roman": "Sahit",
        "es": "Gracias",
        "meaning": "Thanks"
    },
    {
        "category": "🔥 Expresiones",
        "dz": "بلا مزية",
        "roman": "Bla mziya",
        "es": "De nada",
        "meaning": "You're welcome"
    },
    {
        "category": "🔥 Expresiones",
        "dz": "ماشي هكا",
        "roman": "Machi haka",
        "es": "No es así",
        "meaning": "It's not like that"
    },
    {
        "category": "🔥 Expresiones",
        "dz": "عندك الحق",
        "roman": "3andek l7a9",
        "es": "Tienes razón",
        "meaning": "You're right"
    },
    {
        "category": "🔥 Expresiones",
        "dz": "ما عندكش الحق",
        "roman": "Ma 3andekch l7a9",
        "es": "No tienes razón",
        "meaning": "You're not right"
    },
    {
        "category": "🔥 Expresiones",
        "dz": "خليني",
        "roman": "Khallini",
        "es": "Déjame",
        "meaning": "Leave me / let me"
    },
    {
        "category": "🔥 Expresiones",
        "dz": "دير عقلك",
        "roman": "Dir 3a9lek",
        "es": "Ten cuidado",
        "meaning": "Be careful"
    },
    {
        "category": "🔥 Expresiones",
        "dz": "ما تزيدش",
        "roman": "Ma tzidch",
        "es": "No sigas",
        "meaning": "Don't continue"
    },
    {
        "category": "🔥 Expresiones",
        "dz": "خلاص",
        "roman": "Khlas",
        "es": "Ya está",
        "meaning": "That's it / enough"
    },

    # =====================================================
    # 😎 SLANG / SOCIAL
    # =====================================================

    {
        "category": "😎 Argot",
        "dz": "واه",
        "roman": "Wah",
        "es": "Sí",
        "meaning": "Yes"
    },
    {
        "category": "😎 Argot",
        "dz": "لا",
        "roman": "La",
        "es": "No",
        "meaning": "No"
    },
    {
        "category": "😎 Argot",
        "dz": "يا خو",
        "roman": "Ya kho",
        "es": "Tío",
        "meaning": "Bro / dude"
    },
    {
        "category": "😎 Argot",
        "dz": "صحا خو",
        "roman": "Saha kho",
        "es": "Gracias, tío",
        "meaning": "Thanks bro"
    },
    {
        "category": "😎 Argot",
        "dz": "حشومة",
        "roman": "Hchouma",
        "es": "Qué vergüenza",
        "meaning": "That's shameful / embarrassing"
    },
    {
        "category": "😎 Argot",
        "dz": "مخلوع",
        "roman": "Makhlo3",
        "es": "Asustado",
        "meaning": "Scared"
    },
    {
        "category": "😎 Argot",
        "dz": "مجنون",
        "roman": "Mejnoun",
        "es": "Loco",
        "meaning": "Crazy"
    },
    {
        "category": "😎 Argot",
        "dz": "هايل",
        "roman": "Hayel",
        "es": "Genial",
        "meaning": "Awesome / great"
    },
    {
        "category": "😎 Argot",
        "dz": "فور",
        "roman": "Four",
        "es": "Muy bueno",
        "meaning": "Very good / impressive"
    },
    {
        "category": "😎 Argot",
        "dz": "روعة",
        "roman": "Raw3a",
        "es": "Increíble",
        "meaning": "Amazing"
    },

    # =====================================================
    # 🧠 USEFUL PHRASES
    # =====================================================

    {
        "category": "🧠 Útiles",
        "dz": "ما نعرفش",
        "roman": "Ma n3rafch",
        "es": "No lo sé",
        "meaning": "I don't know"
    },
    {
        "category": "🧠 Útiles",
        "dz": "نعرف",
        "roman": "N3raf",
        "es": "Lo sé",
        "meaning": "I know"
    },
    {
        "category": "🧠 Útiles",
        "dz": "نسيت",
        "roman": "Nsit",
        "es": "Me olvidé",
        "meaning": "I forgot"
    },
    {
        "category": "🧠 Útiles",
        "dz": "تسنى شوية",
        "roman": "Tsanna chwiya",
        "es": "Espera un poco",
        "meaning": "Wait a little"
    },
    {
        "category": "🧠 Útiles",
        "dz": "عاود",
        "roman": "3awed",
        "es": "Repite",
        "meaning": "Repeat"
    },
    {
        "category": "🧠 Útiles",
        "dz": "هدر بشوية",
        "roman": "Hder bchwiya",
        "es": "Habla despacio",
        "meaning": "Speak slowly"
    },
    {
        "category": "🧠 Útiles",
        "dz": "ما سمعتكش",
        "roman": "Ma sme3tekch",
        "es": "No te he oído",
        "meaning": "I didn't hear you"
    },
    {
        "category": "🧠 Útiles",
        "dz": "فهمتني؟",
        "roman": "Fhemtni?",
        "es": "¿Me entiendes?",
        "meaning": "Do you understand me?"
    },
]


# =========================================================
# CATEGORY COLORS
# =========================================================

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
    "😎 Argot": "#9333ea",
    "🧠 Útiles": "#475569",
}


# =========================================================
# CSS
# =========================================================

st.markdown(
    """
<style>

@import url(
'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap'
);

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(
            circle at 10% 10%,
            rgba(16,185,129,.07),
            transparent 30%
        ),
        radial-gradient(
            circle at 90% 20%,
            rgba(239,68,68,.06),
            transparent 30%
        ),
        #f8faf9;
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
    max-width: 1150px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}


/* HERO */

.hero {
    position: relative;
    overflow: hidden;

    padding: 42px 35px;

    border-radius: 28px;

    background:
        linear-gradient(
            135deg,
            #063f2e 0%,
            #087653 55%,
            #0c9369 100%
        );

    color: white;

    margin-bottom: 25px;

    box-shadow:
        0 18px 50px rgba(5,90,65,.18);
}

.hero::after {
    content: "🇩🇿";

    position: absolute;

    right: 35px;
    top: 8px;

    font-size: 110px;

    opacity: .10;
}

.made-by {
    position: absolute;

    top: 18px;
    right: 22px;

    font-size: 11px;

    font-weight: 700;

    letter-spacing: 1px;

    color: rgba(255,255,255,.75);

    background:
        rgba(255,255,255,.10);

    border:
        1px solid rgba(255,255,255,.18);

    padding: 5px 10px;

    border-radius: 999px;
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

    background:
        rgba(255,255,255,.13);

    border:
        1px solid rgba(255,255,255,.20);

    padding: 7px 12px;

    border-radius: 999px;

    font-size: 12px;

    margin-bottom: 15px;
}


/* STREAMLIT INPUTS */

div[data-testid="stTextInput"] input {
    border-radius: 14px;

    border: 1px solid #dfe7e3;

    padding: 13px 16px;

    font-size: 15px;
}

div[data-baseweb="select"] > div {
    border-radius: 14px;

    border: 1px solid #dfe7e3;
}


/* FOOTER */

.app-footer {
    text-align: center;

    color: #8a9691;

    font-size: 12px;

    margin-top: 30px;
}


/* MOBILE */

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

    .made-by {
        font-size: 9px;

        padding: 4px 8px;

        top: 14px;

        right: 14px;
    }

}

</style>
""",
    unsafe_allow_html=True
)


# =========================================================
# HERO
# =========================================================

st.markdown(
    """
<div class="hero">

    <div class="made-by">
        MADE BY YASSER
    </div>

    <div class="badge">
        🇩🇿 Algerian Darija → 🇪🇸 Spanish
    </div>

    <h1>
        Dzayer → Español
    </h1>

    <p>
        Algerian words and expressions translated into
        natural, everyday Spanish — not boring
        word-for-word translations.
        <br><br>
        <strong>
            Tap any 🇪🇸 translation to hear it.
        </strong>
    </p>

</div>
""",
    unsafe_allow_html=True
)


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

    categories = [
        "Todas"
    ] + sorted(
        set(item["category"] for item in WORDS)
    )

    selected_category = st.selectbox(
        "Category",
        categories,
        label_visibility="collapsed"
    )


# =========================================================
# FILTER
# =========================================================

filtered = WORDS.copy()

if selected_category != "Todas":

    filtered = [
        item
        for item in filtered
        if item["category"] == selected_category
    ]


if search:

    query = search.lower().strip()

    filtered = [
        item
        for item in filtered
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
        Mostrando
        <strong>{len(filtered)}</strong>
        expresiones
    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# CREATE CARDS
# =========================================================

if filtered:

    cards = []

    for item in filtered:

        dz = html.escape(item["dz"])
        roman = html.escape(item["roman"])
        spanish = html.escape(item["es"])
        meaning = html.escape(item["meaning"])
        category = html.escape(item["category"])

        accent = CATEGORY_COLORS.get(
            item["category"],
            "#087653"
        )

        # JSON-style JavaScript string
        # using repr keeps apostrophes safe
        speech_text = item["es"].replace(
            "\\",
            "\\\\"
        ).replace(
            "'",
            "\\'"
        )

        card = f"""
        <div class="word-card">

            <div
                class="word-category"
                style="color:{accent};"
            >
                {category}
            </div>

            <div class="word-dz">
                {dz}
            </div>

            <div class="word-roman">
                {roman}
            </div>

            <div class="word-divider"></div>

            <div
                class="spanish-row"
                style="
                    background:{accent}12;
                    border:1px solid {accent}25;
                    color:{accent};
                "
                onclick="speakSpanish('{speech_text}')"
                title="Escuchar pronunciación"
            >

                <span class="spanish-text">
                    🇪🇸 {spanish}
                </span>

                <span class="speaker">
                    🔊
                </span>

            </div>

            <div class="word-meaning">
                {meaning}
            </div>

        </div>
        """

        cards.append(card)

    cards_html = "".join(cards)

    # =====================================================
    # COMPONENT HTML
    # =====================================================

    component_html = f"""
<!DOCTYPE html>

<html>

<head>

<meta
    name="viewport"
    content="width=device-width, initial-scale=1"
>

<style>

* {{
    box-sizing: border-box;
}}

html,
body {{
    margin: 0;
    padding: 0;
    background: transparent;
}}

body {{
    font-family:
        Inter,
        -apple-system,
        BlinkMacSystemFont,
        "Segoe UI",
        sans-serif;
}}

.word-grid {{

    display: grid;

    grid-template-columns:
        repeat(2, minmax(0, 1fr));

    gap: 14px;

    width: 100%;
}}

.word-card {{

    background: #ffffff;

    border:
        1px solid #e4ebe7;

    border-radius: 18px;

    padding: 18px;

    box-shadow:
        0 5px 18px rgba(0,0,0,.035);

    transition:
        transform .15s ease,
        box-shadow .15s ease;
}}

.word-card:hover {{

    transform:
        translateY(-3px);

    box-shadow:
        0 12px 30px rgba(0,0,0,.09);
}}

.word-category {{

    font-size: 11px;

    font-weight: 800;

    text-transform: uppercase;

    letter-spacing: .5px;

    margin-bottom: 12px;
}}

.word-dz {{

    color: #202825;

    font-size: 23px;

    font-weight: 700;

    direction: rtl;

    text-align: right;

    line-height: 1.4;
}}

.word-roman {{

    color: #84918c;

    font-size: 13px;

    margin-top: 4px;

    font-style: italic;
}}

.word-divider {{

    height: 1px;

    background: #edf1ef;

    margin: 14px 0;
}}


/* ================================================
   CLEAN CLICKABLE SPANISH TRANSLATION
   ================================================ */

.spanish-row {{

    width: 100%;

    min-height: 46px;

    border-radius: 13px;

    padding:
        9px 13px;

    display: flex;

    align-items: center;

    justify-content: space-between;

    gap: 10px;

    cursor: pointer;

    user-select: none;

    -webkit-tap-highlight-color:
        transparent;

    transition:
        transform .12s ease,
        filter .15s ease,
        box-shadow .15s ease;
}}

.spanish-row:hover {{

    filter:
        brightness(.96);

    box-shadow:
        0 4px 12px rgba(0,0,0,.06);
}}

.spanish-row:active {{

    transform:
        scale(.985);
}}

.spanish-text {{

    font-size: 18px;

    font-weight: 750;

    line-height: 1.3;
}}

.speaker {{

    font-size: 17px;

    opacity: .70;

    flex-shrink: 0;
}}

.word-meaning {{

    color: #707b76;

    font-size: 13px;

    margin-top: 9px;

    line-height: 1.4;
}}


/* ================================================
   MOBILE
   ================================================ */

@media (max-width: 700px) {{

    .word-grid {{

        grid-template-columns:
            1fr;

        gap: 11px;
    }}

    .word-card {{

        padding: 16px;

        border-radius: 16px;
    }}

    .word-dz {{

        font-size: 21px;
    }}

    .spanish-text {{

        font-size: 17px;
    }}

}}

</style>

</head>


<body>

<div class="word-grid">

{cards_html}

</div>


<script>

/*
=====================================================
SPANISH PRONUNCIATION
=====================================================
Uses the device/browser's native speech synthesis.

Important:
The audio starts ONLY after the user taps the
Spanish translation, so mobile browser autoplay
restrictions do not block it.
=====================================================
*/

function speakSpanish(text) {{

    if (!window.speechSynthesis) {{

        alert(
            "Your browser does not support Spanish speech."
        );

        return;
    }}

    // Stop anything currently speaking
    window.speechSynthesis.cancel();


    const utterance =
        new SpeechSynthesisUtterance(text);


    // Spanish from Spain
    utterance.lang = "es-ES";


    // Natural learning speed
    utterance.rate = 0.90;


    // Normal pitch
    utterance.pitch = 1.0;


    // Slight volume boost
    utterance.volume = 1.0;


    /*
    -------------------------------------------------
    Try to select a Spanish voice.
    -------------------------------------------------
    */

    const voices =
        window.speechSynthesis.getVoices();


    let spanishVoice =
        voices.find(
            voice =>
                voice.lang === "es-ES"
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

        utterance.voice =
            spanishVoice;
    }}


    /*
    -------------------------------------------------
    Speak
    -------------------------------------------------
    */

    window.speechSynthesis.speak(
        utterance
    );

}}


/*
Some mobile browsers load their voices
asynchronously.
*/

window.speechSynthesis.onvoiceschanged =
    function() {{

        window.speechSynthesis.getVoices();

    }};

</script>

</body>

</html>
"""


    # =====================================================
    # COMPONENT HEIGHT
    # =====================================================

    if len(filtered) == 1:
        rows = 1
    else:
        rows = (
            len(filtered) + 1
        ) // 2

    component_height = max(
        300,
        rows * 245 + 40
    )


    # =====================================================
    # RENDER
    # =====================================================

    components.html(
        component_html,
        height=component_height,
        scrolling=False
    )


# =========================================================
# EMPTY SEARCH
# =========================================================

else:

    st.markdown(
        """
        <div style="
            text-align:center;
            padding:55px 20px;
            color:#7b8782;
        ">

            <div style="
                font-size:45px;
            ">
                🔎
            </div>

            <h3>
                No se encontraron expresiones
            </h3>

            <p>
                Prueba con otra palabra o categoría.
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div class="app-footer">
        🇩🇿 Hecho para quienes aprenden español desde Argelia 🇪🇸
        <br>
        <span style="opacity:.65;">
            100+ expresiones · Darija → Español
        </span>
    </div>
    """,
    unsafe_allow_html=True
)
