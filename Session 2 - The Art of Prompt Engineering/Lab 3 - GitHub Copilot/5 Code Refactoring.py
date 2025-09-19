def calculate_area_and_perimeter(shape, dimensions):
    if shape == 'rectangle':
        length, width = dimensions
        area = length * width
        perimeter = 2 * (length + width)
        return area, perimeter
    elif shape == 'circle':
        radius = dimensions[0]
        area = 3.14159 * radius * radius
        perimeter = 2 * 3.14159 * radius
        return area, perimeter
    elif shape == 'triangle':
        base, height = dimensions
        area = 0.5 * base * height
        perimeter = 'Not implemented'
        return area, perimeter
    else:
        return 'Invalid shape', 'Invalid shape'

# Example usage
print(calculate_area_and_perimeter('rectangle', (5, 10)))
print(calculate_area_and_perimeter('circle', (7,)))
print(calculate_area_and_perimeter('triangle', (6, 8)))
print(calculate_area_and_perimeter('hexagon', (6,)))
