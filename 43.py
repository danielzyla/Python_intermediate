import math, time

formulas_list = [
     "abs(x**3 - x**0.5)",
     "abs(math.sin(x) * x**2)"
     ]

argument_list = []
for i in range (1000000):
    argument_list.append(i/10)
    i += 1

for formula in formulas_list:
    results_list = []
    print(formula)
    start = time.time()
    for x in argument_list:
        results_list.append(eval(formula))
    print(min(results_list))
    print(max(results_list))
    stop = time.time()
    print(stop - start)
    

for formula in formulas_list:
    results_list = []
    print(formula)
    start = time.time()
    compiled_formula = compile(formula, 'formula', 'eval')
    print(compiled_formula)
    for x in argument_list:
        results_list.append(eval(compiled_formula))
    print(min(results_list))
    print(max(results_list))
    stop = time.time()
    print(stop - start)
