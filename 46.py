""" def show_progress(character='*', how_many=1):
    print(character*how_many)

show_progress(10)
show_progress(how_many=15)
show_progress(character='&')
    
show_progress(10, '-')
show_progress(15, '+') """

def show_progress(how_many, character='*'):
    
    line = character * how_many
    print(line)
    
show_progress(10)
show_progress(15)
show_progress(30)
    
show_progress(10, '-')
show_progress(15, '+')