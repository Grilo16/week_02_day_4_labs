def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    top_three = []
    rounds = 3
    if len(scores) < rounds:
        rounds = len(scores)
    for _ in range(rounds):
        top_three.append(max(scores))
        scores.pop(scores.index(max(scores)))
    return top_three


def ordered_scores(scores):
    scores.sort(reverse=True)
    return scores