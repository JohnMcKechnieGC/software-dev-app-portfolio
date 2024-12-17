import streamlit as st

st.set_page_config(page_title="Skills Criteria", page_icon="💻")

st.title("Skills Criteria")
st.write("Record evidence for each Skills (S) requirement.")

skills_criteria = {
    "S2": "Develop effective user interfaces",
    "S3": "Link code to data sets",
    "S5": "Conduct a range of test types (Integration, System, UAT, Non-Functional, Performance, Security)",
    "S8": "Create simple software designs to communicate program understanding",
    "S9": "Create analysis artefacts (e.g. use cases/user stories)",
    "S13": "Follow testing frameworks and methodologies",
    "S14": "Follow company/team/client approaches to CI, version, and source control",
    "S15": "Communicate software solutions to technical & non-technical stakeholders",
    "S17": "Implement a given design, compliant with security & maintainability"
}

# Filter/search
search_term = st.text_input("Search Skills by keyword", "")
filtered_criteria = {k: v for k, v in skills_criteria.items()
                     if search_term.lower() in v.lower()
                     or search_term.lower() in k.lower()}

# Layout the skills criteria with input fields for evidence
for code, description in filtered_criteria.items():
    with st.expander(f"{code}: {description}"):
        st.write("**Evidence / Examples:**")
        evidence_text = st.text_input(f"Evidence summary for {code}", key=f"{code}_text")
        evidence_link = st.text_input(f"Link to supporting evidence (Code, Design Docs, etc.) for {code}",
                                      key=f"{code}_link")

        # Additional tagging or categorization
        tags = st.text_input(f"Tags for {code} (e.g. 'Project A, Frontend, Security')", key=f"{code}_tags")

        st.markdown("---")

if st.button("Save Skills Evidence"):
    st.success("Skills evidence saved (placeholder action).")
