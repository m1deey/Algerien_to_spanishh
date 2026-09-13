import streamlit as st
import html
import base64
import asyncio
import edge_tts
import streamlit.components.v1 as components

cards = []

for item in filtered:
    dz = html.escape(item["dz"])
    roman = html.escape(item["roman"])
    spanish = html.escape(item["es"])
    meaning = html.escape(item["meaning"])
    category = html.escape(item["category"])
    accent = CATEGORY_COLORS.get(item["category"], "#087653")

    # Get generated Edge-TTS audio
    b64_audio = AUDIO_MAP.get(item["es"], "")

    # Use a safe ID for every audio element
    audio_id = f"audio_{len(cards)}"

    if b64_audio:
        audio_html = f"""
        <audio id="{audio_id}">
            <source src="data:audio/mp3;base64,{b64_audio}" type="audio/mpeg">
        </audio>
        """
        play_action = f"""
            const audio = document.getElementById('{audio_id}');
            audio.currentTime = 0;
            audio.play().catch(() => {{
                speakSpanish('{item["es"].replace("'", "\\'")}');
            }});
        """
    else:
        # Browser fallback if Edge-TTS failed
        audio_html = ""
        safe_text = item["es"].replace("\\", "\\\\").replace("'", "\\'")
        play_action = f"speakSpanish('{safe_text}');"

    card = f"""
    <div class="word-card">

        <div class="word-category" style="color:{accent};">
            {category}
        </div>

        <div class="word-dz">
            {dz}
        </div>

        <div class="word-roman">
            {roman}
        </div>

        <div class="word-divider"></div>

        <!-- CLICKABLE SPANISH TRANSLATION -->
        <div
            class="spanish-row"
            style="
                background:{accent}12;
                border:1px solid {accent}25;
                color:{accent};
            "
            onclick="{play_action}"
            title="Escuchar pronunciación"
        >
            <span class="spanish-text">🇪🇸 {spanish}</span>
            <span class="speaker">🔊</span>
        </div>

        <div class="word-meaning">
            {meaning}
        </div>

        {audio_html}

    </div>
    """

    cards.append(card)


cards_html = "".join(cards)


# =========================================================
# PLAYABLE COMPONENT
# =========================================================

if filtered:

    rows = (len(filtered) + 1) // 2
    component_height = max(300, rows * 280 + 40)

    html_app = f"""
    <!DOCTYPE html>
    <html>
    <head>

    <meta name="viewport" content="width=device-width, initial-scale=1">

    <style>

        * {{
            box-sizing: border-box;
        }}

        body {{
            margin: 0;
            padding: 0;
            background: transparent;
            font-family: Inter, -apple-system, BlinkMacSystemFont,
                         "Segoe UI", sans-serif;
        }}

        .word-grid {{
            display: grid;
            grid-template-columns: repeat(2, minmax(0, 1fr));
            gap: 14px;
            width: 100%;
        }}

        .word-card {{
            background: #ffffff;
            border: 1px solid #e4ebe7;
            border-radius: 18px;
            padding: 18px;
            box-shadow: 0 5px 18px rgba(0,0,0,.035);
            transition: transform .15s ease,
                        box-shadow .15s ease;
        }}

        .word-card:hover {{
            transform: translateY(-3px);
            box-shadow: 0 12px 30px rgba(0,0,0,.09);
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

        /* NOT A BUTTON — just a clean clickable translation */

        .spanish-row {{
            width: 100%;
            min-height: 46px;
            border-radius: 13px;
            padding: 9px 13px;

            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 10px;

            cursor: pointer;
            user-select: none;

            transition:
                transform .12s ease,
                filter .15s ease,
                box-shadow .15s ease;
        }}

        .spanish-row:hover {{
            filter: brightness(.97);
            box-shadow: 0 4px 12px rgba(0,0,0,.05);
        }}

        .spanish-row:active {{
            transform: scale(.985);
        }}

        .spanish-text {{
            font-size: 18px;
            font-weight: 750;
            line-height: 1.3;
        }}

        .speaker {{
            font-size: 17px;
            opacity: .7;
            flex-shrink: 0;
        }}

        .word-meaning {{
            color: #707b76;
            font-size: 13px;
            margin-top: 9px;
        }}

        @media (max-width: 700px) {{

            .word-grid {{
                grid-template-columns: 1fr;
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

        // Browser speech fallback
        function speakSpanish(text) {{

            if (!("speechSynthesis" in window)) {{
                return;
            }}

            window.speechSynthesis.cancel();

            const utterance =
                new SpeechSynthesisUtterance(text);

            utterance.lang = "es-ES";
            utterance.rate = 0.92;
            utterance.pitch = 1;

            window.speechSynthesis.speak(utterance);
        }}

        </script>

    </body>
    </html>
    """

    components.html(
        html_app,
        height=component_height,
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
            <h3>No se encontraron expresiones</h3>
            <p>Prueba con otra palabra o categoría.</p>
        </div>
        """,
        unsafe_allow_html=True
      )
