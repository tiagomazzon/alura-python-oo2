import re 

class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def valida_url(self):
        self.url = self.sanitiza_url(self.url)
        if not self.url:
            raise ValueError('A URL está vazia')
        
        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(self.url)
        if not match:
            raise ValueError('A URL não é válida.')

    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[:indice_interrogacao]
        return url_base

    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao+1:]
        return url_parametros

    def get_valor_parametro(self, nome_parametro):
        indice_parametro = self.get_url_parametros().find(nome_parametro)
        indice_valor = indice_parametro + len(nome_parametro) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)

        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor

    def converte_valor(self, valor_dolar):
        #valor_dolar = 5.50  # 1 dólar = 5.50 reais
        moeda_origem = extrator_url.get_valor_parametro("moedaOrigem")
        moeda_destino = extrator_url.get_valor_parametro("moedaDestino")
        quantidade = extrator_url.get_valor_parametro("quantidade")

        if moeda_destino == "dolar":
            return float(quantidade) / valor_dolar
        else:
            return float(quantidade) * valor_dolar

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return f' URL: {self.url} \n Parâmetros: {self.get_url_parametros()} \n URL Base: {self.get_url_base()}'

    def __eq__(self, other):
        return self.url == other.url


url = "bytebank.com/cambio?quantidade=100&moedaOrigem=dolar&moedaDestino=real"
extrator_url = ExtratorURL(url)

valor = extrator_url.converte_valor(5.50)
print(valor)