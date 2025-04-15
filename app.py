import streamlit as st
from PIL import Image

# ---------------------------
# Configuración General
# ---------------------------
st.set_page_config(page_title="Portafolio de Ricardo Salazar", layout="wide")

# ---------------------------
# Selector de Idioma
# ---------------------------
language = st.sidebar.selectbox("🌐 Language / Idioma", ["Español", "English"])

# ---------------------------
# Navegación Dinámica
# ---------------------------
nav_options = {
    "Español": ["🏠 Inicio", "🙋‍♂️ Sobre mí", "🧠 Tech Stack", "📊 Proyectos", "📄 CV & 📬 Contacto"],
    "English": ["🏠 Home", "🙋‍♂️ About Me", "🧠 Tech Stack", "📊 Projects", "📄 Resume & 📬 Contact"]
}
selection = st.sidebar.radio("Navegación", nav_options[language])

# ---------------------------
# Contenido en Español
# ---------------------------
def contenido_es():
    def header():
        st.markdown("<h1 style='font-size: 48px;'>👨‍💻 Ricardo Salazar Vázquez</h1>", unsafe_allow_html=True)
        st.markdown("<h3 style='color:gray;'>Ingeniero en Desarrollo de Software | Data Scientist en formación</h3>", unsafe_allow_html=True)
        st.markdown("🔗 [LinkedIn](https://linkedin.com/in/ricardo-salazarv) &nbsp;&nbsp;&nbsp; 💻 [GitHub](https://github.com/RicardoSalazarV) &nbsp;&nbsp;&nbsp; 📧 ricardo.sv99@gmail.com")

    def about_me():
        st.markdown("## 🙋‍♂️ Sobre Mí")
        st.markdown("""
Soy un ingeniero en formación apasionado por los datos, el desarrollo de software y la tecnología aplicada a resolver problemas reales. Actualmente estudio Ingeniería en Desarrollo de Software mientras curso un bootcamp en Ciencia de Datos con TripleTen.

Me especializo en **Python**, análisis de datos, **machine learning**, y visualización, además de tener experiencia en desarrollo de aplicaciones con **.NET**, **Java (Android Studio)** y **Access**.

> 🧠 *"Data is the new oil, and I’m here to refine it."*

🎵 *Fun fact:* Amante de la música frustrado, nunca afinado... pero siempre codificando.
""")

    def tech_stack():
        st.markdown("## 🧠 Tech Stack")
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### 💻 Lenguajes")
            st.markdown("- Python (Avanzado)\n- Java (Intermedio, apps móviles con Android Studio)\n- SQL (Intermedio)\n- C# (Intermedio, aplicaciones con .NET)\n- JavaScript\n- Visual Basic")

            st.markdown("### 📊 Visualización")
            st.markdown("- Matplotlib\n- Seaborn\n- Plotly\n- Tableau")

            st.markdown("### 🧰 Otros")
            st.markdown("- GitHub\n- Microsoft Access\n- Canva\n- Adobe Creative Cloud")

        with col2:
            st.markdown("### 📚 Librerías")
            st.markdown("- Pandas\n- NumPy\n- Scikit-learn\n- TensorFlow\n- PyTorch")

            st.markdown("### 🏗️ Frameworks")
            st.markdown("- .NET Framework\n- Streamlit\n- Android SDK (Java)\n- SQLite\n- REST API")

    def proyectos():
        st.markdown("## 📊 Proyectos Destacados")
        project_data = [
            {"title": "🔬 Análisis de Pureza en Metales", "url": "https://gold-recovery.onrender.com", "desc": "Modelo para evaluar pureza de oro, plata y cobre."},
            {"title": "🎭 IMDB Sentiment Analysis", "url": "https://imdb-sentiment-app.onrender.com", "desc": "Clasificador de sentimientos en reseñas de películas."},
            {"title": "🚗 Predicción de Precios de Vehículos", "url": "https://vehicle-hz75.onrender.com", "desc": "Modelo para estimar precios según características."},
            {"title": "🚕 Taxi Insights", "url": "https://taxi-insights.onrender.com", "desc": "Visualización interactiva sobre taxis y demanda."},
            {"title": "📡 Segmentación de Clientes (Megaline)", "url": "https://megaline.onrender.com", "desc": "Clusterización de clientes para telecom."},
            {"title": "💸 Optimización de Precios (Rusty Bargain)", "url": "https://rustybargain.onrender.com", "desc": "Optimización de precios para productos usados."},
            {"title": "🎮 Análisis de Juegos (Games XTFR)", "url": "https://games-xtfr.onrender.com", "desc": "Dashboard sobre consumo gamer."},
            {"title": "🔮 Predicción de Eventos (Sure Tomorrow)", "url": "https://sure-tomorrow.onrender.com", "desc": "Predicción de tendencias futuras con ML."},
        ]
        for p in project_data:
            with st.expander(p["title"]):
                st.markdown(f"📝 {p['desc']}")
                st.markdown(f"[🌐 Ver Proyecto]({p['url']})")

    def contacto():
        st.markdown("## 📄 CV & 📬 Contacto")
        st.markdown("""
- 📧 **Correo:** ricardo.sv99@gmail.com  
- 📱 **Teléfono:** +52 246 377 5523  
- 🔗 **LinkedIn:** [linkedin.com/in/ricardo-salazarv](https://linkedin.com/in/ricardo-salazarv)  
- 💻 **GitHub:** [github.com/RicardoSalazarV](https://github.com/RicardoSalazarV)  
- 📄 **CV:** [Descargar PDF](https://drive.google.com/file/d/1Cw5d56d4yXXSHv7O_dsdr9y572iNIJqG/view?usp=drive_link)
""")

    # Routing
    if selection == "🏠 Inicio":
        header()
    elif selection == "🙋‍♂️ Sobre mí":
        about_me()
    elif selection == "🧠 Tech Stack":
        tech_stack()
    elif selection == "📊 Proyectos":
        proyectos()
    elif selection == "📄 CV & 📬 Contacto":
        contacto()

# ---------------------------
# Contenido en Inglés
# ---------------------------
def contenido_en():
    def header():
        st.markdown("<h1 style='font-size: 48px;'>👨‍💻 Ricardo Salazar Vázquez</h1>", unsafe_allow_html=True)
        st.markdown("<h3 style='color:gray;'>Software Engineer | Aspiring Data Scientist</h3>", unsafe_allow_html=True)
        st.markdown("🔗 [LinkedIn](https://linkedin.com/in/ricardo-salazarv) &nbsp;&nbsp;&nbsp; 💻 [GitHub](https://github.com/RicardoSalazarV) &nbsp;&nbsp;&nbsp; 📧 ricardo.sv99@gmail.com")

    def about_me():
        st.markdown("## 🙋‍♂️ About Me")
        st.markdown("""
I'm a software engineer in training, passionate about data, intelligent systems, and building tech that solves real-world problems. I’m currently studying Software Development Engineering and enrolled in a Data Science bootcamp by TripleTen.

I specialize in **Python**, **data analysis**, **machine learning**, and **data visualization**. I’ve also developed practical tools using **.NET Framework**, **Java (Android)**, and **Microsoft Access**.

> 🧠 *"Data is the new oil, and I’m here to refine it."*

🎵 *Fun fact:* I’m a frustrated music enthusiast—never in tune, always in sync with the code.
""")

    def tech_stack():
        st.markdown("## 🧠 Tech Stack")
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### 💻 Languages")
            st.markdown("- Python (Advanced)\n- Java (Intermediate – Android Studio)\n- SQL (Intermediate)\n- C# (.NET Desktop)\n- JavaScript\n- Visual Basic")

            st.markdown("### 📊 Visualization")
            st.markdown("- Matplotlib\n- Seaborn\n- Plotly\n- Tableau")

            st.markdown("### 🧰 Tools")
            st.markdown("- GitHub\n- Microsoft Access\n- Canva\n- Adobe Creative Cloud")

        with col2:
            st.markdown("### 📚 Libraries")
            st.markdown("- Pandas\n- NumPy\n- Scikit-learn\n- TensorFlow\n- PyTorch")

            st.markdown("### 🏗️ Frameworks")
            st.markdown("- .NET Framework\n- Streamlit\n- Android SDK (Java)\n- SQLite\n- REST API")

    def projects():
        st.markdown("## 📊 Featured Projects")
        project_data = [
            {"title": "🔬 Gold Purity Analysis", "url": "https://gold-recovery.onrender.com", "desc": "Machine learning model to assess the purity of gold, silver, and copper."},
            {"title": "🎭 IMDB Sentiment Analysis", "url": "https://imdb-sentiment-app.onrender.com", "desc": "NLP-based sentiment analysis for movie reviews."},
            {"title": "🚗 Vehicle Price Prediction", "url": "https://vehicle-hz75.onrender.com", "desc": "ML model to predict vehicle prices based on technical features."},
            {"title": "🚕 Taxi Insights", "url": "https://taxi-insights.onrender.com", "desc": "Interactive dashboard exploring taxi traffic and demand."},
            {"title": "📡 Customer Segmentation (Megaline)", "url": "https://megaline.onrender.com", "desc": "Customer clustering for telecom business insights."},
            {"title": "💸 Rusty Bargain", "url": "https://rustybargain.onrender.com", "desc": "Price optimization for used products."},
            {"title": "🎮 Games XTFR", "url": "https://games-xtfr.onrender.com", "desc": "Gaming market data visualization and trends."},
            {"title": "🔮 Sure Tomorrow", "url": "https://sure-tomorrow.onrender.com", "desc": "Forecasting app using ML for future event trends."},
        ]
        for p in project_data:
            with st.expander(p["title"]):
                st.markdown(f"📝 {p['desc']}")
                st.markdown(f"[🌐 View Project]({p['url']})")

    def contact():
        st.markdown("## 📄 Resume & 📬 Contact")
        st.markdown("""
- 📧 **Email:** ricardo.sv99@gmail.com  
- 📱 **Phone:** +52 246 377 5523  
- 🔗 **LinkedIn:** [linkedin.com/in/ricardo-salazarv](https://linkedin.com/in/ricardo-salazarv)  
- 💻 **GitHub:** [github.com/RicardoSalazarV](https://github.com/RicardoSalazarV)  
- 📄 **Resume:** [Download PDF](https://drive.google.com/file/d/1Cw5d56d4yXXSHv7O_dsdr9y572iNIJqG/view?usp=drive_link)
""")

    # Routing
    if selection == "🏠 Home":
        header()
    elif selection == "🙋‍♂️ About Me":
        about_me()
    elif selection == "🧠 Tech Stack":
        tech_stack()
    elif selection == "📊 Projects":
        projects()
    elif selection == "📄 Resume & 📬 Contact":
        contact()

# ---------------------------
# Render por idioma
# ---------------------------
if language == "Español":
    contenido_es()
else:
    contenido_en()
