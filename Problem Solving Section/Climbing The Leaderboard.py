import os


""" Problem Description:
An arcade game player wants to climb to the top of the leaderboard and track their ranking.
The game uses Dense Ranking, so its leaderboard works like this:

The player with the highest score is ranked number 1 on the leaderboard. 
Players who have equal scores receive the same ranking number, and the next player(s) receive the immediately following ranking number.

Example:
ranked = [100, 90, 90, 80]
player = [70, 80, 105]
The ranked players will have ranks 1, 2, 2, and 3, respectively.
If the player's scores are 70,  80 and ,  105, their rankings after each game are 4th, 3rd and 1st. Return [4, 3, 1].
"""


def climbingLeaderboard(ranked, player):
    # Write your code here
    # Step 1: Remove duplicates and sort in descending order
    unique_ranks = sorted(set(ranked), reverse=True)

    results = []
    index = len(unique_ranks) - 1  # Start from the lowest rank

    for score in player:
        # Step 2: Move up while player score is >= ranked score
        while index >= 0 and score >= unique_ranks[index]:
            index -= 1
        # Step 3: Player's rank is index+2 (because rank is 1-based, and index moved past)
        results.append(index + 2)

    return results


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()