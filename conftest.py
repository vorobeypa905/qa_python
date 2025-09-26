import pytest
from main import BooksCollector



@pytest.fixture
def collector():
    return BooksCollector()

@pytest.fixture
def filled_collector():
    collector = BooksCollector()
    books = {
        'Гарри Поттер': 'Фантастика',
        'Шерлок Холмс': 'Детективы',
        'Корпорация монстров': 'Мультфильмы',
        'Оно': 'Ужасы',
        'Не может быть': 'Комедии'
        
    }
    for name, genre in books.items():
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
    return collector