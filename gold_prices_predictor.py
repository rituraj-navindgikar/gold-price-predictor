import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.statespace.sarimax import SARIMAX
import json

# Load Data
file_path = "gold_prices.json"
with open(file_path, "r") as file:
    data = json.load(file)

# Convert JSON to DataFrame
df = pd.DataFrame([(date, info["price"]) for date, info in data.items()], columns=["Date", "Price"])
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

# Train SARIMA Model
model = SARIMAX(df["Price"], order=(1, 1, 1), seasonal_order=(1, 1, 1, 365))
model_fit = model.fit(disp=True)

# Forecast next 30 days
# forecast = model_fit.forecast(steps=30)

# Plot Forecast
plt.figure(figsize=(10, 5))
# plt.plot(df.index, df["Price"], label="Actual Prices", color="blue")
# plt.plot(pd.date_range(df.index[-1], periods=30, freq='D'), forecast, label="Forecast", linestyle="dashed", color="red")
# plt.xlabel("Date")
# plt.ylabel("Gold Price")
# plt.title("Gold Price Prediction Using SARIMA")
# plt.legend()
# plt.show()
