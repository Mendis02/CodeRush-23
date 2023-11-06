finald = []
finalm = []
n = int(input(""))
crypt = str(input(""))
arr = crypt.split("++")
# print(arr)
# print(len(arr))
month = arr[0].split("+")
day = arr[1].split("+")

additional = []
dayp2final = []
dayp2 = []

if len(arr) > 2:
    additional = arr[2].split("+")
    print(additional)
    for c in additional:
        count = len(c)
        dayp2.append(chr(count + 13))
        print(dayp2)
    dayp2final = [item for item in dayp2 if item.isalpha()]

day_f = [item for item in day if item.strip() != ""]
for c in month:
    count = len(c)
    finalm.append(chr(count + 13))

for c in day:
    count = len(c)
    finald.append(chr(count + 13))

result_list = [item for item in finald if item.isalpha()]
# print(dayp2final)

finalres = ''.join(finalm) + " " + ''.join(result_list) + " " + ''.join(dayp2final)
print(finalres)
# print(finalm)
# print(result_list)
# print(dayp2final)
