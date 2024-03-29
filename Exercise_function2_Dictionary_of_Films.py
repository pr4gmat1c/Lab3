# Dictionary of movies

movies = [
{
"name": "Usual Suspects",
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

def imdb_find(movie):
    if movie["imdb"] > 5.5:
        return True
    else:
        return False
movie = {
"name": "Usual Suspects",
"imdb": 7.0,
"category": "Thriller"
}
print(imdb_find(movie))


def imdb_findlist(movies):
    result = []
    for m in movies:
        if imdb_find(m):
            result.append(m)
    return result


print(imdb_findlist(movies))


def find_bycategory(category):
    result = []
    for m in movies:
        if m["category"] == category:
            result.append(m)
    return result


print(find_bycategory("Thriller"))

def imdb_avg(movies):
    sum = 0
    for m in movies:
        sum += m["imdb"]
    return (sum/len(movies))


print(imdb_avg(movies))


def category_avg(category):
    result = find_bycategory(category)
    return imdb_avg(result)


print(category_avg("Thriller"))
