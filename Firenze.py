import streamlit as st
import urllib.parse


hub_firenze = st.sidebar.selectbox(
    'Hub Firenze', ['WhatsApp', 'Imóvel reservado', 'Imóvel disponível', 'Imóvel indisponível', 'NFS-e Curitiba'], 0)

if hub_firenze == 'WhatsApp':
    # Função para gerar o link do WhatsApp
    def gerar_link_whatsapp(numero, texto):
        texto_codificado = urllib.parse.quote(texto)
        link = f"https://wa.me/{numero}?text={texto_codificado}"
        return link

    # Interface do Streamlit
    st.title("Gerador de Links de WhatsApp")

    # Entrada de número de telefone e mensagem
    numero = st.text_input("Digite o número de telefone (com código do país):", "41995465023")
    texto = st.text_input("Digite a mensagem:", 'Oi, gostaria de mais informações sobre esse imóvel: ')

    # Quando o botão é clicado, gera o link
    if st.button("Gerar Link"):
        if numero and texto:
            link_whatsapp = gerar_link_whatsapp(numero, texto)
            st.success("Link gerado com sucesso!")
            st.write(f"[Clique aqui para enviar mensagem no WhatsApp]({link_whatsapp})")
        else:
            st.error("Por favor, insira tanto o número quanto a mensagem.")

    # Adicionando um link em uma palavra com HTML
    #st.markdown("""
    ### Exemplo de Link em uma Palavra:
    #Clique no link abaixo para visitar o Google:
    #<a href="https://www.google.com" target="_blank">Google</a>
    #""", unsafe_allow_html=True)


if hub_firenze == 'Imóvel reservado':
    def generate_message(nome, email, endereco, link_endereco, link_whatsapp):
        message = f"""Oi, **{nome}**,
        tudo bem?\n Aqui é **Wemerson da Firenze Imóveis**, recebi seu e-mail referente ao imóvel em [{endereco}]({link_endereco}), só passando para informar que esse imóvel encontra-se reservado.
        A reserva do imóvel não garante a locação, para ter mais informações e um atendimento mais rápido, envie uma mensagem clicando no nosso [WhatsApp]({link_whatsapp}) \n Aguardo o seu contato!"""
        return message

    st.title("Mensagem para imóvel reservado")
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

if hub_firenze == 'Imóvel disponível':
    def generate_message(nome, email, endereco, link_endereco, link_whatsapp,Colaborador):
        message = f"""Oi, **{nome}**,
        tudo bem? \nAqui é **{Colaborador} da Firenze Imóveis,** recebi seu e-mail referente ao imóvel em [{endereco}]({link_endereco}), só passando para informar que esse imóvel encontra-se disponível.
        Para ter mais informações e um atendimento mais rápido, envie uma mensagem clicando no nosso [WhatsApp]({link_whatsapp})\n Aguardo o seu contato!"""
        return message

    st.title("Mensagem para imóvel disponível")
    nome = st.text_input("Nome")
    email = st.text_input("E-mail")
    Colaboardor = st.text_input("Colaborador")
    endereco = st.text_input("Endereço")
    link_endereco = st.text_input("Link do imóvel")
    link_whatsapp = st.text_input("Link do WhatsApp")

    if st.button("Gerar Mensagem"):
        if nome and email and endereco and link_endereco and link_whatsapp and Colaboardor:
            message = generate_message(nome, email, endereco, link_endereco, link_whatsapp, Colaboardor)
            st.markdown(message)


        else:
            st.error("Por favor, preencha todos os campos.")

if hub_firenze == 'Imóvel indisponível':
    def generate_message(nome, email, endereco, link_endereco, link_whatsapp):
        message = f"""Oi, {nome},
        tudo bem? Aqui é Wemerson da Firenze Imóveis, recebi seu e-mail referente ao imóvel em [{endereco}]({link_endereco}), só passando para informar que esse imóvel encontra-se disponível.
        Para ter mais informações e um atendimento mais rápido, envie uma mensagem clicando no nosso [WhatsApp]({link_whatsapp}) Aguardo o seu contato"""
        return message

    st.title("Mensagem para imóvel indisponível")
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
if hub_firenze == 'Gerador de QR-Code':
    def generate_qr_code(data):
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        return img


if hub_firenze == 'NFS-e Curitiba':

    # Inicializa a variável de soma na sessão
    if 'soma' not in st.session_state:
        st.session_state.soma = 0.0

    # Entrada para o valor da comissão
    valor_comissao = st.number_input("Digite um valor da comissão R$:", min_value=0.0, format="%.2f")

    # Botão para adicionar o valor
    if st.button('Adicionar valor'):
        st.session_state.soma += valor_comissao
        st.success(f"Valor de R${valor_comissao:.2f} adicionado.")

    # Botão para resetar a soma
    if st.button('Resetar soma'):
        st.session_state.soma = 0.0
        st.success("Soma reiniciada.")

    # Exibe o total acumulado
    st.write(f"Taxa de administração: R${st.session_state.soma:.2f}")
st.echo()
