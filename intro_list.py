# list lets you store information is a single place
# and it starts with a square brackets => []

movies = ["Avengers", "Iron Man 1 - 2- 3", "Wakanda Forever"]
print(movies)

# can retrieve a singular item in the list
_first__movie = movies[2]
print(_first__movie)

# when you append a value into a list, it gets added at the end of the list
movies.append('Transformers')
print(movies[-1])

# inserting an element in a list
car = []
car.insert(0, "Ford Mustang 1967")
print(car)

del movies[0]
print(movies)

# when you sort a list, it sorts it in alphabetical order
# example
cars = ["ford", "lamborghini", 'toyota', 'nissan']
cars.sort()
print(cars)

# you can also use this method if you want the items in your list to be reversed
cars.sort(reverse=True)
print(cars)

# sorted
a = [56, 1, 123, 45, 76]
x = sorted(a)
print(x)
print(len(x))