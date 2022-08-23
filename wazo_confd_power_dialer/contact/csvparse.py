import csv
import time

from collections import namedtuple
from flask import request

from xivo_dao.helpers import errors

ParseRule = namedtuple('ParseRule', ['csv_name', 'parser', 'name'])


class CsvParser:
    def __init__(self, lines):
        self.reader = csv.DictReader(lines)

    def __iter__(self):
        return CsvIterator(self.reader)


class CsvIterator:
    def __init__(self, reader):
        self.reader = reader
        self.position = 0

    def __next__(self):
        row = next(self.reader)
        self.position += 1
        return CsvRow(row, self.position)


class Rule:
    def __init__(self, csv_name, name):
        self.csv_name = csv_name
        self.name = name

    def insert(self, fields, entry):
        if self.csv_name in fields:
            value = fields.get(self.csv_name, "")
            entry[self.name] = self.parse(value)


class UnicodeRule(Rule):
    def parse(self, value):
        if value == "":
            return None
        return value


class BooleanRule(Rule):
    def parse(self, value):
        if value == "":
            return None
        if value not in ("0", "1"):
            raise errors.invalid_choice(self.csv_name, ["0", "1"])
        return value == "1"


class IntRule(Rule):
    def parse(self, value):
        if value == "":
            return None
        if not value.isdigit():
            raise errors.wrong_type(self.csv_name, 'integer')
        return int(value)


class ColonListRule(Rule):
    def parse(self, value):
        if value == "":
            return []
        return value.split(";")


class CsvRow:
    CONTACT_RULES = (
        UnicodeRule('name', 'name'),
        UnicodeRule('family', 'family'),
        UnicodeRule('phone', 'phone'),
        UnicodeRule('email', 'email'),
        UnicodeRule('email2', 'email2'),
        UnicodeRule('title', 'title'),
        UnicodeRule('company', 'company'),
        UnicodeRule('address', 'address'),
    )

    def __init__(self, fields, position):
        self.fields = fields
        self.position = position

    def parse(self):
        return self.parse_rules(self.CONTACT_RULES)

    def parse_rules(self, rules):
        entry = {}
        for rule in rules:
            rule.insert(self.fields, entry)
        return entry

    def format_error(self, exc):
        return {
            'message': str(exc),
            'timestamp': int(time.time()),
            'details': {'row': self.fields, 'row_number': self.position},
        }


def parse():
    charset = request.mimetype_params.get('charset', 'utf-8')
    lines = request.data.decode(charset)
    lines = lines.split('\n')
    return CsvParser(lines)
