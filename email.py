import streamlit as st

def generate_message(nome, email, endereco, link_endereco, link_whatsapp):
    message = f"""Oi, {nome},
tudo bem? Aqui é Wemerson da Firenze Imóveis, recebi seu e-mail referente ao imóvel em [{endereco}]({link_endereco}), só passando para informar que esse imóvel enctra-se reservado.
A reserva do imóvel não garante a locação, pra ter mais informações e um atendimento mais rápido, envie uma mensagem clicando no nosso [WhatsApp]({link_whatsapp}) Aguardo o seu contato :)"""
    return message

st.title("Gerador de Mensagem Imobiliária")
nome = st.text_input("Nome")
email = st.text_input("E-mail")
endereco = st.text_input("Endereço")
link_endereco = st.text_input("Link do imóvel")
link_whatsapp = st.text_input("Link do WhatsApp")

if st.button("Gerar Mensagem"):
    if nome and email and endereco and link_endereco and link_whatsapp:
        message = generate_message(nome, email, endereco, link_endereco, link_whatsapp)
        st.markdown(message)

        st.subheader("Prévia da message:")
        st.write("Oi, " + nome)
        st.write("Tudo bem? Recebemos seu e-mail reference ao imóvel em ", end="")
        st.markdown(f"[{endereco}]({link_endereco})", unsafe_allow_html=True)
        st.write(", esse imóvel está disponível para visitas :)")
        st.write("Para um atendimento mais rápido, envie uma mensagem para o nosso ", end="")
        st.markdown(f"[WhatsApp]({link_whatsapp})", unsafe_allow_html=True)
        st.write(" :)")
        st.write("\n \n At.te Wemerson")
    else:
        st.error("Por favor, preencha todos os campos.")