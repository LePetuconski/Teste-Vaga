word = input('Digite uma palavra: \n') #str
characters = []
inversed = ''

for letter in word:
    characters.append(letter)

size = len(characters) - 1

while size >= 0:
    inversed += characters[size]
    size -= 1

print(inversed)
