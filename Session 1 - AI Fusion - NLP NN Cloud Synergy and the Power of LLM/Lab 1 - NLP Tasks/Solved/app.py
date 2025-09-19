import spacy
import streamlit as st

# Load the pre-trained model
nlp = spacy.load("en_core_web_sm")

# Process the text
text = "Peter Jackson is the director of The Lord of the Rings movies. He was born in New Zealand. The movies were filmed in New Zealand. The Lord of the Rings movies are based on the books by J.R.R. Tolkien, a British author. The books were written in the 1950s. The movies were filmed in the 2000s."
doc = nlp(text)

# Extract entities
entities = [(ent.text, ent.label_) for ent in doc.ents]

# Display the text and entities
st.write("Text:", text)
st.write("Entities:")
for entity in entities:
    st.write(f"{entity[0]} ({entity[1]})")

# Run the Streamlit app
# Save this script as app.py and run `streamlit run app.py` in the terminal
