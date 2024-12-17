import streamlit as st

st.set_page_config(page_title="Behaviours Criteria", page_icon="🤝")

st.title("Behaviours Criteria")
st.write("Record evidence for each Behaviour (B) requirement.")

behaviour_criteria = {
    "B1": "Works independently and takes responsibility",
    "B4": "Works collaboratively with a wide range of people",
    "B5": "Acts with integrity with respect to ethical, legal and regulatory requirements",
    "B6": "Shows initiative and takes responsibility for solving problems",
    "B7": "Communicates effectively to both technical and non-technical audiences",
    "B8": "Shows curiosity and inquisitiveness about the business context",
    "B9": "Committed to continued professional development"
}

# Filter/search
search_term = st.text_input("Search Behaviours by keyword", "")
filtered_criteria = {k: v for k, v in behaviour_criteria.items()
                     if search_term.lower() in v.lower()
                     or search_term.lower() in k.lower()}

# Layout the behaviours criteria with input fields for evidence
for code, description in filtered_criteria.items():
    with st.expander(f"{code}: {description}"):
        st.write("**Evidence / Examples:**")

        # For behaviours, evidence might be feedback from mentors, emails, or scenario descriptions
        evidence_text = st.text_area(f"Describe evidence for {code} (e.g. scenario, feedback excerpt)",
                                     key=f"{code}_text")

        # Mentor confirmation field
        mentor_contact = st.text_input(f"Mentor/Manager who can confirm {code}", key=f"{code}_mentor")

        # File uploader for screenshots of communications or feedback docs
        evidence_file = st.file_uploader(f"Upload supporting document for {code}", type=["pdf", "png", "jpg"],
                                         key=f"{code}_file")

        st.markdown("---")

if st.button("Save Behaviours Evidence"):
    st.success("Behaviours evidence saved (placeholder action).")
