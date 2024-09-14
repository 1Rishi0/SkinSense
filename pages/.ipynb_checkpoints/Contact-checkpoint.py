import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(
    page_title="Find a Dermatologist",
    page_icon="♋",
    layout="centered",
    initial_sidebar_state="expanded",
)

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_contact = load_lottieurl(
    " https://lottie.host/08d5c1cb-a1bc-4010-99ed-a42d1b0e3b0d/xLDHt6hPgx.json"
)

st.title("Find a Dermatologist")
st_lottie(lottie_contact, height=200, key="contact")

# Define dermatologist information for different cities
dermatologists = {
    "Hyderabad": {
        "Clinicaderm - Hyderabad": "2ND FLOOR ,H.No:8-2-686, 16/2, Road No. 12, beside Pepperfry, NBT Nagar, Banjara Hills, Hyderabad, Telangana 500034, India",
        "Dr Madhavi's Advanced Skin Hair and Laser Clinic": "first Floor, Sravya D estates, Bahloolguda, 7-1-220/46, near, Prashant Colony Rd, opp. to nature cure hospital, Prashanth Colony, Balkampet, Hyderabad, Telangana 500016, India",
        "SHINE SKIN CLINIC": "Narayana College Building, Naryana Junior College, opp. Yadagiri Theater, inside the kaman, Sai Ratna Arcade, New Santoshnagar, Santosh Nagar, Hyderabad, Telangana 500059, India",
        "Dr Sushma Raavi - Skin & Hair Specialist": "SunCare Clinic, 7-17/3, Suncity Rd, Bandlaguda Jagir, Hyderabad, Telangana 500086, India",
        "Dr K S Ram": "Sonabhan Complex, 3rd Floor, Rashtrapati Rd, above Sri Krishna Sweets & Kanchipuram Silks Showroom, Kummari Guda, Shivaji Nagar, Secunderabad, Telangana 500003, India",
        "Dr Shravya G: Best Dermatologist In Hyderabad | Laser, Acne, Scar, Skin Whitening, PRP Treatments Specialist": "Flat No.301, 3rd Floor, In Park View Edifice, Road No. 1, Journalist Colony, Jubilee Hills, Hyderabad, Telangana 500033, India",
        "Dr. Lakshmi Sowjanya Chekuri MD (DVL) | AVNI Dermatology and Aesthetics | Best Dermatologist in Madhapur | Skin, Hair & Laser": "1st floor, plot no 120, Vamsiram jyothi galaxy, 121, Kavuri Hills, Madhapur, Hyderabad, Telangana 500033, India",
        "Sitarra Dermatology clinics": "Siri Laxmi Arcade,Near MORE Super Mart LANE opposite to Metro Pillar B1114 & B1115 LANE Opposite to Pista House CHIKADAPALLY, Chikkadpally, RTC Cross Road, Himayatnagar, Hyderabad, Telangana 500020, India",
        "DermaCos | Dermatology and Cosmetology Clinic": "Plot No.14, Kavuri hills, Phase 3 Adj to Kakatiya Hills Kamman, Jubliee Hills, Rd Number 36, Kavuri Hills Phase 3, Kavuri Hills, Extension, Hyderabad, Telangana 500081, India",
        "Dr. GSN Reddy's Skin & Hair Clinic": "2-3-64/14 cpl road, beside gurudwar, Tirumala Nagar, Quadri Bagh, Amberpet, Hyderabad, Telangana 500013, India",
        "Dr. Preethi Skin Clinic": "4th Floor, Doyen Galaxy, Srinagar Colony Main Rd, Srinagar Colony, Sri Nagar Colony, Aurora Colony, Yella Reddy Guda, Hyderabad, Telangana 500073, India",
        "Dr Vimala's Skin Hair And Laser Clinic | Best Dermatologist in Hyderabad | Best Cosmetologist Doctor in Hyderabad": "3RD, Apurupa, COMPLEX, Shaikpet Rd, near JRC CONVENTION CENTER, Radhe Nagar, Rai Durg, Hyderabad, Telangana 500033, India",
        "DR.NILOFER SKIN &HAIR AND GENERAL CLINIC": "Plot no 4, Sri Ram nagar colony, Pupalaguda Manikonda, Pipeline Road, beside Vijaya diagnostics, Sri Ram Nagar Colony, Hyderabad, Pokalwada, Telangana 500089, India",
        "Hair and Skin Clinic Dr.A Kiran Kumar": "Apurupa LN Chambers, 2nd floor, Above Indus Ind Bank Opposite to Telangana Tourism, Old MLA Quarters Rd, AP State Housing Board, Himayatnagar, Hyderabad, Telangana 500029, India",
        "Skin Theory Clinic Dermatology & Aesthetics by Dr. Guruvani Ravu": "3rd Floor, Rd Number 36, above SKODA Showroom, CBI Colony, Jubilee Hills, Hyderabad, Telangana 500033, India",
        "DERMA HUB CLINIC (Dr Azheel) ( Skin | Aesthetics | Hair transplant )": "5-7-320, Nampally Road, Aghapura, Nampally, Hyderabad, Telangana 500001, India",
        "Dr. Aparna's Skin, Hair and Laser Clinic | Dermatologist in Amberpet": "CG38+R43 1st Floor, 2-2-7/1/1, Srirang Hemanth Golden Towers, above HDFC Bank, Indraprasth Colony, DD Colony, Amberpet, Hyderabad, Telangana 500044, India",
        "Dr Sushma Raavi - Advanced Skin & Hair Clinic": "theNewYou, Opp KBR Park main Gate, Indo American Cancer Hospital Road, 2nd floor, Guv-Vivilash Chambers, 8-2-293/104, Road No. 14, BNR Colony, BN Reddy Colony, Banjara Hills, Hyderabad, Telangana 500034, India",
        "Dr Suhasini Dermatologist Healthcare clinic": "plotno 12 door, Raghava Nilayam, Huda Colony Rd, Saroornagar, Huda Colony, Kothapet, Hyderabad, Telangana 500035, India",
        "The Skin Sensé": "202, Bhavyas Fantastika, Road No. 12, Anand Banjara Colony, Banjara Hills, Hyderabad, Telangana 500034, India"
    },
    
      "Mumbai": {
        "Dr. Anju Methil - Best Dermatologist in Mumbai": "302, Aston Sundervan, Lokhandwala Rd, Sundervan Complex, Shastri Nagar, Andheri West, Mumbai, Maharashtra 400053, India",
        "Kopikar Dermatology - Dr. Radhika Kopikar": "Sai Prasad Shopping Centre, E, 3/23, below Vikhroli Court, Kannamwar Nagar II, Vikhroli, Mumbai, Maharashtra 400083, India",
        "Cutis Skin Clinic | Best Dermatologist in Bandra West Mumbai": "First Floor, Kukreja House, Telephone Exchange, 12th Rd, opposite Khar, Khar, Khar West, Mumbai, Maharashtra 400052, India",
        "Dr. Reshma Ahuja | Best Dermatologist, Cosmetologist, Trichologist | Powai, Mumbai": "803, Hiranandani Garden, Sorrento, High St, opp. Golden Oak, Hiranandani Gardens, Powai, Mumbai, Maharashtra 400076, India",
        "DR.SKINN CLINIC - Sarika Holmukhe - Best family dermatologist": "Shop no 40, Dr. Skinn Clinic Evershine no 2 co-op housing society, Ratan Nagar Lane Seven Bungalows, Andheri West, near Versova, Gharkul Society, Ratan Nagar, Four Bungalows, Metro, Mumbai, Maharashtra 400053, India",
        "Dr. Dhayal's Skin Clinic by Dr Mamta Dhayal": "Shop no 13, Sheetal F Building, VN Purav Marg, near Santrupti Hospital, Samarth Nagar, Chunabhatti, Sion, Mumbai, Maharashtra 400022, India",
        "RD Clinic - Best Dermatologist in Chembur | Skin & Hair Specialist in Chembur": "906, 9th floor Signature Business Park Postal Colony Road, K A, Gaikwad Road, Postal Colony, Chembur, Mumbai, Maharashtra 400071, India",
        "Dr. Sheetal Patil | Best Dermatologist in Chembur | Skin and Hair Specialist in Chembur": "Pioneer, Shop 2, Runwal Grandeur, Rd Number 18, near 15th Road, Mahadeo Wadi, Chembur, Mumbai, Maharashtra 400071, India",
        "My Skin My Health - Dr. Pallavi Rathi / Skin, Hair, Nail / Laser, Cosmetology, Aesthetics": "My Skin My Health Pranik Chambers Unit No. A 407/408, A Wing, Saki Vihar Rd, opp. H.P petrol pump, Sag Baug, Marol, Saki Naka, Mumbai, Maharashtra 400072, India",
        "Skin Essence": "Shop number 3 & 4, Ramjharukha Apartment, Swami Vivekananda Rd, Zalawad Nagar, Shree Ram Nagar, Andheri West, Mumbai, Maharashtra 400047, India",
        "Dermatologist Dr. Sujit Shanshanwal": "Rizvi Park CHS, #103, 1st Floor, B-Wing, S V Road, Santacruz West, Near Reliance ACME Mall, Rizvi Nagar, Khira Nagar, Santacruz (West), Mumbai, Maharashtra 400054, India",
        "Dr. Sonali's Skin & Hair Clinic": "2nd floor, Vimal Appt, Swami Vivekananda Rd, opp. Patel Petrol Pump, near Mahesh Nagar, Mahesh Nagar, Goregaon West, Mumbai, Maharashtra 400104, India",
        "Dr. Shareefa's Skin Care Clinic": "At Niramaya Clinic, Bus Stop, Sion - Trombay Rd, opposite Maitri Park, Union Park, Chembur, Mumbai, Maharashtra 400071, India",
        "Dr. Priyanka S. Jain": "Flat no.7, 1st floor, Prem Kunj Society, Sion Cir, Sion West, Sion, Mumbai, Maharashtra 400022, India",
        "Dr. Angela Nagpal MD | Best Dermatologist | Skin Specialist in Ghatkopar | Skin and Hair Clinic | Gold Medalist": "The Doctors' Hub, 102, 1st floor, 3WM4+RX RNJ Corporate, Jawahar Rd, next to Parakh Hospital, Saibaba Nagar, Pant Nagar, Ghatkopar East, Mumbai, Maharashtra 400077, India",
        "Dr. Mrinmayee Mukund - Dermatologist in Chembur | Cosmetologist | Skin Treatment | Hair Specialist Doctor in Chembur": "5th Floor, Cozderm Clinic, Signature Business Park, 505, above ACME Hospital, Postal Colony, Chembur, Mumbai, Maharashtra 400071, India",
        "Skin Saga": "104, Sai Iconic, opp. Kokilaben Hospital, Sahayog Nagar, Four Bungalows, Andheri West, Mumbai, Maharashtra 400053, India",
        "Dr. Sejal Saheta - InUrSkn - Skin, Hair & Body": "705, 7th Floor, Powai Plaza, Commercial Wing, B-WING, Central Ave, Hiranandani Gardens, Sainath Nagar, Powai, Mumbai, Maharashtra 400076, India",
        "Dr. Shreya Singh (Dermatologist)": "Swapnapurti Hospital, Shyam Nagar, Jogeshwari East, Mumbai, Maharashtra 400060, India",
        "Dr. Rajan T D": "No102-B, 1st Floor, Samrock Apartment, Juhu Lane, Off SV Road, Barfiwala Road, Andheri West, Zalawad Nagar, Shree Ram Nagar, Andheri West, Mumbai, Maharashtra 400058, India"
    },

    "Bangalore": {
        "Dr. Tina's Skin Solutionz": "11/12, Bellary Rd, below Bata showroom, Sahakar Nagar, Bengaluru, Karnataka 560092, India",
        "SurgiDerma Hospital Skin Hair Laser Plastic surgery": "No. 5ac, 927, 5th A Cross Rd, HRBR Layout 1st Block, Babusabpalya, Kalyan Nagar, Bengaluru, Karnataka 560043, India",
        "Dr. Janet Alexander Castelino - DermaZeal Clinic": "422, 1st & 2nd Floor, 27th Main Rd, 1st Sector, HSR Layout, Bengaluru, Karnataka 560102, India",
        "Dr. Vanita Mathew": "No 15, Ground floor, 5th A cross, 1st B Main Rd, Mico Layout, BTM 2nd Stage, BTM Layout, Bengaluru, Karnataka 76, India",
        "SkinCure Clinic - Dr. Ashish B Shetty": "1051, Doctors, Vijaya Bank Layout, Gangaparameshwari Nagar, Kodichikknahalli, Vijaya Bank Layout, Bilekahalli, Bengaluru, Karnataka 560076, India",
        "Dr Shireen Furtado- Ayana Clinic": "Ayana Clinic, Ground Floor, 13A Cross, 278, 15th Main Rd, behind SBI Bank, F Block, Sahakar Nagar, Byatarayanapura, Bengaluru, Karnataka 560092, India",
        "Dr Dixit Cosmetic Dermatology in Bangalore": "32, 1st Floor, 1st Main Rd, above HDFC Bank, 1st Block Koramangala, Koramangala, Bengaluru, Karnataka 560034, India",
        "Dr. Umashankar's DERMAVISION": "794, 15th Main Rd, Stage 2, BTM Layout, Bengaluru, Karnataka 560076, India",
        "Dr. T. S. Manjunath": "Agadi Hospital & Research Center, #35, Siddaiah Rd, Vinayaka Nagar, Chinnayanpalya, Wilson Garden, Bengaluru, Karnataka 560027, India",
        "Dr. Anita Skinn Clinic": "No.445, 1st Floor, 6th Main Rd, above M.R Complex, 7th Cross, Mico Layout, BTM 2nd Stage, BTM 1st Stage, Bengaluru, Karnataka 560076, India",
        "Sapphire Skin & Aesthetics Clinic": "6th Phase, 718, 24th Main Rd, beside Dmart on line, Marenahalli, J P Nagar Phase 5, J. P. Nagar, Bengaluru, Karnataka 560078, India",
        "Dr. Dharam's Skin O' Hair Clinic | BTM Layout Bangalore": "91, 1st floor, above IndusInd bank, 9th main road, Outer Ring Rd, KEB Colony, Vysya Bank Colony, BTM 1st Stage, Bengaluru, Karnataka 560029, India",
        "iSkin clinic-Advanced Skin and hair clinic BTM 4th Stage, Bilekahalli": "57, near RTO circle, 2nd Block, BTS Layout, Bilekahalli, Bengaluru, Karnataka 560076, India",
        "Dr.K.Srinivasa Murthy": "32/4, 1-B, 1st Floor, Alsa Glenridge Apts, Langford Rd, next to ST Joseph’s PG Centre, Bheemanna Garden, Shanti Nagar, Bengaluru, Karnataka 560025, India",
        "Pelure DR. Nydile's Skin and Cosmetic Clinic": "12th Main Road, Sector 6 HSR Layout 2nd Floor Maruthi HP Gas Agency, near Amma's Pasteries, Sector 6, HSR Layout, Bengaluru, Karnataka 560102, India",
        "Centre for Skin Care": "Horamavu Main Rd, opp. Gandhi Statue, near Sendhoor Coffee, Chinnaswamappa Layout, Ashirvad Colony, Horamavu, Bengaluru, Karnataka 560043, India",
        "Dr. Franklin's Dermacare Clinic": "#310, 1st Floor, 6th Cross, Kaggadasapura Main Rd, Vignan Nagar, Malleshpalya, Doddanekkundi, Bengaluru, Karnataka 560075, India",
        "Dr. Sachith Abraham, MD (Dermatology), The Medical Skin Clinic": "474, 1st Cross Rd, KHB Colony, 5th Block, Koramangala, Bengaluru, Karnataka 560095, India",
        "Dr Seema’s Skin Care and Laser Center": "1/1, Mysore Rd, Pantarapalya, Nayanda Halli, Bengaluru, Karnataka 560039, India",
        "Dr. Parthasarathi's Asian Hair & Skin Hospitals": "Sadath Court, 5 & 6, Magrath Rd, opp. Garuda Mall, Ashok Nagar, Bengaluru, Karnataka 560025, India"
    },

    "Chennai": {
        "SOUL SKIN CLINIC": "1542, H bloc, 5th street, 11th Main Rd, H Block, Anna Nagar, Anna Nagar West, Anna Nagar, Chennai, Tamil Nadu 600040, India",
        "Dr Zee’s SKINMED": "33, Thayar Sahib St, Mount Road, Border Thottam, Padupakkam, Triplicane, Chennai, Tamil Nadu 600002, India",
        "DERMIPURE DERMACLINIC - ADYAR SKIN CLINIC": "9th Ln, Shastri Nagar, Adyar, Chennai, Tamil Nadu 600020, India",
        "Dr. Neha Vani - Best Dermatologist, Skin Specialist in Chennai": "Ojas Health, No 69-JPS Complex, Royapettah High Rd, Jagadambal Colony, Sripuram, Teachers Colony, Royapettah, Chennai, Tamil Nadu 600004, India",
        "DR MERWIN SKIN CLINIC": "EMAAR ESPLANADE APARTMENT, 75, Vaithynathan St, Tondiarpet, Chennai, Tamil Nadu 600081, India",
        "Dr. Dinesh's Skin & Hair Clinic": "A, 31, 6th St, next to Al Maza restaurant, Kumaran Nagar, A Block, Annanagar East, Chennai, Tamil Nadu 600102, India",
        "Dr. Uma's Skin Hair & Laser Clinic ( Shreya Medical Centre)": "W-614,5 th STREET,D SECTOR, near SBOA SCHOOL AND JUNIOR COLLEGE, WEST GATE, Anna Nagar West Extension, Chennai, Tamil Nadu 600101, India",
        "Armoraa Clinic (Dermatologist in Anna Nagar)": "Second, floor , No 109/3, AB 5, 2nd Ave, AB Block, Shanthi Colony, Anna Nagar, Chennai, Tamil Nadu 600040, India",
        "Halos Dermatology": "250, Poonamallee High Rd, Aminjikarai, Chennai, Tamil Nadu 600029, India",
        "Dr. Sajai Varghese": "154, Poonamallee High Rd, New Bupathy Nagar, Chetpet, Chennai, Tamil Nadu 600031, India",
        "Venus Skin Clinic - Dr.Sharanya K, MD Dermatologist": "22, Nageswara Rd, Nungambakkam, Chennai, Tamil Nadu 600034, India",
        "Provas - Dermatology and Medical Cosmetology clinic": "171, Netta Muthiyalkhan St, Bharathi Nagar, Ayanavaram, Chennai, Tamil Nadu 600023, India",
        "Ruchera Skin Care": "No. 2/15, Nathans Arcade 3rd Floor , Malaviya Avenue , Opp. HDFC Bank, Lattice Brg Rd, near Adyar Depot, Subramaniam Colony, Thiruvanmiyur, Chennai, Tamil Nadu 600041, India",
        "ARK Skin Clinic - Dr.K.J.Karrunya": "48 (New no.22), Q block, 48, Q block 15th St, Block Q, Anna Nagar, Chennai, Tamil Nadu 600040, India",
        "Hydra Dermatology - By Dr. Shwetha Rahul": "52, Eldams Rd, Vannia Teynampet, Venus Colony, Teynampet, Chennai, Tamil Nadu 600018, India",
        "Kosmoderma Skin Clinic in Chennai": "No. 140, Chotabhai centre, Thousand Lights West, Nungambakkam, Chennai, Tamil Nadu 600034, India",
        "Dr Gayathri Skin and sugar clinic": "Block No 5, 2nd Cross St, opposite to siet college, Baruva Nagar, Seethammal Extension, Teynampet, Chennai, Tamil Nadu 600018, India",
        "Aarthi Skin Care Clinic, MRC Nagar": "32 , First Floor, Kasturi Ave, MRC Nagar, Raja Annamalai Puram, Chennai, Tamil Nadu 600028, India",
        "Dr. Deepika Lunawat | Mahi Skin, Hair & Laser Clinic": "18, Millers Rd, Kilpauk, Chennai, Tamil Nadu 600010, India",
        "Dermis Skin & Hair Clinic | Dr Ganga Ravikumar": "60/D, 1st Floor, Ashvin Arcade, opp. to Pillayar Kovil, Venkata Rathnam Nagar Extension, Venkata Rathinam Nagar, Adyar, Chennai, Tamil Nadu 600020, India"
    },

    "New Delhi": {
        "Dadu Medical Centre": "J-12/25, 1st Floor, Block J, Rajouri Garden Extension, Rajouri Garden, New Delhi, Delhi, 110027, India",
        "Dr. Rohit Batra | Best Dermatologist & Skin Specialist in Delhi": "Q-4, New, Janta Market, Rajouri Garden, Delhi, 110027, India",
        "Dr. Jyoti Gupta Clinic": "B-43, 1st floor, Block B, Soami Nagar South, Soami Nagar, New Delhi, Delhi 110017, India",
        "Dr Lipy Gupta": "Family Medicine Clinic, S-34, Market, Block S, Green Park, New Delhi, Delhi 110016, India",
        "Dermatologie": "Basement, 115A, next to JRD hotel, B-7/Extension, Block B 7, Arjun Nagar, Safdarjung Enclave, New Delhi, Delhi 110029, India",
        "Dr. Rohit Batra I Skin Specialist Sir Ganga Ram Hospital": "Department of Dermatology New Rajinder Nagar Room No F 24, Private OPD, SIR GANGA RAM HOSPITAL, New, Old Rajinder Nagar, Rajinder Nagar, New Delhi, Delhi, 110060, India",
        "Dr Sandesh Gupta": "Skin n laser centre, F-10/9, Mandir Marg, Block F, Krishna Nagar, New Delhi, Delhi, 110051, India",
        "Dr Shankila Mittal": "27B/4, First Floor Govinda Medicenter Opp Sarai Rohilla Station, New Rohtak Rd, Block 27B, Dev Nagar, Karol Bagh, New Delhi, Delhi, 110005, India",
        "(Antiaging skin clinic)": "Okhla road, Sukhdev Vihar Metro Station Fertis Escorts Heart Institute, Gate no-5, Upper basement, Deptt of Dermatology New Delhi-19, H76F+5F7, Okhla Rd, opp. Holy Family Hospital, New Friends Colony, New Delhi, Delhi 110025, India",
        "Dr. Indu Kumari": "C95, Shivalik Rd, Block C, Shivalik Colony, Malviya Nagar, New Delhi, Delhi, 110017, India",
        "Skin Well Dermatology & Cosmetology Clinic": "37/6 East, Rd Number 6, East Avenue Market, Punjabi Bagh Cooperative Housing Soceity, East Punjabi Bagh, Punjabi Bagh, New Delhi, Delhi, 110026, India",
        "ISAAC Luxe - Best Dermatologist in Vasant Vihar, Best Skin specialist & Clinic in Delhi, Best Emface in Delhi": "26, Poorvi Marg, near Modern School, Block E, Vasant Vihar, New Delhi, Delhi 110057, India",
        "Advanced Dermatology": "G-1219A, Basement Main Market, Chittaranjan Park(C.R.Park), Block G, Chittaranjan Park, New Delhi, Delhi 110019, India",
        "DR AMIT LUTHRA": "Ishira Clinic S-341, Block S, Panchsheel Park South, Panchsheel Park, New Delhi, Delhi 110017, India",
        "Dr. Deepti Shrivastava's Skin Hair & You | Dermatologist in Delhi": "Lower Ground Floor, Petrol Pump, 48, opposite Anand Vihar, near YAMUNA SPORTS COMPLEX, Ram Vihar, Anand Vihar, Delhi, 110092, India",
        "Dr Pallavi Chandna Rohatgi | Best Dermatologist in South Delhi": "Dermedico, D-95, Block D, Defence Colony, New Delhi, Delhi 110024, India",
        "Dr Amit Seth's": "Shopping Center, 130, Shankar Rd, Block E, Rajender Nagar Part 2, New Rajinder Nagar, New Delhi, Delhi, 110060, India",
        "Dr.Nitika": "D 151, Shankar Rd, Block E, Rajender Nagar Part 2, New Rajinder Nagar, New Delhi, Delhi, 110060, India",
        "Delhi Dermatology Group": "10, Aradhana Enclave, Sector 13 R K Puram, Sector 13, Rama Krishna Puram, New Delhi, Delhi 110066, India",
        "Dr Neeharika Goyal Best Dermatologist & Skin Specialist in Delhi | Skin Doctor | Hair Specialist": "C, 38, Ashok Vihar Phase 1 Rd, near Golden Bell’s School, Pocket C, Ashok Vihar, New Delhi, Delhi, 110052, India"
    },
    
    }
    

# Create a dropdown menu for city selection
city = st.selectbox(
    label="Select your city",
    options=["Select a city", "Hyderabad", "Chennai", "Bangalore", "Mumbai", "New Delhi"],
    index=0
)

if city != "Select a city":
    if city in dermatologists:
        st.header(f"Dermatologists in {city}")

        for name, address in dermatologists[city].items():
            st.markdown(f"**{name}**")
            st.markdown(f"**Address:** {address}")
            st.markdown("---")
    else:
        st.error("No information available for the selected city")
else:
    st.info("Please select a city to find dermatologists")
