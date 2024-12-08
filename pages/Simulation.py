import streamlit as st


st.set_page_config(
    layout="wide",
    page_title="Simulation", page_icon="🚀"
    )

# Agregar Google Fonts (Poppins) y aplicar los estilos personalizados
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
    
    /* Aplicar la fuente Poppins a todo el cuerpo */
    body {
        font-family: 'Poppins', sans-serif;
    }

    /* Aplicar la fuente Poppins específicamente a los párrafos */
    p {
        font-family: 'Poppins', sans-serif !important;
    }

    .st-do {
        background-color: #f8f9fa !important;
    }

    .st-e5 {
        background-color: #f8f9fa !important;
    }

    /* Sobrescribir los estilos específicos de los elementos generados por Emotion y Streamlit */
    .stApp, 
    .st-emotion-cache, 
    .st-emotion-cache-global, 
    .css-1v0yizf, 
    .stMarkdown,
    .stMarkdown p, 
    .stMarkdown h1, 
    .stMarkdown h2, 
    .stMarkdown h3, 
    .stMarkdown h4, 
    .stMarkdown h5, 
    .stMarkdown h6 {
        font-family: 'Poppins', sans-serif !important;
    }

    /* Encabezados en azul */
    h1, h2, h3, h4, h5, h6 {
        color: #001978;  /* Azul (ajustar según el tema) */
    }

    </style>
    """, 
    unsafe_allow_html=True
)


# Función para mostrar etiqueta con ahorro de tiempo y pasos
def mostrar_etiqueta(tiempo_ahorrado, pasos_eliminados, detalles_pasos):
    st.markdown(
        f"""
        <div style="display: inline-block; margin-left: 10px; padding: 5px; background-color: #f9f9f9; border: 1px solid #ddd; border-radius: 5px;">
            <strong>Beneficio:</strong> Ahorro de {tiempo_ahorrado}, eliminando {pasos_eliminados} pasos manuales.
            <br><strong>Detalles de los pasos ahorrados:</strong><br>{detalles_pasos}
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("### Simulación escenario Derecho Civil")

# Comparación de caso sin y con la Suite AI Legal 360°
col1, col2 = st.columns(2)

# Historia sin Suite AI Legal 360° (izquierda)
with col1:
    st.markdown("##### Flujo de trabajo actual")
    st.write("""
    **María García**, buscando información sobre negligencia médica, encuentra el perfil del despacho en redes sociales, pero la gestión del despacho es manual y poco eficiente.
    
    **Pasos del proceso:**
    1. **Captación del cliente:** El despacho realiza publicaciones manuales sobre negligencia médica en redes sociales y responde individualmente a las interacciones.
    2. **Agendamiento de cita:** María tiene que contactar manualmente con el despacho para fijar la cita. El despacho coordina los horarios a través de mensajes o llamadas telefónicas.
    3. **Preparación para la consulta:** El despacho recopila información de María de forma manual a través de correos electrónicos y formularios, sin automatización para organizar los documentos.
    4. **Consulta inicial:** El abogado recibe la información manualmente y no tiene un sistema que agilice el proceso de consulta.
    5. **Investigación y recopilación de pruebas:** La investigación y la recopilación de pruebas es completamente manual.
    6. **Redacción y presentación de la demanda:** El abogado redacta la demanda y la presenta manualmente.
    7. **Encuesta de satisfacción:** Se envía manualmente a través de correos electrónicos sin personalización.
    8. **Fidelización:** El despacho envía correos manualmente para seguir en contacto con los clientes y mantener su lealtad.
    
    **Desventajas de este proceso:**
    - Mayor tiempo invertido en tareas manuales.
    - Posibilidad de errores humanos.
    - Falta de eficiencia en la coordinación y comunicación con los clientes.
    """)

# Historia con Suite AI Legal 360° (derecha)
with col2:
    st.markdown("##### Usando la Suite AI Legal 360°")
    st.write("""
    **María García**, al buscar información sobre negligencia médica, encuentra el perfil del despacho, que utiliza la Suite AI Legal 360° para gestionar cada parte del proceso de manera eficiente.

    **Pasos del proceso con la suite:**
    1. **Captación del cliente:** La Suite AI Lead Booster crea publicaciones automáticas sobre negligencia médica y responde automáticamente a las interacciones de los clientes.
    2. **Agendamiento de cita:** El sistema AI Booking contacta a María a través de WhatsApp, ofrece horarios disponibles y coordina automáticamente la cita.
    3. **Preparación para la consulta:** Alerta Legal 360° extrae automáticamente la información relevante de los correos electrónicos y organiza los documentos necesarios.
    4. **Consulta inicial:** El abogado accede a la información organizada y preparada por la suite, lo que permite una consulta más eficiente.
    5. **Investigación y recopilación de pruebas:** La Suite AI organiza y recopila automáticamente pruebas y documentos necesarios, ahorrando tiempo y esfuerzo.
    6. **Redacción y presentación de la demanda:** La Suite facilita la redacción de la demanda y su presentación automatizada.
    7. **Encuesta de satisfacción:** Se envía automáticamente una encuesta personalizada a María para medir su satisfacción.
    8. **Fidelización:** La Suite AI envía correos electrónicos automatizados de fidelización, recordatorios y contenidos relevantes.
    
    **Ventajas de este proceso con la Suite AI Legal 360°:**
    - Ahorro significativo de tiempo.
    - Reducción de errores humanos.
    - Mejora en la eficiencia y la experiencia del cliente.
    """)

st.markdown("---") 

# Continuación con el flujo de la simulación
# Paso 1: Captación de Lead
st.markdown("##### 1. Captación de María García como cliente potencial (Lead)")
st.write("""
María, buscando información sobre negligencia médica, encuentra el perfil del despacho en redes sociales. Este perfil, gestionado con AI Lead Booster, publica contenido atractivo generado automáticamente.
Ejemplos de contenido:
- Publicaciones con consejos para identificar una posible negligencia médica.
- Testimonios de clientes satisfechos que han ganado sus casos.
""")
st.write("""
María interactúa con una publicación, mostrando interés. Un AI Agent inicia una conversación automatizada, ofreciendo información adicional y la posibilidad de agendar una consulta gratuita. María proporciona sus datos de contacto, convirtiéndose en un lead para el despacho.
""")
if st.button("Crear automatización", key="lead"):
    st.success("Automatización para captación de clientes creada exitosamente.")
mostrar_etiqueta("2 horas por cliente", "3 pasos", "- Redacción de publicaciones manualmente\n- Publicación manual de contenido en redes sociales\n- Seguimiento manual de interacciones")
st.markdown("<br>", unsafe_allow_html=True)

# Paso 2: Gestión de la cita
st.markdown("##### 2. Gestión de la cita con AI Booking")
st.write("""
El AI Agent de AI Booking contacta a María por WhatsApp para agendar la consulta. Ofrece horarios disponibles, evita dobles reservas y sincroniza el calendario automáticamente.
""")
if st.button("Crear automatización", key="booking"):
    st.success("Automatización para gestión de citas creada exitosamente.")
mostrar_etiqueta("1 hora por cita", "2 pasos", "- Contacto manual con el cliente para agendar la cita\n- Coordinación manual de horarios para evitar dobles reservas")
st.markdown("<br>", unsafe_allow_html=True)

# Paso 3: Preparación para la consulta
st.markdown("##### 3. Preparación para la consulta con Alerta Legal 360°")
st.write("""
Al recibir el correo electrónico de María confirmando la cita, Alerta Legal 360° extrae información clave: nombre del doctor, clínica, fecha de la cirugía, etc. También envía correos automatizados con listas de documentos necesarios.
""")
if st.button("Crear automatización", key="alerta"):
    st.success("Automatización para preparación de consultas creada exitosamente.")
mostrar_etiqueta("1.5 horas por consulta", "4 pasos", "- Revisión manual de los correos electrónicos para confirmar la cita\n- Creación manual de listas de documentos\n- Envío manual de correos electrónicos con la lista de documentos\n- Organización manual de la información del cliente")
st.markdown("<br>", unsafe_allow_html=True)

# Paso 4: Investigación y recopilación de pruebas
st.markdown("##### 4. Investigación y recopilación de pruebas")
st.write("""
El abogado lleva a cabo la investigación del caso, recopilando pruebas necesarias, como registros médicos y declaraciones.
""")
mostrar_etiqueta("2.5 horas por cliente", "5 pasos", "- Búsqueda manual de documentos y pruebas\n- Contacto manual con entidades externas para obtener información\n- Revisión manual de registros médicos y declaraciones\n- Organización de la información recopilada\n- Clasificación manual de los documentos necesarios")
st.markdown("<br>", unsafe_allow_html=True)

# Paso 5: Redacción y presentación de la demanda
st.markdown("##### 5. Redacción y presentación de la demanda")
st.write("""
Con la información reunida, el abogado redacta la demanda y la presenta ante la corte.
""")
mostrar_etiqueta("3 horas por cliente", "6 pasos", "- Redacción manual de la demanda\n- Revisión manual de la demanda antes de su presentación\n- Presentación física de la demanda ante la corte\n- Coordinación manual con el equipo legal para asegurar que todos los datos estén correctos\n- Preparación de copias de la demanda para la corte\n- Envío manual de la demanda a los involucrados")
st.markdown("<br>", unsafe_allow_html=True)

# Paso 6: Feedback del cliente
st.markdown("##### 6. Customer Feedback 360° para evaluar la experiencia de María")
st.write("""
María recibe una encuesta automatizada que mide su satisfacción. Si es positiva, se genera una invitación para dejar una reseña en Google. Si es negativa, el equipo se comunica con ella para mejorar su experiencia.
""")
if st.button("Crear automatización", key="feedback"):
    st.success("Automatización para encuestas de satisfacción creada exitosamente.")
mostrar_etiqueta("30 minutos por cliente", "2 pasos", "- Creación manual de encuestas de satisfacción\n- Envío manual de encuestas al cliente")
st.markdown("<br>", unsafe_allow_html=True)

# Paso 7: Fidelización del cliente
st.markdown("##### 7. Lead Nurturing para fidelizar a María")
st.write("""
María recibe correos electrónicos personalizados con:
- Información relevante sobre sus derechos.
- Consejos para prevenir negligencias.
- Ofertas para futuras consultas.
""")
if st.button("Crear automatización", key="nurturing"):
    st.success("Automatización para fidelización creada exitosamente.")
mostrar_etiqueta("1 hora por cliente", "3 pasos", "- Envío manual de correos electrónicos\n- Creación manual de contenido personalizado\n- Seguimiento manual de clientes para mantenerlos leales")
st.markdown("<br>", unsafe_allow_html=True)

# st.write("¡Todo el proceso de gestión de casos con la Suite AI Legal 360° ha sido automatizado!")


