import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
np.random.seed(42)
n_hours = 1000
time = np.arange(n_hours)
# Simulate a temperature time series with daily and seasonal patterns
daily_pattern = 10 * np.sin(2 * np.pi * time / 24)
seasonal_pattern = 15 * np.sin(2 * np.pi * time / (24  * 365 / 12))
trend = 0.01 * time
noise = np.random.normal(0, 2, n_hours)
temperature = 20 + daily_pattern + seasonal_pattern + trend + noise
data = pd.DataFrame({'Temperature': temperature}, index=pd.date_range(start='2020-01-01', periods=n_hours, freq='H'))
data['Temperature'].plot(title="Simulated Temperature Time Series")
print(data.head())
plt.figure(figsize=(10, 5))
plt.plot(data.index, data['Temperature'], label='Temperature (°C)', color='orange')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Simulated Temperature Time Series')
plt.legend()
plt.grid()
plt.show() 

