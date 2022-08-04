def get_result(final_score):
    home_score = final_score["home_score"]
    away_score = final_score["away_score"]
    if home_score > away_score:
        return "Home win"
    elif away_score > home_score:
        return "Away win"
    else:
        return "Draw"

def get_results(final_scores):
    # (You could try and use a list comprehension for this)
    return [get_result(score) for score in final_scores]