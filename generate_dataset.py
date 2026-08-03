import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Number of samples
n = 1000

# Generate features
age = np.random.randint(1, 100, n)  # Age in years
crack_width = np.random.uniform(0, 20, n)  # Crack width in mm
vibration = np.random.uniform(0, 50, n)  # Vibration level in Hz
load_stress = np.random.uniform(10, 100, n)  # Load stress %
weather_impact = np.random.randint(1, 11, n)  # Weather impact scale 1-10
maintenance_score = np.random.randint(1, 11, n)  # Maintenance score 1-10

# Risk logic (IMPORTANT – makes data realistic)
failure_risk = (
    (age > 50).astype(int) +
    (crack_width > 10).astype(int) +
    (vibration > 25).astype(int) +
    (load_stress > 70).astype(int) +
    (weather_impact > 7).astype(int) -
    (maintenance_score > 7).astype(int)
)

# Convert to binary (0 or 1)
failure_risk = (failure_risk > 2).astype(int)

# Create dataframe
data = pd.DataFrame({
    "Age": age,
    "CrackWidth": crack_width,
    "VibrationLevel": vibration,
    "LoadStress": load_stress,
    "WeatherImpact": weather_impact,
    "MaintenanceScore": maintenance_score,
    "FailureRisk": failure_risk
})

# Save to CSV
data.to_csv("structurex_dataset.csv", index=False)

print("Dataset created successfully!")
print(data.head())