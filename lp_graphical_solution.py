import matplotlib.pyplot as plt

def plot_individual_graphs(points_list):
    """
    Creates separate line graphs for each pair or set of points.

    Args:
    points_list (list): A list where each element is a list of points [(x1, y1), (x2, y2)].

    Returns:
    None
    """
    for i, points in enumerate(points_list):
        x, y = zip(*points)  # Extract x and y coordinates
        plt.figure(figsize=(6, 4))
        plt.plot(x, y, marker='o', label=f'Line Graph {i+1}')
        plt.title(f"Graph {i+1}")
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)
        plt.grid(color='gray', linestyle='--', linewidth=0.5)
        plt.legend()
        plt.show()

# Define the points for each problem
points_list = [
    [(6, 4), (8, 4)],      # Problem 1
    [(6, 3), (2.5, 5)],    # Problem 2
    [(10, 20), (18, 18), (10, 15)],  # Problem 3
    [(15, 7), (20, 10)],   # Problem 4
    [(3, 3), (4, 6)],      # Problem 5
    [(4, 6), (8, 4)]       # Problem 6
]

# Generate separate line graphs
plot_individual_graphs(points_list)
