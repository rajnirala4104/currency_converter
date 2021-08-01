with open("currency.txt") as f:
    DATA = f.readlines()

DataDic = {}
for line in DATA:
    take = line.split("\t")
    DataDic[take[0]] = take[1]

# print(DataDic)

askAmount = float(input("Enter the Amount: "))
data = DataDic.keys()
for curr in data:
    print(curr)
askCurr = input("Enter the Currency name: ")
print(f"\n{askAmount}INR is euqal to {askAmount*float(DataDic[askCurr])} {askCurr}")
