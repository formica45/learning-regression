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
x_all = 2.5 * np.random.randn(fifo_size) + 1.5  # Initial dataset
y_all = 2 + 0.3 * x_all + 0.5 * np.random.randn(fifo_size)  # Dependent on x_all with some noise

plt.figure(figsize=(10, 6))
plt.ion()  # Turn the interactive mode on

while True:  # This loop will run forever
    new_x = 2.5 * np.random.randn(1) + 1.5  # Generate a new x value
    new_y = 2 + 0.3 * new_x + 0.5 * np.random.randn(1)  # Generate a new y value based on new_x
    x_all = np.append(x_all[1:], new_x)  # Update x_all by removing the oldest value and adding new_x
    y_all = np.append(y_all[1:], new_y)  # Update y_all similarly
    
    beta_0, beta_1 = calculate_slope_intercept(x_all, y_all)  # Calculate new slope and intercept
    if beta_0 is not None and beta_1 is not None:
        y_pred = beta_0 + beta_1 * x_all  # Calculate predicted y values
        plt.clf()  # Clear the current figure
        plt.scatter(x_all, y_all, color='blue')  # Plot the actual data points
        plt.plot(x_all, y_pred, color='red')  # Plot the regression line

        # Draw residual lines for each data point
        for xi, yi, ypi in zip(x_all, y_all, y_pred):
            plt.plot([xi, xi], [yi, ypi], color='grey', linestyle='--', linewidth=1)

        # Display the slope and intercept on the plot
        plt.text(0.05, 0.95, f'b0 (intercept): {beta_0:.2f}\nb1 (slope): {beta_1:.2f}', 
                 transform=plt.gca().transAxes, fontsize=9, verticalalignment='top', 
                 bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

        plt.xlim(np.min(x_all) - 1, np.max(x_all) + 1)  # Set x-axis limits
        plt.ylim(np.min(y_all) - 1, np.max(y_all) + 1)  # Set y-axis limits
        plt.xlabel('X')  # Label x-axis
        plt.ylabel('Y')  # Label y-axis
        plt.title('Linear Regression Fit with FIFO Data Set')  # Set title
        plt.draw()  # Redraw the current figure
        plt.pause(0.1)  # Pause for a short moment to update the plot

plt.ioff()  # Turn the interactive mode off
plt.show()  # Show the plot
