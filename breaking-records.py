# https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem


def breakingRecords(scores):
    # place to store the count of lowest scores broke
    lowest_score_count = 0
    # a place to store count of highest scores broke
    highest_score_count = 0
    # a place to store the lowest and highest scores
    lowest = None
    highest = None
    # loop over scores
    for score in scores:
        # if result is equal to an empty array
        if lowest == None and highest == None:
            # Set the lowest and highest scores to first game score
            lowest = score
            highest = score
        # check if the score is less than lowest score
        if score < lowest:
            # if true - increment lowest score
            lowest_score_count += 1
            # set lowest score to that score count
            lowest = score
        # check if the score is higher than the highest score
        if score > highest:
            # if true increment highest score count
            highest_score_count += 1
          # set highest score to that score
            highest = score
    # return scores
    return highest_score_count, lowest_score_count
