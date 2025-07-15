import streamlit as st
from PIL import Image
import base64
from io import BytesIO

# Page config
st.set_page_config(page_title="Arif Khan | Portfolio", layout="wide")
def get_pdf_download_button(pdf_path, label):
    with open(pdf_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'''
        <div style="position: absolute; top: 10px; left: 10px; z-index: 1000;">
            <a href="data:application/pdf;base64,{base64_pdf}" download="Arif_Khan_Data_Scientist.pdf">
                <button style="padding: 6px 12px; background-color: #4CAF50; color: white; border: none; border-radius: 5px; cursor: pointer;">
                    📄 {label}
                </button>
            </a>
        </div>
    '''
    return pdf_display

st.markdown(get_pdf_download_button("Arif_Khan_Data_Scientist.pdf", "Download My Resume"), unsafe_allow_html=True)
# Load image
img = Image.open("Arif_image.jpg")

# Convert image to base64
buffered = BytesIO()
img.save(buffered, format="JPEG")
img_base64 = base64.b64encode(buffered.getvalue()).decode()

# Display with circular style and base64 inline HTML
st.markdown(f"""
    <style>
        .centered-img {{
            display: flex;
            justify-content: center;
        }}
        .circular-img {{
            border-radius: 50%;
            width: 120px;
            height: 120px;
            object-fit: cover;
            box-shadow: 0 2px 4px rgba(0,0,0,0.2);
        }}
    </style>
    <div class="centered-img">
        <img class="circular-img" src="data:image/jpeg;base64,{img_base64}" alt="Arif Khan"/>
    </div>
    <h2 style='text-align: center;'>👨‍💻 Arif Khan</h2>
    <h4 style='text-align: center;'>Aspiring AI/ML Engineer | Data Scientist | Data Analyst</h4>
""", unsafe_allow_html=True)
# Resume Download Button (Top-left)





# -----------------------------
# HOME / ABOUT
# -----------------------------

st.markdown("## About Me")

st.markdown("""
Hello! I'm **Arif Khan**, a passionate Computer Science graduate driven by a deep interest in **Artificial Intelligence**, **Machine Learning**, and **Data Analytics**.
My journey into data science began with curiosity and has since evolved into a full-fledged pursuit of building intelligent systems that solve real-world problems. I thrive at the intersection of code, data, and decision-making — transforming raw data into actionable insights.
With hands-on experience in building **NLP models**, developing **predictive analytics tools**, and applying **deep learning techniques**, I have worked on projects spanning healthcare, insurance, and energy. Whether it's extracting meaning from unstructured text or forecasting trends from time series data, I bring both technical depth and creative problem-solving to the table.
Beyond just model building, I'm passionate about **end-to-end ML workflows** — from **data preprocessing and feature engineering**, to **model evaluation**, **hyperparameter tuning**, and **deployment**. I enjoy using tools like **Scikit-learn, Hugging Face Transformers, TensorFlow, and Streamlit** to bring ideas to life.
I'm a continuous learner, always exploring new trends in **LLMs**, **MLOps**, and **cloud deployment**, and I enjoy collaborating on impactful projects with a data-driven mindset. Let’s connect and turn data into decisions that make a difference!

---

### 🎓 EDUCATION

**Master of Science in Computer Science**  
📅 *2024 – Pursuing (Expected 2026)*  
🏫 *Ramniranjan Jhunjhunwala College, Mumbai*

**Bachelor of Science in Computer Science**  
📅 *2021 – 2024*  
🏫 *Ramniranjan Jhunjhunwala College, Mumbai*  
📊 **CGPA:** 8.28

---

- 🧠 Strong analytical and problem-solving mindset with hands-on experience in:
  - **Natural Language Processing (NLP)**
  - **Classification and Regression Modeling**
  - **Time Series Forecasting**
  - **Data Cleaning and Visualization**
- 🔧 Proficient with tools like **Python, Scikit-learn, Pandas, Matplotlib, Seaborn, Hugging Face Transformers, and Streamlit**
- 🧪 Built multiple end-to-end ML projects that solve real-world problems in healthcare, energy, and insurance
- 🌐 Fluent in **English** and **Hindi**
- 💡 Passionate about exploring cutting-edge trends in **AI**, **LLMs**, and **Model Deployment**
""")

# -----------------------------
# PROJECTS
# -----------------------------
st.markdown("## 💼 Projects")

st.subheader("🔹 Drug Prediction using NLP")
st.markdown("""
- Developed a Natural Language Processing model to classify medical conditions such as **diabetes**, **anxiety**, and **hypertension** based on patient drug reviews.
- Applied advanced **text preprocessing** techniques including stopword removal, stemming, and tokenization.
- Utilized **BERT** from Hugging Face Transformers for contextual embeddings and fine-tuned it for multiclass classification.
- Achieved high **accuracy and F1-score** with class balancing and hyperparameter tuning.
""")

st.subheader("🔹 Insurance Claim Prediction")
st.markdown("""
- Built a machine learning model to **predict whether an insurance claim is fraudulent or genuine**.
- Performed **EDA**, handled class imbalance with **SMOTE**, and engineered relevant features.
- Trained models like **Random Forest, Logistic Regression, and XGBoost**, evaluated with accuracy and AUC.
""")

st.subheader("🔹 House Price Prediction")
st.markdown("""
- Developed a **regression model** to predict house prices based on area, location, rooms, and amenities.
- Performed **feature engineering**, scaling, and cross-validation.
- Used models like **Linear Regression, Ridge, Lasso, and XGBoost**, achieving strong **R² and RMSE** metrics.
""")

# -----------------------------
# SKILLS
# -----------------------------
st.markdown("## 🧠 Skills")

st.markdown("""
### 👨‍💻 Programming & Data Handling
- Python, R, SQL

### 📚 Frameworks & Libraries
- Pandas, NumPy, Scikit-learn, Keras, TensorFlow, Matplotlib, Seaborn

### 📊 Data Analytics & Visualization
- Excel, Tableau, Power BI, Data Visualization

### 🤖 Machine Learning & AI
- Machine Learning, Deep Learning, Artificial Intelligence, MLOps, NLP, LLMs

### 📈 Statistical & Analytical Methods
- Statistics, Time Series Analysis, Forecasting, Data Analytics

### 🔄 Version Control & Workflow
- Git

### 💼 Soft Skills
- Critical Thinking, Problem Solving, Business Acumen, Analytical Thinking, Research
""")

# -----------------------------
# CERTIFICATIONS
# -----------------------------
st.markdown("## 📜 Certifications")

col1, col2, col3 = st.columns(3)

with col1:
    st.image("course_certificate.jpg", caption="ExcelR Solution – Data Science", use_container_width=True)

with col2:
    st.image("certificate.png", caption="AI Variant – Data Science Internship", use_container_width=True)

with col3:
    st.image("GenAi.png", caption="Coursera – GenAI, ML, Python", use_container_width=True)

# -----------------------------
# CONTACT
# -----------------------------
st.markdown("## 📬 Contact")

st.markdown("""
- 📧 Email: arifkhan50636@gmail.com  
- 📱 Phone: +91-9136259776  
- 🔗 [GitHub](https://github.com/Arifkhd)  
- 🔗 [LinkedIn](https://www.linkedin.com/in/arik7)
""")

st.markdown("""<hr style="margin-top:50px;">""", unsafe_allow_html=True)

st.markdown("""
    <style>
        .footer {
            position: relative;
            bottom: 0;
            width: 100%;
            padding: 10px 0;
            text-align: center;
            color: gray;
            font-size: 14px;
        }
        .footer a {
            color: gray;
            text-decoration: none;
            margin: 0 8px;
        }
        .footer a:hover {
            color: #1f77b4;
        }
    </style>

    <div class="footer">
        © 2025 Arif Khan • 
        <a href="https://github.com/Arifkhd" target="_blank">GitHub</a> |
        <a href="https://www.linkedin.com/in/arik7" target="_blank">LinkedIn</a> |
        <a href="mailto:arifkhan123@example.com">Email</a>
    </div>
""", unsafe_allow_html=True)
