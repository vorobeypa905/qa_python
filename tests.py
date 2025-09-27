import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    # ---------- add_new_book ----------
    def test_add_new_book_success(self, collector):
        collector.add_new_book("Гарри Поттер")
        assert "Гарри Поттер" in collector.get_books_genre()

    def test_add_new_book_too_long(self, collector):
        long_name = "А" * 41
        collector.add_new_book(long_name)
        assert long_name not in collector.get_books_genre()

    def test_add_new_book_duplicate(self, collector):
        collector.add_new_book("Гарри Поттер")
        collector.add_new_book("Гарри Поттер")
        assert list(collector.get_books_genre().keys()).count("Гарри Поттер") == 1

    # ---------- set_book_genre ----------
    @pytest.mark.parametrize("genre", ["Фантастика", "Мультфильмы"])
    def test_set_book_genre_valid(self, collector, genre):
        collector.add_new_book("Книга")
        collector.set_book_genre("Книга", genre)
        assert collector.get_book_genre("Книга") == genre

    def test_set_book_genre_invalid(self, collector):
        collector.add_new_book("Книга")
        collector.set_book_genre("Книга", "Поэзия")
        assert collector.get_book_genre("Книга") == ""

    # ---------- get_book_genre ----------
    def test_get_book_genre_returns_none(self, collector):
        assert collector.get_book_genre("Несуществующая") is None

    # ---------- get_books_with_specific_genre ----------
    def test_get_books_with_specific_genre(self, collector):
        collector.add_new_book("Книга")
        collector.set_book_genre("Книга", "Фантастика")
        assert collector.get_books_with_specific_genre("Фантастика") == ["Книга"]

    def test_get_books_with_specific_genre_empty(self, collector):
        assert collector.get_books_with_specific_genre("Фантастика") == []

    # ---------- get_books_genre ----------
    def test_get_books_genre_returns_dict(self, filled_collector):
        books_genre = filled_collector.get_books_genre()
        assert isinstance(books_genre, dict)
        assert books_genre["Гарри Поттер"] == "Фантастика"
        assert books_genre["Шерлок Холмс"] == "Детективы"
        assert books_genre["Корпорация монстров"] == "Мультфильмы"

    # ---------- get_books_for_children ----------
    def test_get_books_for_children_excludes_age_rating(self, collector):
        collector.add_new_book("Хоррор")
        collector.set_book_genre("Хоррор", "Ужасы")
        assert "Хоррор" not in collector.get_books_for_children()

    def test_get_books_for_children_includes_allowed(self, collector):
        collector.add_new_book("Мульт")
        collector.set_book_genre("Мульт", "Мультфильмы")
        assert "Мульт" in collector.get_books_for_children()

    # ---------- favorites ----------
    def test_add_book_in_favorites(self, collector):
        collector.add_new_book("Книга")
        collector.add_book_in_favorites("Книга")
        assert "Книга" in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites(self, collector):
        collector.add_new_book("Книга")
        collector.add_book_in_favorites("Книга")
        collector.delete_book_from_favorites("Книга")
        assert "Книга" not in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_twice(self, collector):
        collector.add_new_book("Книга")
        collector.add_book_in_favorites("Книга")
        collector.add_book_in_favorites("Книга")
        assert collector.get_list_of_favorites_books().count("Книга") == 1