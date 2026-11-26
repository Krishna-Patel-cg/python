def stop_at_zero(n):
    if n == 0:
        return 8

    return stop_at_zero(n - 1)
print(stop_at_zero(5))