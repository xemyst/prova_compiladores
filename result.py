livros = {
    'artes' :{'current':20, 'total':20}
}
while 1:
    command = input('input command: ').split(' ')
    if command[0] == 'empresta':
        if livros[command[1]]['current'] - 1 >= 0:
            livros[command[1]]['current'] -= 1
    if command[0] == 'devolve':
        livros[command[1]]['current'] += 1
    if command[0] == 'livros':
        for key in livros:
            print('current', livros[key]['current'], 'total', livros[key]['total'])
