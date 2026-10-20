import streamlit as st
import streamlit.components.v1 as components

# ---------------------------------------------------------
# 1. Configuração da Página e Cores (Design System)
# ---------------------------------------------------------
# initial_sidebar_state="expanded" garante que o menu não suma por padrão.
st.set_page_config(page_title="DataTour Analytics", page_icon="✈️", layout="wide", initial_sidebar_state="expanded")

# CSS Totalmente Refatorado para um UX Mais Premium
st.markdown("""
    <style>
    /* Espaço no topo ajustado para não cortar o título nem o botão de Voltar */
    .block-container {
        padding-top: 3.5rem !important;
        padding-bottom: 2.5rem !important;
        max-width: 1200px;
    }

    /* Cabeçalho transparente (evita cortar o topo dos botões) e esconde o botão "Implantar" sem sumir com a seta do menu lateral */
    header[data-testid="stHeader"] {
        background: transparent !important;
    }
    .stAppDeployButton, [data-testid="stAppDeployButton"], [data-testid="stToolbarActions"] {
        display: none !important;
    }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    /* ----------------------------------------------------- */
    /* SIDEBAR (MENU LATERAL) COM DESIGN MODERNO E ELEGANTE  */
    /* ----------------------------------------------------- */
    [data-testid="stSidebar"] {
        background-color: #FFFFFF !important;
        border-right: 1px solid #E2E8F0;
    }
    [data-testid="stSidebar"] > div:first-child {
        padding-top: 1rem !important;
    }
    .sidebar-nav-header {
        font-size: 0.78rem;
        font-weight: 800;
        color: #64748B;
        letter-spacing: 1.2px;
        text-transform: uppercase;
        margin: 0.5rem 0 0.6rem 0.2rem;
    }
    /* Transformando os itens do radio em botões modernos de menu */
    [data-testid="stSidebar"] [role="radiogroup"] {
        gap: 0.45rem !important;
    }
    [data-testid="stSidebar"] [role="radiogroup"] label {
        background-color: #F8FAFC !important;
        border: 1px solid #E2E8F0 !important;
        border-left: 4px solid #CBD5E1 !important;
        border-radius: 10px !important;
        padding: 0.65rem 0.95rem !important;
        width: 100% !important;
        transition: all 0.2s ease-in-out !important;
        cursor: pointer !important;
        margin: 0 !important;
    }
    /* Esconde a bolinha vermelha padrão do radio no menu lateral */
    [data-testid="stSidebar"] [role="radiogroup"] label > div:first-child {
        display: none !important;
    }
    [data-testid="stSidebar"] [role="radiogroup"] label p {
        font-size: 0.98rem !important;
        font-weight: 600 !important;
        color: #1E293B !important;
        margin: 0 !important;
    }
    /* Efeito ao passar o mouse nos itens do menu */
    [data-testid="stSidebar"] [role="radiogroup"] label:hover {
        background-color: #FFF7ED !important;
        border-color: #FED7AA !important;
        border-left: 4px solid #F26A21 !important;
        transform: translateX(3px);
    }
    /* Item ativo/selecionado no menu lateral */
    [data-testid="stSidebar"] [role="radiogroup"] label:has(input:checked) {
        background: linear-gradient(90deg, #003366 0%, #004080 100%) !important;
        border-color: #003366 !important;
        border-left: 5px solid #F26A21 !important;
        box-shadow: 0 4px 10px rgba(0, 51, 102, 0.18) !important;
    }
    [data-testid="stSidebar"] [role="radiogroup"] label:has(input:checked) p {
        color: #FFFFFF !important;
        font-weight: 700 !important;
    }
    /* Rodapé estilizado do Menu Lateral */
    .sidebar-footer {
        background-color: #F8FAFC;
        border: 1px solid #E2E8F0;
        border-left: 4px solid #D4AF37;
        border-radius: 10px;
        padding: 0.85rem 1rem;
        margin-top: 1rem;
        font-size: 0.82rem;
        color: #475569;
        line-height: 1.5;
    }
    .sidebar-footer strong {
        color: #003366;
        display: block;
        font-size: 0.86rem;
    }

    /* Tipografia Principal - Título */
    .titulo-principal { 
        color: #003366; 
        font-size: 3rem; 
        font-weight: 900; 
        line-height: 1.2; 
        margin-top: 0rem !important;
        margin-bottom: 0.5rem;
        letter-spacing: -0.5px;
    }

    .destaque-laranja { 
        color: #F26A21; 
    }

    .subtitulo { 
        font-size: 1.2rem; 
        color: #64748B; 
        margin-bottom: 1.8rem; 
        line-height: 1.6;
        font-weight: 400;
    }

    /* Barra de Selos Rápidos (Página Inicial) - 4 itens na mesma linha */
    .badge-bar {
        display: flex;
        flex-wrap: nowrap;
        justify-content: space-between;
        gap: 10px;
        margin-bottom: 2rem;
        width: 100%;
    }
    .badge-item {
        flex: 1;
        background-color: #F1F5F9;
        color: #003366;
        padding: 0.5rem 0.65rem;
        border-radius: 999px;
        font-size: 0.84rem;
        font-weight: 700;
        border: 1px solid #E2E8F0;
        text-align: center;
        white-space: nowrap;
    }

    /* Caixas de Informação/Alerta com design mais clean */
    .disclaimer-box { 
        background-color: #FFFBEB; 
        color: #334155; 
        padding: 1.4rem 1.6rem; 
        border-radius: 10px; 
        border: 1px solid #FDE68A;
        border-left: 5px solid #F59E0B;
        font-size: 1.03rem;
        margin-bottom: 2.5rem;
        line-height: 1.6;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.02);
    }

    /* Cards de Perfil na Página Inicial */
    .perfil-card-viajante {
        background-color: #FFFFFF;
        padding: 1.8rem;
        border-radius: 14px;
        border: 1px solid #E2E8F0;
        border-top: 5px solid #003366;
        box-shadow: 0 4px 12px rgba(0, 51, 102, 0.05);
        margin-bottom: 1rem;
        min-height: 220px;
    }
    .perfil-card-agencia {
        background-color: #FFFFFF;
        padding: 1.8rem;
        border-radius: 14px;
        border: 1px solid #E2E8F0;
        border-top: 5px solid #D4AF37;
        box-shadow: 0 4px 12px rgba(212, 175, 55, 0.06);
        margin-bottom: 1rem;
        min-height: 220px;
    }
    .perfil-titulo {
        color: #003366;
        font-size: 1.5rem;
        font-weight: 800;
        margin-bottom: 0.75rem;
    }
    .perfil-texto {
        color: #475569;
        font-size: 1.02rem;
        line-height: 1.6;
        margin-bottom: 1rem;
    }
    .perfil-lista {
        color: #334155;
        font-size: 0.92rem;
        line-height: 1.6;
    }

    /* Botão de Voltar */
    .btn-voltar {
        margin-bottom: 20px;
    }

    /* Cards de Apoio ao Viajante (Checklist e Canais) */
    .guia-card {
        background-color: #FFFFFF;
        padding: 1.4rem;
        border-radius: 10px;
        border: 1px solid #E2E8F0;
        border-top: 4px solid #003366;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.03);
        height: 100%;
        color: #334155;
        font-size: 0.98rem;
        line-height: 1.6;
    }
    .canal-card {
        background-color: #F8FAFC;
        padding: 1.1rem;
        border-radius: 10px;
        border: 1px solid #E2E8F0;
        border-left: 4px solid #F26A21;
        margin-bottom: 0.8rem;
    }
    .canal-card a {
        color: #003366;
        font-weight: 700;
        text-decoration: none;
    }
    .canal-card a:hover {
        color: #F26A21;
        text-decoration: underline;
    }

    /* Estilos da Página Sobre o Projeto */
    .sobre-card {
        background-color: #FFFFFF;
        padding: 1.75rem;
        border-radius: 12px;
        border: 1px solid #E2E8F0;
        border-left: 5px solid #003366;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.04);
        margin-bottom: 2rem;
        color: #334155;
        font-size: 1.05rem;
        line-height: 1.7;
    }
    .secao-titulo {
        color: #003366;
        font-size: 1.35rem;
        font-weight: 800;
        margin-top: 1rem;
        margin-bottom: 1rem;
        border-bottom: 2px solid #F1F5F9;
        padding-bottom: 0.5rem;
    }
    .membro-card {
        background-color: #F8FAFC;
        padding: 0.85rem 1.2rem;
        border-radius: 8px;
        border: 1px solid #E2E8F0;
        border-left: 4px solid #D4AF37;
        margin-bottom: 0.75rem;
        font-weight: 600;
        color: #0F172A;
        font-size: 1.02rem;
    }
    .orientacao-card {
        background-color: #FFFBEB;
        padding: 1.25rem 1.5rem;
        border-radius: 10px;
        border: 1px solid #FDE68A;
        border-left: 5px solid #F26A21;
        color: #334155;
        font-size: 1.05rem;
        line-height: 1.6;
    }

    /* Melhoria nos Botões Nativos do Streamlit com as cores da marca */
    div.stButton > button:first-child {
        height: 3.1rem;
        font-size: 1.08rem;
        font-weight: 700;
        border-radius: 10px;
        transition: all 0.2s ease-in-out;
    }

    /* Botão Primário na cor Marinho da marca */
    div.stButton > button[kind="primary"] {
        background-color: #003366 !important;
        border-color: #003366 !important;
        color: #FFFFFF !important;
    }
    div.stButton > button[kind="primary"]:hover {
        background-color: #F26A21 !important;
        border-color: #F26A21 !important;
        color: #FFFFFF !important;
    }

    /* Botão de Destaque da Agência B2B (Cor Laranja Vibrante para chamar atenção) */
    .st-key-btn_dashboard_b2b button,
    [data-testid="stColumn"]:nth-of-type(2) div.stButton > button[kind="primary"],
    [data-testid="column"]:nth-of-type(2) div.stButton > button[kind="primary"] {
        background: linear-gradient(90deg, #F26A21 0%, #E05A12 100%) !important;
        border-color: #F26A21 !important;
        color: #FFFFFF !important;
        box-shadow: 0 4px 12px rgba(242, 106, 33, 0.25) !important;
    }
    .st-key-btn_dashboard_b2b button:hover,
    [data-testid="stColumn"]:nth-of-type(2) div.stButton > button[kind="primary"]:hover,
    [data-testid="column"]:nth-of-type(2) div.stButton > button[kind="primary"]:hover {
        background: linear-gradient(90deg, #D4AF37 0%, #B89327 100%) !important;
        border-color: #D4AF37 !important;
        color: #FFFFFF !important;
    }

    /* Botão Secundário mais visível e elegante */
    div.stButton > button[kind="secondary"] {
        border: 2px solid #003366 !important;
        color: #003366 !important;
        background-color: #FFFFFF !important;
    }
    div.stButton > button[kind="secondary"]:hover {
        background-color: #F8FAFC !important;
        border-color: #F26A21 !important;
        color: #F26A21 !important;
    }

    div.stButton > button:first-child:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.08);
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Lógica de Navegação por Botões
# ---------------------------------------------------------
OPCOES_MENU = [
    "🏠 Página Inicial",
    "🧳 Área do Viajante",
    "⚖️ Direitos do Viajante (FAQ)",
    "📊 Dashboard Agência",
    "ℹ️ Sobre o Projeto"
]

if "menu_state" not in st.session_state or st.session_state["menu_state"] not in OPCOES_MENU:
    st.session_state["menu_state"] = "🏠 Página Inicial"


def set_page(page_name):
    st.session_state["menu_state"] = page_name


# Função para criar o botão de voltar em páginas secundárias
def botao_voltar():
    st.button("🔙 Voltar para a Página Inicial", on_click=set_page, args=("🏠 Página Inicial",),
              key=f"btn_voltar_{st.session_state['menu_state']}")
    st.markdown("<br>", unsafe_allow_html=True)


# ---------------------------------------------------------
# 2. Menu Lateral e Logo
# ---------------------------------------------------------
try:
    st.sidebar.image("logonome.png", use_container_width=True)
except Exception:
    st.sidebar.warning("Salve a imagem 'logonome.png' na mesma pasta deste script para exibir a logo.")

st.sidebar.markdown('<div class="sidebar-nav-header">🧭 Menu Principal</div>', unsafe_allow_html=True)

menu = st.sidebar.radio(
    "Navegação:",
    OPCOES_MENU,
    index=OPCOES_MENU.index(st.session_state["menu_state"]),
    label_visibility="collapsed"
)

# Atualiza o state caso o usuário clique no menu lateral
st.session_state["menu_state"] = menu

st.sidebar.markdown("""
    <div class="sidebar-footer">
        <strong>🎓 Projeto Integrador (PI)</strong>
        Turma 108 • Ciência de Dados<br>
        SENAC-DF • 2026
    </div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# PÁGINA INICIAL
# ---------------------------------------------------------
if st.session_state["menu_state"] == "🏠 Página Inicial":

    st.markdown(
        '<h1 class="titulo-principal">Inteligência de Dados para <span class="destaque-laranja">Salvar a SUA Viagem</span></h1>',
        unsafe_allow_html=True)

    st.markdown(
        '<p class="subtitulo">A ponte transparente entre os seus direitos como passageiro e a eficiência operacional das agências de turismo.</p>',
        unsafe_allow_html=True)

    st.markdown("""
        <div class="badge-bar">
            <span class="badge-item">⚖️ Baseado na ANAC, ANTT e CDC</span>
            <span class="badge-item">🔒 100% Privado (Sem coleta de dados)</span>
            <span class="badge-item">⚡ Gerador Automático de Relato</span>
            <span class="badge-item">📊 Pipeline Python + MySQL + Power BI</span>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="disclaimer-box">
            <strong>⚠️ Guia de Orientação Inteligente:</strong><br><br>
            Esta plataforma <strong>NÃO</strong> registra reclamações oficiais nem envia dados automaticamente para as empresas (aéreas, viações de ônibus ou hotéis). 
            Nós te ajudamos a organizar seu relato com embasamento na Lei, gerando um documento estruturado para você utilizar nos canais oficiais competentes (Consumidor.gov.br, Procon, ANAC ou ANTT).
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<h3 style='color: #0F172A; margin-bottom: 1.2rem;'>Selecione seu perfil para iniciar:</h3>",
                unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown("""
            <div class="perfil-card-viajante">
                <div class="perfil-titulo">🧳 Sou Viajante</div>
                <div class="perfil-texto">
                    Teve um problema com voo, ônibus, hotel ou pacote e não sabe por onde começar? Gere um documento formal pronto para copiar e enviar.
                </div>
                <div class="perfil-lista">
                    ✔️ Rascunho fundamentado nas normas vigentes<br>
                    ✔️ Checklist de provas e links dos órgãos oficiais<br>
                    ✔️ Página exclusiva de FAQ com prazos e direitos
                </div>
            </div>
        """, unsafe_allow_html=True)
        st.button("Gerar Rascunho e Ver Canais ➔", use_container_width=True, type="primary", on_click=set_page,
                  args=("🧳 Área do Viajante",), key="btn_viajante_home")
        st.button("⚖️ Consultar Meus Direitos (FAQ)", use_container_width=True, on_click=set_page,
                  args=("⚖️ Direitos do Viajante (FAQ)",), key="btn_faq_home")

    with col2:
        st.markdown("""
            <div class="perfil-card-agencia">
                <div class="perfil-titulo">📊 Sou Agência B2B</div>
                <div class="perfil-texto">
                    Monitoramento corporativo e inteligência analítica. Visualize SLAs, índices de resolução e qualidade de dados estruturados.
                </div>
                <div class="perfil-lista">
                    ✔️ Dados tratados e validados via Python<br>
                    ✔️ Modelagem dimensional Star Schema (MySQL)<br>
                    ✔️ Painel interativo integrado ao Power BI
                </div>
            </div>
        """, unsafe_allow_html=True)
        st.button("Acessar Dashboard B2B ➔", use_container_width=True, type="primary", on_click=set_page,
                  args=("📊 Dashboard Agência",), key="btn_dashboard_b2b")

# ---------------------------------------------------------
# ÁREA DO VIAJANTE (GERADOR + CHECKLIST + LINKS OFICIAIS)
# ---------------------------------------------------------
elif st.session_state["menu_state"] == "🧳 Área do Viajante":
    col_nav1, col_nav2 = st.columns([1, 1])
    with col_nav1:
        st.button("🔙 Voltar para a Página Inicial", on_click=set_page, args=("🏠 Página Inicial",),
                  key="btn_voltar_viajante")
    with col_nav2:
        st.button("⚖️ Dúvidas sobre a Lei? Acesse o FAQ do Viajante ➔", on_click=set_page,
                  args=("⚖️ Direitos do Viajante (FAQ)",), key="btn_ir_faq", use_container_width=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.header("🧳 Gerador de Ocorrência Padronizada")

    st.info(
        "💡 **Como funciona:** Preencha os campos abaixo. O sistema aplicará a normalização técnica e criará um 'Rascunho Oficial'. Logo abaixo do gerador, você encontra o **Checklist de Provas** e os **Links Oficiais** para enviar sua reclamação. (Não guardamos os seus dados pessoais).")

    with st.form("form_ocorrencia"):
        col_prob, col_pedido = st.columns(2)
        with col_prob:
            st.markdown("**1. O que aconteceu?** `(Validação Regex Ativa ✅)`")
            problema = st.selectbox("Selecione a categoria técnica da falha:",
                                    ["",
                                     "Voo Cancelado / Atraso de Voo",
                                     "Overbooking (Venda acima da capacidade)",
                                     "Extravio/Dano de Bagagem",
                                     "Ônibus Atrasado ou Cancelado",
                                     "Problema no Hotel (Reserva não localizada / Más condições)",
                                     "Problema com Pacote de Viagem (CVC, Decolar, etc)",
                                     "Locação de Veículo (Cobrança indevida / Carro indisponível)",
                                     "Reembolso Negado ou Taxa Abusiva de Cancelamento"])
        with col_pedido:
            st.markdown("**2. O que você deseja solicitar?**")
            solicitacao = st.selectbox("Selecione a providência principal:",
                                       ["Reembolso integral dos valores pagos e despesas extras",
                                        "Indenização pelos danos materiais e morais sofridos",
                                        "Reacomodação imediata / Cumprimento forçado da oferta",
                                        "Abatimento proporcional do valor pago pelo serviço",
                                        "Localização urgente da bagagem ou reparação integral"])

        st.markdown("<br>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([2, 1, 1])
        with col1:
            empresa = st.text_input("**3. Empresa Envolvida:**",
                                    placeholder="Ex: AeroViva, Viação Estrela, Hotel Mar Azul")
        with col2:
            codigo_reserva = st.text_input("**4. Reserva / Bilhete (Opcional):**",
                                           placeholder="Ex: ABC1234 / Voo 4512")
        with col3:
            data_ocorrido = st.date_input("**5. Data do Ocorrido:**", format="DD/MM/YYYY")

        detalhes_extras = st.text_area(
            "**6. Detalhes adicionais do ocorrido (Opcional):**",
            placeholder="Ex: Fiquei 6 horas aguardando sem receber voucher de alimentação e perdi uma diária de hotel...",
            height=80
        )

        st.markdown("<br>", unsafe_allow_html=True)
        gerar = st.form_submit_button("Gerar Rascunho de Reclamação 📝", use_container_width=True, type="primary")

    if gerar:
        if problema == "":
            st.error("⚠️ Por favor, selecione um problema na lista acima para continuarmos.")
        else:
            st.success("✅ Rascunho gerado com sucesso! Copie o texto no ícone do canto superior direito do quadro ou baixe o arquivo e acesse um dos canais oficiais abaixo.")

            # Ajuste dinâmico do órgão regulador
            if "Ônibus" in problema:
                orgao = "ANTT, Código de Defesa do Consumidor (CDC) e Senacon"
            elif "Hotel" in problema or "Pacote" in problema or "Locação" in problema:
                orgao = "Senacon, Ministério do Turismo e Código de Defesa do Consumidor (CDC)"
            else:
                orgao = "ANAC (Resolução nº 400), Código de Defesa do Consumidor (CDC) e Senacon"

            info_reserva = f" (Código de Reserva/Bilhete: {codigo_reserva.strip()})" if codigo_reserva.strip() else ""
            bloco_detalhes = f"\nRelato complementar dos fatos: {detalhes_extras.strip()}\n" if detalhes_extras.strip() else ""

            texto_oficial = f"""À Ouvidoria / Serviço de Atendimento ao Consumidor da empresa {empresa.strip() or "[Nome da Empresa]"}.

Assunto: Reclamação Formal — {problema}{info_reserva}

No dia {data_ocorrido.strftime("%d/%m/%Y")}, fui vítima de uma falha na prestação de serviço por parte desta empresa, classificada tecnicamente como "{problema}"{info_reserva}.
{bloco_detalhes}
Conforme as diretrizes de qualidade e de proteção aos direitos do consumidor vigentes estabelecidas pela {orgao}, solicito como providência imediata: {solicitacao.lower()}.

Ressalto que o não atendimento desta demanda no prazo legal resultará no registro formal da ocorrência junto aos órgãos reguladores e de defesa do consumidor (Consumidor.gov.br / Procon), sem prejuízo das medidas judiciais cabíveis.

Aguardo retorno conclusivo.
"""
            st.code(texto_oficial, language="markdown")
            st.download_button(
                label="📥 Baixar Rascunho em Arquivo (.txt)",
                data=texto_oficial,
                file_name=f"reclamacao_datatour_{data_ocorrido.strftime('%d_%m_%Y')}.txt",
                mime="text/plain"
            )

    st.markdown("---")
    col_provas, col_canais = st.columns(2, gap="large")

    with col_provas:
        st.subheader("📸 Checklist: O que guardar de prova?")
        st.markdown("""
            <div class="guia-card">
                Para garantir o reembolso ou indenização, reúna estas evidências no momento do ocorrido:<br><br>
                ✅ <strong>Foto do painel de voos/embarque</strong> mostrando o status de "Atrasado" ou "Cancelado".<br>
                ✅ <strong>Cartão de embarque, bilhete rodoviário ou voucher</strong> da reserva do hotel/pacote.<br>
                ✅ <strong>Notas fiscais e recibos</strong> de tudo o que você precisou gastar do próprio bolso (refeições, água, Uber/táxi, hotel, itens de higiene).<br>
                ✅ <strong>Número de protocolo</strong> do atendimento no balcão, SAC ou RIB (no caso de bagagem).<br>
                ✅ <strong>Prints de conversas</strong> no WhatsApp, chat do aplicativo ou e-mails trocados com a empresa.
            </div>
        """, unsafe_allow_html=True)

    with col_canais:
        st.subheader("🏛️ Onde registrar sua reclamação?")
        st.markdown("""
            <div class="canal-card">
                🌐 <a href="https://www.consumidor.gov.br" target="_blank">Consumidor.gov.br (Senacon / Governo Federal)</a><br>
                <span style="font-size: 0.9rem; color: #475569;">Canal oficial para resolver conflitos direto com aéreas, agências, viações e hotéis em até 10 dias.</span>
            </div>
            <div class="canal-card">
                ✈️ <a href="https://www.gov.br/anac/pt-br/canais_atendimento/fale-com-a-anac" target="_blank">ANAC — Agência Nacional de Aviação Civil</a><br>
                <span style="font-size: 0.9rem; color: #475569;">Fiscalização e normas sobre atrasos, cancelamentos, overbooking e bagagens em voos.</span>
            </div>
            <div class="canal-card">
                🚌 <a href="https://www.gov.br/antt/pt-br/canais_atendimento/ouvidoria" target="_blank">ANTT — Ouvidoria (Transporte Rodoviário)</a><br>
                <span style="font-size: 0.9rem; color: #475569;">Canal para denunciar viações de ônibus interestaduais (Tel: 166).</span>
            </div>
            <div class="canal-card">
                ⚖️ <a href="https://www.gov.br/mj/pt-br/assuntos/seus-direitos/consumidor" target="_blank">SENACON</a><br>
                <span style="font-size: 0.9rem; color: #475569;">Se a empresa não resolver, você pode exigir indenização gratuita no JEC (causas de até 20 salários mínimos não exigem advogado).</span>
            </div>
        """, unsafe_allow_html=True)

# ---------------------------------------------------------
# NOVA PÁGINA: DIREITOS DO VIAJANTE (FAQ COMPLETO)
# ---------------------------------------------------------
elif st.session_state["menu_state"] == "⚖️ Direitos do Viajante (FAQ)":
    col_nav1, col_nav2 = st.columns([1, 1])
    with col_nav1:
        st.button("🔙 Voltar para a Página Inicial", on_click=set_page, args=("🏠 Página Inicial",),
                  key="btn_voltar_faq")
    with col_nav2:
        st.button("🧳 Ir para o Gerador de Reclamação ➔", on_click=set_page,
                  args=("🧳 Área do Viajante",), key="btn_ir_gerador", type="primary", use_container_width=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.header("⚖️ Seus Direitos (FAQ Completo do Viajante)")
    st.info("Consulte abaixo de forma rápida o que dizem as leis da **ANAC**, **ANTT** e do **Código de Defesa do Consumidor (CDC)** para cada situação de viagem. Clique sobre o tema para abrir os detalhes:")

    with st.expander("✈️ O que diz a Lei sobre Voo Cancelado ou Atrasado?"):
        st.markdown("""
        **Base Legal:** Resolução nº 400 da ANAC e Código de Defesa do Consumidor (CDC).
- **A partir de 1 hora de atraso:** Direito à comunicação gratuita (internet Wi-Fi ou telefone).

- **A partir de 2 horas de atraso:** Direito à alimentação (voucher para lanche/refeição e bebidas).

- **A partir de 4 horas de atraso ou Cancelamento:** Você escolhe entre **reacomodação** gratuita (em voo próprio ou de outra companhia), **reembolso integral** (inclusive da tarifa de embarque) ou execução do serviço por outra modalidade (ex: ônibus/táxi).

- **Necessidade de Pernoite:** A companhia deve fornecer **hospedagem gratuita** e **transporte de ida e volta** até o hotel ou sua residência.
        """)

    with st.expander("✈️ Fui vítima de Overbooking (Preterição de Embarque). O que fazer?"):
        st.markdown("""
        **Base Legal:** Artigos 22 a 25 da Resolução nº 400 da ANAC.
- Ocorre quando a empresa vende mais passagens do que assentos disponíveis e nega o seu embarque.

- **Indenização Imediata:** Caso você não tenha se voluntariado para ceder o assento, a companhia aérea é obrigada a pagar imediatamente uma compensação financeira de **250 DES** (aprox. R$ 1.800 em voos domésticos) ou **500 DES** (aprox. R$ 3.600 em voos internacionais).

- **Assistência Completa:** Além da indenização, você continua tendo direito à reacomodação no próximo voo disponível, alimentação e hospedagem.
        """)

    with st.expander("🧳 Minhas malas sumiram ou foram danificadas!"):
        st.markdown("""
        **Base Legal:** Resolução nº 400 da ANAC / Resolução nº 4.282 da ANTT e CDC.
- **1º Passo Obrigatório:** Não saia da área de desembarque sem preencher o **RIB (Relatório de Irregularidade de Bagagem)** no guichê da companhia ou viação. Tire foto do protocolo e da etiqueta da mala.

- **Despesas de Emergência:** Se estiver fora da sua cidade, a empresa aérea deve pagar um auxílio imediato para compra de itens de higiene e roupas básicas. Guarde todas as notas fiscais.

- **Prazo para Localização:** Até **7 dias** em voos domésticos, **21 dias** em voos internacionais e até **30 dias** em viagens de ônibus. Após esse prazo, a empresa é obrigada a indenizar o passageiro.

- **Bagagem Danificada:** Comunique o dano imediatamente no desembarque (ou em até 7 dias após o voo) com fotos da avaria.
        """)

    with st.expander("🚌 Minha viagem de Ônibus Interestadual atrasou ou foi cancelada (ANTT)"):
        st.markdown("""
        **Base Legal:** Resolução nº 4.282/2014 da ANTT.
- **Mais de 1 hora de atraso:** Você pode exigir o **reembolso integral imediato** da passagem ou a realocação em outra empresa que faça o mesmo trecho, por conta da viação original.

- **Mais de 3 horas de atraso ou interrupção na estrada:** A empresa é obrigada a fornecer **alimentação** (lanche ou refeição) e, se não houver como seguir viagem no mesmo dia, **hospedagem gratuita**.

- **Remarcação / Devolução da passagem:** Com até 3 horas de antecedência do embarque, o passageiro pode pedir o reembolso (com retenção máxima de 5% a título de multa) ou remarcar o bilhete para até 1 ano.
        """)

    with st.expander("🏨 Tive problemas com o meu Hotel (Reserva não localizada, más condições)"):
        st.markdown("""
        **Base Legal:** Artigos 14, 20 e 35 do Código de Defesa do Consumidor (CDC) e Lei Geral do Turismo.
- **Overbooking Hoteleiro (Reserva não encontrada):** O hotel deve realocar você imediatamente em outro estabelecimento de **categoria igual ou superior**, pagando o transporte até o novo local e qualquer diferença de tarifa.

- **Propaganda Enganosa / Más Condições:** Se o quarto não tiver os itens contratados (ex: ar-condicionado quebrado, sujeira, falta de água), exija a troca imediata de acomodação, o abatimento proporcional do preço ou a devolução integral do valor pago.
        """)

    with st.expander("🌴 A Agência/Operadora alterou ou cancelou o meu Pacote de Viagem (CVC, Decolar, etc)"):
        st.markdown("""
        **Base Legal:** Artigos 7º, 14 e 25 do CDC (Responsabilidade Solidária).
- **Quem responde pelo problema?** Na compra de pacotes turísticos ou passagens intermediadas, **tanto a agência/plataforma online quanto a companhia aérea ou hotel respondem solidariamente** pelos prejuízos. A agência não pode se eximir empurrando a culpa apenas para o fornecedor.

- **Seus Direitos:** Exigir o cumprimento forçado da oferta exatamente como anunciado, aceitar outro pacote equivalente ou receber a restituição integral do valor atualizado, além de eventuais perdas e danos.
        """)

    with st.expander("🚗 Aluguel de Carro e Transfer (Cobranças indevidas ou veículo indisponível)"):
        st.markdown("""
        **Base Legal:** Artigos 30, 35 e 39 do Código de Defesa do Consumidor (CDC).
- **Veículo indisponível na retirada:** Se você reservou uma categoria de carro e a locadora não tiver o veículo na hora, ela deve fornecer um modelo de **categoria superior (upgrade) pelo mesmo preço** contratado.

- **Vistoria na retirada e devolução:** Faça sempre vídeos e fotos da lataria, pneus, estepe e nível de combustível antes de sair da locadora e no momento da entrega.

- **Cobranças abusivas no cartão (Caução):** A locadora não pode lançar cobranças de avarias ou multas sem comprovação prévia e sem o laudo assinado na vistoria de devolução.
        """)

    with st.expander("💳 Direito de Arrependimento (24h/7 dias) e Taxas Abusivas de Cancelamento"):
        st.markdown("""
        **Base Legal:** Art. 11 da Resolução nº 400 da ANAC e Art. 49 do CDC.
- **Regra das 24 horas (Passagens Aéreas):** Você pode desistir da compra de qualquer passagem aérea em até **24 horas após o recebimento do comprovante**, sem qualquer custo (reembolso de 100%), desde que a compra tenha sido feita com pelo menos **7 dias de antecedência** da data do voo.

- **Compras Online de Hotéis e Pacotes (Art. 49 do CDC):** Para reservas de hospedagem e pacotes comprados pela internet ou telefone, o consumidor tem até **7 dias corridos** a partir da compra para desistir e receber 100% do valor de volta.

- **Multas Abusivas:** Cláusulas que retêm 80% a 100% do valor pago em caso de cancelamento com antecedência razoável são consideradas abusivas pela Justiça (Art. 51 do CDC).
        """)

# ---------------------------------------------------------
# DASHBOARD DA AGÊNCIA (POWER BI EMBARCADO)
# ---------------------------------------------------------
elif st.session_state["menu_state"] == "📊 Dashboard Agência":
    botao_voltar()  # Adiciona o botão de voltar no topo

    st.header("📊 Monitoramento B2B de Qualidade de Dados")
    st.write("Visão Gerencial Integrada (Pipeline: Python Pandas -> MySQL Star Schema -> Power BI).")

    # Link convertido para o formato de incorporação (reportEmbed) com o ID do seu relatório
    LINK_DO_SEU_POWER_BI = "https://app.powerbi.com/reportEmbed?reportId=62c559f6-85ef-4989-aa4c-8c7e008fc095&autoAuth=true&pageName=d93bde49e35911c10e11"

    # Sem o width="100%" (omitindo esse parâmetro, ele já ocupa 100% da largura sem dar erro)
    components.iframe(LINK_DO_SEU_POWER_BI, height=650, scrolling=True)

    st.markdown(
        '<div style="text-align: right; margin-top: 0.5rem;">'
        '<a href="https://app.powerbi.com/groups/me/reports/62c559f6-85ef-4989-aa4c-8c7e008fc095/d93bde49e35911c10e11?experience=power-bi" '
        'target="_blank" style="color: #003366; font-weight: 700; text-decoration: none;">'
        '🔗 Abrir painel em tela cheia no Power BI ➔</a></div>',
        unsafe_allow_html=True
    )

# ---------------------------------------------------------
# SOBRE O PROJETO (INTEGRANTES)
# ---------------------------------------------------------
elif st.session_state["menu_state"] == "ℹ️ Sobre o Projeto":
    botao_voltar()  # Adiciona o botão de voltar no topo

    st.header("ℹ️ Sobre o Projeto DataTour Analytics")

    st.markdown("""
        <div class="sobre-card">
            A plataforma <strong>DataTour Analytics</strong> é um <strong>Produto Mínimo Viável (MVP)</strong> desenvolvido como Trabalho de Conclusão de Curso (Projeto Integrador) do <strong>Curso Técnico em Ciência de Dados</strong> do SENAC-DF.<br><br>
            O nosso principal foco tecnológico foi arquitetar uma solução completa de engenharia de dados — abrangendo extração, tratamento com <strong>Python (Pandas)</strong>, validação de qualidade com <strong>Great Expectations</strong>, modelagem dimensional <strong>Star Schema em MySQL</strong> e visualização analítica via <strong>Power BI</strong> — para estancar a degradação e elevar a confiabilidade dos registros públicos e corporativos de turismo.
        </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="secao-titulo">🎓 Equipe Técnica de Ciência de Dados (Turma 108)</div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="membro-card">🔹 Bárbara Cavalcanti</div>', unsafe_allow_html=True)
        st.markdown('<div class="membro-card">🔹 Cláudia Santos</div>', unsafe_allow_html=True)
        st.markdown('<div class="membro-card">🔹 Daiana Ribeiro</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="membro-card">🔹 Evanildo Silva</div>', unsafe_allow_html=True)
        st.markdown('<div class="membro-card">🔹 Luis Eduardo Sousa</div>', unsafe_allow_html=True)

    st.markdown('<div class="secao-titulo">👨‍🏫 Orientação</div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="orientacao-card">
            Deixamos um agradecimento especial aos professores e instrutores <strong>Diego Lohan</strong> e <strong>Cleiton Sousa</strong> (SENAC-DF) por toda a base técnica e apoio ao longo da formação.
        </div>
    """, unsafe_allow_html=True)