# coding: UTF-8

class Task:
    '''
    タスクを扱うクラス
    '''
    def __init__(self, title, details, limit, insert, user_name='shimizu'):
        self.__title = title
        self.__details = details
        self.__limit = limit
        self.__insert = insert
        self.__user_name = user_name

    @property
    def title(self):
        return self.__title

    @property
    def details(self):
        return self.__details

    @property
    def limit(self):
        return self.__limit

    @property
    def insert(self):
        return self.__insert

    @property
    def user_name(self):
        return self.__user_name