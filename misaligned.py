
def get_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    mapping = []
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            mapping.append(f'{i * 5 + j} | {major} | {minor}')
    return mapping

def print_color_map():
    for entry in get_color_map():
        print(entry)
    return len(get_color_map())

# Strengthened test: check the first mapping value for correct alignment
mapping = get_color_map()
assert(mapping[0] == '0 | White | Blue')  # This will pass, but let's check a misaligned value
assert(mapping[5] == '5 | Red | Blue')   # This should fail if misaligned
result = print_color_map()
assert(result == 25)
print("All is well (maybe!)")
