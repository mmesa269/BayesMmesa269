import streamlit as st

def Teorema_bayes(Aprior, Sensitividad, Especificidad):
    """Teorema de Bayes para determinar el chance de tener covid si se stiene un test positivo"""
    Falsos_pos = 1 - Especificidad
    p_b = (Sensitividad * Aprior) + (Falsos_pos * (1 - Aprior))
    aposterior = (Sensitividad * Aprior) / p_b
    return aposterior

st.title("Uso del Teorema de Bayes para determinar el chance de tener covid si se stiene un test positivo")

# User inputs
Aprior = st.slider("Probabilidad de tener covid [P(A)]", 0.01, 1.0, 0.04, 0.01)
Sensitividad = st.slider("¿Cual es la sensitividad? (Aka: Tasa de positivos reales, [P(B | A)])", 0.01, 1.0, 0.73, 0.01)
Especificidad = st.slider("¿Cual es la Especificidad? (Aka: Tasa de negativos reales, [P(¬B | ¬A)])", 0.01, 1.0, 0.95, 0.01)

# Compute aposterior probability
aposterior = Teorema_bayes(Aprior, Sensitividad, Especificidad)

# Display result
st.write(f"### La probabilidad de que tengas Covid-19 si tienes un resultado positivo es del: **{aposterior:.4f} ({aposterior*100:.2f}%)**")

if (Especificidad < 0.3):
    st.write ("Advertencia: La especificidad que se seleciono es menos de 30%, esto posiblemente causara que sus chances de tener covid sean extremadamente bajos")

if (Aprior > 0.7):
    st.write ("Advertencia: La probabilidad de estar contagiado es muy alta (mayor a 70%), esto posiblemente causara que sus chances de tener covid sean extremadamente altos")
