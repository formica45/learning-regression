import numpy as np
import matplotlib.pyplot as plt
import time

def calculate_slope_intercept(x_vals, y_vals):
    if len(x_vals) < 2:
        return None, None
    x_mean = np.mean(x_vals)
    y_mean = np.mean(y_vals)
    cov_xy = np.sum((x_vals - x_mean) * (y_vals - y_mean))
    var_x = np.sum((x_vals - x_mean)**2)
    if var_x == 0:
        return None, None
    else:
        beta_1 = cov_xy / var_x
        beta_0 = y_mean - (beta_1 * x_mean)
        return beta_0, beta_1

plt.figure(figsize=(10, 6))
plt.ion()

while True:
    np.random.seed()  # Use current time as random seed for each iteration
    total_points = 100
    x_all = 2.5 * np.random.randn(total_points) + 1.5
    res_all = 0.5 * np.random.randn(total_points)
    y_all = 2 + 0.3 * x_all + res_all
    
    for i in range(1, total_points + 1):
        x = x_all[:i]
        y = y_all[:i]
        beta_0, beta_1 = calculate_slope_intercept(x, y)
        
        if beta_0 is not None and beta_1 is not None:
            y_pred = beta_0 + beta_1 * x
            plt.clf()
            plt.scatter(x, y, color='blue')
            plt.plot(x, y_pred, color='red')

            # Draw residual lines for each data point
            for xi, yi, ypi in zip(x, y, y_pred):
                plt.plot([xi, xi], [yi, ypi], color='grey', linestyle='--', linewidth=1)

            # Add text for b0 and b1
            plt.text(0.05, 0.95, f'b0 (intercept): {beta_0:.2f}\nb1 (slope): {beta_1:.2f}', 
                     transform=plt.gca().transAxes, fontsize=9, verticalalignment='top', 
                     bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

            plt.xlim(np.min(x_all) - 1, np.max(x_all) + 1)
            plt.ylim(np.min(y_all) - 1, np.max(y_all) + 1)
            plt.xlabel('X')
            plt.ylabel('Y')
            plt.title(f'Linear Regression Fit with {i} Data Points')
            plt.draw()
            plt.pause(0.1)
    
    time.sleep(5 - 0.1)  # Adjust for the time spent on plotting

