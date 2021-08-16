import unittest
from datetime import datetime

from long_weekends.long_weekends import spot_holiday_bridges


class TestLongWeekends(unittest.TestCase):

    def test1(self):
        #          date  weekend  holiday  bridge long_weekend
        # 0  2020-11-30    False    False       -            -
        # 1  2020-12-01    False    False   False        False
        # 2  2020-12-02    False    False   False        False
        # 3  2020-12-03    False    False   False        False
        # 4  2020-12-04    False     True   False         True
        # 5  2020-12-05     True    False   False         True
        # 6  2020-12-06     True    False   False         True
        # 7  2020-12-07    False    False   False        False
        # 8  2020-12-08    False    False   False        False
        # 9  2020-12-09    False    False   False        False
        # 10 2020-12-10    False     True   False         True
        # 11 2020-12-11    False    False    True         True
        # 12 2020-12-12     True    False   False         True
        # 13 2020-12-13     True    False   False         True
        # 14 2020-12-14    False    False   False        False
        # 15 2020-12-15    False    False   False        False
        # 16 2020-12-16    False     True   False         True
        # 17 2020-12-17    False    False    True         True
        # 18 2020-12-18    False     True   False         True
        # 19 2020-12-19     True    False   False         True
        # 20 2020-12-20     True    False   False         True
        # 21 2020-12-21    False    False   False        False
        # 22 2020-12-22    False    False   False        False
        # 23 2020-12-23    False    False   False        False
        # 24 2020-12-24    False     True   False         True
        # 25 2020-12-25    False    False    True         True
        # 26 2020-12-26     True    False       -            -
        # holidays dates are completely made up
        start = '2020-12-01'
        end = '2020-12-25'
        holidays = ['2020-12-04',
                    '2020-12-10',
                    '2020-12-16',
                    '2020-12-18',
                    '2020-12-24',
                    ]
        bridges, long_weekends = spot_holiday_bridges(
            start=start, end=end, holidays=holidays)
        self.assertEqual(len(bridges), 3)
        self.assertIn(datetime(2020, 12, 11), bridges)
        self.assertIn(datetime(2020, 12, 17), bridges)
        self.assertIn(datetime(2020, 12, 25), bridges)
        self.assertEqual(len(long_weekends), 14)
        self.assertIn(datetime(2020, 12, 4), long_weekends)
        self.assertIn(datetime(2020, 12, 5), long_weekends)
        self.assertIn(datetime(2020, 12, 6), long_weekends)
        self.assertIn(datetime(2020, 12, 10), long_weekends)
        self.assertIn(datetime(2020, 12, 11), long_weekends)
        self.assertIn(datetime(2020, 12, 12), long_weekends)
        self.assertIn(datetime(2020, 12, 13), long_weekends)
        self.assertIn(datetime(2020, 12, 16), long_weekends)
        self.assertIn(datetime(2020, 12, 17), long_weekends)
        self.assertIn(datetime(2020, 12, 18), long_weekends)
        self.assertIn(datetime(2020, 12, 19), long_weekends)
        self.assertIn(datetime(2020, 12, 20), long_weekends)
        self.assertIn(datetime(2020, 12, 24), long_weekends)
        self.assertIn(datetime(2020, 12, 25), long_weekends)

    def test_no_holidays(self):
        start = '2020-12-01'
        end = '2020-12-25'
        holidays = []
        bridges, long_weekends = spot_holiday_bridges(
            start=start, end=end, holidays=holidays)
        self.assertEqual(bridges, [])
        self.assertEqual(long_weekends, [])

    def test2(self):
        #          date  weekend  holiday  bridge long_weekend
        # 0  2020-11-30    False     True       -            -
        # 1  2020-12-01    False    False   False        False
        # 2  2020-12-02    False    False   False        False
        # 3  2020-12-03    False     True   False         True
        # 4  2020-12-04    False    False    True         True
        # 5  2020-12-05     True     True   False         True
        # 6  2020-12-06     True    False   False         True
        # 7  2020-12-07    False    False   False        False
        # 8  2020-12-08    False    False   False        False
        # 9  2020-12-09    False    False   False        False
        # 10 2020-12-10    False    False   False        False
        # 11 2020-12-11    False    False   False        False
        # 12 2020-12-12     True     True   False         True
        # 13 2020-12-13     True     True   False         True
        # 14 2020-12-14    False     True   False         True
        # 15 2020-12-15    False    False   False        False
        # 16 2020-12-16    False    False   False        False
        # 17 2020-12-17    False    False   False        False
        # 18 2020-12-18    False    False   False        False
        # 19 2020-12-19     True    False   False         True
        # 20 2020-12-20     True    False   False         True
        # 21 2020-12-21    False    False    True         True
        # 22 2020-12-22    False     True   False         True
        # 23 2020-12-23    False    False    True         True
        # 24 2020-12-24    False     True   False         True
        # 25 2020-12-25    False    False    True         True
        # 26 2020-12-26     True    False       -            -
        # holidays dates are completely made up
        start = '2020-12-01'
        end = '2020-12-25'
        holidays = ['2020-11-30',
                    '2020-12-03',
                    '2020-12-05',
                    '2020-12-12',
                    '2020-12-13',
                    '2020-12-14',
                    '2020-12-22',
                    '2020-12-24'
                    ]
        bridges, long_weekends = spot_holiday_bridges(
            start=start, end=end, holidays=holidays)
        self.assertEqual(len(bridges), 4)
        self.assertIn(datetime(2020, 12, 4), bridges)
        self.assertIn(datetime(2020, 12, 21), bridges)
        self.assertIn(datetime(2020, 12, 23), bridges)
        self.assertIn(datetime(2020, 12, 25), bridges)
        self.assertEqual(len(long_weekends), 14)
        self.assertIn(datetime(2020, 12, 3), long_weekends)
        self.assertIn(datetime(2020, 12, 4), long_weekends)
        self.assertIn(datetime(2020, 12, 5), long_weekends)
        self.assertIn(datetime(2020, 12, 6), long_weekends)
        self.assertIn(datetime(2020, 12, 12), long_weekends)
        self.assertIn(datetime(2020, 12, 13), long_weekends)
        self.assertIn(datetime(2020, 12, 14), long_weekends)
        self.assertIn(datetime(2020, 12, 19), long_weekends)
        self.assertIn(datetime(2020, 12, 20), long_weekends)
        self.assertIn(datetime(2020, 12, 21), long_weekends)
        self.assertIn(datetime(2020, 12, 22), long_weekends)
        self.assertIn(datetime(2020, 12, 23), long_weekends)
        self.assertIn(datetime(2020, 12, 24), long_weekends)
        self.assertIn(datetime(2020, 12, 25), long_weekends)

    def test_end_before_start(self):
        start = '2020-01-10'
        end = '2020-01-01'
        msg = "Start date must be before end date."
        with self.assertRaisesRegex(ValueError, msg):
            _ = spot_holiday_bridges(start=start, end=end, holidays=[])

    def test_end_equal_start(self):
        start = '2020-01-10'
        end = '2020-01-10'
        msg = "Start date must be before end date."
        with self.assertRaisesRegex(ValueError, msg):
            _ = spot_holiday_bridges(start=start, end=end, holidays=[])

    def test_start_as_datetime(self):
        #          date  weekend  holiday  bridge long_weekend
        # 0  2020-11-30    False    False       -            -
        # 1  2020-12-01    False    False   False        False
        # 2  2020-12-02    False    False   False        False
        # 3  2020-12-03    False    False   False        False
        # 4  2020-12-04    False     True   False         True
        # 5  2020-12-05     True    False   False         True
        # 6  2020-12-06     True    False       -            -
        start = datetime(2020, 12, 1)
        end = '2020-12-05'
        holidays = ['2020-12-04']
        bridges, long_weekends = spot_holiday_bridges(
            start=start, end=end, holidays=holidays)
        self.assertEqual(bridges, [])
        self.assertEqual(len(long_weekends), 2)
        self.assertIn(datetime(2020, 12, 4), long_weekends)
        self.assertIn(datetime(2020, 12, 5), long_weekends)

    def test_start_and_end_as_datetime(self):
        #          date  weekend  holiday  bridge long_weekend
        # 0  2020-11-30    False    False       -            -
        # 1  2020-12-01    False    False   False        False
        # 2  2020-12-02    False    False   False        False
        # 3  2020-12-03    False    False   False        False
        # 4  2020-12-04    False     True   False         True
        # 5  2020-12-05     True    False   False         True
        # 6  2020-12-06     True    False       -            -
        start = datetime(2020, 12, 1)
        end = datetime(2020, 12, 5)
        holidays = ['2020-12-04']
        bridges, long_weekends = spot_holiday_bridges(
            start=start, end=end, holidays=holidays)
        self.assertEqual(bridges, [])
        self.assertEqual(len(long_weekends), 2)
        self.assertIn(datetime(2020, 12, 4), long_weekends)
        self.assertIn(datetime(2020, 12, 5), long_weekends)

    def test_holidays_as_datetime(self):
        #          date  weekend  holiday  bridge long_weekend
        # 0  2020-11-30    False    False       -            -
        # 1  2020-12-01    False    False   False        False
        # 2  2020-12-02    False    False   False        False
        # 3  2020-12-03    False     True   False         True
        # 4  2020-12-04    False     True   False         True
        # 5  2020-12-05     True    False   False         True
        # 6  2020-12-06     True    False       -            -
        start = datetime(2020, 12, 1)
        end = datetime(2020, 12, 5)
        holidays = [datetime(2020, 12, 3), datetime(2020, 12, 4)]
        bridges, long_weekends = spot_holiday_bridges(
            start=start, end=end, holidays=holidays)
        self.assertEqual(bridges, [])
        self.assertEqual(len(long_weekends), 3)
        self.assertIn(datetime(2020, 12, 3), long_weekends)
        self.assertIn(datetime(2020, 12, 4), long_weekends)
        self.assertIn(datetime(2020, 12, 5), long_weekends)

    def test_start_one_day_before_end(self):
        #          date  weekend  holiday  bridge long_weekend
        # 0  2020-12-02    False    False       -            -
        # 1  2020-12-03    False     True   False         True
        # 2  2020-12-04    False    False    True         True
        # 3  2020-12-05     True    False       -            -
        start = datetime(2020, 12, 3)
        end = datetime(2020, 12, 4)
        holidays = ['2020-12-03']
        bridges, long_weekends = spot_holiday_bridges(
            start=start, end=end, holidays=holidays)
        self.assertEqual(len(bridges), 1)
        self.assertIn(datetime(2020, 12, 4), bridges)
        self.assertEqual(len(long_weekends), 2)
        self.assertIn(datetime(2020, 12, 3), long_weekends)
        self.assertIn(datetime(2020, 12, 4), long_weekends)


if __name__ == '__main__':
    unittest.main()
