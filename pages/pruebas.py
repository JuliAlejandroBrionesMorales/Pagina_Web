# LIBRERIAS 
import streamlit as st
from PIL import Image
import math

# Configurar la página
st.set_page_config(page_title="Sneakers Shop", page_icon=":sneaker:", layout="wide")

# CSS PARA CAMBIAR COLOR DE FONDO
page_bg_color = '''
<style>
    .stApp {
        background-color: #E0E0E0; /* Gris más oscuro */
    }
</style>
'''
st.markdown(page_bg_color, unsafe_allow_html=True)

# Encabezado
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

# HERO SECTION
st.markdown("""
    <div style="text-align: center;">
        <h1 class="header">Just <span class="highlight">Do It</span></h1>
        <p class="subheader">¡Descubre la diferencia con nuestras zapatillas 100% originales y de alta calidad: Vive la experiencia de llevarte a casa unas zapatillas excepcionales a un precio increíble.</p>
    </div>
    
""", unsafe_allow_html=True)

# BARRA DE LOGOS
st.markdown("""
    <div style="display: flex; justify-content: center; align-items: center; flex-wrap: wrap;">
        <img src="https://upload.wikimedia.org/wikipedia/commons/a/a6/Logo_NIKE.svg" width="100" style="margin: 10px;">
        <img src="https://upload.wikimedia.org/wikipedia/commons/2/20/Adidas_Logo.svg" width="100" style="margin: 10px;">
        <img src="https://th.bing.com/th/id/R.b4049b31f88c336c5a56325f84393742?rik=kdIFVZfk3usVjw&pid=ImgRaw&r=0" width="100" style="margin: 10px;">
        <img src="https://logos-world.net/wp-content/uploads/2020/04/Puma-Logo.png" width="100" style="margin: 10px;">
        <img src="https://th.bing.com/th/id/OIP.LUkdc8RvH1wyDVtuKtaRbQHaDI?rs=1&pid=ImgDetMain" width="100" style="margin: 10px;">
    </div>
""", unsafe_allow_html=True)

# TÍTULO PRODUCTOS
st.markdown("<h2 style='text-align: center; margin-top: 50px;'>Productos</h2>", unsafe_allow_html=True)

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

# Ajusta el número de columnas según el ancho de la pantalla
num_cols = st.slider('Número de columnas por fila', min_value=1, max_value=4, value=2)

# Agregamos estilos CSS para los recuadros
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

# Itera sobre los productos en grupos del tamaño `num_cols`
for i in range(0, len(productos), num_cols):
    cols = st.columns(num_cols)
    
    for j in range(num_cols):
        index = i + j
        if index < len(productos):
            producto = productos[index]
            with cols[j]:
                st.image(producto['image'], use_column_width=True)
                st.markdown(f"""
                    <div class="product-card">
                        <div class="product-name">{producto['name']}</div>
                        <div>Talla: {', '.join(map(str, producto['talla']))}</div>
                        <div class="product-price">S/ {producto['price']:.2f}</div>
                        <div>{"⭐" * producto['rating'] + "☆" * (5 - producto['rating'])}</div>
                    </div>
                """, unsafe_allow_html=True)


# Pie de página
st.markdown("""
    <div style="background-color: black; color: white; padding: 20px; margin-bottom: 0;">
        <div style="display: flex; justify-content: space-around; text-align: center; flex-wrap: wrap;">
            <div style="flex: 1; margin: 10px;">
                <h4 style="color: white;">Contacto</h4>
                <p style="color: white;">Telf: +51 962 793 952</p>
            </div>
            <div style="flex: 1; margin: 10px;">
                <h4 style="color: white;">Redes Sociales</h4>
                <p style="color: white;">FB: Sneakers Store</p>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# Pie de página
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
