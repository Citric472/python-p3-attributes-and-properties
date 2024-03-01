#!/usr/bin/env python3

from person import Person
import io
import sys

class TestPerson:
    '''Person in person.py'''

    def test_is_class(self):
        '''is a class with the name "Person".'''
        guido = Person(name='Guido', job='Sales')
        assert type(guido) == Person
        
    def test_name_not_empty(self):
        '''prints "Name must be string between 1 and 25 characters." if empty string.'''
        with io.StringIO() as captured_out:
            sys.stdout = captured_out
            try:
                Person(name="", job="Sales")
            except ValueError as e:
                assert "Name must be a string between 1 and 25 characters." in str(e)

        sys.stdout = sys.__stdout__

    def test_name_string(self):
        '''prints "Name must be string between 1 and 25 characters." if not string.'''
        with io.StringIO() as captured_out:
            sys.stdout = captured_out
            try:
                Person(name=123, job='Sales')
            except ValueError as e:
                assert "Name must be a string between 1 and 25 characters." in str(e)

        sys.stdout = sys.__stdout__

    def test_name_under_25(self):
        '''prints "Name must be string between 1 and 25 characters." if string over 25 characters.'''
        with io.StringIO() as captured_out:
            sys.stdout = captured_out
            try:
                Person(name="What do Persons do on their day off? Can't lie around - that's their job.",
                       job='Sales')
            except ValueError as e:
                assert "Name must be a string between 1 and 25 characters." in str(e)

        sys.stdout = sys.__stdout__

    def test_valid_name(self):
        '''saves name if string between 1 and 25 characters.'''
        guido = Person("Guido")
        assert guido.name == "Guido"

    def test_valid_name_title_case(self):
        '''converts name to title case and saves if between 1 and 25 characters'''
        guido = Person(name="guido van rossum")
        assert guido.name == "Guido Van Rossum"

    def test_job_not_in_list(self):
        '''prints "Job must be in list of approved jobs." if not in job list.'''
        with io.StringIO() as captured_out:
            sys.stdout = captured_out
            try:
                Person(job="Benevolent dictator for life")
            except ValueError as e:
                assert "Job must be in list of approved jobs." in str(e)

        sys.stdout = sys.__stdout__

    def test_job_in_list(self):
        '''saves job if in job list.'''
        guido = Person(job="ITC")
        assert guido.job == "ITC"
