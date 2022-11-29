import random as r


def update_state(state, r, c, v):
    state[r * 3 + c] = choice_symbol(v)
    return not v


def choice_symbol(v):
    return 'X' if v else 'O'


def gen_moves(state, v):
    s = choice_symbol(v)
    poss_moves = []
    for i, x in enumerate(state):
        if x == -1:
            poss_moves.append(state[:])
            poss_moves[-1][i] = s
    r.shuffle(poss_moves)
    return poss_moves


def win_state(state: list):
    for i in range(3):
        if state[3 * i + 0] == state[3 * i + 1] == state[3 * i + 2] != -1: return True
        if state[0 + i] == state[3 + i] == state[6 + i] != -1: return True
    return state[0] == state[4] == state[8] != -1 or state[2] == state[4] == state[6] != -1


def is_draw(state: list):
    return -1 not in state


def final_score(state):
    res = 0
    for x in state:
        if x == -1: res += 1
    return res


def find_best_move(state, is_ai, v):
    if win_state(state): return state, 1 + final_score(state) if not is_ai else -final_score(state) - 1  
    if is_draw(state): return state, 0
    poss_moves = gen_moves(state, v)
    b = -10 if is_ai else 10
    next_move = None
    for move in poss_moves:
        _, score = find_best_move(move, not is_ai, not v)
        if (score > b and is_ai) or (score < b and not is_ai):
            next_move, b = move, score
    return next_move, b
    