"""
CSV Parser Plugin
=================

A plugin which reads your CSV files and supplies them as a Dict to Pelican.

Settings:
CSV_DICTS = { 'MY_VALUES': 'my_values.csv' }

Filenames must be relative to Pelican blog root, i.e. where your Makefile lives.

Usage:
Available in your page context as 'csv_dicts'.
"""

from csv import DictReader

from pelican import signals


class CsvParser(object):
    def __init__(self, generator):
        self.dicts = generator.settings['CSV_DICTS']

    def get_dicts(self):
        csv_dicts = {}
        for key, filename in self.dicts.iteritems():
            csv_dicts.update({key: self.parse(filename)})
        return csv_dicts

    def parse(self, filename):
        try:
            with open(filename, 'rU') as f:
                reader = DictReader(f, dialect='excel')
                csv = [row for row in reader]
                return csv
        except IOError:
            return []


def csv_parse(generator):
    if 'CSV_DICTS' in generator.settings.keys():
        parser = CsvParser(generator)
        generator.context['csv_dicts'] = parser.get_dicts()


def register():
    signals.page_generator_init.connect(csv_parse)
