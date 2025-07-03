if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    run_score = sorted(list(set(arr)))[-2]
    
    print(run_score)