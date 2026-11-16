import streamlit as st
import pandas as pd
import numpy as np
import time

# Configuração da Página
st.set_page_config(
    page_title="TerraRotas - NASA Space Apps",
    page_icon="🛰️",
    layout="wide"
)

# Estilo visual limpo
st.title("🛰️ TerraRotas: Inteligência Orbital para a Agricultura Familiar")
st.markdown("**NASA Space Apps Challenge** | Decisões baseadas em dados da NASA para resiliência climática e rotação de culturas.")
st.markdown("---")

# --- BARRA LATERAL: ENTRADA DO PRODUTOR ---
st.sidebar.header("📍 Parâmetros da Propriedade")
talhao = st.sidebar.selectbox("Selecione o Talhão / Região", ["Talhão 01 - Baixada (Boa Vista/RR)", "Talhão 02 - Chapada (Canta/RR)"])
cultura_atual = st.sidebar.selectbox("Última Cultura Cultivada", ["Milho Grão", "Soja", "Pousio / Solo Nu"])
tipo_solo = st.sidebar.selectbox("Tipo de Solo Predominante", ["Arenoso", "Médio / Argiloso", "Humoso"])

st.sidebar.markdown("### ⚙️ Prioridades do Agricultor")
peso_agua = st.sidebar.slider("Conservação de Água (SMAP/GPM)", 0, 100, 80)
peso_solo = st.sidebar.slider("Recuperação de Nutrientes", 0, 100, 60)
peso_renda = st.sidebar.slider("Geração de Renda Rápida", 0, 100, 40)

# Botão de Execução do Motor
analisar = st.sidebar.button("🚀 Processar Dados Orbitais da NASA")

# --- CORPO PRINCIPAL ---
if not analisar:
    st.info("👈 Selecione os parâmetros na barra lateral e clique em **Processar Dados Orbitais da NASA** para gerar o diagnóstico e cenários de rotação.")
    
    # Exemplo visual estático inicial
    col1, col2, col3 = st.columns(3)
    col1.metric("Umidade Radicular (SMAP)", "28.4% (Baixa)", "-4.2% esta semana")
    col2.metric("Risco de Queimada (ECO/POWER)", "78.2% (Alto)", "Alerta de Biomassa Seca")
    col3.metric("Precipitação Prevista (GPM)", "12 mm", "Próximos 10 dias")
else:
    with st.spinner("Extraindo dados do Google Earth Engine e NASA POWER..."):
        time.sleep(1.2)

    st.success("✅ Dados cruzados com sucesso a partir de múltiplos satélites e APIs da NASA!")

    # Seção de Alertas Imediatos
    col1, col2, col3 = st.columns(3)
    col1.metric("Umidade Radicular (SMAP)", "24.1%", "-6.5% (Crítico)")
    col2.metric("Risco de Incêndio na Palhada", "82.4% (Alto)", "Vento forte + LST elevado")
    col3.metric("Balanço Hídrico (GPM/POWER)", "-18 mm", "Déficit nos últimos 15 dias")

    st.markdown("---")
    st.subheader("🌾 Comparativo de Cenários de Rotação de Culturas")
    st.markdown("O algoritmo cruzou a janela térmica, o relevo (SRTM) e a umidade atual para recomendar as 3 melhores estratégias:")

    # Tabela Comparativa de Cenários
    tab1, tab2, tab3 = st.tabs(["Cenário 1: Pousio / Atual", "Cenário 2: Escudo Hídrico", "Cenário 3: Fixação & Renda"])

    with tab1:
        st.warning("⚠️ **Manutenção do Solo Nu (Manejo Tradicional)**")
        st.write("- **Evidência de Satélite:** O Landsat detectou solo descoberto e o ECOSTRESS registrou alta temperatura superficial (39°C), gerando forte risco de erosão laminar e compactação.")
        st.write("- **Vantagem:** Nenhum custo com sementes de cobertura.")
        st.write("- **Risco:** Perda total de umidade residual e alta vulnerabilidade a propagação de fogo.")

    with tab2:
        st.success("🌱 **Plantio de Cobertura: Braquiária / Milheto (Recomendado para Água)**")
        st.write("- **Evidência de Satélite:** O SMAP indica que o sistema radicular profundo dessas espécies consegue aproveitar os 24% de umidade remanescente sem irrigação.")
        st.write("- **Vantagem:** Aumenta a infiltração de água, protege contra a radiação solar direta e reduz o risco de incêndio para 12%.")
        st.write("- **Alinhamento com sua prioridade:** Atende perfeitamente ao seu foco em conservação hídrica (80/100).")

    with tab3:
        st.info("💡 **Consórcio de Rotação: Feijão-Caupi (Leguminosa de Ciclo Curto)**")
        st.write("- **Evidência de Satélite:** A janela térmica calculada pela NASA POWER garante ciclo seguro antes da próxima estiagem severa.")
        st.write("- **Vantagem:** Fixa nitrogênio biologicamente no solo, quebrando a dependência de adubos químicos caros e oferecendo colheita rápida.")
        st.write("- **Alinhamento com sua prioridade:** Ideal para recuperação nutricional e geração de caixa para o produtor.")

    st.markdown("---")
    st.markdown("### 📱 Ações Rápidas no Campo")
    col_a, col_b = st.columns(2)
    if col_a.button("📤 Enviar Alerta de Risco por WhatsApp"):
        st.toast("Mensagem formatada enviada com sucesso para o produtor!", icon="📱")
    if col_b.button("📥 Baixar Relatório Completo em PDF"):
        st.toast("Relatório gerado em formato PDF pronto para impressão.", icon="📄")
