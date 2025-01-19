try:
    name=int(input(''))
    if name<0 or name>=32768:
        raise ValueError

    if name%4==0:
        least=name//4
        most=name//2
        print(str(int(least))+' ' +str(int(most)))
    else:
        if name%4!=0 and name%2==0:
            least=(name-2)//4+1
            most=name//2
            print(str(int(least))+" " +str(int(most)))

        else: print('0 0')
except ValueError as e:
    print(e)