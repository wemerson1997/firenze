import streamlit as st
import qrcode
from PIL import Image
import io

def generate_qr_code(data):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    return img

def main():
    st.title("Gerador de QR Code")

    # Campo de entrada para o texto ou URL
    data = st.text_input("Digite o texto ou URL para gerar o QR Code:")

    if st.button("Gerar QR Code"):
        if data:
            qr_image = generate_qr_code(data)

            # Convertendo a imagem para bytes
            img_byte_arr = io.BytesIO()
            qr_image.save(img_byte_arr, format='PNG')
            img_byte_arr = img_byte_arr.getvalue()

            # Exibindo o QR Code
            st.image(img_byte_arr, caption='QR Code gerado', use_column_width=True)

            # Botão para download
            st.download_button(
                label="Baixar QR Code",
                data=img_byte_arr,
                file_name="qr_code.png",
                mime="image/png"
            )
        else:
            st.warning("Por favor, insira um texto ou URL para gerar o QR Code.")

if __name__ == "__main__":
    main()