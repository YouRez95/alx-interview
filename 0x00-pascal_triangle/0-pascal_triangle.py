def pascal_triangle(n):
    if n <= 0:
        return []
    if n == 1:
        return [[1]]
    if n > 1:
        return [n for n in pascal_triangle(n - 1)]
    

print(pascal_triangle(6))