import streamlit as st

def bayes_theorem(prior, sensitivity, specificity):
    """Calculate the posterior probability using Bayes' Theorem."""
    false_positive_rate = 1 - specificity
    p_b = (sensitivity * prior) + (false_positive_rate * (1 - prior))
    posterior = (sensitivity * prior) / p_b
    return posterior

st.title("Bayes' Theorem: COVID-19 Test Probability Calculator")

# User inputs
prior = st.slider("Prior Probability (Prevalence of COVID-19 in population, P(A))", 0.01, 1.0, 0.04, 0.01)
sensitivity = st.slider("Test Sensitivity (True Positive Rate, P(B | A))", 0.5, 1.0, 0.73, 0.01)
specificity = st.slider("Test Specificity (True Negative Rate, P(¬B | ¬A))", 0.5, 1.0, 0.95, 0.01)

# Compute posterior probability
posterior = bayes_theorem(prior, sensitivity, specificity)

# Display result
st.write(f"### Probability that you actually have COVID-19 given a positive test result: **{posterior:.4f} ({posterior*100:.2f}%)**")
