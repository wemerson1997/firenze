import streamlit as st
import urllib.parse
import pyperclip

hub_firenze = st.sidebar.selectbox(
    'Hub Firenze',
    ['WhatsApp', 'Imóvel reservado', 'Imóvel disponível', 'Imóvel indisponível', 'NFS-e Curitiba', 'Mensagem WhatsApp'],
    0)

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
    def generate_message(nome, email, endereco, link_endereco, link_whatsapp, Colaborador):
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

if hub_firenze == 'Mensagem WhatsApp':

    def main():
        #st.set_page_config(page_title="Gerador de Links WhatsApp - Firenze Imóveis", page_icon="🏠")

        # Título e descrição
        st.title("Gerador de Links de WhatsApp")
        st.subheader("Firenze Imóveis")
        st.write("Preencha os dados do cliente e do imóvel para gerar um link de WhatsApp personalizado.")

        # Lista de DDDs por estado
        ddds = {
            "Acre (AC)": ["68"],
            "Amapá (AP)": ["96"],
            "Amazonas (AM)": ["92", "97"],
            "Pará (PA)": ["91", "93", "94"],
            "Rondônia (RO)": ["69"],
            "Roraima (RR)": ["95"],
            "Tocantins (TO)": ["63"],
            "Alagoas (AL)": ["82"],
            "Bahia (BA)": ["71", "73", "74", "75", "77"],
            "Ceará (CE)": ["85", "88"],
            "Maranhão (MA)": ["98", "99"],
            "Paraíba (PB)": ["83"],
            "Pernambuco (PE)": ["81", "87"],
            "Piauí (PI)": ["86", "89"],
            "Rio Grande do Norte (RN)": ["84"],
            "Sergipe (SE)": ["79"],
            "Distrito Federal (DF)": ["61"],
            "Goiás (GO)": ["62", "64"],
            "Mato Grosso (MT)": ["65", "66"],
            "Mato Grosso do Sul (MS)": ["67"],
            "Espírito Santo (ES)": ["27", "28"],
            "Minas Gerais (MG)": ["31", "32", "33", "34", "35", "37", "38"],
            "Rio de Janeiro (RJ)": ["21", "22", "24"],
            "São Paulo (SP)": ["11", "12", "13", "14", "15", "16", "17", "18", "19"],
            "Paraná (PR)": ["41", "42", "43", "44", "45", "46"],
            "Rio Grande do Sul (RS)": ["51", "53", "54", "55"],
            "Santa Catarina (SC)": ["47", "48", "49"],
        }

        # Criar uma lista plana de todos os DDDs para o seletor
        all_ddds = []
        for estado, codigos in ddds.items():
            for codigo in codigos:
                all_ddds.append(f"{codigo} ({estado})")

        # Formulário para coletar dados
        with st.form(key="whatsapp_form"):
            nome_cliente = st.text_input("Nome do Cliente")

            # Campo de WhatsApp separado por DDD e número
            col1, col2 = st.columns([1, 3])
            with col1:
                ddd_selecionado = st.selectbox("DDD", options=all_ddds)
            with col2:
                numero_whatsapp = st.text_input("Número de WhatsApp (somente números, sem o DDD)")

            referencia_imovel = st.text_input("Referência do Imóvel")
            endereco_imovel = st.text_input("Endereço do Imóvel")
            link_imovel = st.text_input("Link do Imóvel (URL da página)")

            # Botão para gerar o link
            submit_button = st.form_submit_button(label="Gerar Link")

        if submit_button:
            if not nome_cliente or not numero_whatsapp or not endereco_imovel:
                st.error("Por favor, preencha todos os campos obrigatórios.")
            else:
                # Extrair o DDD do seletor (pegando apenas os dois primeiros dígitos)
                ddd = ddd_selecionado.split()[0]

                # Limpar o número de telefone (remover espaços, traços, parênteses)
                numero_limpo = ''.join(filter(str.isdigit, numero_whatsapp))

                # Montar o número completo com código do país
                whatsapp_limpo = f"55{ddd}{numero_limpo}"

                # Criar o texto do endereço com link, se fornecido
                endereco_texto = endereco_imovel
                if link_imovel:
                    endereco_texto = f"{endereco_imovel} (Veja mais detalhes em: {link_imovel})"

                # Criar a mensagem personalizada
                ref_texto = f"(Ref: {referencia_imovel}) " if referencia_imovel else ""
                mensagem = f"Olá! {nome_cliente}. Tudo bem? Sou da Firenze Imóveis. Vi que você demonstrou interesse no imóvel {ref_texto}localizado em {endereco_texto}. Se ainda tiver interesse, posso te passar mais detalhes e marcar uma visita pra você. Atenciosamente, Firenze Imóveis."

                # Codificar a mensagem para URL
                mensagem_codificada = urllib.parse.quote(mensagem)

                # Gerar o link do WhatsApp
                link_whatsapp = f"https://wa.me/{whatsapp_limpo}?text={mensagem_codificada}"

                # Exibir o link e a mensagem
                st.success("Link gerado com sucesso!")

                st.subheader("Link do WhatsApp:")
                st.code(link_whatsapp, language="text")

                st.subheader("Mensagem que será enviada:")

                # Exibir a mensagem com formatação para destacar o link do imóvel se existir
                if link_imovel:
                    # Separar a mensagem para destacar o link
                    partes = mensagem.split(link_imovel)
                    if len(partes) > 1:
                        st.write(partes[0], unsafe_allow_html=True)
                        st.markdown(
                            f"<a href='{link_imovel}' target='_blank' style='color:blue;text-decoration:underline;'>{link_imovel}</a>",
                            unsafe_allow_html=True)
                        st.write(partes[1], unsafe_allow_html=True)
                    else:
                        st.write(mensagem)
                else:
                    st.write(mensagem)

                # Adicionar botões para copiar e abrir o link
                col1, col2 = st.columns(2)

                with col1:
                    if st.button("Copiar Link"):
                        pyperclip.copy(link_whatsapp)
                        st.success("Link copiado para a área de transferência!")

                with col2:
                    st.markdown(
                        f"<a href='{link_whatsapp}' target='_blank'><button style='background-color:#25D366;color:white;padding:10px;border:none;border-radius:5px;cursor:pointer;'>Abrir no WhatsApp</button></a>",
                        unsafe_allow_html=True)


    if __name__ == "__main__":
        main()
st.echo()