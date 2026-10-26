import icao

name = input('Enter your name: ')

word = [icao.icao(letter) for letter in name]

print('ICAO words for spelling out your name:', word)