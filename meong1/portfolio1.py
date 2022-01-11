class meong1(Exception):
    pass
class meong2(meong1):
    pass
class meong3(meong1):
    pass
class meong4(meong1):
    pass
class meong5(meong1):
    pass



num1=[]
num2=[]
num3=[]

def meong(a,b=False):
    try:
        for bubu in a:

            a1=bubu.split()
            num1.append(a1[0])
            num2.append(a1[1])
            num3.append(a1[2])

        #error handling
        if len(a)>5:
            raise meong2
        for mee in num2:
            if mee!='+':
                if mee!='-':
                    raise meong3
        for mee in num1:
            if mee.isnumeric()==False:
                raise meong4
            if len(mee)>4:
                raise meong5
        for mee in num3:
            if mee.isnumeric()==False:
                raise meong4
            if len(mee)>4:
                raise meong5
        for bubu in num1:
            print(f'{bubu:>6}',end='    ')
        print(' ')
        counter=0
        for bubu in num3:
            juju=f'{num2[counter]}{bubu:>5}'
            print(juju,end='    ')
            counter+=1
        print(' ')











        for bubu in range(len(num3)):
            asli=''
            max=0
            if len(num1[bubu])>len(num3[bubu]) or len(num1[bubu])==len(num3[bubu]):
                max=len(num1[bubu])+2
            else:
                max=len(num3[bubu])+2
            asli='-'*max







            print(f'{asli:>6}',end='    ')
        print(' ')























        if b:
            counter=0
            for bubu in num1:
                if num2[counter]=="+":
                    print(f'{int(num1[counter])+int(num3[counter]):>6}',end='    ')
                elif num2[counter]=="-":
                    print(f'{int(num1[counter])-int(num3[counter]):>6}',end='    ')
                counter+=1
            print(' ')
    except meong2:
        print('Error: Too many problems.')
    except meong3:
        print("Error: Operator must be '+' or '-'.")
    except meong4:
        print('Error: Numbers must only contain digits.')
    except meong5:
        print('Error: Numbers cannot be more than four digits.')



# meong(['1200 + 123','23 - 69','2433 + 69','2553 - 69','3223 - 69'],True)
