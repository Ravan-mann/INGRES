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


# Define groundwater-related keywords
# Ensure this list is correctly terminated before defining other variables
groundwater_keywords = [
    "groundwater", "aquifer", "water table", "groundwater levels", "groundwater reservoir",
    "underground water", "subterranean water", "aquifer storage", "phreatic zone",
    "confined aquifer", "unconfined aquifer", "percolation", "infiltration",
    "recharge rate", "discharge rate", "groundwater flow", "hydrogeology",
    "aquifer properties", "porosity", "permeability", "hydraulic conductivity",
    "specific yield", "specific retention", "groundwater basin", "aquifer depletion",
    "groundwater extraction", "pumping", "borewell", "tube well", "dug well",
    "open well", "submersible pump", "handpump", "irrigation", "agricultural water use",
    "domestic water supply", "industrial water use", "overexploitation", "over-pumping",
    "groundwater withdrawal", "sustainable yield", "water abstraction",
    "deep aquifer extraction", "shallow aquifer extraction", "groundwater mining",
    "well drilling", "well depth", "pump capacity", "water yield", "groundwater demand",
    "groundwater quality", "contamination", "pollution", "arsenic contamination",
    "fluoride contamination", "nitrate pollution", "salinity", "salinization",
    "hard water", "total dissolved solids", "heavy metals", "pesticide contamination",
    "industrial effluents", "sewage contamination", "bacterial contamination",
    "chemical pollutants", "water purity", "groundwater treatment", "reverse osmosis",
    "water purification", "aquifer pollution", "groundwater remediation",
    "water quality testing", "pH levels", "turbidity", "recharge", "artificial recharge",
    "rainwater harvesting", "percolation tank", "check dam", "recharge well",
    "injection well", "watershed management", "soil conservation", "afforestation",
    "groundwater replenishment", "recharge basin", "spreading basin", "infiltration rate",
    "rainwater storage", "surface runoff", "water conservation", "sustainable water use",
    "aquifer restoration", "managed aquifer recharge", "roof-top harvesting",
    "contour bunding", "trenching", "farm ponds", "water retention",
    "groundwater regulation", "Groundwater Act", "Central Ground Water Authority",
    "groundwater management", "water policy", "extraction limits", "permit system",
    "restricted zones", "notified areas", "overexploited zones", "critical zones",
    "semi-critical zones", "safe zones", "groundwater monitoring", "water audit",
    "extraction ban", "licensing", "water use permits", "regulatory framework",
    "groundwater guidelines", "water law", "environmental clearance",
    "no-objection certificate", "CGWA guidelines", "water conservation policy",
    "alluvial aquifer", "hard rock aquifer", "coastal aquifer", "Indo-Gangetic plain",
    "Deccan plateau", "Himalayan aquifers", "arid zones", "semi-arid zones",
    "coastal salinization", "Ganga basin", "Brahmaputra basin", "Godavari basin",
    "Krishna basin", "Cauvery basin", "Narmada basin", "Mahanadi basin", "Yamuna river",
    "Punjab groundwater", "Rajasthan groundwater", "Gujarat groundwater",
    "Maharashtra groundwater", "Tamil Nadu groundwater", "Karnataka groundwater",
    "Uttar Pradesh groundwater", "West Bengal groundwater", "groundwater depletion",
    "falling water table", "aquifer exhaustion", "water scarcity", "drought impact",
    "overdraft", "groundwater stress", "aquifer degradation", "saltwater intrusion",
    "land subsidence", "waterlogging", "aquifer compaction", "water crisis",
    "groundwater overuse", "declining water levels", "seasonal fluctuations",
    "dry wells", "aquifer vulnerability", "water shortage", "contaminated aquifers",
    "groundwater monitoring", "water level sensor", "piezometer",
    "observation well", "groundwater mapping", "remote sensing", "GIS mapping",
    "hydrogeological survey", "aquifer testing", "pump test", "water table fluctuation",
    "data logger", "groundwater modeling", "hydrological model"
]

# Define Indian states and capitals
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

# Add state/union territory names to the groundwater_keywords list
for item in india_states_and_capitals:
    if "state" in item:
        groundwater_keywords.append(item["state"].lower()) # Append lowercased names
    elif "union_territory" in item:
        groundwater_keywords.append(item["union_territory"].lower()) # Append lowercased names

# Convert all existing keywords to lowercase for case-insensitive matching
groundwater_keywords = [kw.lower() for kw in groundwater_keywords]


# Session state for messages
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi there! I'm a specialized chatbot here to answer your questions about **groundwater in India**. Please ask away!"}
    ]

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])


# Chat input
if prompt := st.chat_input("What’s your question?"):
    # Check if the prompt contains any of the defined groundwater keywords
    # Ensure both prompt and keywords are lowercased for case-insensitive matching
    if not any(keyword in prompt.lower() for keyword in groundwater_keywords):
        # If the question is not about groundwater in India, display an error
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        error_message = "I can only answer questions about groundwater in India. Please try a different question."
        st.session_state.messages.append({"role": "assistant", "content": error_message})
        with st.chat_message("assistant"):
            st.markdown(error_message)
    else:
        # If the question is relevant, proceed with API call
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Call Gemini API
        try:
            # For a simple Q&A, generate_content with the prompt is sufficient.
            # For multi-turn conversations, you would typically use model.start_chat()
            # and pass the history.
            response = model.generate_content(prompt)

            # Extract reply
            reply = response.text

            # Store & display assistant reply
            st.session_state.messages.append({"role": "assistant", "content": reply})
            with st.chat_message("assistant"):
                st.markdown(reply)

        except Exception as e:
            st.error(f"An error occurred: {e}")
            # Also add the error message to the chat history for visibility
            st.session_state.messages.append({"role": "assistant", "content": f"Sorry, I encountered an error: {e}"})
            with st.chat_message("assistant"):
                st.markdown(f"Sorry, I encountered an error: {e}")