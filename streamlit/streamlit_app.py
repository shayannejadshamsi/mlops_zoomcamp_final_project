import pickle

import streamlit as st

st.write(
    """
# Customer Churn Prediction App
"""
)

st.markdown(
    """
<style>
.big-font {
    font-size:50px !important;
}
</style>
""",
    unsafe_allow_html=True,
)


@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def load_model():
    model = '../models/pipeline.bin'

    with open(model, 'rb') as f_in:
        pipeline = pickle.load(f_in)

    return pipeline


pipeline = load_model()

col11, col12, col13 = st.columns(3)

gender = col11.selectbox('Gender', ('Female', 'Male'))
subscription_type = col12.selectbox('Subscription Type', ('Standard', 'Basic', 'Premium'))
contract_length = col13.selectbox('Contract Length', ('Annual', 'Monthly', 'Quarterly'))




col31, col32, col33 = st.columns(3)

age = col31.slider(
    'Age',
    min_value=18,
    max_value=90,
    value=30,
)

tenure = col32.slider(
    'Tenure',
    min_value=0,
    max_value=1500,
    value=0,
)

usage_frequency = col33.slider(
    'Usage Frequency',
    min_value=0,
    max_value=30,
    value=0,
)

col41, col42, col43 = st.columns(3)

support_calls = col41.slider(
    'Support Calls',
    min_value=1,
    max_value=5,
    value=1,
)

payment_delay = col42.slider(
    'Payment Delay',
    min_value=1,
    max_value=4,
    value=1,
)

total_spend = col43.slider(
    'Total Spend',
    min_value=0,
    max_value=100,
    value=0,
)
col51, col52, col53 = st.columns(3)

last_interaction = col51.slider(
    'Last Interaction',
    min_value=1,
    max_value=4,
    value=1,
)


customer = {
    'Age': int(age),
    'Gender': gender,
    'Tenure': int(tenure),
    'Usage Frequency': int(usage_frequency),
    'Support Calls': int(support_calls),
    'Payment Delay': int(payment_delay),
    'Subscription Type': subscription_type,
    'Contract Length': contract_length,
    'Total Spend': int(total_spend),
    'Last Interaction': int(last_interaction),
}

pred = pipeline.predict_proba(customer)[0, 1]
pred = float(pred)

col114, col115 = st.columns(2)

col114.write('<p class="small-font"> Customer Churn Probability: </p> ', unsafe_allow_html=True)
col115.write(
    f"""<p class="big-font">
{pred:0.2f}
</p>
""",
    unsafe_allow_html=True,
)

st.write(

)
