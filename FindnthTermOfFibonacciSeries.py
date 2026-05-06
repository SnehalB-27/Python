def fibnth(N):
    PrevNum = 0
    CurrNum = 1
    for i in range(1,N):
        PrePrevNum = PrevNum
        PrevNum = CurrNum
        CurrNum = PrevNum +  PrePrevNum
    return CurrNum

if __name__ == "__main__":
    num = int(input("Enter the number"))
    print(f"{fibnth(num)}")
