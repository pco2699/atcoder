
def main():
    n = int(input())
    towns = list(map(int,input().split()))
    braves = list(map(int,input().split()))

    count = 0
    for b in range(n-1, -1, -1):
        if towns[b+1] > braves[b]:
            count = count + braves[b]
            towns[b+1] = towns[b+1] - braves[b]
            braves[b] = 0
            
        else:
            count = count + towns[b+1]
            braves[b] = braves[b] - towns[b+1]
            towns[b+1] = 0

        if braves[b]:
            if towns[b] > braves[b]:
                count = count + braves[b]
                towns[b] = towns[b] - braves[b]
                braves[b] = 0
                
            else:
                count = count + towns[b]
                braves[b] = braves[b] - towns[b]
                towns[b] = 0

    print(count)

if __name__ == "__main__":
    main()