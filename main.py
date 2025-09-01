import streamlit as st
import google.generativeai as genai


try:
    genai.configure(api_key="AIzaSyDgeMV9-MPxx10FUo_U2yJQoq47obU6Yno") 
except Exception as e:
    st.error(f"Failed to configure Gemini API: {e}")

st.title("🤖 My Gemini Chatbot")

try:
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"Failed to initialize Gemini model: {e}")
    st.stop()


if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi there! How can I assist you today?(only ask quesions about ground water in india)"}

    ]

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
groundwater_keywords = [
    "groundwater",
    "aquifer",
    "water table",
    "groundwater levels",
    "groundwater reservoir",
    "underground water",
    "subterranean water",
    "aquifer storage",
    "phreatic zone",
    "confined aquifer",
    "unconfined aquifer",
    "percolation",
    "infiltration",
    "recharge rate",
    "discharge rate",
    "groundwater flow",
    "hydrogeology",
    "aquifer properties",
    "porosity",
    "permeability",
    "hydraulic conductivity",
    "specific yield",
    "specific retention",
    "groundwater basin",
    "aquifer depletion",
    "groundwater extraction",
    "pumping",
    "borewell",
    "tube well",
    "dug well",
    "open well",
    "submersible pump",
    "handpump",
    "irrigation",
    "agricultural water use",
    "domestic water supply",
    "industrial water use",
    "overexploitation",
    "over-pumping",
    "groundwater withdrawal",
    "sustainable yield",
    "water abstraction",
    "deep aquifer extraction",
    "shallow aquifer extraction",
    "groundwater mining",
    "well drilling",
    "well depth",
    "pump capacity",
    "water yield",
    "groundwater demand",
    "groundwater quality",
    "contamination",
    "pollution",
    "arsenic contamination",
    "fluoride contamination",
    "nitrate pollution",
    "salinity",
    "salinization",
    "hard water",
    "total dissolved solids",
    "heavy metals",
    "pesticide contamination",
    "industrial effluents",
    "sewage contamination",
    "bacterial contamination",
    "chemical pollutants",
    "water purity",
    "groundwater treatment",
    "reverse osmosis",
    "water purification",
    "aquifer pollution",
    "groundwater remediation",
    "water quality testing",
    "pH levels",
    "turbidity",
    "recharge",
    "artificial recharge",
    "rainwater harvesting",
    "percolation tank",
    "check dam",
    "recharge well",
    "injection well",
    "watershed management",
    "soil conservation",
    "afforestation",
    "groundwater replenishment",
    "recharge basin",
    "spreading basin",
    "infiltration rate",
    "rainwater storage",
    "surface runoff",
    "water conservation",
    "sustainable water use",
    "aquifer restoration",
    "managed aquifer recharge",
    "roof-top harvesting",
    "contour bunding",
    "trenching",
    "farm ponds",
    "water retention",
    "groundwater regulation",
    "Groundwater Act",
    "Central Ground Water Authority",
    "groundwater management",
    "water policy",
    "extraction limits",
    "permit system",
    "restricted zones",
    "notified areas",
    "overexploited zones",
    "critical zones",
    "semi-critical zones",
    "safe zones",
    "groundwater monitoring",
    "water audit",
    "extraction ban",
    "licensing",
    "water use permits",
    "regulatory framework",
    "groundwater guidelines",
    "water law",
    "environmental clearance",
    "no-objection certificate",
    "CGWA guidelines",
    "water conservation policy",
    "alluvial aquifer",
    "hard rock aquifer",
    "coastal aquifer",
    "Indo-Gangetic plain",
    "Deccan plateau",
    "Himalayan aquifers",
    "arid zones",
    "semi-arid zones",
    "coastal salinization",
    "Ganga basin",
    "Brahmaputra basin",
    "Godavari basin",
    "Krishna basin",
    "Cauvery basin",
    "Narmada basin",
    "Mahanadi basin",
    "Yamuna river",
    "Punjab groundwater",
    "Rajasthan groundwater",
    "Gujarat groundwater",
    "Maharashtra groundwater",
    "Tamil Nadu groundwater",
    "Karnataka groundwater",
    "Uttar Pradesh groundwater",
    "West Bengal groundwater",
    "groundwater depletion",
    "falling water table",
    "aquifer exhaustion",
    "water scarcity",
    "drought impact",
    "overdraft",
    "groundwater stress",
    "aquifer degradation",
    "saltwater intrusion",
    "land subsidence",
    "waterlogging",
    "aquifer compaction",
    "water crisis",
    "groundwater overuse",
    "declining water levels",
    "seasonal fluctuations",
    "dry wells",
    "aquifer vulnerability",
    "water shortage",
    "contaminated aquifers",
    "groundwater monitoring",
    "water level sensor",
    "piezometer",
    "observation well",
    "groundwater mapping",
    "remote sensing",
    "GIS mapping",
    "hydrogeological survey",
    "aquifer testing",
    "pump test",
    "water table fluctuation",
    "data logger",
    "groundwater modeling",
    "hydrological model",
    india_states_and_capitals
]
india_states_and_capitals = [
    {"state": "Andhra Pradesh", "capital": "Amaravati"},
    {"state": "Arunachal Pradesh", "capital": "Itanagar"},
    {"state": "Assam", "capital": "Dispur"},
    {"state": "Bihar", "capital": "Patna"},
    {"state": "Chhattisgarh", "capital": "Raipur"},
    {"state": "Goa", "capital": "Panaji"},
    {"state": "Gujarat", "capital": "Gandhinagar"},
    {"state": "Haryana", "capital": "Chandigarh"},
    {"state": "Himachal Pradesh", "capital": "Shimla"},
    {"state": "Jharkhand", "capital": "Ranchi"},
    {"state": "Karnataka", "capital": "Bengaluru"},
    {"state": "Kerala", "capital": "Thiruvananthapuram"},
    {"state": "Madhya Pradesh", "capital": "Bhopal"},
    {"state": "Maharashtra", "capital": "Mumbai"},
    {"state": "Manipur", "capital": "Imphal"},
    {"state": "Meghalaya", "capital": "Shillong"},
    {"state": "Mizoram", "capital": "Aizawl"},
    {"state": "Nagaland", "capital": "Kohima"},
    {"state": "Odisha", "capital": "Bhubaneswar"},
    {"state": "Punjab", "capital": "Chandigarh"},
    {"state": "Rajasthan", "capital": "Jaipur"},
    {"state": "Sikkim", "capital": "Gangtok"},
    {"state": "Tamil Nadu", "capital": "Chennai"},
    {"state": "Telangana", "capital": "Hyderabad"},
    {"state": "Tripura", "capital": "Agartala"},
    {"state": "Uttar Pradesh", "capital": "Lucknow"},
    {"state": "Uttarakhand", "capital": "Dehradun"},
    {"state": "West Bengal", "capital": "Kolkata"},
    {"union_territory": "Andaman and Nicobar Islands", "capital": "Port Blair"},
    {"union_territory": "Chandigarh", "capital": "Chandigarh"},
    {"union_territory": "Dadra and Nagar Haveli and Daman and Diu", "capital": "Daman"},
    {"union_territory": "Delhi", "capital": "New Delhi"},
    {"union_territory": "Jammu and Kashmir", "capital": "Srinagar"},
    {"union_territory": "Ladakh", "capital": "Leh"},
    {"union_territory": "Lakshadweep", "capital": "Kavaratti"},
    {"union_territory": "Puducherry", "capital": "Puducherry"}
]
# Chat input
if prompt := st.chat_input("What’s your question?"):
  if not any(keyword.lower() in prompt.lower() for keyword in groundwater_keywords):
    st.error("Please ask a question about groundwater in India.")
  else:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Call Gemini API
    try:
        # The Gemini API expects a list of content, not roles like OpenAI
        # We will just send the latest user prompt
        response = model.generate_content(prompt)

        # Extract reply
        reply = response.text

        # Store & display assistant reply
        st.session_state.messages.append({"role": "assistant", "content": reply})
        with st.chat_message("assistant"):
            st.markdown(reply)
            
    except Exception as e:
        st.error(f"An error occurred: {e}")
        # Optionally, you can add the error as a message to the chat
        st.session_state.messages.append({"role": "assistant", "content": f"Sorry, I encountered an error: {e}"})
        with st.chat_message("assistant"):
            st.markdown(f"Sorry, I encountered an error: {e}")