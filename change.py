def change(cents):
    dimes = cents // 10
    cents = cents % 10
    
    nickels = cents // 5
    cents = cents % 5
    
    pennies = cents  # remaining cents are pennies
    
    total_coins = dimes + nickels + pennies

    
    return(total_coins)


if __name__ == '__main__':
    m = int(input())
    print(change(m))
