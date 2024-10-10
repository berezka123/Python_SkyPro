from book import Book

library = [Book("Мастер и Маргарита", "М.Булгаков"),
           Book("Преступлене и наказание", "Ф.Достоевский"),
           Book("Пиковая дама", "А.Пушкин")]

for i in library:
    print(f"{i.name} - {i.autor}")
