import streamlit as st

st.set_page_config(
    page_title="¿Amigos digitales o riesgos invisibles?",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# -----------------------------
# ESTADO
# -----------------------------
if "page" not in st.session_state:
    st.session_state.page = 0

if "selected_ref" not in st.session_state:
    st.session_state.selected_ref = None

# -----------------------------
# ESTILOS
# -----------------------------
st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Libre+Baskerville:wght@400;700&display=swap');

        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
        }

        .stApp {
            background: linear-gradient(180deg, #f8f8f6 0%, #f3f2ee 100%);
            color: #111111;
        }

        [data-testid="stHeader"] {
            height: 0rem;
        }

        .block-container {
            padding-top: 0.4rem !important;
            padding-bottom: 0.8rem !important;
            max-width: 1200px;
        }

        .section-wrap {
            min-height: 78vh;
            display: flex;
            align-items: center;
            justify-content: center;
            animation: fadeSlide 0.45s ease;
        }

        .section-card {
            width: 100%;
            background: rgba(255,255,255,0.78);
            border: 1px solid rgba(0,0,0,0.08);
            border-radius: 28px;
            padding: 2.3rem 2.5rem 2rem 2.5rem;
            box-shadow: 0 10px 35px rgba(0,0,0,0.06);
            backdrop-filter: blur(10px);
        }

        .eyebrow {
            letter-spacing: 0.16em;
            text-transform: uppercase;
            font-size: 0.75rem;
            color: #666;
            margin-bottom: 0.8rem;
            font-weight: 600;
        }

        .hero-title, .section-title {
            font-family: 'Inter', sans-serif;
            font-weight: 700;
            line-height: 1.05;
            color: #111111;
            margin-bottom: 1rem;
        }

        .hero-title {
            font-size: clamp(2.2rem, 5vw, 4.8rem);
            max-width: 920px;
        }

        .section-title {
            font-size: clamp(1.6rem, 3vw, 2.7rem);
        }

        .quote {
            text-align: right;
            font-size: 1rem;
            color: #4b4b4b;
            margin-top: 1rem;
            margin-bottom: 1.5rem;
            font-style: italic;
        }

        .body-text {
            font-family: 'Libre Baskerville', serif;
            font-size: 1rem;
            line-height: 1.95;
            color: #222;
            max-width: 900px;
        }

        .lead {
            font-family: 'Libre Baskerville', serif;
            font-size: 1.08rem;
            line-height: 1.95;
            color: #222;
            max-width: 980px;
        }

        .bullet-box {
            margin-top: 1.2rem;
            padding: 1.1rem 1.2rem;
            border-radius: 18px;
            background: rgba(17,17,17,0.03);
            border: 1px solid rgba(17,17,17,0.07);
        }

        .bullet-box ul {
            margin: 0;
            padding-left: 1.2rem;
            line-height: 1.9;
            font-family: 'Libre Baskerville', serif;
        }

        .progress-wrap {
            display: flex;
            justify-content: center;
            margin-bottom: 0.4rem;
        }

        .progress-pill {
            display: inline-flex;
            gap: 0.5rem;
            align-items: center;
            background: rgba(255,255,255,0.7);
            border: 1px solid rgba(0,0,0,0.07);
            border-radius: 999px;
            padding: 0.45rem 0.85rem;
            box-shadow: 0 4px 18px rgba(0,0,0,0.05);
            font-size: 0.88rem;
            color: #444;
        }

        .key-card {
            border-radius: 20px;
            padding: 1rem 1.1rem;
            background: rgba(255,255,255,0.78);
            border: 1px solid rgba(0,0,0,0.07);
            height: 100%;
            box-shadow: 0 6px 20px rgba(0,0,0,0.04);
            font-family: 'Libre Baskerville', serif;
            line-height: 1.8;
        }

        .ref-note {
            font-size: 0.92rem;
            color: #666;
            margin-top: 0.5rem;
            margin-bottom: 1rem;
        }

        .footer-mini {
            text-align: center;
            color: #666;
            font-size: 0.9rem;
            margin-top: 0.8rem;
        }

        @keyframes fadeSlide {
            from {
                opacity: 0;
                transform: translateY(12px);
            }
            to {
                opacity: 1;
                transform: translateY(0px);
            }
        }

        div[data-testid="stButton"] > button {
            border-radius: 999px;
            border: 1px solid rgba(0,0,0,0.10);
            background: rgba(255,255,255,0.84);
            color: #111;
            padding: 0.6rem 1.2rem;
            font-weight: 600;
        }

        div[data-testid="stButton"] > button:hover {
            border-color: rgba(0,0,0,0.22);
            background: white;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# CONTENIDO
# -----------------------------
sections = [
    {
        "label": "Portada",
        "title": "¿Amigos digitales o riesgos invisibles? El desafío ético de los chatbots en salud mental",
        "quote": "La inteligencia artificial conversa, pero la inteligencia humana comprende las consecuencias",
        "body": """
        La forma en que buscamos apoyo emocional está cambiando radicalmente. Hemos pasado de sistemas digitales rígidos a una era dominada por Modelos de Lenguaje Extensos (LLM), una tecnología que ha remodelado la interacción humana con las máquinas. Hoy, los chatbots ya no son solo herramientas que dan información; muchas personas los perciben como compañeros, amigos o socios de IA.
        <br><br>
        Sin embargo, este lazo digital no está libre de peligros. Cuando estas herramientas se despliegan en situaciones de alta vulnerabilidad clínica, aparecen riesgos críticos que no siempre son evidentes a simple vista. La pregunta central es si la fluidez con la que habla una IA basta para proteger la seguridad de una persona que busca apoyo terapéutico.
        """,
    },
    {
        "label": "Introducción",
        "title": "Introducción",
        "body": """
        Este artículo de divulgación examina cómo las alucinaciones y los sesgos algorítmicos pueden comprometer la seguridad de los pacientes en contextos de salud mental. Aunque los chatbots ofrecen disponibilidad constante, accesibilidad y rapidez de respuesta, estos beneficios no eliminan sus límites clínicos, éticos y culturales.
        <br><br>
        La discusión no gira solo en torno a si la IA puede conversar bien, sino a si puede hacerlo de manera segura, justa y responsable cuando una persona atraviesa crisis, angustia o vulnerabilidad emocional.
        """,
    },
    {
        "label": "Punto 1",
        "title": "1. ¿Qué son los chatbots de salud mental y por qué se usan?",
        "body": """
        Los chatbots de salud mental son sistemas conversacionales diseñados para ofrecer acompañamiento, psicoeducación, orientación general o apoyo emocional. Los modelos más recientes funcionan bajo principios probabilísticos: generan texto calculando qué palabra es más probable que siga en una secuencia.
        <br><br>
        Por eso pueden sonar empáticos y coherentes, pero no poseen comprensión genuina de los hechos ni de las consecuencias clínicas de lo que recomiendan. El problema es que muchos usuarios interpretan esa fluidez como si fuera criterio profesional real. También pueden asumir erróneamente que sus datos están protegidos bajo el mismo nivel de confidencialidad que con un terapeuta licenciado.
        """,
    },
    {
        "label": "Punto 2",
        "title": "2. ¿Qué significa que una IA alucine y por qué importa aquí?",
        "body": """
        En inteligencia artificial, una alucinación ocurre cuando el sistema produce información que parece lógica, convincente y bien estructurada, pero que es falsa, inventada o clínicamente inadecuada.
        <br><br>
        En salud mental esto resulta especialmente delicado porque el tono seguro del chatbot puede hacer que una respuesta incorrecta parezca confiable. El riesgo no es solo técnico: una recomendación falsa sobre síntomas, medicamentos, crisis o tratamiento puede afectar decisiones reales de personas vulnerables.
        <br><br>
        Las alucinaciones no son un accidente aislado, sino una limitación estructural de los modelos generativos actuales.
        """,
    },
    {
        "label": "Punto 3",
        "title": "3. Sesgos: cómo aparecen y a quién pueden afectar más",
        "body": """
        Los chatbots no son neutrales. Aprenden de enormes volúmenes de datos y, con ello, pueden reproducir desigualdades históricas, prejuicios culturales y visiones parciales del bienestar.
        <br><br>
        Esto puede traducirse en respuestas que estigmaticen, invisibilicen o interpreten mal experiencias relacionadas con género, raza, orientación sexual, identidad LGBTQ+ o contexto sociocultural. Un problema especialmente importante es la tendencia a ofrecer una visión occidentalizada del bienestar, como si fuese universal.
        <br><br>
        Cuando la IA ignora la diversidad cultural y social, el daño no se distribuye de manera igual: suele recaer con mayor fuerza sobre poblaciones minoritarias o ya vulneradas.
        """,
    },
    {
        "label": "Punto 4",
        "title": "4. Riesgos de desinformación y posibles daños",
        "body": """
        La desinformación en salud mental no siempre se queda en un error menor. Puede tener consecuencias emocionales, clínicas e incluso físicas. Se han documentado respuestas donde los modelos distorsionan información sobre medicamentos, inventan pautas terapéuticas o emiten consejos inseguros en escenarios de crisis.
        """,
        "bullets": [
            "Sugerencias letales o peligrosas en escenarios extremos.",
            "Distorsión de información médica o farmacológica.",
            "Sicofancia: tendencia a darle la razón al usuario aunque sus creencias sean delirantes o dañinas.",
            "Escalada de crisis en personas con manía, psicosis o ideación suicida.",
            "Invalidación del proceso terapéutico al reforzar interpretaciones peligrosas en vez de redirigir a ayuda profesional.",
        ],
    },
    {
        "label": "Punto 5",
        "title": "5. Dilemas éticos y marcos de seguridad",
        "body": """
        Uno de los desafíos más importantes es la vulnerabilidad intangible: las personas pueden revelar información profundamente sensible sin percibir el riesgo real de hacerlo ante un sistema no humano.
        <br><br>
        Para reducir daños, la literatura propone que estos sistemas no operen con autonomía plena en casos de alto riesgo clínico. También se recomienda incorporar filtros de seguridad para detectar ideación suicida, autolesiones o señales indirectas de crisis, y activar el escalamiento inmediato hacia servicios humanos.
        <br><br>
        Además, se insiste en la transparencia: el chatbot debe declarar de forma clara que no es un profesional humano, explicar sus límites y evitar presentarse como sustituto del cuidado clínico.
        """,
        "bullets": [
            "Niveles de autonomía limitados en situaciones de alto riesgo.",
            "Guardrails para detectar crisis y derivar a soporte humano.",
            "Transparencia sobre su naturaleza no humana y sus límites.",
            "Mayor claridad en privacidad, regulación y responsabilidad.",
        ],
    },
    {
        "label": "Ideas clave",
        "title": "Ideas clave",
        "cards": [
            "Los chatbots conversan con fluidez, pero no comprenden las consecuencias clínicas de lo que dicen.",
            "Las alucinaciones son respuestas falsas presentadas con apariencia de verdad.",
            "Los modelos heredan prejuicios culturales, sociales y raciales de sus datos de entrenamiento.",
            "La sicofancia puede volver peligrosa la interacción al reforzar delirios o creencias dañinas.",
            "El parecido con un terapeuta humano es una simulación, no un reemplazo del estándar profesional.",
        ],
    },
    {
        "label": "Cierre",
        "title": "Cierre",
        "body": """
        Aunque los modelos de lenguaje ofrecen oportunidades importantes para ampliar el acceso a información y apoyo, su tendencia a la alucinación, el sesgo y la respuesta inapropiada impide que igualen el estándar de cuidado profesional humano.
        <br><br>
        En crisis agudas, el daño potencial derivado de la desinformación puede superar sus beneficios. El reto futuro no consiste solo en hacer que la IA suene más humana, sino en validarla rigurosamente, supervisarla clínicamente y diseñarla con prioridad absoluta en la seguridad del paciente.
        <br><br>
        La IA puede ser una herramienta de apoyo. Lo que no debe ser, al menos por ahora, es un sustituto del juicio humano en momentos de vulnerabilidad psicológica.
        """,
    },
    {
        "label": "Referencias",
        "title": "Referencias utilizadas",
        "body": """
        Haz clic en cada referencia para abrir un resumen en una ventana emergente.
        """,
    },
]

references = [
    {
        "short": "Arnaiz-Rodríguez et al. (2025)",
        "full": "Arnaiz-Rodríguez, A., et al. (2025). Between Help and Harm: An Evaluation of Mental Health Crisis Handling by LLMs. arXiv:2509.24857v2.",
        "summary": "Analiza cómo distintos modelos de lenguaje responden ante crisis de salud mental, incluyendo ideación suicida y autolesiones. El estudio muestra que, aunque algunos modelos detectan crisis explícitas, siguen existiendo respuestas inapropiadas, peligrosas o desalineadas con el contexto clínico. Concluye que se necesitan mejores salvaguardas, detección de crisis y protocolos clínicos para reducir daño.",
    },
    {
        "short": "Blease & Rodman (2025)",
        "full": "Blease, C. & Rodman, A. (2025). Generative Artificial Intelligence in Mental Healthcare: An Ethical Evaluation. Current Treatment Options in Psychiatry. https://doi.org/10.1007/s40501-024-00340-x.",
        "summary": "Revisión ética del uso de IA generativa en salud mental a partir de los principios de la bioética. Reconoce el potencial de estas herramientas para tareas clínicas, pero subraya dudas sobre responsabilidad, seguridad, explicabilidad y consecuencias éticas específicas en atención psicológica y psiquiátrica.",
    },
    {
        "short": "Chow & Li (2025)",
        "full": "Chow, J. C. L. & Li, K. (2025). Large Language Models in Medical Chatbots: Opportunities, Challenges, and the Need to Address AI Risks. Information, 16(7).",
        "summary": "Presenta un panorama general del uso de LLM en chatbots médicos, incluyendo apoyo en salud mental. Identifica beneficios como escalabilidad y personalización, pero destaca riesgos críticos: alucinaciones, sesgos, falta de claridad regulatoria, problemas de privacidad y responsabilidad clínica insuficiente.",
    },
    {
        "short": "De Choudhury et al. (2023)",
        "full": "De Choudhury, M., Pendse, S. R. & Kumar, N. (2023). Benefits and Harms of Large Language Models in Digital Mental Health. arXiv:2311.14693v1.",
        "summary": "Examina beneficios y daños potenciales de los LLM en salud mental digital desde una perspectiva ecológica. Discute su impacto en búsqueda de ayuda, provisión comunitaria, instituciones y sociedad. Señala que estas tecnologías pueden ampliar acceso, pero también introducir riesgos de equidad, seguridad y diseño irresponsable.",
    },
    {
        "short": "Grabb et al. (2024)",
        "full": "Grabb, D., Lamparth, M. & Vasan, N. (2024). Risks from Language Models for Automated Mental Healthcare: Ethics and Structure for Implementation. medRxiv. https://doi.org/10.1101/2024.04.07.24305462.",
        "summary": "Evalúa modelos de lenguaje con preguntas vinculadas a depresión, psicosis, manía, ideación suicida y homicida. Los hallazgos indican que la mayoría de los sistemas actuales no alcanzan el estándar humano de atención y pueden causar daño en emergencias, debido a respuestas sicofánticas, excesivamente cautelosas o sin guardrails adecuados.",
    },
    {
        "short": "Hua et al. (2024)",
        "full": "Hua, Y., et al. (2024). Charting the evolution of artificial intelligence mental health chatbots from rule-based systems to large language models: a systematic review. World Psychiatry, 23, 364-386.",
        "summary": "Revisión sistemática de 160 estudios sobre chatbots de salud mental. Muestra que los sistemas basados en LLM crecieron rápidamente, pero todavía cuentan con muy poca validación clínica robusta. Señala riesgos de respuestas incorrectas, problemas de privacidad y beneficios terapéuticos no comprobados en contextos de alto riesgo.",
    },
    {
        "short": "Kwesi et al. (2025)",
        "full": "Kwesi, J., et al. (2025). Exploring User Security and Privacy Attitudes and Concerns Toward the Use of General-Purpose LLM Chatbots for Mental Health. arXiv:2507.10695v1.",
        "summary": "Basado en entrevistas semiestructuradas, muestra que muchos usuarios confunden la empatía simulada del chatbot con responsabilidad humana y suponen erróneamente que existe protección legal equivalente a la de un terapeuta licenciado. Introduce la idea de vulnerabilidad intangible para explicar por qué se subestiman estos riesgos.",
    },
    {
        "short": "Londoño Villarreal (2025)",
        "full": "Londoño Villarreal, L. F. (2025). Guía de cumplimiento: regulación de IA generativa en asesoría jurídica por chatbot en Colombia. Revista Criminalidad, 67(2).",
        "summary": "Aunque se centra en chatbots jurídicos, el artículo es útil para pensar principios regulatorios transferibles: evaluación de riesgos, transparencia, protección de datos y límites de uso en contextos de alta responsabilidad. Su inclusión ayuda a reforzar el argumento sobre claridad normativa y deberes de información.",
    },
    {
        "short": "Massenon et al. (2025)",
        "full": "Massenon, R., et al. (2025). 'My AI is Lying to Me': User-reported LLM hallucinations in AI mobile apps reviews. Scientific Reports, 15:30397.",
        "summary": "Analiza millones de reseñas de aplicaciones móviles con IA para identificar reportes de alucinaciones. Encuentra que los usuarios sí perciben incorrecciones factuales, información fabricada y respuestas sin sentido, lo cual afecta la confianza y confirma que las alucinaciones también son visibles en entornos reales de uso cotidiano.",
    },
    {
        "short": "Silveira & Paravidini (2024)",
        "full": "Silveira, P. V. R. & Paravidini, J. L. L. (2024). Ética da aplicação de inteligências artificiais e chatbots na saúde mental: uma perspectiva psicanalítica. Revista Psicologia e Questões Contemporâneas (RPQ), 12(30).",
        "summary": "Discute implicaciones éticas del uso de IA y chatbots en salud mental desde una revisión narrativa y una perspectiva psicoanalítica. Destaca daño emocional complejo, falta de validez y confiabilidad, ausencia de responsabilidad clara y la necesidad de desarrollar sistemas más éticos y seguros.",
    },
]

# -----------------------------
# FUNCIONES DE NAVEGACIÓN
# -----------------------------
def go_prev():
    if st.session_state.page > 0:
        st.session_state.page -= 1


def go_next():
    if st.session_state.page < len(sections) - 1:
        st.session_state.page += 1


@st.dialog("Resumen de referencia", width="large")
def show_reference_dialog(idx: int):
    ref = references[idx]
    st.markdown(f"### {ref['short']}")
    st.write(ref["full"])
    st.markdown("---")
    st.write(ref["summary"])
    if st.button("Cerrar", key=f"close_dialog_{idx}", use_container_width=True):
        st.session_state.selected_ref = None
        st.rerun()


current = sections[st.session_state.page]

# -----------------------------
# PROGRESO
# -----------------------------
st.markdown(
    f"""
    <div class="progress-wrap">
        <div class="progress-pill">Sección {st.session_state.page + 1} de {len(sections)} · {current['label']}</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# CONTENIDO PRINCIPAL
# -----------------------------
st.markdown('<div class="section-wrap"><div class="section-card">', unsafe_allow_html=True)

if st.session_state.page == 0:
    st.markdown('<div class="eyebrow">Artículo de divulgación científica</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="hero-title">{current["title"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="quote">{current["quote"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="lead">{current["body"]}</div>', unsafe_allow_html=True)

elif current["label"] == "Ideas clave":
    st.markdown(f'<div class="section-title">{current["title"]}</div>', unsafe_allow_html=True)
    cols = st.columns(len(current["cards"]))
    for col, item in zip(cols, current["cards"]):
        with col:
            st.markdown(f'<div class="key-card">{item}</div>', unsafe_allow_html=True)

elif current["label"] == "Referencias":
    st.markdown(f'<div class="section-title">{current["title"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="body-text">{current["body"]}</div>', unsafe_allow_html=True)
    st.markdown('<div class="ref-note">Cada botón abre un resumen legible y luego puedes cerrarlo.</div>', unsafe_allow_html=True)

    for i, ref in enumerate(references):
        c1, c2 = st.columns([5, 1])
        with c1:
            st.markdown(
                f'<div class="body-text" style="font-size:0.95rem; line-height:1.7;">{ref["full"]}</div>',
                unsafe_allow_html=True,
            )
        with c2:
            if st.button("Ver resumen", key=f"ref_{i}", use_container_width=True):
                st.session_state.selected_ref = i

else:
    st.markdown(f'<div class="section-title">{current["title"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="body-text">{current["body"]}</div>', unsafe_allow_html=True)
    if current.get("bullets"):
        bullet_html = "<ul>" + "".join([f"<li>{b}</li>" for b in current["bullets"]]) + "</ul>"
        st.markdown(f'<div class="bullet-box">{bullet_html}</div>', unsafe_allow_html=True)

st.markdown('</div></div>', unsafe_allow_html=True)

# -----------------------------
# BOTONES DE NAVEGACIÓN
# -----------------------------
left, center, right = st.columns([1, 2, 1])
with left:
    st.button("← Anterior", on_click=go_prev, use_container_width=True, disabled=st.session_state.page == 0)
with center:
    st.markdown(
        '<div class="footer-mini">Navegación por pasos · vista tipo presentación · una sección por pantalla</div>',
        unsafe_allow_html=True,
    )
with right:
    st.button(
        "Siguiente →",
        on_click=go_next,
        use_container_width=True,
        disabled=st.session_state.page == len(sections) - 1,
    )

# -----------------------------
# DIÁLOGO DE REFERENCIAS
# -----------------------------
if st.session_state.selected_ref is not None:
    show_reference_dialog(st.session_state.selected_ref)

# -----------------------------
# PIE DE APP
# -----------------------------
st.markdown(
    """
    <div class="footer-mini">
        Dashboard en Streamlit · diseño minimalista · navegación horizontal por secciones
    </div>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# INSTRUCCIONES RÁPIDAS DE USO
# -----------------------------
with st.expander("Cómo ejecutarlo"):
    st.code(
        """pip install streamlit
streamlit run streamlit_chatbots_salud_mental_app.py""",
        language="bash",
    )
