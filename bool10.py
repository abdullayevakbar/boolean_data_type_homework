def main(a):
    """check that the number "a" is a perfect square.
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    from math import sqrt
    b = sqrt(a)
    b = int(b)
    return (b*b == a)
