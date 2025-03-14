import streamlit as st


st.markdown(
    """
    <style>
        html, body, [data-testid="stAppViewContainer"] {
            background-color: #ffccdc !important; /* Light Pink */
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Unit Converter")

def convert_units(value, unit_from, unit_to):
    conversions = {
        "meter_kilometer": 0.001,
        "kilometer_meter": 1000,
        "gram_kilogram": 0.001,
        "kilogram_gram": 1000,
    }

    key = f"{unit_from}_{unit_to}"

    if key in conversions:
        conversion = conversions[key]
        return value * conversion
    else:
        return "Conversion not supported"

value = st.number_input("Enter value:", min_value=0.0, format="%.2f")

unit_from = st.selectbox("Convert from:", ["meter", "kilometer", "gram", "kilogram"])
unit_to = st.selectbox("Convert to:", ["meter", "kilometer", "gram", "kilogram"])

if st.button("Convert"):
    result = convert_units(value, unit_from, unit_to)
    st.success(f"The converted value is: {result}")
