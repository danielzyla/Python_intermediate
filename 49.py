""" def calculate_paint(efficency_ltr_per_m2, *surface_m2_per_room):
    for surface in surface_m2_per_room:
        amount_of_paint=efficency_ltr_per_m2*surface
        print('The neede amount of the paint is: ', amount_of_paint, 'for the surface: ', surface)

calculate_paint(5, 20, 30)

surfaces = [15,25]

calculate_paint(5, *surfaces) """


def log_it(*args):
    filepath= r'/tmp/log_it.txt'
    with open(filepath, 'a') as file:
        for arg in args:
            file.write(arg+' ')
        file.write('\n')

""" log_it('Starting processing forecasting')
log_it('ERROR', 'Not enough data', 'invoices', '2020') """


log_it('word', 'hello', 'spicy', 'ggggtest')