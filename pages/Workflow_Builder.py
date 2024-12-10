
import streamlit as st
import requests
import json
from datetime import datetime
import graphviz

# API Key predefinida (oculta)
api_key_default = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MjY4ZDg5My1jMWUzLTRkMDktOGQ1OC1lMzBiNTg5MmQ1NDAiLCJpc3MiOiJuOG4iLCJhdWQiOiJwdWJsaWMtYXBpIiwiaWF0IjoxNzMzNDE4Nzg0fQ.bzkVpmCpAcuTh3lYalIG2reEtjxzCakHVQHFAWNuiWA"

# # Interfaz de Streamlit

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

# Descripción inicial
st.subheader("Ejemplo de creación de servicio Lead Nurturing")
st.write("""
Este proceso es parte de la Suite AI 360º, que gestiona el flujo de leads para clientes legales. 
En este flujo, gestionaremos el proceso de comunicación con los leads, utilizando WhatsApp y notificaciones móviles mediante la API de Ntfy.
""")

st.write("""
1. **Nodo de WhatsApp**: Recibe los mensajes de los leads a través de la API de WhatsApp.
2. **AI Agent (LLM)**: Procesa el mensaje recibido y genera una respuesta automática utilizando la inteligencia artificial de Google Gemini.
3. **Memoria Buffer**: Guarda el contexto y las conversaciones previas para mantener la coherencia en la interacción.
4. **Notificación Móvil (Ntfy)**: Si se activa, envía una notificación móvil a los responsables con el resumen de la conversación.

""")

# Entrada del usuario para el nombre del workflow (solo el nombre, sin fecha visible)
nombre_workflow = st.text_input("Nombre del Workflow:", "")

# Si no se ha proporcionado un nombre, se agrega la fecha y hora automáticamente
if not nombre_workflow:
    nombre_workflow = f"AI agent Whatsapp real time {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

# Switch para activar notificación móvil
activar_notificacion = st.checkbox("¿Activar notificación móvil?", value=False)

# Definición del workflow
workflow_data = {
    "name": nombre_workflow,
    "nodes": [
        {
            "parameters": {
                "sessionIdType": "customKey",
                "sessionKey": "{{ $json.body.data.message.conversation }}"
            },
            "id": "372777e8-ce90-4dea-befc-ac1b2eb4729f",
            "name": "Window Buffer Memory",
            "type": "@n8n/n8n-nodes-langchain.memoryBufferWindow",
            "position": [540, 520],
            "typeVersion": 1.2
        },
        {
            "parameters": {
                "options": {}
            },
            "id": "a7624108-e3da-4193-a625-887314216b8b",
            "name": "When chat message received",
            "type": "@n8n/n8n-nodes-langchain.chatTrigger",
            "position": [-420, 460],
            "webhookId": "53c136fe-3e77-4709-a143-fe82746dd8b6",
            "typeVersion": 1.1
        },
        {
            "parameters": {
                "options": {}
            },
            "id": "3468894a-7f3b-47ca-ae1a-89cc6c695334",
            "name": "Google Gemini Chat Model",
            "type": "@n8n/n8n-nodes-langchain.lmChatGoogleGemini",
            "typeVersion": 1,
            "position": [360, 520],
            "credentials": {
                "googlePalmApi": {
                    "id": "gT9857NZIEXLaQ2C",
                    "name": "Google Gemini(PaLM) Api account"
                }
            }
        },
        {
            "parameters": {
                "resource": "messages-api",
                "instanceName": "alb1",
                "remoteJid": "={{ $('Webhook').item.json.body.data.key.remoteJid }}",
                "messageText": "={{ $json.output }}"
            },
            "id": "edcfa0d5-1712-41c1-ae4a-ef619d251593",
            "name": "Evolution API",
            "type": "n8n-nodes-evolution-api.httpBin",
            "typeVersion": 1,
            "position": [1040, 340],
            "credentials": {
                "httpbinApi": {
                    "id": "ZdZh2hzU1FK9IpEm",
                    "name": "Evolution account"
                }
            }
        },
        {
            "parameters": {
                "promptType": "define",
                "text": "={{ $json.body.data.message.conversation }}",
                "options": {}
            },
            "id": "6b8b7de8-fe3f-43b5-97ce-a52a9e44eb5e",
            "name": "AI Agent",
            "type": "@n8n/n8n-nodes-langchain.agent",
            "position": [360, 280],
            "typeVersion": 1.6
        },
        {
            "parameters": {
                "httpMethod": "POST",
                "path": "76fe60dc-83e1-4bd0-be5c-84559e2fc234",
                "options": {}
            },
            "id": "36d78e64-1f0c-483c-89e6-dd4773eed5e6",
            "name": "Webhook",
            "type": "n8n-nodes-base.webhook",
            "typeVersion": 2,
            "position": [-240, 260],
            "webhookId": "76fe60dc-83e1-4bd0-be5c-84559e2fc234"
        }
    ],
    "connections": {
        "Google Gemini Chat Model": {
            "ai_languageModel": [
                [
                    {
                        "node": "AI Agent",
                        "type": "ai_languageModel",
                        "index": 0
                    }
                ]
            ]
        },
        "Window Buffer Memory": {
            "ai_memory": [
                [
                    {
                        "node": "AI Agent",
                        "type": "ai_memory",
                        "index": 0
                    }
                ]
            ]
        },
        "AI Agent": {
            "main": [
                [
                    {
                        "node": "Evolution API",
                        "type": "main",
                        "index": 0
                    },
                    {
                        "node": "HTTP Request",
                        "type": "main",
                        "index": 0
                    }
                ]
            ]
        },
        "Webhook": {
            "main": [
                [
                    {
                        "node": "AI Agent",
                        "type": "main",
                        "index": 0
                    }
                ]
            ]
        }
    },
    "settings": {}
}

# Si se activa la notificación, agregamos el nodo correspondiente
if activar_notificacion:
    workflow_data["nodes"].append({
        "parameters": {
            "method": "POST",
            "url": "https://ntfy.sh/albtest",
            "sendHeaders": True,
            "headerParameters": {
                "parameters": [
                    {"name": "Content-Type", "value": "text/plain; charset=utf-8:"},
                    {"name": "Click", "value": "https://lefebvre.es"},
                    {"name": "Actions", "value": "http, Contactar, https://webhook.demo.com"}
                ]
            },
            "sendBody": True,
            "contentType": "raw",
            "body": "=Nuevo Lead de Alto Valor  Un posible cliente ha solicitado información sobre tus servicios legales. Contáctalo ahora. 📞\nEl Usuario pregunta: {{ $('Webhook').item.json.body.data.message.conversation }}\nEl agente contesta: {{ $json.output }}",
            "options": {}
        },
        "id": "8175fd91-fa70-4353-9c2d-b01ad7d7a18f",
        "name": "HTTP Request",
        "type": "n8n-nodes-base.httpRequest",
        "typeVersion": 4.2,
        "position": [1400, 660]
    })

    # También agregamos la conexión de este nodo de notificación
    workflow_data["connections"]["HTTP Request"] = {
        "main": [
            [
                {
                    "node": "Webhook",
                    "type": "main",
                    "index": 0
                }
            ]
        ]
    }

# Interfaz de Streamlit
# activar_notificacion = st.checkbox("¿Activar notificación móvil?", value=False)

# Crear el flujo de trabajo básico sin Push Notifications
dot = graphviz.Digraph()

# Definir los nodos y conexiones
dot.node('Lead', 'Lead')
dot.node('AI Agent', 'AI Agent')
dot.node('LLM Model', 'LLM Model')
dot.node('Whatsapp API', 'Whatsapp API')

dot.edge('Lead', 'AI Agent')
dot.edge('AI Agent', 'LLM Model')
dot.edge('AI Agent', 'Whatsapp API')
dot.edge('Whatsapp API', 'Lead')

# Agregar Push Notifications si se activa la opción
if activar_notificacion:
    dot.node('Push Notifications', 'Push Notifications')
    dot.node('User', 'User')
    dot.edge('AI Agent', 'Push Notifications')
    dot.edge('Push Notifications', 'User')

# Mostrar el gráfico en Streamlit
st.graphviz_chart(dot)

# Botón de acción
if st.button("Insertar Workflow"):
    if api_key_default and nombre_workflow:
        url = "http://localhost:5678/api/v1/workflows/"
        headers = {
            'Content-Type': 'application/json',
            'X-N8N-API-KEY': api_key_default
        }
        try:
            response = requests.post(url, headers=headers, data=json.dumps(workflow_data))
            
            # Verificar si la respuesta fue exitosa
            if response.status_code == 200:
                workflow_id = response.json().get("id")  # Obtenemos el ID del workflow creado
                link = f"http://localhost:5678/workflow/{workflow_id}"  # Creamos el link para acceder al workflow
                st.success(f"Workflow creado con éxito: [Abrir en n8n]({link})")  # Mostrar el link para visitar el workflow
                st.write(f"ID del Workflow: {workflow_id}")  # Mostrar el ID del workflow
            else:
                st.error(f"Error al crear el workflow: {response.text}")

        
        except requests.exceptions.RequestException as e:
            # Si ocurre un error en la solicitud, mostrar un mensaje controlado
            st.error("En estos momentos el servicio no está activo. Por favor, inténtelo más tarde.")
    else:
        st.warning("Por favor, introduce el nombre del workflow.")




url = "http://localhost:5678/api/v1/workflows"

# Headers para la API
headers = {
    'Content-Type': 'application/json',
    'X-N8N-API-KEY': api_key_default
}

# Interfaz de Streamlit
st.title("Gestión de Workflow")
workflow_id = st.text_input("ID del Workflow", "")

# Botón para activar el workflow
if st.button("Activar Workflow"):
    if workflow_id:
        response = requests.post(
            f"{url}/{workflow_id}/activate",
            headers=headers
        )
        if response.status_code == 200:
            st.success("Workflow activado con éxito.")
        else:
            st.error(f"Error al activar: {response.text}")
    else:
        st.warning("Por favor, introduce un ID de Workflow válido.")

# Botón para desactivar el workflow
if st.button("Desactivar Workflow"):
    if workflow_id:
        response = requests.post(
            f"{url}/{workflow_id}/deactivate",
            headers=headers
        )
        if response.status_code == 200:
            st.success("Workflow desactivado con éxito.")
        else:
            st.error(f"Error al desactivar: {response.text}")
    else:
        st.warning("Por favor, introduce un ID de Workflow válido.")

        