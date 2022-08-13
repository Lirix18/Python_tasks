from time import perf_counter
from sys import getsizeof

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# result = [12, 44, 4, 10, 78, 123]


start = perf_counter()
result = [src[i] for i in range(1, len(src)) if src[i] > src[i-1]]
print(result, 'Time:', perf_counter() - start, 'Size:', getsizeof(result))

start2 = perf_counter()
result2 = [elem2 for (elem1, elem2) in zip(src[:-1], src[1:]) if elem1 < elem2]  # быстрее
print(result2, 'Time:', perf_counter() - start2, 'Size:', getsizeof(result2))
