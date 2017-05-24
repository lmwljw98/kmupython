import time

def fibonachi(n):
    if n == 1 or n == 2:
        return 1

    else:
        return fibonachi(n-1) + fibonachi(n-2)

n = 40

start = time.time()
print(n, fibonachi(n))
end = time.time()
print(end - start, "Seconds")
