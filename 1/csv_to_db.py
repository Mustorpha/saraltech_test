from datetime import datetime
from myapp.models import Book

import csv

def import_books(file_path):
    with open(file_path, 'r') as file:
        reader=csv.DictReader(file)
        for row in reader:
            Book.objects.create(
                tile=row["titile"],
                author=row['author'])

if __name__ == '__main__':
    csv_file_path = 'path/to/books.csv'
    import_books(csv_file_path)
