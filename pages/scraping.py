import streamlit as st
import requests
from bs4 import BeautifulSoup
from openpyxl import load_workbook, Workbook
import io


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

# Configuración de la aplicación
st.markdown("#### Buscador de Palabras Clave en Sitios Web")

# Entrada de palabras clave
keywords_input = st.text_input("Palabras clave (separadas por comas)", "denuncias, canal de denuncias, canal, canal ético, compliance")
keywords = [kw.strip().lower() for kw in keywords_input.split(",")]

# Subir archivo Excel
uploaded_file = st.file_uploader("Sube tu archivo Excel", type=["xlsx"])

# Configuración de columna
selected_column = st.text_input("Nombre de la columna de links", "WEBSITE")

# Botón de ejecución
if st.button("Ejecutar búsqueda") and uploaded_file and selected_column:
    try:
        # Cargar archivo
        workbook = load_workbook(uploaded_file)
        sheet = workbook.active

        # Buscar la columna seleccionada
        website_column_index = None
        for cell in sheet[1]:
            if cell.value == selected_column:
                website_column_index = cell.column
                break

        if not website_column_index:
            st.error(f"Columna '{selected_column}' no encontrada.")
            st.stop()

        # Añadir columna de resultados
        result_col_index = sheet.max_column + 1
        sheet.cell(row=1, column=result_col_index, value="Resultado")

        # Lista de logs en tiempo real
        logs = st.empty()

        # Procesar cada URL
        for row in range(2, sheet.max_row + 1):
            url = sheet.cell(row=row, column=website_column_index).value
            if url:
                if not url.startswith("http"):
                    url = f"https://{url}"
                try:
                    response = requests.get(url, timeout=10)
                    response.raise_for_status()
                    soup = BeautifulSoup(response.content, "html.parser")
                    text = soup.get_text().lower()

                    # Buscar palabras clave
                    found = False
                    for keyword in keywords:
                        if keyword in text:
                            link = soup.find('a', string=lambda text: text and keyword in text.lower())
                            link_href = link['href'] if link else 'Link no encontrado'
                            sheet.cell(row=row, column=result_col_index, value=link_href)
                            logs.info(f"✔️ Palabra clave '{keyword}' encontrada en {url}")
                            found = True
                            break

                    if not found:
                        sheet.cell(row=row, column=result_col_index, value="Palabras clave no encontradas")
                        logs.warning(f"⚠️ No se encontraron palabras clave en {url}")

                except requests.exceptions.RequestException as e:
                    sheet.cell(row=row, column=result_col_index, value=f"Error al acceder: {e}")
                    logs.error(f"❌ Error al acceder a {url}: {e}")
                except Exception as e:
                    sheet.cell(row=row, column=result_col_index, value=f"Error inesperado: {e}")
                    logs.error(f"❌ Error inesperado en {url}: {e}")
            else:
                sheet.cell(row=row, column=result_col_index, value="URL vacía")
                logs.warning(f"⚠️ URL vacía en la fila {row}")

        # Guardar archivo en memoria
        output = io.BytesIO()
        workbook.save(output)
        output.seek(0)

        # Descargar archivo procesado
        st.success("Archivo procesado con éxito.")
        st.download_button(
            label="Descargar archivo procesado",
            data=output,
            file_name="output_with_results.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

    except Exception as e:
        st.error(f"Ocurrió un error: {e}")
