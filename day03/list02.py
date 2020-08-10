superheroes = ['batman', 'joker', 'superman', 'thor', 'flash', 'arrow']
print(superheroes)

superheroes.append('captain america')
print(superheroes)

deleted =  superheroes.pop()
superheroes.remove('joker')
print(superheroes)

print(deleted)

del superheroes[2]
print(superheroes)
