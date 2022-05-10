import logging
from sqlalchemy import asc, desc
from sqlalchemy.inspection import inspect
from flask_restx import fields



class QueryDateFilter(object):
    """ Create query date filter (qdf) object with correct time appended, and null parameter initialisation to use in session.query(Model).filter(qdf)"""
    def __init__(self, date_args: dict, date_column):
        date_from = date_args['date_from'] if date_args['date_from'] is not None else '1900-01-01'
        date_to = date_args['date_to'] if date_args['date_to'] is not None else '3000-01-01'

        self.date_from = date_from + ' 00:00:00.00000'
        self.date_to = date_to + ' 23:59:59.99999'
        self.date_column = date_column

    @property
    def date_filter(self) -> []:
        return [self.date_column >= self.date_from, self.date_column <= self.date_to]


class QueryOrderBy(object):
    """ Create query ordering object (qob) to use in session.query(Model).order_by(qob) """
    def __init__(self, order_by_args: dict, model):

        self.args = order_by_args
        self.model = model
        self.order_direction = asc if order_by_args['order_direction'] == 'asc' else desc

    @property
    def column(self):
        order_by = self.args['order_by']
        column_obj = None

        # If column name has been specified
        if self.args['order_by']:
            for column in self.model.__table__.columns:
                if str(column) == self.model.__table__.name + '.' + order_by:
                    column_obj = column
            # If by_column has not been set, column name supplied does not exist
            if column_obj is None:
                raise KeyError

        # If column name has not been specified and column created at_exists
        elif not self.args['order_by']:
            for column in self.model.__table__.columns:
                if str(column) == self.model.__table__.name + '.created_at':
                    column_obj = column
            # If by_column has not been set, created_at does not exist, and primary key column will be used
            if column_obj is None:
                for column in self.model.__table__.columns:
                    if str(column) == self.model.__table__.name + '.' + inspect(self.model).primary_key[0].name:
                        column_obj = column

        return self.order_direction(column_obj)


class QuerySearchFilter(object):
    def __init__(self, search_string: str):
        self.search_string = search_string if search_string else ""


    def all_columns(self, model) -> []:
        search_objects = []
        for column in model.__table__.columns:
            if str(column.type) == 'VARCHAR':
                search_objects.append(column.like(f'%{self.search_string}%'))
        return search_objects


    def by_columns(self, columns: list):
        search_objects = []
        for column in columns:
            if str(column.type) == 'VARCHAR':
                search_objects.append(column.like(f'%{self.search_string}%'))
        return search_objects


class NoPagination(object):
    def __init__(self, query, items):
        self.query = query
        self.page = 1
        self.per_page = len(items)
        self.total = len(items)
        self.items = items
        self.pages = 1


class AuthenticationError(Exception):
    """ Exception for data access failure """
    def __init__(self, logger, msg=''):
        self.msg = msg
        logger = logging.getLogger(logger)
        logger.exception(msg)

    def __str__(self):
        return self.msg


class NullableInteger(fields.Integer):
    __schema_type__ = ['integer', 'null']
    __schema_example__ = 'nullable integer'


class NullableString(fields.String):
    __schema_type__ = ['string', 'null']
    __schema_example__ = 'nullable string'