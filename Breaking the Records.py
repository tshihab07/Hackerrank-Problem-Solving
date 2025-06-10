import os
import re
import sys

""" Problem Description:
Maria plays college basketball and wants to go pro. Each season she maintains a record of her play.
She tabulates the number of times she breaks her season record for most points and least points in a game.
Points scored in the first game establish her record for the season, and she begins counting from there.

Example:
scores = [12, 24, 10, 24]
Scores are in the same order as the games played. She tabulates her results as follows:
                                  Count
    Game  Score  Minimum  Maximum   Min Max
     0      12     12       12       0   0
     1      24     12       24       0   1
     2      10     10       24       1   1
     3      24     10       24       1   1

Given the scores for a season, determine the number of times Maria breaks her records for most and least points scored during the season.
"""



def breakingRecords(scores):

    highest_score = scores[0]
    lowest_score = scores[0]
    new_record_count = 0
    worst_record_count = 0

    for score in scores[1:]:
        if score > highest_score:
            highest_score = score
            new_record_count += 1
        elif score < lowest_score:
            lowest_score = score
            worst_record_count += 1

    return [new_record_count, worst_record_count]
            
            
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
