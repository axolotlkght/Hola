import streamlit as st 
# 'import' trae la *Librería* (las herramientas prestadas) a tu proyecto.

# 1. El Título y Textos
st.title("🤠 Hi you awesome girl! :)")
st.write("So it turns out that I learnt something interesting today!")
st.write("I hope you had a chill and amazing day.")




# 2. Interactividad con *Widgets* (Elementos visuales como botones o cajas de texto)
# Aquí creamos una *Variable* (una caja con nombre para guardar datos) llamada 'nombre'.

nombre = st.text_input("Now just for the sake of this small thing, write your name please")

# 3. El Botón y la *Lógica Condicional* (Si pasa esto, haz aquello)
if st.button("Fine"):
    # 'if' pregunta: "¿Hay algo guardado en la variable nombre?"
    if nombre:
        st.success(f"¡Hola {nombre}! I just wanted to let you know that I think you're so bonita!")
        st.balloons()  # ¡Efecto especial sorpresa!
    else:
        st.error("Please say your name")
