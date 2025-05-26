
import streamlit as st
import pandas as pd

st.title("Pavement Life Prediction from ESALs")
st.write("This tool estimates when a roadway segment will reach its pavement design limit based on traffic inputs.")

# Default values
stations = [1000, 2000, 3000, 4000, 5000]

# User-adjustable global values
design_esals = st.number_input("Design ESALs", value=10_000_000, step=100_000)
growth_rate = st.slider("Traffic Growth Rate (%)", 0.0, 5.0, 2.0) / 100

# Table input for each segment
st.write("### Segment Traffic Inputs")
segment_data = []
for station in stations:
    st.subheader(f"Station {station} ft")
    aadt = st.number_input(f"AADT for {station}", value=18000, key=f"aadt_{station}")
    truck_pct = st.slider(f"Truck % for {station}", 0, 50, 10, key=f"truck_{station}")
    esal_factor = st.slider(f"Truck ESAL Factor for {station}", 1.0, 2.0, 1.5, step=0.1, key=f"esal_{station}")
    cumulative_esals = st.number_input(f"Cumulative ESALs for {station}", value=6_000_000, step=100_000, key=f"cum_{station}")

    segment_data.append({
        "Station": station,
        "AADT": aadt,
        "Truck_%": truck_pct,
        "ESAL_Factor": esal_factor,
        "Cumulative_ESALs": cumulative_esals,
        "Design_ESALs": design_esals,
        "Growth_Rate": growth_rate
    })

df = pd.DataFrame(segment_data)

# Prediction logic
def estimate_failure_year(row, current_year=2025):
    esals = row["Cumulative_ESALs"]
    annual_esals = row["AADT"] * 365 * (row["Truck_%"] / 100) * row["ESAL_Factor"]
    year = current_year
    while esals < row["Design_ESALs"]:
        esals += annual_esals
        annual_esals *= (1 + row["Growth_Rate"])
        year += 1
    return year

df["Failure_Year"] = df.apply(estimate_failure_year, axis=1)
df["Years_Remaining"] = df["Failure_Year"] - 2025

st.write("### Pavement Failure Projection")
st.dataframe(df[["Station", "Failure_Year", "Years_Remaining"]])

st.markdown("---")
st.caption("Built with Streamlit for digital twin pavement modeling.")
