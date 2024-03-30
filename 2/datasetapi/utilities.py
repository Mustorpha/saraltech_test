from . import models

import csv

def import_stock_csv_to_db(file_path):
    """
    Loads CSV file's data into stock database
    """
    with open(file_path, 'r') as file:
        reader=csv.DictReader(file)
        for row in reader:
            if models.Stock.objects.filter(name=row["name"]).exists():
                continue
            models.Stock.objects.create(
                name=row["name"],
                price=row['price'],
                quantity=row["quantity"],
                category=row["category"].lower(),
                )
