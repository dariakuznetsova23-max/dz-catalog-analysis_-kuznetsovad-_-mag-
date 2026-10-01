import math

movies = [
    {
        "title": "The Dune Chronicles",
        "year": 2021,
        "genres": {"sci-fi", "drama"},
        "rating": 8.6,
        "duration_min": 155,
        "actors": [
            "T. Chalamet",
            "R. Ferguson",
            "O. Isaac",
        ],
    },
    {
        "title": "Kitchen Stories",
        "year": 2019,
        "genres": {"comedy", "drama"},
        "rating": 7.1,
        "duration_min": 98,
        "actors": [
            "A. Novak",
            "M. Ferguson",
        ],
    },
    {
        "title": "silent hours",
        "year": 2016,
        "genres": {"thriller", "drama"},
        "rating": 6.4,
        "duration_min": 112,
        "actors": [
            "J. Bloom",
            "K. Lee",
        ],
    },
    {
        "title": "Comet Racers",
        "year": 2023,
        "genres": {"sci-fi", "action"},
        "rating": 5.9,
        "duration_min": 101,
        "actors": [
            "O. Isaac",
            "P. Diaz",
        ],
    },
    {
        "title": "The Last Bakery",
        "year": 2014,
        "genres": {"comedy"},
        "rating": 7.8,
        "duration_min": 89,
        "actors": [
            "A. Novak",
            "T. Chalamet",
        ],
    },
    {
        "title": "midnight in oslo",
        "year": 2020,
        "genres": {"thriller", "mystery"},
        "rating": 8.9,
        "duration_min": 124,
        "actors": [
            "K. Lee",
            "R. Ferguson",
        ],
    },
    {
        "title": "Garden of Static",
        "year": 2022,
        "genres": {"drama"},
        "rating": 4.8,
        "duration_min": 137,
        "actors": [
            "P. Diaz",
            "J. Bloom",
        ],
    },
    {
        "title": "The Quiet Algorithm",
        "year": 2024,
        "genres": {"sci-fi", "drama"},
        "rating": 9.2,
        "duration_min": 118,
        "actors": [
            "M. Ferguson",
            "O. Isaac",
        ],
    },
    {
        "title": "Two Left Shoes",
        "year": 2011,
        "genres": {"comedy"},
        "rating": 6.0,
        "duration_min": 95,
        "actors": [
            "A. Novak",
            "K. Lee",
        ],
    },
    {
        "title": "Red Harbor",
        "year": 2018,
        "genres": {"action", "thriller"},
        "rating": 7.3,
        "duration_min": 129,
        "actors": [
            "P. Diaz",
            "T. Chalamet",
        ],
    },
]


def average_rating(movies):
    total_rating = sum(movie["rating"] for movie in movies)
    average = total_rating / len(movies)
    return round(average, 1)


def catalog_age_stats(movies, current_year=2026):
    ages = [current_year - movie["year"] for movie in movies]

    oldest_age = max(ages)
    newest_age = min(ages)
    average_age = math.ceil(sum(ages) / len(ages))

    return oldest_age, newest_age, average_age


def duration_in_hours(minutes):
    hours = minutes // 60
    remaining_minutes = minutes % 60
    return f"{hours}ч {remaining_minutes}м"


def print_non_comedy_movies(movies):
    for movie in movies:
        if "comedy" in movie["genres"]:
            continue

        print(movie["title"])


def find_first_masterpiece(movies):
    index = 0

    while index < len(movies):
        movie = movies[index]

        if movie["rating"] > 9.0:
            print(f"Найден шедевр: {movie['title']}, рейтинг — {movie['rating']}")
            break

        index += 1
    else:
        print("Шедевров не найдено")


def count_long_movies(movies, threshold=120):
    count = 0

    for movie in movies:
        if movie["duration_min"] > threshold:
            count += 1

    return count


if __name__ == "__main__":
    print(f"Средняя оценка: {average_rating(movies)}")
    print(f"Статистика возраста: {catalog_age_stats(movies)}")
    print(f"155 минут: {duration_in_hours(155)}")
    print("Фильмы, которые не относятся к жанру comedy:")
    print_non_comedy_movies(movies)
    print("\nПоиск первого фильма с рейтингом выше 9.0:")
    find_first_masterpiece(movies)
    print("\nПроверка каталога без шедевров:")
    find_first_masterpiece(movies[:7])
    long_movies_count = count_long_movies(movies)
    print(f"\nКоличество фильмов длиннее 120 минут: {long_movies_count}")
