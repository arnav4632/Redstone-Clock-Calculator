import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# we exclude x<=2, we would never use a hopper dropper chained clock for less time wanted
data = [[3,3,216],[64,64,129536],[320,16,163456],[320,3,30648],[320,5,51080],[10,20,5920]  
]
df = pd.DataFrame(data, columns=['x1', 'x2', 'y'])

# 2. Train the polynomial regression model
poly = PolynomialFeatures(degree=2, include_bias=False)
X_poly = poly.fit_transform(df[['x1', 'x2']])
model = LinearRegression().fit(X_poly, df['y'])

# --- NEW: Extract R², Coefficients, and Equation ---
r2_score = model.score(X_poly, df['y'])
intercept = model.intercept_
coefs = model.coef_
feature_names = poly.get_feature_names_out(['x1', 'x2'])

print("--- Model Metrics & Coefficients ---")
print(f"R² Score: {r2_score:.4f}")
print(f"Intercept: {intercept:.4f}")
print("Coefficients:")
for name, coef in zip(feature_names, coefs):
    print(f"  {name}: {coef:.4f}")

# Constructing the equation string dynamically
equation = f"y = {intercept:.2f}"
for name, coef in zip(feature_names, coefs):
    equation += f" + ({coef:.2f} * {name})"
print(f"\nFull Equation:\n{equation}\n")
# --------------------------------------------------

# --- NEW: Predict a New Value ---
# Define your new custom inputs here: [x1, x2]
new_input = np.array([[50, 15]]) 
new_input_poly = poly.transform(new_input)
predicted_y = model.predict(new_input_poly)[0]

print("--- New Prediction ---")
print(f"For x1={new_input[0][0]}, x2={new_input[0][1]} -> Predicted y = {predicted_y:.2f}\n")
# --------------------------------------------------

# 3. Create a 2D meshgrid grid to generate the surface coordinates
x1_range = np.linspace(df['x1'].min(), df['x1'].max(), 50)
x2_range = np.linspace(df['x2'].min(), df['x2'].max(), 50)
X1_grid, X2_grid = np.meshgrid(x1_range, x2_range)

# 4. Flatten grid and predict 'y' values across the grid surface
grid_points = np.c_[X1_grid.ravel(), X2_grid.ravel()]
grid_poly = poly.transform(grid_points)
Y_grid_pred = model.predict(grid_poly).reshape(X1_grid.shape)

# 5. Initialize the 3D plot
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Plot actual data points (Scatter plot)
ax.scatter(df['x1'], df['x2'], df['y'], color='red', s=50, label='Actual Data', zorder=5)

# Plot predicted regression model (Surface plot)
surface = ax.plot_surface(X1_grid, X2_grid, Y_grid_pred, cmap='viridis', alpha=0.6)

# --- NEW: Plot the Predicted Point ---
ax.scatter(new_input[0][0], new_input[0][1], predicted_y, color='blue', marker='*', s=200, label='New Prediction', zorder=10)

# Labels and configuration
ax.set_xlabel('Input 1 (x1)')
ax.set_ylabel('Input 2 (x2)')
ax.set_zlabel('Output (y)')
ax.set_title('3D Polynomial Regression Surface Fit')
ax.legend()

plt.show()