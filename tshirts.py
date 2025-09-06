# tshirts.py

def size(cms):
    if cms < 38:
        return 'S'
    elif cms > 38 and cms < 42:
        return 'M'
    else:
        return 'L'


# ===== Strengthened failing tests =====
# The classification leaves out cms == 38. We expect it to be 'M'.
# The current code returns 'L' for 38 -> this test must FAIL.
assert(size(37) == 'S')
assert(size(38) == 'M')  # should fail with current implementation
assert(size(40) == 'M')
assert(size(43) == 'L')
print("All is well (maybe!)")
