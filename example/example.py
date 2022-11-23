from memory_profiler import profile

@profile
def profile_func():
    a = []
    for i in range(100):
        a.append(2**i)
    return a


if __name__ == '__main__':
    profile_func()