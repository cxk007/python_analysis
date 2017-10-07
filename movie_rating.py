import pandas as pd

unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
users=pd.read_table('/Users/chenxing/Documents/pydata-book-master/ch02/movielens/users.dat',sep='::', header=None, names=unames)
# print(users[:5])

rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table('/Users/chenxing/Documents/pydata-book-master/ch02/movielens/ratings.dat', sep='::', header=None, names=rnames)
# print(ratings[:5])

mnames = ['movie_id', 'title', 'genres']
movies = pd.read_table('/Users/chenxing/Documents/pydata-book-master/ch02/movielens/movies.dat', sep='::', header=None, names=mnames)
# print(movies[:5])

data = pd.merge(pd.merge(ratings, users), movies)
# print(data)
# print(data.ix[0])
mean_ratings = data.pivot_table('rating', rows='title', cols='gender', aggfunc='mean')
print(mean_ratings[:5])
