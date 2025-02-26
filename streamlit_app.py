import streamlit as st

def Teorema_bayes(Aprior, Sensitividad, Specificidad):
    """Teorema de Bayes para determinar el chance de tener covid si se stiene un test positivo"""
    Falsos_pos = 1 - Specificidad
    p_b = (Sensitividad * Aprior) + (Falsos_pos * (1 - Aprior))
    aposterior = (Sensitividad * Aprior) / p_b
    return aposterior

st.title("Uso del Teorema de Bayes para determinar el chance de tener covid si se stiene un test positivo")

# User inputs
Aprior = st.slider("Probabilidad de tener covid [P(A)]", 0.01, 1.0, 0.04, 0.01)
Sensitividad = st.slider("¿Cual es la sensitividad? (Aka: Tasa de positivos reales, [P(B | A)])", 0.5, 1.0, 0.73, 0.01)
Specificidad = st.slider("¿Cual es la Specificidad? (Aka: Tasa de negativos reales, [P(¬B | ¬A)])", 0.5, 1.0, 0.95, 0.01)

# Compute aposterior probability
aposterior = Teorema_bayes(Aprior, Sensitividad, Specificidad)

# Display result
st.write(f"### La probabilidad de que tengas Covid-19 si tienes un resultado positivo es del: **{aposterior:.4f} ({aposterior*100:.2f}%)**")
