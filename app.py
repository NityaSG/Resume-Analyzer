import streamlit as st

# Page Config
st.set_page_config(page_title="Analyst Job Application Form", page_icon="📈")

st.title("Analyst Job Application Form")

with st.form("job_application_form"):
    st.subheader("Personal Information")
    # Personal Information
    first_name = st.text_input("First Name")
    last_name = st.text_input("Last Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone Number")

    st.subheader("Professional Background")
    # Professional Background
    latest_job_title = st.text_input("Latest Job Title")
    company = st.text_input("Company Name")
    years_of_experience = st.number_input("Years of Experience", min_value=0, format="%d")

    st.subheader("Education")
    # Education
    highest_degree = st.selectbox("Highest Degree Obtained", 
                                  ["High School", "Bachelor's", "Master's", "PhD", "Other"])
    field_of_study = st.text_input("Field of Study")
    university = st.text_input("University Name")

    st.subheader("Skills and Certifications")
    # Skills
    skills = st.text_area("List your relevant skills")
    certifications = st.text_area("List any relevant certifications")

    st.subheader("Resume")
    # Resume Upload
    resume = st.file_uploader("Upload your resume (PDF)", type=["pdf"])

    # Submit button
    submit_button = st.form_submit_button("Submit Application")

if submit_button:
    st.success("Thank you for your application. We will review it and contact you soon.")
