====================
python-long-weekends
====================

.. image:: https://img.shields.io/pypi/l/python-long-weekends.svg??style=plastic&logo=appveyor
   :target: https://pypi.python.org/pypi/python-long-weekends/

.. image:: https://img.shields.io/pypi/v/python-long-weekends.svg??style=plastic&logo=appveyor
   :target: https://pypi.python.org/pypi/python-long-weekends/
   
.. image:: https://github.com/kryptonite0/python-long-weekends/workflows/CI/badge.svg
   :target: https://github.com/kryptonite0/python-long-weekends/actions
   
.. image:: https://img.shields.io/badge/Used%20by-HIVE%20POWER-orange?color=fca311
   :target: https://hivepower.tech/

.. image:: https://github.com/kryptonite0/python-long-weekends/blob/main/img/calendar.png
   :target: https://github.com/kryptonite0/python-long-weekends/blob/main/notebooks/example.ipynb

A simple python library to spot holiday "bridges" and long weekends.
When a public holiday falls on a Tuesday or a Thursday, 
people typically take Monday or Friday off work to enjoy long vacations.
Italians call those days "ponti" ("bridges").
To the best of my knowledge, there is no English translation for this term 
apart from a generic "long weekend".

This library spots single working days that are preceded
and followed by a weekend and/or a public holiday, and classifies them as "bridges". 
Based on the identified "bridges", this library also labels "long weekends", 
here defined as a series of 3 or more days that are either weekend, 
holidays, or holiday "bridges".

This library is intended to help generate informative features for 
energy consumption prediction models. 

Inspired by https://stackoverflow.com/a/57865434/7059626 (thank you @jezrael).

Example Usage
-------------

Simply invoke ``spot_holiday_bridges`` and pass start and end dates, plus a list of public holiday dates.
If a public holiday falls on the day before ``start`` or the day after ``end``, 
it is important to include it in the list of holidays 
to make sure that the algorithm works correctly at the borders.

This `notebook <https://github.com/kryptonite0/python-long-weekends/blob/main/notebooks/example.ipynb/>`_ 
uses the example below and shows how to generate a colored calendar.


.. code-block:: python
    
    >>> import holidays as holidays_api
    >>> from long_weekends.long_weekends import spot_holiday_bridges
    
    >>> start = '2021-01-01'
    >>> end = '2021-12-31'
    >>> holidays = holidays_api.CH(prov='TI', years=[2020, 2021, 2022])
    >>> bridges, long_weekends = spot_holiday_bridges(
            start=start, end=end, holidays=holidays)
    
    >>> bridges
    [Timestamp('2021-05-14 00:00:00'),
     Timestamp('2021-06-04 00:00:00'),
     Timestamp('2021-06-28 00:00:00')]
    
    >>> long_weekends
    [Timestamp('2021-01-01 00:00:00'),
     Timestamp('2021-01-02 00:00:00'),
     Timestamp('2021-01-03 00:00:00'),
     Timestamp('2021-03-19 00:00:00'),
     Timestamp('2021-03-20 00:00:00'),
     Timestamp('2021-03-21 00:00:00'),
     Timestamp('2021-04-02 00:00:00'),
     Timestamp('2021-04-03 00:00:00'),
     Timestamp('2021-04-04 00:00:00'),
     Timestamp('2021-04-05 00:00:00'),
     Timestamp('2021-05-13 00:00:00'),
     Timestamp('2021-05-14 00:00:00'),
     Timestamp('2021-05-15 00:00:00'),
     Timestamp('2021-05-16 00:00:00'),
     Timestamp('2021-05-22 00:00:00'),
     Timestamp('2021-05-23 00:00:00'),
     Timestamp('2021-05-24 00:00:00'),
     Timestamp('2021-06-03 00:00:00'),
     Timestamp('2021-06-04 00:00:00'),
     Timestamp('2021-06-05 00:00:00'),
     Timestamp('2021-06-06 00:00:00'),
     Timestamp('2021-06-26 00:00:00'),
     Timestamp('2021-06-27 00:00:00'),
     Timestamp('2021-06-28 00:00:00'),
     Timestamp('2021-06-29 00:00:00'),
     Timestamp('2021-10-30 00:00:00'),
     Timestamp('2021-10-31 00:00:00'),
     Timestamp('2021-11-01 00:00:00')]


License
-------

.. __: https://github.com/kryptonite0/python-long-weekends/blob/main/LICENSE

Code and documentation are available according to the MIT License
(see LICENSE__).
