import streamlit as st

# Configurar la página
st.set_page_config(page_title="Sneakers Shop", page_icon=":sneaker:", layout="wide")

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
        <button style="background-color: red; color: white; border: none; padding: 10px 20px; border-radius: 5px;">Comprar</button>
    </div>
""", unsafe_allow_html=True)
st.write('')
st.write('')


# BARRA DE LOGOS 
st.image(["https://upload.wikimedia.org/wikipedia/commons/a/a6/Logo_NIKE.svg",
          "https://upload.wikimedia.org/wikipedia/commons/2/20/Adidas_Logo.svg",
          "https://th.bing.com/th/id/R.b4049b31f88c336c5a56325f84393742?rik=kdIFVZfk3usVjw&pid=ImgRaw&r=0",
          "https://logos-world.net/wp-content/uploads/2020/04/Puma-Logo.png",
          "https://th.bing.com/th/id/OIP.LUkdc8RvH1wyDVtuKtaRbQHaDI?rs=1&pid=ImgDetMain"], width=240)

st.markdown("<h2 style='text-align: center; margin-top: 50px;'>Productos</h2>", unsafe_allow_html=True)

# Lista de productos
productos = [
    {"name": "Nike Air Jordan 1 Elevate Low", "price": 560.00, "image": "https://via.placeholder.com/150", "rating": 4},
    {"name": "Adidas NMD_V3", "price": 500.00, "image": "https://via.placeholder.com/150", "rating": 5},
    {"name": "Nike Air Max Bolla TR 5 Premium - mujer", "price": 380.00, "image": "https://via.placeholder.com/150", "rating": 4},
    {"name": "Nike Air Max Dawn - mujer", "price": 160.00, "image": "https://via.placeholder.com/150", "rating": 3},
    {"name": "Nike Air Max SYSTM - mujer", "price": 340.00, "image": "https://via.placeholder.com/150", "rating": 4},
    {"name": "Nike Defy All Day", "price": 240.00, "image": "https://via.placeholder.com/150", "rating": 4},
    {"name": "Nike Downshifter 11 - Mujer", "price": 250.00, "image": "https://via.placeholder.com/150", "rating": 4},
    {"name": "Nike Dunk Low Next Nature - mujer", "price": 480.00, "image": "https://via.placeholder.com/150", "rating": 5},
    {"name": "Nike M2K Tekno - mujer", "price": 400.00, "image": "https://via.placeholder.com/150", "rating": 4},
    {"name": "Nike Quest 4 - mujer", "price": 300.00, "image": "https://via.placeholder.com/150", "rating": 4},
    {"name": "Nike Revolution 6 - mujer", "price": 230.00, "image": "https://via.placeholder.com/150", "rating": 4},
    {"name": "Nike Zapatillas Running Flex Runner PS - mujer", "price": 165.00, "image": "https://via.placeholder.com/150", "rating": 4},
]

cols = st.columns(4)
for index, producto in enumerate(productos):
    with cols[index % 4]:
        st.image(producto["image"], use_column_width=True)
        st.write(f"**{producto['name']}**")
        st.write(f"S/ {producto['price']:.2f}")
        st.write("⭐" * producto["rating"] + "☆" * (5 - producto["rating"]))


# Pie de página
st.markdown("""
    <hr>
    <div style="display: flex; justify-content: space-around; text-align: center;">
        <div>
            <h4>Contacto</h4>
            <p>Telf: +34 630 318 586</p>
        </div>
        <div>
            <h4>Redes Sociales</h4>
            <p>Facebook: Sneakers Store</p>
        </div>
        <div>
            <h4>¿Quienes Somos?</h4>
            <p>Somos un pequeño grupo de emprendedores que ofrecenn productos 100% originales y únicos.</p>
        </div>
        <div>
            <h4>WhatsApp</h4>
            <textarea id="message" placeholder="Escribenos un mensaje" style="width: 200px; height: 100px;"></textarea><br>
            <!-- Actualiza esta línea con tu número de WhatsApp -->
            <a id="whatsapp-link" href="https://wa.me/34630318586?text=" target="_blank"><button onclick="sendMessage()" style="background-color: red; color: white; border: none; padding: 10px 20px; border-radius: 5px;">Enviar</button></a>
        </div>
    </div>

    <script type="text/javascript">
        function sendMessage() {
            var message = document.getElementById('message').value;
            var whatsapp_url = "https://wa.me/34630318586?text=" + encodeURIComponent(message);
            document.getElementById('whatsapp-link').href = whatsapp_url;
        }
    </script>
""", unsafe_allow_html=True)
