import requests
import streamlit as st
from streamlit_lottie import st_lottie

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

st.set_page_config(
    page_title="SkinSense",
    page_icon="♋",
    layout="wide",
    initial_sidebar_state="expanded",
)

lottie_health = load_lottieurl(
    "https://assets2.lottiefiles.com/packages/lf20_5njp3vgg.json"
)
lottie_welcome = load_lottieurl(
    "https://assets1.lottiefiles.com/packages/lf20_puciaact.json"
)
lottie_healthy = load_lottieurl(
    "https://assets10.lottiefiles.com/packages/lf20_x1gjdldd.json"
)
lottie_why = load_lottieurl(
    "https://lottie.host/111f3906-8bfa-48e7-987e-ee4a21326bac/N0mZ1wkftS.json"
)
lottie_doc = load_lottieurl(
    " https://lottie.host/7909df43-3ece-415a-a5c7-b291b3ff61c2/piBfhTfsNr.json"
)
lottie_find = load_lottieurl(
    "https://lottie.host/0c31858c-8efe-476b-b13c-c9120ee3bbb1/UwiM0Zk1Rv.json"
)

st.title("Welcome to SKINSENSE!")
st.write("SkinSense is a cutting-edge application designed to enhance skin health awareness and early detection. In India, where skin conditions like Actinic Keratosis, Basal Cell Carcinoma, Dermatofibroma, Melanoma, Nevus, Pigmented Benign Keratosis, Seborrheic Keratosis, Squamous Cell Carcinoma, and Vascular Lesions are increasingly prevalent, early diagnosis is crucial.")
st_lottie(lottie_welcome, height=300, key="welcome")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    
    with left_column:
        st.write("##")
        st.header("What Are Skin Diseases?")
        st.write(
            """
            
            Skin diseases encompass a wide range of conditions affecting the skin, which is the body's largest organ. These conditions can vary from benign to malignant and include:
            
            * Infections: Bacterial, viral, or fungal infections.
            * Inflammatory Conditions: Such as eczema and psoriasis.
            * Tumors: Both benign (e.g., dermatofibromas) and malignant (e.g., skin cancers like melanoma).
            * Pigmentation Disorders: Such as pigmented benign keratosis, vitiligo and melasma.
            * Sun-Related Conditions: Like actinic keratosis and squamous cell carcinoma.
            """
        )
    
    with right_column:
        st_lottie(lottie_why, height=300, key="check")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    
    with left_column:
        st.write("##")
        st.header("How Often Do Skin Diseases Occur?")
        st.write(
            """
            
            Skin diseases are prevalent and can affect individuals of all ages. Their frequency can vary based on factors such as:
            
            * Geographic Location: Sun exposure and climate can influence the prevalence of certain conditions.
            * Age: Some conditions are more common in specific age groups (e.g., melanoma is more common in adults over 50).
            * Lifestyle: Factors like sun exposure, smoking, and personal hygiene can affect skin health.
            
            In India, with its diverse climate and increasing exposure to environmental pollutants, skin diseases are a growing concern. Early detection and diagnosis are crucial for effective treatment and management.
            """
        )

    with right_column:
        st_lottie(lottie_healthy, height=300, key="healthy")

with st.container():
    st.write("---")
    cols = st.columns(2)
    with cols[0]:
        st.header("How Can SkinSense Help?")
        st.write(
            """
            **SkinSense** is designed to address these concerns by:
            
            * **Early Detection:** Our application uses advanced algorithms to identify potential skin conditions from images, enabling early diagnosis before symptoms become severe.
            * **Comprehensive Analysis:** It provides detailed assessments of various skin conditions, including Actinic Keratosis, Basal Cell Carcinoma, Melanoma, and more, by analyzing visual data.
            * **Personalized Recommendations:** Based on the detected condition, SkinSense offers tailored advice and guidelines for seeking professional medical consultation.
            * **Educational Resources:** The app includes information about different skin diseases, their symptoms, and preventive measures to enhance awareness and promote skin health.
            * **Convenience:** With an easy-to-use interface, users can quickly check their skin condition without needing immediate access to a dermatologist, ensuring timely intervention when needed.
            """
        )
    with cols[1]:
        st_lottie(lottie_doc, height=250, key="doc")
        st_lottie(lottie_find, height=250, key="find")
        
