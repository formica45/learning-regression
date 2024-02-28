import numpy as np
import matplotlib.pyplot as plt

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

# Initialize FIFO dataset
fifo_size = 50  # Size of the FIFO dataset
x_all = 2.5 * np.random.randn(fifo_size) + 1.5
y_all = 2 + 0.3 * x_all + 0.5 * np.random.randn(fifo_size)

plt.figure(figsize=(10, 6))
plt.ion()

for update_count in range(1000):  # Arbitrary large number for continuous updates
    # Update FIFO dataset
    new_x = 2.5 * np.random.randn(1) + 1.5
    new_y = 2 + 0.3 * new_x + 0.5 * np.random.randn(1)
    x_all = np.append(x_all[1:], new_x)  # Remove the oldest, add the newest
    y_all = np.append(y_all[1:], new_y)
    
    beta_0, beta_1 = calculate_slope_intercept(x_all, y_all)
    if beta_0 is not None and beta_1 is not None:
        y_pred = beta_0 + beta_1 * x_all
        plt.clf()
        plt.scatter(x_all, y_all, color='blue')
        plt.plot(x_all, y_pred, color='red')

        # Draw residual lines for each data point
        for xi, yi, ypi in zip(x_all, y_all, y_pred):
            plt.plot([xi, xi], [yi, ypi], color='grey', linestyle='--', linewidth=1)

        # Add text for b0 and b1
        plt.text(0.05, 0.95, f'b0 (intercept): {beta_0:.2f}\nb1 (slope): {beta_1:.2f}', 
                 transform=plt.gca().transAxes, fontsize=9, verticalalignment='top', 
                 bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

        plt.xlim(np.min(x_all) - 1, np.max(x_all) + 1)
        plt.ylim(np.min(y_all) - 1, np.max(y_all) + 1)
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Linear Regression Fit with FIFO Data Set')
        plt.draw()
        plt.pause(0.05)

plt.ioff()
plt.show()

