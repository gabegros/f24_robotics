#file_path = '/home/gabe/Desktop/Trials Text Files/Trial3.txt'  # Update with your actual file path
import matplotlib.pyplot as plt
import numpy as np
# Open the log file
file_path = '/home/gabe/cs460_proj3/Trial Positions/trial3.txt'  # Update with your actual file path
x_coords = []
y_coords = []

try:
    with open(file_path, 'r') as file:
        for line in file:
            # Strip whitespace and split by comma
            values = line.strip().split(',')
            if len(values) == 2:  # Ensure there are both x and y values
                x = float(values[0].strip())  # Convert x to float
                y = float(values[1].strip())  # Convert y to float
                x_coords.append(x)
                y_coords.append(y)

except FileNotFoundError:
    print("File not found. Please check the path and try again.")
except ValueError:
    print("Error in converting values to float. Please check the file format.")

# Check if coordinates were extracted
if not x_coords or not y_coords:
    print("No valid coordinates were extracted from the file.")
else:
    
    distances = np.sqrt(np.diff(x_coords)**2 + np.diff(y_coords)**2)  # Euclidean distance
    total_distance = np.sum(distances)

    print(f"Total Path Distance: {total_distance:.2f} units")  # Print total distance
    # Plot the robot's path with no grid, labels, or title
    plt.figure()
    plt.plot(y_coords, x_coords, 'o', color='black', markersize=5)  # 'o' for dots only
    #blue, red, green, orange, purple
    plt.axis('equal')  # Keep the aspect ratio equal
    plt.axis('off')    # Turn off the axis
    plt.show()
    
    plt.savefig('home/gabe/cs460_proj3/Trial Photos/trial3.png', transparent=True, bbox_inches='tight')
