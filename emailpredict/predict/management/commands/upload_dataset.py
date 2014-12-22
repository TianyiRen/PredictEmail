import csv

from django.core.management.base import BaseCommand
from predict.parse_dataset import parse_dataset


class Command(BaseCommand):
    help = 'Upload dataset'

    def handle(self, *args, **options):
        FILE = 'dataset/dataset.csv'
        with open(FILE, 'rb') as csvfile:
            rows = csv.reader(csvfile, delimiter=',')
            for row in rows:
                name = row[0]
                email = row[1]
                dataset = {name: email}
                parse_dataset(dataset)
