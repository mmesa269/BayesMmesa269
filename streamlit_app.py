import streamlit as st

def Teorema_bayes(Aprior, Sensitividad, Specificidad):
    """Uso del Teorema de Bayes para determinar el chance de tener covid si se stiene un test positivo"""
    Falsos_pos = 1 - Specificidad
    p_b = (Sensitividad * Aprior) + (Falsos_pos * (1 - Aprior))
    aposterior = (Sensitividad * Aprior) / p_b
    return aposterior

st.title("Bayes' Theorem: COVID-19 Test Probability Calculator")

# User inputs
Aprior = st.slider("Probabilidad de tener covid, P(A))", 0%, 100%, 4%, 0)
Sensitividad = st.slider("Test Sensitividad (True Positive Rate, P(B | A))", 0.5, 1.0, 0.73, 0.01)
Specificidad = st.slider("Test Specificidad (True Negative Rate, P(¬B | ¬A))", 0.5, 1.0, 0.95, 0.01)

# Compute aposterior probability
aposterior = Teorema_bayes(Aprior, Sensitividad, Specificidad)

# Display result
st.write(f"### Probability that you actually have COVID-19 given a positive test result: **{aposterior:.4f} ({aposterior*100:.2f}%)**")
