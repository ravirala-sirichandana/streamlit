import streamlit as st

# Title
st.title("📘 Student Marks Calculator")

# Number inputs for marks
maths = st.number_input("Enter Maths Marks:", min_value=0, max_value=100, step=1)
science = st.number_input("Enter Science Marks:", min_value=0, max_value=100, step=1)
english = st.number_input("Enter English Marks:", min_value=0, max_value=100, step=1)

# Button to calculate
if st.button("Calculate Result"):
    total = maths + science + english
    percentage = total / 3

    # Grade logic
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 75:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 40:
        grade = "C"
    else:
        grade = "Fail"

    # Display results
    st.success(f"✅ Total Marks: {total}")
    st.success(f"📊 Percentage: {percentage:.2f}%")
    st.success(f"🎓 Grade: {grade}")
