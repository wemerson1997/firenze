import streamlit as st
import urllib.parse

hub_firenze = st.sidebar.selectbox(
    'Hub Firenze', ['E-mail', 'WhatsApp'], 0)

if hub_firenze == 'WhatsApp':
    # Função para gerar o link do WhatsApp
    def gerar_link_whatsapp(numero, texto):
        texto_codificado = urllib.parse.quote(texto)
        link = f"https://wa.me/{numero}?text={texto_codificado}"
        return link

    # Interface do Streamlit
    st.title("Gerador de Links de WhatsApp")

    # Entrada de número de telefone e mensagem
    numero = st.text_input("Digite o número de telefone (com código do país):", "41999957504")
    texto = st.text_input("Digite a mensagem:")

    # Quando o botão é clicado, gera o link
    if st.button("Gerar Link"):
        if numero and texto:
            link_whatsapp = gerar_link_whatsapp(numero, texto)
            st.success("Link gerado com sucesso!")
            st.write(f"[Clique aqui para enviar mensagem no WhatsApp]({link_whatsapp})")
        else:
            st.error("Por favor, insira tanto o número quanto a mensagem.")

    # Adicionando um link em uma palavra com HTML
    st.markdown("""
    ### Exemplo de Link em uma Palavra:
    Clique no link abaixo para visitar o Google:
    <a href="https://www.google.com" target="_blank">Google</a>
    """, unsafe_allow_html=True)


if hub_firenze == 'E-mail':
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