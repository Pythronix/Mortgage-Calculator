mylist = ['monthly','weekly','daily']
loan  =  float(input('Your Loan: '))
r = float(input('Enter your Interest rate: '))
mode = str(input('Enter your Style of Payment: '))

if loan <= 0 or r <= 0:
    print('Kindly Enter the Correct Value')
    
else:
    for pay in range(len(mylist)):
        if mode != mylist[pay] or mode != mylist[pay] or mode != mylist[pay]:
            message= 'Kindly enter monthly,weekly,daily'
        elif mode == mylist[0]:
            time = mylist[0]
            rate =  (r/100)
            rates = (r/100) * loan
            result = (rates + loan)/12
        elif mode == mylist[1]:
            time = mylist[1]
            rate =  (r/100)
            rates = (r/100) * loan
            result = (rates + loan)/52
        elif mode == mylist[2]:
            time = mylist[2]
            rate =  (r/100)
            rates = (r/100) * loan
            result = (rates + loan)/365
    print(mylist[pay])

    print(rates)
    print(f'The Loan of {loan}naira at the rate of {rate:.2f}% is {result:.2f}naira and should be paid on a {time} basis')
