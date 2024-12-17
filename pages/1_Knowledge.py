import streamlit as st

st.set_page_config(page_title="Knowledge Criteria", page_icon="🧠")

st.title("Knowledge Criteria")
st.write("Record evidence for each Knowledge (K) requirement.")

# Example data structure for K-items:
knowledge_criteria = {
    "K1": "All stages of the software development life-cycle (what each stage contains, including inputs/outputs)",
    "K3": "Roles and responsibilities of the project life-cycle within your organisation, and your role",
    "K4": "How best to communicate using different methods and adapt to different audiences",
    "K5": "Similarities and differences between different software development methodologies (agile/waterfall)",
    "K7": "Software design approaches and patterns for reusable solutions",
    "K8": "Organisational policies/procedures related to tasks (e.g. GDPR sensitive data handling)",
    "K10": "Principles and uses of relational and non-relational databases",
    "K12": "Software testing frameworks and methodologies"
}

# Filter/search
search_term = st.text_input("Search Knowledge by keyword", "")
filtered_criteria = {k: v for k, v in knowledge_criteria.items()
                     if search_term.lower() in v.lower()
                     or search_term.lower() in k.lower()}

# Layout the knowledge criteria with input fields for evidence
for code, description in filtered_criteria.items():
    with st.expander(f"{code}: {description}"):
        st.write("**Evidence / Examples:**")

        # Text input for a short description of evidence
        evidence_text = st.text_input(f"Evidence summary for {code}", key=f"{code}_text")

        # File uploader or a URL input for linking code samples, documentation, etc.
        evidence_link = st.text_input(f"Link to supporting evidence (GitHub URL, Doc, etc.) for {code}",
                                      key=f"{code}_link")

        # Reflection or notes area
        reflection = st.text_area(f"Reflection on how you met {code}", key=f"{code}_reflection")

        st.markdown("---")

# A placeholder to show how you might save data (we'll have handle persistence later)
if st.button("Save Knowledge Evidence"):
    st.success("Knowledge evidence saved (placeholder action).")
