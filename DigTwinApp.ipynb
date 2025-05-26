{
 "cells": [
  {
   "metadata": {
    "trusted": true
   },
   "cell_type": "code",
   "source": "import streamlit as st\nimport pandas as pd\n\nst.title(\"Pavement Life Prediction from ESALs\")\nst.write(\"This tool estimates when a roadway segment will reach its pavement design limit based on traffic inputs.\")\n\n# Default values\nstations = [1000, 2000, 3000, 4000, 5000]\n\n# User-adjustable global values\ndesign_esals = st.number_input(\"Design ESALs\", value=10_000_000, step=100_000)\ngrowth_rate = st.slider(\"Traffic Growth Rate (%)\", 0.0, 5.0, 2.0) / 100\n\n# Table input for each segment\nst.write(\"### Segment Traffic Inputs\")\nsegment_data = []\nfor station in stations:\n    st.subheader(f\"Station {station} ft\")\n    aadt = st.number_input(f\"AADT for {station}\", value=18000, key=f\"aadt_{station}\")\n    truck_pct = st.slider(f\"Truck % for {station}\", 0, 50, 10, key=f\"truck_{station}\")\n    esal_factor = st.slider(f\"Truck ESAL Factor for {station}\", 1.0, 2.0, 1.5, step=0.1, key=f\"esal_{station}\")\n    cumulative_esals = st.number_input(f\"Cumulative ESALs for {station}\", value=6_000_000, step=100_000, key=f\"cum_{station}\")\n    \n    segment_data.append({\n        \"Station\": station,\n        \"AADT\": aadt,\n        \"Truck_%\": truck_pct,\n        \"ESAL_Factor\": esal_factor,\n        \"Cumulative_ESALs\": cumulative_esals,\n        \"Design_ESALs\": design_esals,\n        \"Growth_Rate\": growth_rate\n    })\n\ndf = pd.DataFrame(segment_data)\n\n# Prediction logic\ndef estimate_failure_year(row, current_year=2025):\n    esals = row[\"Cumulative_ESALs\"]\n    annual_esals = row[\"AADT\"] * 365 * (row[\"Truck_%\"] / 100) * row[\"ESAL_Factor\"]\n    year = current_year\n    while esals < row[\"Design_ESALs\"]:\n        esals += annual_esals\n        annual_esals *= (1 + row[\"Growth_Rate\"])\n        year += 1\n    return year\n\ndf[\"Failure_Year\"] = df.apply(estimate_failure_year, axis=1)\ndf[\"Years_Remaining\"] = df[\"Failure_Year\"] - 2025\n\nst.write(\"### Pavement Failure Projection\")\nst.dataframe(df[[\"Station\", \"Failure_Year\", \"Years_Remaining\"]])\n\nst.markdown(\"---\")\nst.caption(\"Built with Streamlit for digital twin pavement modeling.\")",
   "execution_count": 1,
   "outputs": [
    {
     "output_type": "error",
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'streamlit'",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-1-23793bfa8225>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0;32mimport\u001b[0m \u001b[0mstreamlit\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mst\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      2\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mpandas\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mpd\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0mst\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mtitle\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Pavement Life Prediction from ESALs\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0mst\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mwrite\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"This tool estimates when a roadway segment will reach its pavement design limit based on traffic inputs.\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'streamlit'"
     ]
    }
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "name": "python3",
   "display_name": "Python 3",
   "language": "python"
  },
  "language_info": {
   "name": "python",
   "version": "3.10.4",
   "mimetype": "text/x-python",
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "pygments_lexer": "ipython3",
   "nbconvert_exporter": "python",
   "file_extension": ".py"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}