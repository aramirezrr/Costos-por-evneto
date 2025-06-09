import streamlit as st

st.title("Calculadora de Costos por Evento")

Horas_mensuales = 180
Sueldo_Minimo = 529000

Horas_Trabajadas = st.number_input("Horas trabajadas", min_value=0)
Viatico = st.number_input("Viático por persona", min_value=0)
Transporte_equipo = st.number_input("Costo de transporte del equipo", min_value=0)
Mantencion_maquinas = st.number_input("Costo de mantención de máquinas", min_value=0)
Materiales = st.number_input("Costo de materiales", min_value=0)
Ganancia = st.number_input("Porcentaje de ganancia (%)", min_value=0)

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

    st.subheader("Resultados:")
    st.write(f"Pago al validador: ${Pago}")
    st.write(f"Costo variable: ${Variable}")
    st.write(f"Costo fijo: ${Fijo}")
    st.write(f"Costo total: ${Total}")
    st.write(f"Costo sin IVA: ${SIVA}")
    st.write(f"Costo con IVA: ${CIVA}")
