import streamlit as st 
# 'import' trae la *Librería* (las herramientas prestadas) a tu proyecto.

# 1. El Título y Textos
st.title("🎨 Mi Estudio de Arte Digital")
st.write("Bienvenido. Esta aplicación está corriendo en un navegador web.")

# 2. Interactividad con *Widgets* (Elementos visuales como botones o cajas de texto)
# Aquí creamos una *Variable* (una caja con nombre para guardar datos) llamada 'nombre'.
nombre = st.text_input("¿Cómo te llamas?")

# 3. El Botón y la *Lógica Condicional* (Si pasa esto, haz aquello)
if st.button("Saludar"):
    # 'if' pregunta: "¿Hay algo guardado en la variable nombre?"
    if nombre:
        st.success(f"¡Hola {nombre}! Bienvenido al mundo de los Agentes de IA.")
        st.balloons()  # ¡Efecto especial sorpresa!
    else:
        st.error("Por favor, escribe tu nombre primero.")
