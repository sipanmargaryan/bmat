import os
import csv
import operator
from functools import reduce

from django.db.models import Q, F, Value
from django.db.models.functions import Concat
from django.conf import settings
from django.core.management.base import BaseCommand

from music.models import Music


class Command(BaseCommand):
    help = 'Initialize music metadata'

    def handle(self, *args, **options):
        with open(os.path.join(settings.BASE_DIR, 'music_data/works_metadata.csv'), 'r') as csvfile:
            musics = csv.DictReader(csvfile)
            for music in musics:
                if music['iswc']:
                    single, created = Music.objects.get_or_create(iswc=music['iswc'],
                                                                  defaults={'title': music['title'],
                                                                            'contributors': music['contributors']
                                                                            })
                    if not created:
                        single.contributors = '|'.join(set(f'{single.contributors}|{music["contributors"]}'.split('|')))
                        single.save()
                else:
                    check_contributor = reduce(operator.or_, (
                        Q(contributors__contains=contributor) for contributor in music["contributors"].split('|')))
                    single = Music.objects.filter(Q(title=music['title']) & check_contributor).first()
                    if single:
                        single.contributors = '|'.join(set(f'{single.contributors}|{music["contributors"]}'.split('|')))
                        single.save()

                self.stdout.write(self.style.SUCCESS(f'Successfully imported {music["iswc"]}'))