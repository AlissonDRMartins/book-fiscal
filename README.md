# Simulador Simples Nacional

<div align="center">
  
![Talst Contabilidade](https://d28hb748xidqca.cloudfront.net/520x520x0/oKlYNu9RZcEKWYBOycuosUHviK29g56fmw64BqvK3RH01TXP7V0zu0ObGMuOGock/talst-escritorio-de-contabilidade-em-jundiai-1.png)

*Uma ferramenta simplificada para calcular impostos do Simples Nacional para empresas brasileiras*

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://simulador-simples-nacional.streamlit.app/) 
[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

</div>

## 📋 Sobre o Projeto

O **Simulador Simples Nacional** é uma aplicação web desenvolvida com Streamlit que permite calcular os tributos a serem pagos por empresas optantes pelo regime tributário Simples Nacional no Brasil. A ferramenta oferece cálculos precisos para diferentes anexos fiscais com base na receita bruta anual da empresa.

### ✨ Características

- **Cálculo em Tempo Real**: Visualize alíquotas e valores a pagar instantaneamente
- **Múltiplos Anexos**: Suporte para todos os 5 anexos do Simples Nacional
- **Interface Intuitiva**: Design limpo e responsivo para fácil utilização
- **Precisão Fiscal**: Cálculos alinhados com a legislação tributária brasileira

## 🚀 Como Usar

1. Acesse a [aplicação online](https://simulador-simples-nacional.streamlit.app/)
2. Selecione a categoria do seu negócio (Comércio, Indústria, ou Outros)
3. Insira o valor da receita bruta dos últimos 12 meses
4. Visualize os resultados com alíquotas nominais, efetivas e valores a serem pagos

## 💻 Execução Local

Para executar o simulador em seu ambiente local:

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/simulador-simples-nacional.git
cd simulador-simples-nacional

# Instale as dependências
pip install -r requirements.txt

# Execute a aplicação
streamlit run app.py
```

### 📦 Requisitos

- Python 3.7+
- Streamlit
- Pandas

## 📊 Detalhes Técnicos

O simulador utiliza as tabelas e fórmulas oficiais do Simples Nacional, considerando:

- **Faixas de Faturamento**: 6 faixas baseadas na receita bruta dos últimos 12 meses
- **Alíquotas Nominais**: Percentuais brutos aplicados por faixa
- **Parcelas a Deduzir**: Valores a serem subtraídos para calcular o imposto efetivo
- **Alíquotas Efetivas**: Percentuais reais após aplicação das deduções

## 📘 Anexos do Simples Nacional

- **Anexo I**: Comércio
- **Anexo II**: Indústria 
- **Anexo III**: Serviços e Locação de Bens Móveis
- **Anexo IV**: Serviços especificados em lei
- **Anexo V**: Serviços específicos (ex: advocacia, medicina, engenharia)

## ⚠️ Disclaimer

Esta aplicação é uma ferramenta de simulação para fins educativos e de referência. Para decisões fiscais oficiais, consulte sempre um contador ou profissional qualificado em contabilidade.

## 🤝 Contribuições

Contribuições são bem-vindas! Se encontrar bugs ou tiver sugestões para melhorar o simulador:

1. Abra uma issue descrevendo o problema/sugestão
2. Envie um pull request com suas alterações

## 📜 Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE para mais detalhes.

---

<div align="center">
  
Desenvolvido com ❤️ por [Talst Contabilidade](https://www.talst.com.br)
  
</div>