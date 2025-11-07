from sample import checks


def add(a, b):
    out = a + b
    assert checks.is_int(out)
    return a + b
