import streamlit as st 

# 🎨 Configuración estética de la página
st.set_page_config(
    page_title="Calculadora de Costos por Evento",
    page_icon="📊",
    layout="centered"
)

# 💅 Estilo CSS personalizado
st.markdown(
    """
    <style>
    .title {
        font-size: 36px;
        font-weight: bold;
        color: #004080;
        text-align: center;
    }
    div.stButton > button {
        background-color: #ff4b4b;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        height: 3em;
        width: 100%;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 🧾 Título principal
st.markdown('<div class="title">📊 Calculadora de Costos por Evento</div>', unsafe_allow_html=True)
st.markdown("---")

# 📥 Entradas del usuario
st.header("🔧 Datos del evento")

Horas_mensuales = 180

# 📝 Sueldo mínimo editable
Sueldo_Minimo = st.number_input("Sueldo mínimo mensual ($)", min_value=0, value=529000, step=1000)

Horas_Trabajadas = st.number_input("Horas trabajadas", min_value=0)
Viatico = st.number_input("Viático por persona", min_value=0)
Transporte_equipo = st.number_input("Costo de transporte del equipo", min_value=0)
Mantencion_maquinas = st.number_input("Costo de mantención de máquinas", min_value=0)
Materiales = st.number_input("Costo de materiales", min_value=0)
Ganancia = st.number_input("Porcentaje de ganancia (%)", min_value=0)

# 🔘 Botón para calcular
if st.button("Calcular"):
    Pago = int(Sueldo_Minimo / Horas_mensuales * Horas_Trabajadas)
    Variable = Viatico + Transporte_equipo + Mantencion_maquinas + Materiales + Pago

    Seguro = 2000
    Hosting = 3000
    Gestion = 5000
    Fijo = Seguro + Hosting + Gestion

    Total = Variable + Fijo
    SIVA = int(Total * (1 + Ganancia / 100))
    CIVA = int(SIVA * 1.19)

    # 📊 Resultados
    st.markdown("---")
    st.subheader("📈 Resultados del cálculo")

    st.success(f"💰 Pago al validador: ${Pago:,}")
    st.info(f"📦 Costo variable: ${Variable:,}")
    st.info(f"🏢 Costo fijo: ${Fijo:,}")
    st.warning(f"🧾 Costo total (sin ganancia): ${Total:,}")
    st.success(f"💼 Costo sin IVA (con ganancia): ${SIVA:,}")
    st.error(f"🧮 Costo con IVA (19%): ${CIVA:,}")
