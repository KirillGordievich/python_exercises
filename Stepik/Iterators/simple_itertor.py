list = [i for i in range(1,5)]
iterator = iter(list)

print('How a for-loop works with list: ')
for item in list:
    print(item, end="\t")
print('\n\n---------------')
print('How iterator works with list: ')
while True:
    try:
        print(next(iterator), end="\t")
    except StopIteration:
        print('\n\nStopIteration')
        break

print('\n\n---------------')
string = 'Nothing'
iterator = iter(string)
print('How a for-loop works with string: ')
for letter in string :
    print(letter, end="\t")
print('\n\n---------------')
print('How iterator works with string: ')
while True:
    try:
        print(next(iterator), end="\t")
    except StopIteration:
        print('\n\nStopIteration')
        break