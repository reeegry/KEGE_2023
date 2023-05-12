def game(stones, step, final_step):
    '''
    если игрок достиг победы, то проверяем, что победы достиг игрок с той же четностью, пример: если ищем победу Вани за 2
    ход, то нам нужен либо 2 ход, либо 4, потому что четность ходов Вани = 2
    '''
    if stones >= (количество камней для победы): return step % 2 == final_step % 2
    if step == final_step: return 0

    heaps = [game(stones + (условие 1), step + 1, final_step), game(stone * (условие 2), step + 1, final_step), (следующие условия)]
    '''
    если следующий ход это ход игрок за которого мы ищем победу, то нам нужен ХОТЯ БЫ один выигрышный ход, иначе во всех ходах
    противника нужна победа(потому что у него нет стратегии)
    '''
    return any(heaps) if (step  + 1) % 2 == final_step % 2 else all(heaps) #если нужна победа для неудачного хода, меняем all на any


for s in range(количество камней):
    for step in range(1, 5):
        if game(s, 0, step):
            print(s, step)
            break