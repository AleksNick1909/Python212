import pickle
import os.path


class Article:
    def __init__(self, film, genre, director, year_of_release, duration, studio, actors):
        self.film = film
        self.genre = genre
        self.director = director
        self.year_of_release = year_of_release
        self.duration = duration
        self.studio = studio
        self.actors = actors

    def __str__(self):
        return f"{self.film}: {self.genre}; режисер - {self.director}; {self.duration} мин."


class Article_model:
    def __init__(self):
        self.film = "film.txt"
        self.articles = self.load_data()

    def add_article(self, dict_article):
        article = Article(*dict_article.values())
        self.articles[article.film] = article

    def get_all_articles(self):
        return self.articles.values()

    def get_single_article(self, user_title):
        article = self.articles[user_title]
        dict_article = {
            "название фильма": article.film,
            "жанр": article.genre,
            "режиссер": article.director,
            "год выпуска": article.year_of_release,
            "длительность": article.duration,
            "студия": article.studio,
            "актеры": article.actors
        }
        return dict_article

    def remove_article(self, user_title):
        return self.articles.pop(user_title)

    def load_data(self):
        if os.path.exists(self.film):
            with open(self.film, 'rb') as f:
                return pickle.load(f)
        else:
            return dict()

    def save_data(self):
        with open(self.film, 'wb') as f:
            pickle.dump(self.articles, f)

