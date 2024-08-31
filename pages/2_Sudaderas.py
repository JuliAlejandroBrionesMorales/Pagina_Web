# LIBRERIAS 
import streamlit as st
from PIL import Image, ExifTags
import base64
from io import BytesIO
import math


# ---------------------- CONFIGURACIÓN DE LA PÁGINA ---------------------- 
st.set_page_config(page_title="Sudaderas y Camisetas", page_icon="👕", layout="wide")


# ---------------------- CSS PARA CAMBIAR COLOR DE FONDO ---------------------- 
page_bg_color = '''
<style>
    .stApp {
        background-color: #E0E0E0; /* Gris más oscuro */
    }
</style>
'''
st.markdown(page_bg_color, unsafe_allow_html=True)



# ---------------------- ENCABEZADO ---------------------- 
st.markdown("""
    <style>
        .header {
            font-size: 60px;
            font-weight: bold;
            color: #333;
            margin-bottom: 20px;
            text-align: center;
        }
        .subheader {
            font-size: 20px;
            color: #666;
            text-align: center;
            margin-bottom: 50px;
        }
        .highlight {
            color: brown;
            font-weight: bold;
        }
        .btn {
            display: block;
            width: 150px;
            margin: 0 auto;
            padding: 10px;
            background-color: red;
            color: black;  /* Cambia el color del texto a negro */
            text-align: center;
            font-weight: bold;
            border-radius: 5px;
            text-decoration: none;
        }
        .btn:hover {
            background-color: #ff4c4c;
        }
    </style>
""", unsafe_allow_html=True)



# ---------------------- HERO SECTION ---------------------- 
st.markdown("""
    <div style="text-align: center;">
        <h1 class="header">Sudaderas y Camisetas <span class="highlight">personalizables</span></h1>
        <p class="subheader">
        Bienvenido a este pequeño emprendimiento, tu destino para <span class="highlight">sudaderas y camisetas personalizadas.</span></h1>
        Elige talla, modelo, color y añade tu propio diseño para crear una prenda única. Ofrecemos calidad premium, personalización total y entrega rápida. 
        ¡Empieza a diseñar hoy mismo y haz que tu ropa hable por ti!
        </p>
        
    </div>
    
""", unsafe_allow_html=True)



# ---------------------- PRODUCTOS ----------------------- 
st.markdown("<h2 style='text-align: center; margin-top: 50px;'>Muestras </h2>", unsafe_allow_html=True)