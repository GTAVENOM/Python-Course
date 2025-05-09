highIncome=True
goodCredit=True
if highIncome and goodCredit:
    print("Eligible for loan")

highIncome=False

if highIncome or goodCredit:
    print("Eligible for loan")

criminalRecord=False
if goodCredit and not criminalRecord:
    print("Eligible for loan")