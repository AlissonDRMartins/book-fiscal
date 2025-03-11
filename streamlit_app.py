import streamlit as st
import pandas as pd
from typing import Union, Tuple, Dict, List
from constants import *


def calculate_tax(rbt12: Union[int, float], anexo: int) -> Tuple[float, float]:
    if anexo not in TAX_RATES:
        raise ValueError(f"Anexo desconhecido: {anexo}")

    rates = TAX_RATES[anexo]

    for i, limit in enumerate(LIMITS):
        if rbt12 <= limit:
            return rates[i]

    return rates[-1]


def calculate_effective_rate(rbt12: Union[int, float], anexo: int) -> float:
    if rbt12 <= 0:
        return 0.0

    aliquota, valor_a_deduzir = calculate_tax(rbt12, anexo)
    return (((rbt12 * (aliquota / 100)) - valor_a_deduzir) / rbt12) * 100


def calculate_tax_amount(rbt12: Union[int, float], anexo: int) -> float:
    if rbt12 <= 0:
        return 0.0

    aliquota, valor_a_deduzir = calculate_tax(rbt12, anexo)
    return (rbt12 * (aliquota / 100)) - valor_a_deduzir


def formatar_moeda(valor: Union[float, str, None]) -> str:
    if pd.isna(valor) or valor is None or valor == "":
        return "R$ 0,00"

    try:
        if isinstance(valor, str):
            valor_float = float(
                valor.replace("R$", "").replace(".", "").replace(",", ".").strip()
            )
        else:
            valor_float = float(valor)

        return (
            f"R$ {valor_float:,.2f}".replace(",", "X")
            .replace(".", ",")
            .replace("X", ".")
        )
    except (ValueError, TypeError):
        return "R$ 0,00"


def setup_page():
    st.set_page_config(
        page_title="Simulador Simples Nacional",
        layout="wide",
        initial_sidebar_state="collapsed",
    )

    # Force light mode
    st.markdown(
        """
        <style>
        :root {
            --background-color: #ffffff;
            --secondary-background-color: #f0f2f6;
            --primary-color: #3498db;
            --text-color: #2c3e50;
            --font: "Source Sans Pro", sans-serif;
        }
        </style>
    """,
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown(
            """
            <div style="text-align: center;">
                <a href="https://www.talst.com.br" target="_blank">
                    <img src="https://d28hb748xidqca.cloudfront.net/520x520x0/oKlYNu9RZcEKWYBOycuosUHviK29g56fmw64BqvK3RH01TXP7V0zu0ObGMuOGock/talst-escritorio-de-contabilidade-em-jundiai-1.png" 
                         alt="Talst Contabilidade Logo" 
                         style="max-width: 200px; cursor: pointer;">
                </a>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown(
        """
        <h1 style='text-align: center; color: #2c3e50; font-weight: 600; margin-top: 10px;'>
            Simulador Simples Nacional
        </h1>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        "<hr style='height: 2px; border: none; background-color: #3498db;'>",
        unsafe_allow_html=True,
    )


def category_selection() -> int:
    st.write(
        """
        <h3 style='color: #2c3e50;'>
            Selecione a categoria desejada:
        </h3>
        """,
        unsafe_allow_html=True,
    )

    reverse_categories = {v: k for k, v in CATEGORIES.items()}

    selection = st.pills(
        label="Categoria",
        options=list(CATEGORIES.values()),
        format_func=lambda opt: opt,
        selection_mode="single",
        label_visibility="hidden",
    )

    return reverse_categories.get(selection) if selection is not None else None


def revenue_input() -> float:
    st.markdown(
        "<hr style='height: 1px; border: none; background-color: #e0e0e0;'>",
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <h3 style='color: #2c3e50;'>
            Insira aqui a sua Receita Bruta dos Últimos 12 meses
        </h3>
        """,
        unsafe_allow_html=True,
    )

    st.caption(
        """
        A receita bruta dos últimos 12 meses é a soma de todos os meses precedentes. 
        Caso tenha menos que 12 meses, utilize apenas os meses em que houve faturamento.
        """
    )

    return st.number_input(
        label="faturamento",
        min_value=0,
        max_value=4800000,
        step=1000,
        label_visibility="hidden",
        format="%d",
    )


def display_results(selected_key: int, total_faturamento: float):
    st.markdown(
        "<hr style='height: 1px; border: none; background-color: #e0e0e0;'>",
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <h3 style='color: #2c3e50;'>
            Cálculo do Simples Nacional
        </h3>
        """,
        unsafe_allow_html=True,
    )

    if selected_key is None:
        st.warning("⚠️ Por favor, selecione a categoria para realizar os cálculos.")
        return

    if total_faturamento <= 0:
        st.warning(
            "⚠️ Por favor, informe o faturamento mensal para realizar os cálculos."
        )
        return

    st.info(
        "ℹ️ Os valores de impostos serão calculados com base no faturamento informado."
    )

    anexos = MAP_ANEXO.get(selected_key, [])

    if anexos:
        cols = st.columns(len(anexos))

        for i, anexo in enumerate(anexos):
            with cols[i]:
                display_annex_calculation(anexo, total_faturamento)


def display_annex_calculation(anexo: int, total_faturamento: float):
    nominal_rate, deduction = calculate_tax(total_faturamento, anexo)
    effective_rate = calculate_effective_rate(total_faturamento, anexo)
    tax_amount = calculate_tax_amount(total_faturamento, anexo)

    st.markdown(
        f"""
        <div style="border: 1px solid #e0e0e0; border-radius: 5px; padding: 15px; background-color: #f8f9fa;">
            <h4 style="color: #2c3e50; text-align: center; margin-bottom: 15px;">Anexo {anexo}</h4>
            <table style="width: 100%;">
                <tr>
                    <td style="padding: 8px 0; border-bottom: 1px solid #e0e0e0;">Alíquota Nominal:</td>
                    <td style="text-align: right; font-weight: bold; padding: 8px 0; border-bottom: 1px solid #e0e0e0;">{nominal_rate:.2f}%</td>
                </tr>
                <tr>
                    <td style="padding: 8px 0; border-bottom: 1px solid #e0e0e0;">Valor a Deduzir:</td>
                    <td style="text-align: right; font-weight: bold; padding: 8px 0; border-bottom: 1px solid #e0e0e0;">{formatar_moeda(deduction)}</td>
                </tr>
                <tr>
                    <td style="padding: 8px 0; border-bottom: 1px solid #e0e0e0;">Alíquota Efetiva:</td>
                    <td style="text-align: right; font-weight: bold; padding: 8px 0; border-bottom: 1px solid #e0e0e0;">{effective_rate:.2f}%</td>
                </tr>
                <tr>
                    <td style="padding: 8px 0;">Imposto a Pagar:</td>
                    <td style="text-align: right; font-weight: bold; color: #e74c3c; padding: 8px 0;">{formatar_moeda(tax_amount)}</td>
                </tr>
            </table>
        </div>
        """,
        unsafe_allow_html=True,
    )


def main():
    setup_page()

    selected_key = category_selection()
    total_faturamento = revenue_input()

    display_results(selected_key, total_faturamento)

    st.markdown(
        "<hr style='height: 1px; border: none; background-color: #e0e0e0;'>",
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <footer class="footer">
  <div class="footer-content">
    <div class="copyright">
      © 2025 Talst Contabilidade. Todos os direitos reservados.
    </div>
    <div class="disclaimer">
      <em>Este simulador é apenas uma ferramenta de referência. Para cálculos oficiais, contate um de nossos especialistas.</em>
    </div>
    <div class="contact">
      <a href="tel:+551145261077">(11) 4526-1077</a>
    </div>
  </div>
</footer>

<style>
  .footer {
    background-color: #f8f9fa;
    padding: 20px 0;
    border-top: 1px solid #e9ecef;
    margin-top: 40px;
    font-family: 'Arial', sans-serif;
  }
  
  .footer-content {
    max-width: 800px;
    margin: 0 auto;
    text-align: center;
  }
  
  .copyright {
    color: #495057;
    font-size: 0.9em;
    margin-bottom: 10px;
  }
  
  .disclaimer {
    color: #6c757d;
    font-size: 0.8em;
    margin-bottom: 10px;
    line-height: 1.4;
  }
  
  .contact a {
    color: #0066cc;
    text-decoration: none;
    font-size: 0.9em;
    font-weight: 500;
    transition: color 0.2s;
  }
  
  .contact a:hover {
    color: #004d99;
    text-decoration: underline;
  }
</style>
        """,
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()
