#Создаем список книг
books = [
    {
        #Название книги
        "title": "Пять ночей у Фредди. Серебряные глаза",
        #Автор книги
        "author": "Скотт Коутон",
        #Год публикации
        "year": 2015
    },
    {
        #Название книги
        "title": "Ужасы Фазбера. Хватайка",
        #Автор книги
        "author": "Скотт Коутон",
        #Год публикации
        "year": 2022
    },
    {
        #Название книги
        "title": "Пять ночей у Фредди: Ужасы Фазбера. В бассейн!",
        #Автор книги
        "author": "Скотт Коутон",
        #Год публикации
        "year": 2022
    },
    {
        #Название книги
        "title": "Ужасы Фазбера. 1:35 ночи",
        #Автор книги
        "author": "Скотт Коутон",
        #Год публикации
        "year": 2022
    },
    {
        #Название книги
        "title": "Файлы Фредди",
        #Автор книги
        "author": "Скотт Коутон",
        #Год публикации
        "year": 2018
    }
]
#Функция enumerate() перебирает элементы списка books вместе с их индексами
for index, book in enumerate(books, start=1):
    #Вывод информации о книгах
    print(f"---------------------- Книга {index} -----------------------")
    print(f"Название: {book['title']}, Автор: {book['author']},")
    print(f"-------------------------{book['year']}-------------------------\n")
