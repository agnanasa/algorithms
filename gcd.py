import math
def gcd(a, b):
    #current_gcd = 1
    #for d in range(2, min(a, b) + 1):
        #if a % d == 0 and b % d == 0:
            #if d > current_gcd:
                #current_gcd = d
    return math.gcd(a,b)

    #return current_gcd


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(gcd(a, b))
