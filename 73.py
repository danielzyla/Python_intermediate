import functools
import time

@functools.lru_cache(maxsize=100)
def fib(n):
    
    if n <= 2:
        result = n
    else:
        result = fib(n-1) + fib(n-2)
        
    return result

start = time.time()

for i in range(1,36):
  result = fib(i)
  parttime = time.time()
  print('Result for number {} is {} and it lasted {}:'.format(i, result, parttime-start))

end = time.time()

print('Time of processing: ', end-start)

print(fib.cache_info())
