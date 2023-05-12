def game(stones1, stones2, step, final_step):
    if stones1 + stones2 >= (количество камней для победы): return step % 2 == final_step % 2
    if step == final_step: return 0

    heaps = [game(stones1 + (условие 1), stones2 , step + 1, final_step), game(stones1, stones2 + (условие 2), step + 1, final_step), 
             game(stones1 * (условие 2), stones2,  step + 1, final_step), game(stones1, stones2 * (условие2), step + 1, final_step), (следующие условия)]
    return any(heaps) if (step  + 1) % 2 == final_step % 2 else all(heaps) #если нужна победа для неудачного хода, меняем all на any


for s in range(диапазон камней):
    for step in range(1, 5):
        if game(s,(начальное количество камней в 1 куче), 0, step):
            print(s, step)
            break