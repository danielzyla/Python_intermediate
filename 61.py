import time
import functools

def func_time_span(func):
  def time_span(*args,**kwargs):
    start=time.time()
    v = func(*args, **kwargs)
    end=time.time()
    timespan = end - start
    print('The function "{}" lasted {} '.format(func.__name__, timespan))
    return v
  return time_span

def get_sequence(n):
    
    if n <= 0:
        return 1
    else:
        v = 0
        for i in range(n):
            v += 1 + (get_sequence(i - 1) + get_sequence(i))/2
        return v

x=func_time_span(get_sequence)

print(x(18))