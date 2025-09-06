# misaligned.py

def print_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            print(f'{i * 5 + j} | {major} | {minor}')
    return len(major_colors) * len(minor_colors)


# ===== Strengthened failing tests =====
def _capture_print_color_map_lines():
    from io import StringIO
    import sys
    buf = StringIO()
    old = sys.stdout
    try:
        sys.stdout = buf
        print_color_map()
    finally:
        sys.stdout = old
    return [line.strip() for line in buf.getvalue().strip().splitlines() if line.strip()]

def test_color_map_alignment_and_indexing():
    """Expect 1-based numbering and properly placed separators."""
    lines = _capture_print_color_map_lines()
    # Expect first and last entries to be precisely formatted
    # Buggy function starts from 0 and misaligns expectations -> must FAIL
    assert lines[0] == '1 | White | Blue'
    assert lines[-1] == '25 | Violet | Slate'
    # Also verify total count (this part would pass, kept for completeness)
    assert len(lines) == 25


if __name__ == "__main__":
    result = print_color_map()
    assert(result == 25)
    test_color_map_alignment_and_indexing()
    print("All is well (maybe!)")
