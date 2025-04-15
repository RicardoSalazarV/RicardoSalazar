import streamlit as st
from PIL import Image

# ---------------------------
# Configuración General
# ---------------------------
st.set_page_config(page_title="Portafolio de Ricardo Salazar", layout="wide")

# Estilos personalizados para las pestañas
st.markdown("""
<style>
    /* Estilo para pestañas */
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
        background-color: #4e89ae;
        color: white;
    }
    .big-emoji {
        font-size: 1.5rem;
        margin-right: 5px;
    }
    h1 {
        background: linear-gradient(45deg, #4e89ae, #43658b);
        padding: 10px 15px;
        border-radius: 10px;
        color: white;
        text-align: center;
    }
    .subtitle {
        text-align: center;
        color: #4e89ae;
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------
# Selector de Idioma
# ---------------------------
language = st.sidebar.selectbox("🌐 Language / Idioma", ["Español", "English"])

# ---------------------------
# Navegación con tabs en lugar de radio buttons
# ---------------------------
def render_tabs():
    if language == "Español":
        tabs = st.tabs([
            "🏠 Inicio", 
            "🙋‍♂️ Sobre mí", 
            "🧠 Tech Stack", 
            "📊 Proyectos", 
            "📄 CV & 📬 Contacto"
        ])
        
        with tabs[0]:
            header_es()
        with tabs[1]:
            about_me_es()
        with tabs[2]:
            tech_stack_es()
        with tabs[3]:
            proyectos_es()
        with tabs[4]:
            contacto_es()
    else:
        tabs = st.tabs([
            "🏠 Home", 
            "🙋‍♂️ About Me", 
            "🧠 Tech Stack", 
            "📊 Projects", 
            "📄 Resume & 📬 Contact"
        ])
        
        with tabs[0]:
            header_en()
        with tabs[1]:
            about_me_en()
        with tabs[2]:
            tech_stack_en()
        with tabs[3]:
            projects_en()
        with tabs[4]:
            contact_en()

# ---------------------------
# Contenido en Español
# ---------------------------
def header_es():
    st.markdown("<h1>👨‍💻 Ricardo Salazar Vázquez</h1>", unsafe_allow_html=True)
    st.markdown("<h3 class='subtitle'>Ingeniero en Desarrollo de Software | Data Scientist en formación</h3>", unsafe_allow_html=True)
    
    # Enlaces con iconos más grandes
    col1, col2, col3 = st.columns([1,1,1])
    with col1:
        st.markdown("<div style='text-align: center'><span class='big-emoji'>🔗</span> <a href='https://linkedin.com/in/ricardo-salazarv'>LinkedIn</a></div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div style='text-align: center'><span class='big-emoji'>💻</span> <a href='https://github.com/RicardoSalazarV'>GitHub</a></div>", unsafe_allow_html=True)
    with col3:
        st.markdown("<div style='text-align: center'><span class='big-emoji'>📧</span> ricardo.sv99@gmail.com</div>", unsafe_allow_html=True)

def about_me_es():
    st.markdown("<h2><span class='big-emoji'>🙋‍♂️</span> Sobre Mí</h2>", unsafe_allow_html=True)
    st.markdown("""
Soy un ingeniero en formación apasionado por los datos, el desarrollo de software y la tecnología aplicada a resolver problemas reales. Actualmente estudio Ingeniería en Desarrollo de Software mientras curso un bootcamp en Ciencia de Datos con TripleTen.

Me especializo en **Python**, análisis de datos, **machine learning**, y visualización, además de tener experiencia en desarrollo de aplicaciones con **.NET**, **Java (Android Studio)** y **Access**.

> 🧠 *"Data is the new oil, and I'm here to refine it."*

🎵 *Fun fact:* Amante de la música frustrado, nunca afinado... pero siempre codificando.
""")

def tech_stack_es():
    st.markdown("<h2><span class='big-emoji'>🧠</span> Tech Stack</h2>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<h3><span class='big-emoji'>💻</span> Lenguajes</h3>", unsafe_allow_html=True)
        st.markdown("- Python (Avanzado)\n- Java (Intermedio, apps móviles con Android Studio)\n- SQL (Intermedio)\n- C# (Intermedio, aplicaciones con .NET)\n- JavaScript\n- Visual Basic")

        st.markdown("<h3><span class='big-emoji'>📊</span> Visualización</h3>", unsafe_allow_html=True)
        st.markdown("- Matplotlib\n- Seaborn\n- Plotly\n- Tableau")

        st.markdown("<h3><span class='big-emoji'>🧰</span> Otros</h3>", unsafe_allow_html=True)
        st.markdown("- GitHub\n- Microsoft Access\n- Canva\n- Adobe Creative Cloud")

    with col2:
        st.markdown("<h3><span class='big-emoji'>📚</span> Librerías</h3>", unsafe_allow_html=True)
        st.markdown("- Pandas\n- NumPy\n- Scikit-learn\n- TensorFlow\n- PyTorch")

        st.markdown("<h3><span class='big-emoji'>🏗️</span> Frameworks</h3>", unsafe_allow_html=True)
        st.markdown("- .NET Framework\n- Streamlit\n- Android SDK (Java)\n- SQLite\n- REST API")

def proyectos_es():
    st.markdown("<h2><span class='big-emoji'>📊</span> Proyectos Destacados</h2>", unsafe_allow_html=True)
    
    # Utilizando grid para mostrar los proyectos en tarjetas
    proyectos_data = [
        {"icon": "🔬", "title": "Análisis de Pureza en Metales", "url": "https://gold-recovery.onrender.com", "desc": "Modelo para evaluar pureza de oro, plata y cobre."},
        {"icon": "🎭", "title": "IMDB Sentiment Analysis", "url": "https://imdb-sentiment-app.onrender.com", "desc": "Clasificador de sentimientos en reseñas de películas."},
        {"icon": "🚗", "title": "Predicción de Precios de Vehículos", "url": "https://vehicle-hz75.onrender.com", "desc": "Modelo para estimar precios según características."},
        {"icon": "🚕", "title": "Taxi Insights", "url": "https://taxi-insights.onrender.com", "desc": "Visualización interactiva sobre taxis y demanda."},
        {"icon": "📡", "title": "Segmentación de Clientes (Megaline)", "url": "https://megaline.onrender.com", "desc": "Clusterización de clientes para telecom."},
        {"icon": "💸", "title": "Optimización de Precios (Rusty Bargain)", "url": "https://rustybargain.onrender.com", "desc": "Optimización de precios para productos usados."},
        {"icon": "🎮", "title": "Análisis de Juegos (Games XTFR)", "url": "https://games-xtfr.onrender.com", "desc": "Dashboard sobre consumo gamer."},
        {"icon": "🔮", "title": "Predicción de Eventos (Sure Tomorrow)", "url": "https://sure-tomorrow.onrender.com", "desc": "Predicción de tendencias futuras con ML."},
    ]
    
    # Crear una cuadrícula para las tarjetas de proyectos
    col1, col2 = st.columns(2)
    
    for i, project in enumerate(proyectos_data):
        col = col1 if i % 2 == 0 else col2
        with col:
            with st.container():
                st.markdown(f"""
                <div style="padding: 15px; border-radius: 10px; border: 1px solid #e0e0e0; margin-bottom: 15px; background-color: #f9f9f9;">
                    <h3><span class="big-emoji">{project["icon"]}</span> {project["title"]}</h3>
                    <p>{project["desc"]}</p>
                    <p><a href="{project["url"]}" target="_blank">🌐 Ver Proyecto</a></p>
                </div>
                """, unsafe_allow_html=True)

def contacto_es():
    st.markdown("<h2><span class='big-emoji'>📄</span> CV & <span class='big-emoji'>📬</span> Contacto</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 📱 Información de contacto
        - 📧 **Correo:** ricardo.sv99@gmail.com  
        - 📱 **Teléfono:** +52 246 377 5523  
        - 🔗 **LinkedIn:** [linkedin.com/in/ricardo-salazarv](https://linkedin.com/in/ricardo-salazarv)  
        - 💻 **GitHub:** [github.com/RicardoSalazarV](https://github.com/RicardoSalazarV)  
        """)
    
    with col2:
        st.markdown("""
        ### 📄 Currículum
        Descarga mi CV completo para conocer todos los detalles sobre mi formación académica, experiencia profesional y proyectos destacados.
        """)
        st.markdown("""
        <div style="text-align: center; margin: 20px 0;">
            <a href="https://drive.google.com/file/d/1Cw5d56d4yXXSHv7O_dsdr9y572iNIJqG/view" target="_blank" style="background-color: #4e89ae; color: white; padding: 10px 15px; border-radius: 5px; text-decoration: none; font-weight: bold;">
                <span class="big-emoji">📥</span> Descargar CV en PDF
            </a>
        </div>
        """, unsafe_allow_html=True)

# ---------------------------
# Contenido en Inglés
# ---------------------------
def header_en():
    st.markdown("<h1>👨‍💻 Ricardo Salazar Vázquez</h1>", unsafe_allow_html=True)
    st.markdown("<h3 class='subtitle'>Software Engineer | Aspiring Data Scientist</h3>", unsafe_allow_html=True)
    
    # Enlaces con iconos más grandes
    col1, col2, col3 = st.columns([1,1,1])
    with col1:
        st.markdown("<div style='text-align: center'><span class='big-emoji'>🔗</span> <a href='https://linkedin.com/in/ricardo-salazarv'>LinkedIn</a></div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div style='text-align: center'><span class='big-emoji'>💻</span> <a href='https://github.com/RicardoSalazarV'>GitHub</a></div>", unsafe_allow_html=True)
    with col3:
        st.markdown("<div style='text-align: center'><span class='big-emoji'>📧</span> ricardo.sv99@gmail.com</div>", unsafe_allow_html=True)

def about_me_en():
    st.markdown("<h2><span class='big-emoji'>🙋‍♂️</span> About Me</h2>", unsafe_allow_html=True)
    st.markdown("""
I'm a software engineer in training, passionate about data, intelligent systems, and building tech that solves real-world problems. I'm currently studying Software Development Engineering and enrolled in a Data Science bootcamp by TripleTen.

I specialize in **Python**, **data analysis**, **machine learning**, and **data visualization**. I've also developed practical tools using **.NET Framework**, **Java (Android)**, and **Microsoft Access**.

> 🧠 *"Data is the new oil, and I'm here to refine it."*

🎵 *Fun fact:* I'm a frustrated music enthusiast—never in tune, always in sync with the code.
""")

def tech_stack_en():
    st.markdown("<h2><span class='big-emoji'>🧠</span> Tech Stack</h2>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<h3><span class='big-emoji'>💻</span> Languages</h3>", unsafe_allow_html=True)
        st.markdown("- Python (Advanced)\n- Java (Intermediate – Android Studio)\n- SQL (Intermediate)\n- C# (.NET Desktop)\n- JavaScript\n- Visual Basic")

        st.markdown("<h3><span class='big-emoji'>📊</span> Visualization</h3>", unsafe_allow_html=True)
        st.markdown("- Matplotlib\n- Seaborn\n- Plotly\n- Tableau")

        st.markdown("<h3><span class='big-emoji'>🧰</span> Tools</h3>", unsafe_allow_html=True)
        st.markdown("- GitHub\n- Microsoft Access\n- Canva\n- Adobe Creative Cloud")

    with col2:
        st.markdown("<h3><span class='big-emoji'>📚</span> Libraries</h3>", unsafe_allow_html=True)
        st.markdown("- Pandas\n- NumPy\n- Scikit-learn\n- TensorFlow\n- PyTorch")

        st.markdown("<h3><span class='big-emoji'>🏗️</span> Frameworks</h3>", unsafe_allow_html=True)
        st.markdown("- .NET Framework\n- Streamlit\n- Android SDK (Java)\n- SQLite\n- REST API")

def projects_en():
    st.markdown("<h2><span class='big-emoji'>📊</span> Featured Projects</h2>", unsafe_allow_html=True)
    
    # Utilizando grid para mostrar los proyectos en tarjetas
    projects_data = [
        {"icon": "🔬", "title": "Gold Purity Analysis", "url": "https://gold-recovery.onrender.com", "desc": "Machine learning model to assess the purity of gold, silver, and copper."},
        {"icon": "🎭", "title": "IMDB Sentiment Analysis", "url": "https://imdb-sentiment-app.onrender.com", "desc": "NLP-based sentiment analysis for movie reviews."},
        {"icon": "🚗", "title": "Vehicle Price Prediction", "url": "https://vehicle-hz75.onrender.com", "desc": "ML model to predict vehicle prices based on technical features."},
        {"icon": "🚕", "title": "Taxi Insights", "url": "https://taxi-insights.onrender.com", "desc": "Interactive dashboard exploring taxi traffic and demand."},
        {"icon": "📡", "title": "Customer Segmentation (Megaline)", "url": "https://megaline.onrender.com", "desc": "Customer clustering for telecom business insights."},
        {"icon": "💸", "title": "Rusty Bargain", "url": "https://rustybargain.onrender.com", "desc": "Price optimization for used products."},
        {"icon": "🎮", "title": "Games XTFR", "url": "https://games-xtfr.onrender.com", "desc": "Gaming market data visualization and trends."},
        {"icon": "🔮", "title": "Sure Tomorrow", "url": "https://sure-tomorrow.onrender.com", "desc": "Forecasting app using ML for future event trends."},
    ]
    
    # Crear una cuadrícula para las tarjetas de proyectos
    col1, col2 = st.columns(2)
    
    for i, project in enumerate(projects_data):
        col = col1 if i % 2 == 0 else col2
        with col:
            with st.container():
                st.markdown(f"""
                <div style="padding: 15px; border-radius: 10px; border: 1px solid #e0e0e0; margin-bottom: 15px; background-color: #f9f9f9;">
                    <h3><span class="big-emoji">{project["icon"]}</span> {project["title"]}</h3>
                    <p>{project["desc"]}</p>
                    <p><a href="{project["url"]}" target="_blank">🌐 View Project</a></p>
                </div>
                """, unsafe_allow_html=True)

def contact_en():
    st.markdown("<h2><span class='big-emoji'>📄</span> Resume & <span class='big-emoji'>📬</span> Contact</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 📱 Contact Information
        - 📧 **Email:** ricardo.sv99@gmail.com  
        - 📱 **Phone:** +52 246 377 5523  
        - 🔗 **LinkedIn:** [linkedin.com/in/ricardo-salazarv](https://linkedin.com/in/ricardo-salazarv)  
        - 💻 **GitHub:** [github.com/RicardoSalazarV](https://github.com/RicardoSalazarV)  
        """)
    
    with col2:
        st.markdown("""
        ### 📄 Resume
        Download my complete resume to learn all the details about my academic background, professional experience, and featured projects.
        """)
        st.markdown("""
        <div style="text-align: center; margin: 20px 0;">
            <a href="https://drive.google.com/file/d/1Cw5d56d4yXXSHv7O_dsdr9y572iNIJqG/view" target="_blank" style="background-color: #4e89ae; color: white; padding: 10px 15px; border-radius: 5px; text-decoration: none; font-weight: bold;">
                <span class="big-emoji">📥</span> Download Resume PDF
            </a>
        </div>
        """, unsafe_allow_html=True)

# ---------------------------
# Renderizar todo el contenido
# ---------------------------
render_tabs()