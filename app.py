import streamlit as st

st.set_page_config(
    page_title="¿Amigos digitales o riesgos invisibles?",
    layout="wide",
    initial_sidebar_state="collapsed",
)

if "page" not in st.session_state:
    st.session_state.page = 0

if "selected_ref" not in st.session_state:
    st.session_state.selected_ref = None

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

        [data-testid="stHeader"],
        [data-testid="stToolbar"],
        [data-testid="stDecoration"] {
            display: none !important;
            height: 0 !important;
        }

        #MainMenu, footer {
            visibility: hidden;
        }

        .stApp > div:first-child,
        .main,
        section[data-testid="stMain"] {
            padding-top: 0 !important;
            margin-top: 0 !important;
        }

        .block-container {
            padding-top: 0 !important;
            padding-bottom: 0.35rem !important;
            margin-top: 0 !important;
            max-width: 1200px;
        }

        .progress-wrap {
            display: flex;
            justify-content: center;
            margin: 0 0 0.25rem 0;
            padding: 0;
        }

        .progress-pill {
            display: inline-flex;
            gap: 0.5rem;
            align-items: center;
            background: rgba(255,255,255,0.7);
            border: 1px solid rgba(0,0,0,0.07);
            border-radius: 999px;
            padding: 0.4rem 0.8rem;
            box-shadow: 0 4px 18px rgba(0,0,0,0.05);
            font-size: 0.88rem;
            color: #444;
        }

        .section-wrap {
            min-height: auto;
            display: block;
            margin: 0 !important;
            padding: 0 !important;
            animation: fadeSlide 0.35s ease;
        }

        .section-card {
            width: 100%;
            background: rgba(255,255,255,0.78);
            border: 1px solid rgba(0,0,0,0.08);
            border-radius: 28px;
            padding: 2rem 2.35rem 1.9rem 2.35rem;
            box-shadow: 0 10px 35px rgba(0,0,0,0.06);
            backdrop-filter: blur(10px);
            margin-top: 0 !important;
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

        .body-text, .lead {
            font-family: 'Libre Baskerville', serif;
            font-size: 1rem;
            line-height: 1.95;
            color: #222;
            max-width: 980px;
        }

        .lead {
            font-size: 1.08rem;
        }

        .bullet-box {
            margin-top: 1.1rem;
            padding: 1.05rem 1.2rem;
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
            margin-top: 0.6rem;
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

sections = [
    {
        "label": "Título del Artículo",
        "title": "¿Amigos digitales o riesgos invisibles? El desafío ético de los chatbots en salud mental",
        "quote": "La inteligencia artificial conversa, pero la inteligencia humana comprende las consecuencias.",
    },
    {
        "label": "Introducción",
        "title": "Introducción",
        "body": """
        La forma en que buscamos apoyo emocional está cambiando radicalmente. Hemos pasado de sistemas digitales rígidos a una era dominada por Modelos de Lenguaje Extensos (LLM), una tecnología que ha remodelado la interacción humana con las máquinas. Hoy, los chatbots ya no son solo herramientas que dan información; muchas personas los perciben como \"compañeros, amigos o socios\" de IA. Sin embargo, este lazo digital no está libre de peligros. Cuando estas herramientas se despliegan en situaciones de \"alta vulnerabilidad clínica\", aparecen riesgos críticos que no siempre son evidentes a simple vista. La gran pregunta que surge es si la fluidez con la que habla una IA es garantía suficiente para proteger la seguridad de un paciente en terapia.
        """,
    },
    {
        "label": "1",
        "title": "1. ¿Qué son los chatbots de salud mental y por qué se usan?",
        "body": """
        Los chatbots modernos funcionan bajo principios probabilísticos. Esto significa que, aunque pueden mantener una conversación fluida y parecer empáticos, carecen de una \"comprensión genuina de los hechos\" o de las consecuencias que sus consejos pueden tener en la salud de una persona. El problema es que, aunque parecen entender, carecen de una \"comprensión genuina de los hechos o de las consecuencias clínicas\" (Chow & Li, 2025). Los usuarios a menudo confunden esta simulación de empatía con la responsabilidad profesional y asumen erróneamente que sus datos están protegidos por las mismas regulaciones que un terapeuta licenciado (Kwesi et al., 2025).
        """,
    },
    {
        "label": "2",
        "title": "2. ¿Qué significa que una IA “alucine” y por qué importa aquí?",
        "body": """
        En el mundo de la inteligencia artificial, una \"alucinación\" ocurre cuando el sistema genera información que parece lógica y correcta, pero que en realidad es falsa o no tiene sentido. En un contexto de salud mental, esto es especialmente peligroso. Las alucinaciones no son errores al azar, sino una característica de la propia naturaleza de estos modelos generativos. Los usuarios ya han empezado a notar este fenómeno, reportando \"incorrecciones factuales\" y llegando a sentir que su IA les está mintiendo. El riesgo clínico es real: un chatbot puede inventar datos médicos o dar consejos contraproducentes mientras mantiene un tono de voz profesional y seguro.
        """,
    },
    {
        "label": "3",
        "title": "3. Sesgos: cómo aparecen y a quién pueden afectar más",
        "body": """
        Los chatbots no son neutrales; son el reflejo de los datos con los que fueron entrenados. Esto significa que suelen arrastrar \"desigualdades históricas y culturales\". La literatura científica advierte que estos modelos pueden repetir estigmas y prejuicios relacionados con el género, la raza o la comunidad LGBTQ+. Un riesgo importante es la imposición de una \"visión occidentalizada del bienestar\". Al fallar los mecanismos de alineación, la IA ofrece consejos que carecen de sensibilidad cultural, lo que afecta desproporcionadamente a poblaciones minoritarias y viola el principio de justicia distributiva en la salud (Silveira & Paravidini, 2024; Arnaiz-Rodríguez et al., 2025).
        """,
    },
    {
        "label": "4",
        "title": "4. Riesgos de desinformación y posibles daños",
        "body": """
        La desinformación en salud mental puede tener consecuencias físicas. Se han documentado casos donde los modelos distorsionan información sobre medicamentos o fabrican pautas de tratamiento inexistentes. En situaciones de crisis, el panorama es aún más alarmante:
        """,
        "bullets": [
            "Sugerencias letales: Algunos modelos han proporcionado estrategias para someter a individuos o han sugerido dosis letales de fármacos (Grabb et al., 2024).",
            "Sicofancia: La IA tiende a confirmar las creencias del usuario, incluso si estas son delirantes o peligrosas.",
            "Escalada de crisis: En pacientes con cuadros de manía o psicosis, este refuerzo de creencias puede invalidar el proceso terapéutico y escalar los riesgos (Blease & Rodman, 2025).",
        ],
    },
    {
        "label": "5",
        "title": "5. Dilemas éticos y marcos de seguridad",
        "body": """
        Uno de los mayores desafíos es la llamada \"vulnerabilidad intangible\". Los usuarios a menudo confunden la simulación de empatía del bot con una responsabilidad profesional real. Muchos asumen erróneamente que su privacidad está protegida por las mismas leyes que rigen a un terapeuta licenciado, como la normativa HIPAA, cuando no siempre es así. Para mitigar estos riesgos, los expertos proponen:
        """,
        "bullets": [
            "Niveles de Autonomía: La IA no debe actuar de forma autónoma en casos identificados como de alto riesgo clínico (Grabb et al., 2024).",
            "Filtros de Seguridad (Guardrails): Implementación de filtros para detectar ideación suicida y realizar un \"escalamiento inmediato a servicios humanos de emergencia\" (Arnaiz-Rodríguez et al., 2025).",
            "Transparencia Total: Es necesario obligar a declarar la naturaleza no humana del bot y limitar su alcance en asesorías de alta responsabilidad (Londoño Villarreal, 2025).",
        ],
    },
    {
        "label": "Ideas Clave",
        "title": "Ideas Clave",
        "cards": [
            "Los chatbots de IA conversan con fluidez pero no comprenden las consecuencias clínicas de lo que dicen.",
            "Las \"alucinaciones\" son información falsa que la IA presenta como verdadera, incluyendo dosis de fármacos peligrosas.",
            "Los modelos suelen heredar prejuicios culturales y raciales de sus datos de entrenamiento.",
            "La IA tiende a dar la razón al usuario (sicofancia), lo que puede ser peligroso en pacientes con delirios.",
            "El parecido con un terapeuta humano es una simulación; estos sistemas no reemplazan el estándar de cuidado profesional.",
        ],
    },
    {
        "label": "Cierre",
        "title": "Cierre",
        "body": """
        Aunque los modelos de lenguaje ofrecen una gran oportunidad para el acceso a la salud, su tendencia a la alucinación y el sesgo los hace insuficientes para igualar el estándar profesional humano (Grabb et al., 2024). En casos de crisis aguda, el daño potencial derivado de la desinformación supera actualmente los beneficios. El reto futuro reside en llenar el vacío de validación clínica rigurosa, garantizando que la IA sea una herramienta de apoyo y no un riesgo para quienes buscan ayuda.
        """,
    },
    {
        "label": "Referencias",
        "title": "Referencias Bibliográficas (Traducción al Español)",
        "body": "Haz clic en cada referencia para abrir su resumen exacto.",
    },
]

references = [
    {
        "full": "Arnaiz-Rodríguez, A., et al. (2025). Entre la ayuda y el daño: una evaluación del manejo de crisis de salud mental por LLM.",
        "summary": "Los chatbots potenciados por modelos de lenguaje extenso han transformado la forma en que las personas buscan información en contextos de alto riesgo como la salud mental. A pesar de sus capacidades, la detección y respuesta segura a crisis como la ideación suicida y las autolesiones siguen sin estar claras debido a la falta de taxonomías unificadas. Abordamos esto creando una taxonomía de seis categorías de crisis y evaluando cinco modelos. Aunque algunos responden de manera confiable a crisis explícitas, persisten los riesgos. Muchos resultados en las categorías de autolesiones e ideación suicida son inapropiados o inseguros. Los modelos gpt-5-nano y deepseek-v3.2-exp tienen tasas de daño bajas, pero otros como gpt-4o-mini y grok-4-fast generan respuestas más inseguras.",
    },
    {
        "full": "Blease, C. & Rodman, A. (2025). Inteligencia Artificial Generativa en la atención de salud mental: una evaluación ética.",
        "summary": "Esta revisión busca aclarar las implicaciones éticas actuales de los chatbots utilizando principios éticos biomédicos. Estudios recientes demuestran el potencial de la IA para aprobar exámenes médicos, evaluar diagnósticos complejos y brindar atención empática. Sin embargo, se ha prestado poca atención enfocada a las consecuencias éticas para la salud mental. Esta revisión evalúa la ética de las herramientas de IA generativa y motiva a realizar más investigaciones sobre sus beneficios y daños.",
    },
    {
        "full": "Chow, J. C. L. & Li, K. (2025). Modelos de lenguaje extensos en chatbots médicos: oportunidades, desafíos y la necesidad de abordar los riesgos de la IA.",
        "summary": "Los LLM están transformando los chatbots médicos al permitir interacciones más humanas. Se utilizan en roles para pacientes (verificación de síntomas, apoyo en salud mental) y para médicos (documentación, apoyo a decisiones). No obstante, su despliegue plantea preocupaciones críticas: alucinaciones, sesgos algorítmicos, riesgos de privacidad y falta de claridad regulatoria. Abogamos por la innovación responsable y la colaboración para garantizar que se desplieguen de forma segura, equitativa y transparente.",
    },
    {
        "full": "De Choudhury, M., Pendse, S. R. & Kumar, N. (2023). Beneficios y daños de los modelos de lenguaje extensos en la salud mental digital.",
        "summary": "Los LLM prometen llevar la salud mental digital a territorios inexplorados. Este artículo presenta perspectivas contemporáneas sobre las oportunidades y riesgos de los LLM en el diseño e implementación de herramientas de salud mental. Se discuten áreas como los comportamientos de búsqueda de ayuda y la provisión de cuidados comunitarios e institucionales. El objetivo es ayudar a dar forma a futuros esfuerzos de defensa y regulación para crear herramientas más responsables y seguras.",
    },
    {
        "full": "Grabb, D., Lamparth, M. & Vasan, N. (2024). Riesgos de los modelos de lenguaje para la atención de salud mental automatizada: ética y estructura para la implementación.",
        "summary": "Este artículo aborda los desafíos éticos de la IA autónoma en salud mental y propone un marco que delinea niveles de autonomía y requisitos éticos. Evaluamos diez modelos con preguntas sobre psicosis, manía, depresión y tendencias suicidas. Encontramos que los modelos actuales son insuficientes para igualar el estándar humano debido a respuestas demasiado cautelosas o sicofánticas y la ausencia de salvaguardas. Alarmantemente, la mayoría de los modelos podrían causar daño en emergencias de salud mental.",
    },
    {
        "full": "Hua, Y., et al. (2024). Trazando la evolución de los chatbots de salud mental con IA: desde sistemas basados en reglas hasta modelos de lenguaje extensos.",
        "summary": "Revisión sistemática de 160 estudios (2020-2024) que clasifica las arquitecturas de los chatbots. Mientras que los sistemas basados en reglas dominaron hasta 2023, los chatbots basados en LLM aumentaron al 45% en 2024. Sin embargo, solo el 16% de los estudios de LLM pasaron por pruebas de eficacia clínica. Existe una brecha crítica en la validación robusta de los beneficios terapéuticos. El artículo enfatiza la necesidad de evaluaciones estandarizadas para garantizar un despliegue seguro y ético.",
    },
    {
        "full": "Kwesi, J., et al. (2025). Explorando las actitudes y preocupaciones de seguridad y privacidad de los usuarios hacia el uso de chatbots LLM de propósito general para la salud mental.",
        "summary": "A través de 21 entrevistas, identificamos conceptos erróneos críticos y una falta general de conciencia del riesgo. Los participantes confundieron la empatía humana de los LLM con la responsabilidad humana y creyeron erróneamente que sus interacciones estaban protegidas por regulaciones como HIPAA. Introducimos el concepto de \"vulnerabilidad intangible\", donde las revelaciones emocionales se valoran menos que los datos financieros, y proponemos recomendaciones para proteger a los usuarios.",
    },
    {
        "full": "Londoño Villarreal, L. F. (2025). Guía de cumplimiento: regulación de IA generativa en asesoría jurídica por chatbot en Colombia.",
        "summary": "Analiza los aspectos regulatorios y éticos de la implementación de chatbots legales en Colombia. Resalta la necesidad de incluir evaluaciones de riesgo, principios de transparencia y estándares de protección de datos. Se proponen recomendaciones prácticas para garantizar que los chatbots promuevan el acceso igualitario a la justicia respetando los derechos fundamentales.",
    },
    {
        "full": "Massenon, R., et al. (2025). \"Mi IA me está mintiendo\": alucinaciones de LLM reportadas por usuarios en reseñas de aplicaciones móviles de IA.",
        "summary": "Estudio empírico de 3 millones de reseñas de usuarios de 90 aplicaciones móviles de IA. La prevalencia de informes de alucinaciones fue de aproximadamente el 1.75%. La \"Incorrección Factual\" fue el tipo más reportado (38%), seguida de \"Salida sin sentido/irrelevante\" (25%) e \"Información Fabricada\" (15%). Estos hallazgos destacan la necesidad de estrategias de monitoreo y mitigación para mejorar la confianza del usuario.",
    },
    {
        "full": "Silveira, P. V. R. & Paravidini, J. L. L. (2024). Ética de la aplicación de inteligencias artificiales y chatbots en la salud mental: una perspectiva psicoanalítica.",
        "summary": "Discute las implicaciones éticas del uso de IA o chatbots terapeutas desde la perspectiva del psicoanálisis. Destaca los riesgos de daños emocionales complejos, la falta de validez de la información y la ausencia de responsabilidad de los agentes involucrados. Presenta recomendaciones para el desarrollo de IA más éticas.",
    },
]

def go_prev():
    if st.session_state.page > 0:
        st.session_state.page -= 1


def go_next():
    if st.session_state.page < len(sections) - 1:
        st.session_state.page += 1


@st.dialog("Resumen de referencia", width="large")
def show_reference_dialog(idx: int):
    ref = references[idx]
    st.markdown(f"### {ref['full']}")
    st.markdown("---")
    st.write(f"Resumen: {ref['summary']}")
    if st.button("Cerrar", key=f"close_dialog_{idx}", use_container_width=True):
        st.session_state.selected_ref = None
        st.rerun()


current = sections[st.session_state.page]

st.markdown(
    f"""
    <div class="progress-wrap">
        <div class="progress-pill">Sección {st.session_state.page + 1} de {len(sections)} · {current['label']}</div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="section-wrap"><div class="section-card">', unsafe_allow_html=True)

if st.session_state.page == 0:
    st.markdown('<div class="eyebrow">ARTÍCULO DE DIVULGACIÓN CIENTÍFICA</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="hero-title">{current["title"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="quote">{current["quote"]}</div>', unsafe_allow_html=True)

elif current["label"] == "Ideas Clave":
    st.markdown(f'<div class="section-title">{current["title"]}</div>', unsafe_allow_html=True)
    cols = st.columns(len(current["cards"]))
    for col, item in zip(cols, current["cards"]):
        with col:
            st.markdown(f'<div class="key-card">{item}</div>', unsafe_allow_html=True)

elif current["label"] == "Referencias":
    st.markdown(f'<div class="section-title">{current["title"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="body-text">{current["body"]}</div>', unsafe_allow_html=True)
    st.markdown('<div class="ref-note">Cada botón abre el resumen exacto que indicaste.</div>', unsafe_allow_html=True)

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
                st.rerun()

else:
    st.markdown(f'<div class="section-title">{current["title"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="body-text">{current["body"]}</div>', unsafe_allow_html=True)
    if current.get("bullets"):
        bullet_html = "<ul>" + "".join([f"<li>{b}</li>" for b in current["bullets"]]) + "</ul>"
        st.markdown(f'<div class="bullet-box">{bullet_html}</div>', unsafe_allow_html=True)

st.markdown('</div></div>', unsafe_allow_html=True)

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

if st.session_state.selected_ref is not None:
    show_reference_dialog(st.session_state.selected_ref)

st.markdown(
    """
    <div class="footer-mini">
        Dashboard en Streamlit · diseño minimalista · navegación horizontal por secciones
    </div>
    """,
    unsafe_allow_html=True,
)
