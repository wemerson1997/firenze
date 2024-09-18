import requests
from bs4 import BeautifulSoup


def get_imoveis_firenze():
    url = "https://www.firenzeimoveis.com.br/imoveis/comprar"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    imoveis = []
    # Aqui você precisa implementar a lógica para extrair os códigos dos imóveis
    # Exemplo: imoveis = [code.text for code in soup.find_all('div', class_='imovel-code')]
    return [code for code in imoveis if code.startswith('1980')]

def check_portal(portal_url, codigo):
    response = requests.get(f"{portal_url}?q={codigo}")
    return codigo in response.text

def main():
    portais = {
        "ZapImoveis": "https://www.zapimoveis.com.br/venda/imoveis/pr+curitiba/",
        "VivaReal": "https://www.vivareal.com.br/venda/parana/curitiba/",
        "OLX": "https://www.olx.com.br/imoveis/estado-pr/regiao-de-curitiba-e-paranagua"
    }

    imoveis_firenze = get_imoveis_firenze()

    for codigo in imoveis_firenze:
        print(f"Verificando imóvel {codigo}:")
        for portal, url in portais.items():
            if check_portal(url, codigo):
                print(f"  - Encontrado no {portal}")
            else:
                print(f"  - Não encontrado no {portal}")
        print()

if __name__ == "__main__":
    main()