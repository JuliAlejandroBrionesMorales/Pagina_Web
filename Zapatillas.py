# LIBRERIAS 
import streamlit as st
from PIL import Image, ExifTags
import base64
from io import BytesIO
import math


# ---------------------- CONFIGURACIÓN DE LA PÁGINA ---------------------- 
st.set_page_config(page_title="Sneakers Shop", page_icon=":sneaker:", layout="wide")


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
            color: red;
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
        <h1 class="header">Just <span class="highlight">Do It</span></h1>
        <p class="subheader">¡Descubre la diferencia con nuestras zapatillas 100% originales y de alta calidad: Vive la experiencia de llevarte a casa unas zapatillas excepcionales a un precio increíble.</p>
    </div>
    
""", unsafe_allow_html=True)


# ---------------------- BARRA DE LOGOS ----------------------
st.markdown("""
    <div style="display: flex; justify-content: center; align-items: center; flex-wrap: wrap;">
        <img src="https://upload.wikimedia.org/wikipedia/commons/a/a6/Logo_NIKE.svg" width="100" style="margin: 10px;">
        <img src="https://upload.wikimedia.org/wikipedia/commons/2/20/Adidas_Logo.svg" width="100" style="margin: 10px;">
        <img src="https://th.bing.com/th/id/R.b4049b31f88c336c5a56325f84393742?rik=kdIFVZfk3usVjw&pid=ImgRaw&r=0" width="100" style="margin: 10px;">
        <img src="https://logos-world.net/wp-content/uploads/2020/04/Puma-Logo.png" width="100" style="margin: 10px;">
        <img src="https://th.bing.com/th/id/OIP.LUkdc8RvH1wyDVtuKtaRbQHaDI?rs=1&pid=ImgDetMain" width="100" style="margin: 10px;">
    </div>
""", unsafe_allow_html=True)



# ---------------------- PRODUCTOS ----------------------- 
st.markdown("<h2 style='text-align: center; margin-top: 50px;'>Productos</h2>", unsafe_allow_html=True)

# Función para corregir la orientación de la imagen
def corregir_orientacion(image_path):
    image = Image.open(image_path)
    try:
        for orientation in ExifTags.TAGS.keys():
            if ExifTags.TAGS[orientation] == 'Orientation':
                break
        exif = image._getexif()
        if exif is not None:
            orientation = exif.get(orientation)
            if orientation == 3:
                image = image.rotate(180, expand=True)
            elif orientation == 6:
                image = image.rotate(270, expand=True)
            elif orientation == 8:
                image = image.rotate(90, expand=True)
    except (AttributeError, KeyError, IndexError):
        pass  # Si no hay metadatos EXIF, no se realiza ninguna rotación
    return image

# Convierte la imagen en base64
def imagen_a_base64(imagen):
    buffer = BytesIO()
    imagen.save(buffer, format="JPEG")
    imagen_str = base64.b64encode(buffer.getvalue()).decode("utf-8")
    return imagen_str

# Estilos CSS para los recuadros
st.markdown("""
    <style>
    .product-card {
        background-color: #f8f8f8;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
        text-align: center;
    }
    .product-image {
        border-radius: 10px;
        margin-bottom: 10px;
        width: 100%;
    }
    .product-name {
        font-weight: bold;
        margin-bottom: 10px;
    }
    .product-price {
        color: #FF5733;
        font-weight: bold;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)



# Lista de productos
productos = [
    {"name": "Nike Air Jordan 1 Elevate Low", "price": 560.00, "image": "images/IMG_7926.jpg", "talla": (42,41), "rating": 4},
    {"name": "Adidas NMD_V3", "price": 500.00, "image": "images/IMG_7929.jpg","talla": (42,41), "rating": 5},
    {"name": "Nike Air Max Bolla TR 5 Premium - mujer", "price": 380.00, "image": "images/IMG_7947.jpg","talla": (42,41), "rating": 4},
    {"name": "Nike Air Max Dawn - mujer", "price": 160.00, "image": "images/IMG_7946.jpg","talla": (42,41), "rating": 3},
    {"name": "Nike Air Max SYSTM - mujer", "price": 340.00, "image": "images/IMG_7943.jpg","talla": (42,41),"rating": 4},
    {"name": "Nike Defy All Day", "price": 240.00, "image": "images/IMG_7953.jpg","talla": (42,41), "rating": 4},
    {"name": "Nike Downshifter 11 - Mujer", "price": 250.00, "image": "images/IMG_7957.jpg","talla": (42,41), "rating": 4},
    {"name": "Nike Dunk Low Next Nature - mujer", "price": 480.00, "image": "images/IMG_7959.jpg","talla": (42,41), "rating": 5},
    {"name": "Nike M2K Tekno - mujer", "price": 400.00, "image": "images/IMG_7960.jpg","talla": (42,41),"rating": 4},
    {"name": "Nike Quest 4 - mujer", "price": 300.00, "image": "images/IMG_7963.jpg", "talla": (42,41),"rating": 4},
    {"name": "Nike Revolution 6 - mujer", "price": 230.00, "image": "images/IMG_7966.jpg","talla": (42,41), "rating": 4},
    {"name": "Nike Zapatillas Running Flex Runner PS - mujer", "price": 165.00, "image": "images/IMG_7967.jpg","talla": (42,41), "rating": 4},
]

# Número de columnas para la visualización
num_cols = 1

# Itera sobre los productos en grupos del tamaño `num_cols`
for i in range(0, len(productos), num_cols):
    # Crea una nueva fila de columnas
    cols = st.columns(num_cols)
    
    # Itera sobre los productos en este grupo
    for j in range(num_cols):
        # Calcula el índice actual del producto
        index = i + j
        
        # Verifica que el índice no exceda el número de productos
        if index < len(productos):
            producto = productos[index]
            with cols[j]:
                # Corrige la orientación de la imagen antes de mostrarla
                imagen_corregida = corregir_orientacion(producto['image'])
                
                # Convierte la imagen corregida a base64
                imagen_base64 = imagen_a_base64(imagen_corregida)
                
                # Mostrar la imagen y la descripción estilizada en un recuadro
                st.markdown(f"""
                    <div class="product-card">
                        <img src="data:image/jpeg;base64,{imagen_base64}" class="product-image"/>
                        <div class="product-name">{producto['name']}</div>
                        <div>Talla: {', '.join(map(str, producto['talla']))}</div>
                        <div class="product-price">S/ {producto['price']:.2f}</div>
                        <div>{"⭐" * producto['rating'] + "☆" * (5 - producto['rating'])}</div>
                    </div>
                """, unsafe_allow_html=True)



# ---------------------- PIE DE PÁGINA ---------------------- 
st.markdown("""
    <div style="background-color: black; color: white; padding: 20px; margin-bottom: 0;">
        <div style="display: flex; justify-content: space-around; text-align: center; flex-wrap: wrap;">
            <div style="flex: 1; margin: 10px;">
                <h4 style="color: white;">Contacto</h4>
                <p style="color: white;">Telf: +51 962 793 952</p>
            </div>
            <div style="flex: 1; margin: 10px;">
                <h4 style="color: white;">Redes Sociales</h4>
                <p style="color: white;">Facebook: Sneakers Store</p>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)


st.markdown("""
    <div style="background-color: black; color: white; padding: 20px; margin-top: 0;">
        <div style="display: flex; justify-content: space-around; text-align: center; flex-wrap: wrap;">
            <div style="flex: 1; margin: 10px;">
                <h4 style="color: white;">¿Quienes Somos?</h4>
                <p style="color: white;">Somos un pequeño grupo de emprendedores.</p>
            </div>
            <div style="flex: 1; margin: 10px;">
                <h4 style="color: white;">
                    <img src="https://logodownload.org/wp-content/uploads/2015/04/whatsapp-logo-icone.png" alt="WhatsApp Logo" style="width:20px; height:20px; vertical-align:middle; margin-right:5px;">
                    WhatsApp
                </h4>
                <a id="whatsapp-link" href="https://wa.me/51962793952?text=" target="_blank">
                    <button onclick="sendMessage()" style="background-color: green; color: white; border: none; padding: 10px 20px; border-radius: 5px;">Envíanos un mensaje</button>
                </a>
            </div>
        </div>
    </div>

    <script type="text/javascript">
        function sendMessage() {
            var message = document.getElementById('message').value;
            var whatsapp_url = "https://wa.me/51962793952?text=" + encodeURIComponent(message);
            document.getElementById('whatsapp-link').href = whatsapp_url;
        }
    </script>
""", unsafe_allow_html=True)
