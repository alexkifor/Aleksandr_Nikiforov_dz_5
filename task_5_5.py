import sys
import time
# вариант "в лоб"
start = time.perf_counter()
result = []
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
for i in src:
    if src.count(i) == 1:
        result.append(i)
end = time.perf_counter()
print(result, sys.getsizeof(result), f'{end - start} сек.')
# оптимизированный вариант
start = time.perf_counter()
result = [num for num in src if src.count(num) == 1]
end = time.perf_counter()
print(result, sys.getsizeof(result), f'{end - start} сек.')
