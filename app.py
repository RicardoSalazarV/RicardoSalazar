import streamlit as st

# ---------------------------
# Configuración General
# ---------------------------
st.set_page_config(page_title="Ricardo Salazar", layout="wide")

st.markdown("""
<style>
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        border-radius: 10px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        border-radius: 8px;
        font-weight: 600;
        padding: 0px 16px;
        background-color: #f0f2f6;
        margin-right: 4px;
        transition: all 0.3s ease;
    }
    .stTabs [data-baseweb="tab"]:hover {
        background-color: #e0e4ea;
        transform: translateY(-2px);
    }
    .stTabs [data-baseweb="tab-list"] button[aria-selected="true"] {
        background-color: #0F2D5E;
        color: white;
    }
    .big-emoji {
        font-size: 1.5rem;
        margin-right: 5px;
    }
    h1 {
        background: linear-gradient(45deg, #0F2D5E, #1a4a8a);
        padding: 10px 15px;
        border-radius: 10px;
        color: white;
        text-align: center;
    }
    .subtitle {
        text-align: center;
        color: #0F2D5E;
    }
    .project-card {
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #D6E4F0;
        margin-bottom: 15px;
        background-color: #f7f9fc;
        border-left: 4px solid #0F2D5E;
    }
    .project-card h3 { margin-top: 0; color: #0D1B2A; }
    .tag {
        display: inline-block;
        background-color: #D6E4F0;
        color: #0F2D5E;
        padding: 2px 8px;
        border-radius: 4px;
        font-size: 0.75rem;
        font-weight: 600;
        margin: 2px 2px 6px 0;
    }
    .section-divider {
        border: none;
        border-top: 2px solid #D6E4F0;
        margin: 20px 0;
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------
# Datos centralizados
# ---------------------------
CV_LINK_ES = "https://drive.google.com/file/d/1p7loWU7B-kQ8u7aIvbA0ecpzc4CS504m/view?usp=drivesdk"
CV_LINK_EN = "https://drive.google.com/file/d/1STIPeBneqonb6bnIj4sx8TooqO3BQxMz/view?usp=drivesdk"

PROJECTS_ES = [
    {
        "icon": "🌾", "title": "Constanza – Plataforma Agroindustrial",
        "tags": ["Node.js", "FastAPI", "MongoDB", "Docker", "GitLab CI/CD", "Socket.IO", "XGBoost", "Firebase"],
        "desc": "Sistema de gestión empresarial agroindustrial con 8+ microservicios en Docker. Incluye módulo de predicción de cosechas con IA, chat NLP, RRHH, nóminas, control de invernaderos y dashboard de KPIs.",
        "url": None
    },
    {
        "icon": "🧠", "title": "proyecto_cerebro – Motor IA / RAG Backend",
        "tags": ["Python", "FastAPI", "scikit-learn", "XGBoost", "NLP", "Docker", "GitLab"],
        "desc": "Microservicio de IA que actúa como núcleo cognitivo de Constanza. Pipelines de ML para clasificación y predicción, NLP para el módulo de chat, endpoints REST consumidos por todos los servicios.",
        "url": None
    },
    {
        "icon": "⚙️", "title": "FRIDAY PROJECT – Automatización con n8n",
        "tags": ["n8n", "Docker", "REST APIs", "WebHooks", "Notion", "Node.js", "WASAPI"],
        "desc": "Instancias n8n self-hosted en Docker para automatización de flujos administrativos. Integración entre servicios internos, sistemas externos y bases de datos. Workflows para alertas, sincronización y orquestación sin intervención manual.",
        "url": None
    },
    {
        "icon": "🔬", "title": "Análisis de Pureza en Metales",
        "tags": ["Python", "Pandas", "scikit-learn", "Streamlit"],
        "desc": "Modelo de clasificación para evaluar pureza de oro, plata y cobre a partir de datos físicos y químicos. Diagnóstico automatizado con precisión >90%.",
        "url": "https://gold-recovery.onrender.com"
    },
    {
        "icon": "🎭", "title": "IMDB Sentiment Analysis",
        "tags": ["Python", "NLTK", "scikit-learn", "Streamlit"],
        "desc": "Clasificador de sentimientos para reseñas de películas usando NLP y aprendizaje supervisado.",
        "url": "https://imdb-sentiment-app.onrender.com"
    },
    {
        "icon": "🚗", "title": "Predicción de Precios de Vehículos",
        "tags": ["Python", "scikit-learn", "Streamlit", "Matplotlib"],
        "desc": "Modelo predictivo para estimar precios de autos según marca, año, kilometraje y cilindrada.",
        "url": "https://vehicle-hz75.onrender.com"
    },
    {
        "icon": "🚕", "title": "Taxi Insights",
        "tags": ["Python", "GeoPandas", "Streamlit", "Plotly"],
        "desc": "Dashboard interactivo con mapas de calor para analizar demanda de taxis por zona y horario.",
        "url": "https://taxi-insights.onrender.com"
    },
    {
        "icon": "📡", "title": "Segmentación de Clientes – Megaline",
        "tags": ["Python", "scikit-learn", "Seaborn", "Streamlit"],
        "desc": "Clusterización de clientes para telco. Identificación de perfiles para campañas personalizadas y reducción de churn.",
        "url": "https://megaline.onrender.com"
    },
    {
        "icon": "💸", "title": "Rusty Bargain – Optimización de Precios",
        "tags": ["Python", "SciPy", "Streamlit", "Pandas"],
        "desc": "Sistema de ajuste automático de precios de productos usados según demanda, antigüedad y categoría.",
        "url": "https://rustybargain.onrender.com"
    },
    {
        "icon": "🎮", "title": "Games XTFR",
        "tags": ["Python", "Plotly", "Streamlit", "Pandas"],
        "desc": "Dashboard de tendencias de consumo gamer segmentado por género, plataforma y edad.",
        "url": "https://games-xtfr.onrender.com"
    },
    {
        "icon": "🔮", "title": "Sure Tomorrow",
        "tags": ["Python", "XGBoost", "Streamlit", "Pandas"],
        "desc": "Clasificador para prever eventos futuros con base en variables históricas y datos multivariados.",
        "url": "https://sure-tomorrow.onrender.com"
    },
]

PROJECTS_EN = [
    {
        "icon": "🌾", "title": "Constanza – Agroindustrial Management Platform",
        "tags": ["Node.js", "FastAPI", "MongoDB", "Docker", "GitLab CI/CD", "Socket.IO", "XGBoost", "Firebase"],
        "desc": "Production-grade agroindustrial ERP with 8+ Docker microservices. Includes AI crop prediction, NLP chat, HR & payroll, hierarchical greenhouse control, real-time push notifications, and KPI dashboard.",
        "url": None
    },
    {
        "icon": "🧠", "title": "proyecto_cerebro – AI / RAG Backend Engine",
        "tags": ["Python", "FastAPI", "scikit-learn", "XGBoost", "NLP", "Docker", "GitLab"],
        "desc": "AI microservice acting as the cognitive core of Constanza. ML pipelines for classification & prediction, NLP for the chat module, REST endpoints consumed by all other services.",
        "url": None
    },
    {
        "icon": "⚙️", "title": "FRIDAY PROJECT – Workflow Automation with n8n",
        "tags": ["n8n", "Docker", "REST APIs", "WebHooks", "Notion", "Node.js", "WASAPI"],
        "desc": "Self-hosted n8n instances in Docker for administrative workflow automation. Integration pipelines across internal services, external systems, and databases. Workflows for alerts, data sync, and scheduled orchestration.",
        "url": None
    },
    {
        "icon": "🔬", "title": "Metal Purity Analysis",
        "tags": ["Python", "Pandas", "scikit-learn", "Streamlit"],
        "desc": "Classification model to assess gold, silver, and copper purity from physical and chemical data. Automated diagnosis with >90% accuracy.",
        "url": "https://gold-recovery.onrender.com"
    },
    {
        "icon": "🎭", "title": "IMDB Sentiment Analysis",
        "tags": ["Python", "NLTK", "scikit-learn", "Streamlit"],
        "desc": "Sentiment classifier for movie reviews using NLP and supervised learning.",
        "url": "https://imdb-sentiment-app.onrender.com"
    },
    {
        "icon": "🚗", "title": "Vehicle Price Prediction",
        "tags": ["Python", "scikit-learn", "Streamlit", "Matplotlib"],
        "desc": "Predictive model to estimate car prices based on brand, year, mileage, and engine displacement.",
        "url": "https://vehicle-hz75.onrender.com"
    },
    {
        "icon": "🚕", "title": "Taxi Insights",
        "tags": ["Python", "GeoPandas", "Streamlit", "Plotly"],
        "desc": "Interactive dashboard with heat maps to analyze taxi demand by zone and time of day.",
        "url": "https://taxi-insights.onrender.com"
    },
    {
        "icon": "📡", "title": "Customer Segmentation – Megaline",
        "tags": ["Python", "scikit-learn", "Seaborn", "Streamlit"],
        "desc": "Telecom customer clustering for personalized campaigns and churn reduction.",
        "url": "https://megaline.onrender.com"
    },
    {
        "icon": "💸", "title": "Rusty Bargain – Price Optimization",
        "tags": ["Python", "SciPy", "Streamlit", "Pandas"],
        "desc": "Automatic price adjustment system for used products based on demand, age, and category.",
        "url": "https://rustybargain.onrender.com"
    },
    {
        "icon": "🎮", "title": "Games XTFR",
        "tags": ["Python", "Plotly", "Streamlit", "Pandas"],
        "desc": "Gaming consumption trends dashboard segmented by genre, platform, and age.",
        "url": "https://games-xtfr.onrender.com"
    },
    {
        "icon": "🔮", "title": "Sure Tomorrow",
        "tags": ["Python", "XGBoost", "Streamlit", "Pandas"],
        "desc": "Event forecasting classifier using historical and multivariate data.",
        "url": "https://sure-tomorrow.onrender.com"
    },
]

# ---------------------------
# Selector de Idioma
# ---------------------------
language = st.sidebar.selectbox("🌐 Language / Idioma", ["Español", "English"])

# ---------------------------
# Helpers
# ---------------------------
def render_tags(tags):
    return " ".join([f'<span class="tag">{t}</span>' for t in tags])

def render_projects(projects, label_live, label_private):
    col1, col2 = st.columns(2)
    for i, p in enumerate(projects):
        col = col1 if i % 2 == 0 else col2
        with col:
            link_html = (
                f'<a href="{p["url"]}" target="_blank">🌐 {label_live}</a>'
                if p["url"]
                else f'<span style="color:#888;">🔒 {label_private}</span>'
            )
            st.markdown(f"""
            <div class="project-card">
                <h3>{p["icon"]} {p["title"]}</h3>
                <div>{render_tags(p["tags"])}</div>
                <p style="margin-top:8px; color:#3A4A5C;">{p["desc"]}</p>
                <p>{link_html}</p>
            </div>
            """, unsafe_allow_html=True)

# ---------------------------
# ESPAÑOL
# ---------------------------
def render_es():
    tabs = st.tabs(["🙋‍♂️ Sobre mí", "🧠 Tech Stack", "📊 Proyectos", "📄 CV & Contacto 📬"])

    with tabs[0]:
        st.markdown("<h1>👨‍💻 Ricardo Salazar Vázquez</h1>", unsafe_allow_html=True)
        st.markdown("<h3 class='subtitle'>Ingeniero de Software · Data Scientist · DevOps</h3>", unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("<div style='text-align:center'><span class='big-emoji'>🔗</span> <a href='https://linkedin.com/in/ricardo-salazar'>LinkedIn</a></div>", unsafe_allow_html=True)
        with col2:
            st.markdown("<div style='text-align:center'><span class='big-emoji'>💻</span> <a href='https://github.com/RicardoSalazarV'>GitHub</a></div>", unsafe_allow_html=True)
        with col3:
            st.markdown("<div style='text-align:center'><span class='big-emoji'>📧</span> ricardo.sv99@gmail.com</div>", unsafe_allow_html=True)

        st.markdown("<hr class='section-divider'>", unsafe_allow_html=True)
        st.markdown("<h2><span class='big-emoji'>🙋‍♂️</span> Sobre Mí</h2>", unsafe_allow_html=True)
        st.markdown("""
Desarrollador Full Stack con especialización en **Ciencia de Datos, Machine Learning y arquitecturas de microservicios**.
Autor de **Constanza**, plataforma agroindustrial de nivel productivo con 8+ microservicios en Docker/GitLab,
módulos de IA para predicción de cosechas y sistema de chat NLP. Experiencia en diseño de sistemas backend
robustos con Node.js/FastAPI, pipelines de ML, automatización de flujos con **n8n** y despliegue continuo en entornos Linux.

Trabajo full-time, estudio los fines de semana y construyo por las noches.

> 🧠 *"Data is the new oil, and I'm here to refine it."*

🎵 *Fun fact:* Amante de la música frustrado, nunca afinado... siempre codificando.
""")

    with tabs[1]:
        st.markdown("<h2><span class='big-emoji'>🧠</span> Tech Stack</h2>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### 🔬 Backend & APIs")
            st.markdown("""
- **Python / FastAPI** (Avanzado)
- **Node.js / Express.js** (Intermedio)
- **Java · C# / .NET** (Intermedio)
- REST APIs · Arquitectura de Microservicios
""")
            st.markdown("#### 📊 Data Science & ML")
            st.markdown("""
- scikit-learn · XGBoost · Pandas · NumPy
- NLP · Procesamiento de Lenguaje Natural
- Replicate API · LLM integration · ElevenLabs
- Tableau · Matplotlib · Seaborn · Plotly · Streamlit
""")
            st.markdown("#### 🌐 Frontend")
            st.markdown("""
- JavaScript · HTML5 / CSS3 · EJS / SSR
- React (básico)
""")
        with col2:
            st.markdown("#### ⚙️ DevOps & Infraestructura")
            st.markdown("""
- **Docker / Docker Compose**
- **GitLab CI/CD · Git / GitHub**
- Linux (Ubuntu / RHEL) · SSH / IPMI / BMC
- WireGuard / UniFi (VPN & networking)
- n8n (automatización self-hosted)
""")
            st.markdown("#### 🗄️ Bases de Datos")
            st.markdown("""
- MongoDB / Mongoose · Firebase Firestore
- SQL · PostgreSQL · SQLite
- Microsoft Access
""")
            st.markdown("#### 🔒 Seguridad")
            st.markdown("""
- JWT · bcrypt · RBAC · HTTPS / TLS
""")

    with tabs[2]:
        st.markdown("<h2><span class='big-emoji'>📊</span> Proyectos</h2>", unsafe_allow_html=True)
        st.caption("🔒 Proyectos sin enlace son privados / en entorno corporativo.")
        render_projects(PROJECTS_ES, "Ver Proyecto", "Repositorio privado")

    with tabs[3]:
        st.markdown("<h2><span class='big-emoji'>📄</span> CV & <span class='big-emoji'>📬</span> Contacto</h2>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
### 📱 Contacto
- 📧 **Correo:** ricardo.sv99@gmail.com
- 📱 **Teléfono:** +52 246 377 5523
- 🔗 **LinkedIn:** [linkedin.com/in/ricardo-salazar](https://linkedin.com/in/ricardo-salazar)
- 💻 **GitHub:** [github.com/RicardoSalazarV](https://github.com/RicardoSalazarV)
""")
        with col2:
            st.markdown("### 📄 Currículum")
            st.markdown("Descarga mi CV actualizado con todos mis proyectos, stack y experiencia.")
            st.markdown(f"""
<div style="text-align:center; margin:20px 0;">
    <a href="{CV_LINK_ES}" target="_blank"
       style="background-color:#0F2D5E; color:white; padding:10px 20px;
              border-radius:6px; text-decoration:none; font-weight:bold; margin-right:10px;">
        📥 Descargar CV (ES)
    </a>
    <a href="{CV_LINK_EN}" target="_blank"
       style="background-color:#3A4A5C; color:white; padding:10px 20px;
              border-radius:6px; text-decoration:none; font-weight:bold;">
        📥 Download CV (EN)
    </a>
</div>
""", unsafe_allow_html=True)

# ---------------------------
# ENGLISH
# ---------------------------
def render_en():
    tabs = st.tabs(["🙋‍♂️ About Me", "🧠 Tech Stack", "📊 Projects", "📄 Resume & Contact 📬"])

    with tabs[0]:
        st.markdown("<h1>👨‍💻 Ricardo Salazar Vázquez</h1>", unsafe_allow_html=True)
        st.markdown("<h3 class='subtitle'>Software Engineer · Data Scientist · DevOps</h3>", unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("<div style='text-align:center'><span class='big-emoji'>🔗</span> <a href='https://linkedin.com/in/ricardo-salazar'>LinkedIn</a></div>", unsafe_allow_html=True)
        with col2:
            st.markdown("<div style='text-align:center'><span class='big-emoji'>💻</span> <a href='https://github.com/RicardoSalazarV'>GitHub</a></div>", unsafe_allow_html=True)
        with col3:
            st.markdown("<div style='text-align:center'><span class='big-emoji'>📧</span> ricardo.sv99@gmail.com</div>", unsafe_allow_html=True)

        st.markdown("<hr class='section-divider'>", unsafe_allow_html=True)
        st.markdown("<h2><span class='big-emoji'>🙋‍♂️</span> About Me</h2>", unsafe_allow_html=True)
        st.markdown("""
Full Stack Developer specializing in **Data Science, Machine Learning, and microservices architectures**.
Author of **Constanza**, a production-grade agroindustrial platform with 8+ Docker/GitLab microservices,
AI modules for crop yield prediction, and an NLP chat system. Experienced in robust backend design with
Node.js/FastAPI, ML pipelines, workflow automation with **n8n**, and continuous deployment on Linux.

Full-time work, weekend university, coding at night.

> 🧠 *"Data is the new oil, and I'm here to refine it."*

🎵 *Fun fact:* A frustrated music lover, never in tune… always coding.
""")

    with tabs[1]:
        st.markdown("<h2><span class='big-emoji'>🧠</span> Tech Stack</h2>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### 🔬 Backend & APIs")
            st.markdown("""
- **Python / FastAPI** (Advanced)
- **Node.js / Express.js** (Intermediate)
- **Java · C# / .NET** (Intermediate)
- REST APIs · Microservices Architecture
""")
            st.markdown("#### 📊 Data Science & ML")
            st.markdown("""
- scikit-learn · XGBoost · Pandas · NumPy
- NLP · Natural Language Processing
- Replicate API · LLM integration · ElevenLabs
- Tableau · Matplotlib · Seaborn · Plotly · Streamlit
""")
            st.markdown("#### 🌐 Frontend")
            st.markdown("""
- JavaScript · HTML5 / CSS3 · EJS / SSR
- React (basic)
""")
        with col2:
            st.markdown("#### ⚙️ DevOps & Infrastructure")
            st.markdown("""
- **Docker / Docker Compose**
- **GitLab CI/CD · Git / GitHub**
- Linux (Ubuntu / RHEL) · SSH / IPMI / BMC
- WireGuard / UniFi (VPN & networking)
- n8n (self-hosted automation)
""")
            st.markdown("#### 🗄️ Databases")
            st.markdown("""
- MongoDB / Mongoose · Firebase Firestore
- SQL · PostgreSQL · SQLite
- Microsoft Access
""")
            st.markdown("#### 🔒 Security")
            st.markdown("""
- JWT · bcrypt · RBAC · HTTPS / TLS
""")

    with tabs[2]:
        st.markdown("<h2><span class='big-emoji'>📊</span> Projects</h2>", unsafe_allow_html=True)
        st.caption("🔒 Projects without a link are private or deployed in a corporate environment.")
        render_projects(PROJECTS_EN, "View Project", "Private repository")

    with tabs[3]:
        st.markdown("<h2><span class='big-emoji'>📄</span> Resume & <span class='big-emoji'>📬</span> Contact</h2>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
### 📱 Contact
- 📧 **Email:** ricardo.sv99@gmail.com
- 📱 **Phone:** +52 246 377 5523
- 🔗 **LinkedIn:** [linkedin.com/in/ricardo-salazar](https://linkedin.com/in/ricardo-salazar)
- 💻 **GitHub:** [github.com/RicardoSalazarV](https://github.com/RicardoSalazarV)
""")
        with col2:
            st.markdown("### 📄 Resume")
            st.markdown("Download my updated resume with full project history, stack, and experience.")
            st.markdown(f"""
<div style="text-align:center; margin:20px 0;">
    <a href="{CV_LINK_EN}" target="_blank"
       style="background-color:#0F2D5E; color:white; padding:10px 20px;
              border-radius:6px; text-decoration:none; font-weight:bold; margin-right:10px;">
        📥 Download CV (EN)
    </a>
    <a href="{CV_LINK_ES}" target="_blank"
       style="background-color:#3A4A5C; color:white; padding:10px 20px;
              border-radius:6px; text-decoration:none; font-weight:bold;">
        📥 Descargar CV (ES)
    </a>
</div>
""", unsafe_allow_html=True)

# ---------------------------
# Render
# ---------------------------
if language == "Español":
    render_es()
else:
    render_en()
