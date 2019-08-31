from datetime import datetime
 

start = datetime(2019, 1, 1, 0, 0, 0)  
end  = datetime.now()
 
  


def Create_Function(unit):
  func='''
def time_span(start,end):
  duration = end-start
  duration_in_s = duration.total_seconds()
  return divmod(duration_in_s, {})[0]
  '''.format(unit)

  exec(func, globals())
  return time_span
  
time_span_m = Create_Function(60)
time_span_h = Create_Function(3600)
time_span_d = Create_Function(86400)

print(time_span_m(start, end))
print(time_span_h(start, end))
print(time_span_d(start, end))  
