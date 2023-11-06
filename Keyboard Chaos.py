original_alphabet = "abcdefghijklmnopqrstuvwxyz"
reversed_alphabet = "lcbjihgfedsazxwqpukyrvontm"

reverse_mapping = {}

for original, reversed in zip(original_alphabet, reversed_alphabet):
    reverse_mapping[original] = reversed
x = input()

y=[]
j=0
for i in x:
    temp=reverse_mapping.get(i)
    if temp == None:
        y.append(i)
    else:
        y.append(temp)

result = ''.join(y)
print(result)