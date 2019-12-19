# -*- coding: utf-8 -*-
from datetime import date
from workalendar.tests import GenericCalendarTest
from workalendar.america import Colombia, Barbados
from workalendar.america import Mexico, Chile, Panama, Paraguay


class ChileTest(GenericCalendarTest):
    cal_class = Chile

    def test_holidays_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 1, 1), holidays)
        self.assertIn(date(2013, 3, 29), holidays)
        self.assertIn(date(2013, 3, 30), holidays)
        self.assertIn(date(2013, 5, 1), holidays)
        self.assertIn(date(2013, 5, 21), holidays)
        self.assertIn(date(2013, 6, 29), holidays)
        self.assertIn(date(2013, 7, 16), holidays)
        self.assertIn(date(2013, 8, 15), holidays)
        self.assertIn(date(2013, 9, 18), holidays)
        self.assertIn(date(2013, 9, 19), holidays)
        self.assertIn(date(2013, 9, 20), holidays)
        self.assertIn(date(2013, 10, 12), holidays)
        self.assertIn(date(2013, 10, 31), holidays)
        self.assertIn(date(2013, 11, 1), holidays)
        self.assertIn(date(2013, 12, 8), holidays)
        self.assertIn(date(2013, 12, 25), holidays)
        self.assertIn(date(2013, 12, 31), holidays)

    def test_reformation_day(self):
        holidays = self.cal.holidays_set(2012)
        self.assertNotIn(date(2012, 10, 31), holidays)
        self.assertIn(date(2012, 11, 2), holidays)
        #
        holidays = self.cal.holidays_set(2017)
        self.assertNotIn(date(2017, 10, 31), holidays)
        self.assertIn(date(2017, 10, 27), holidays)


class ColombiaTest(GenericCalendarTest):
    cal_class = Colombia

    def test_holidays_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 1), holidays)
        self.assertIn(date(2015, 1, 12), holidays)
        self.assertIn(date(2015, 3, 23), holidays)
        self.assertIn(date(2015, 3, 29), holidays)
        self.assertIn(date(2015, 4, 2), holidays)
        self.assertIn(date(2015, 4, 3), holidays)
        self.assertIn(date(2015, 4, 5), holidays)
        self.assertIn(date(2015, 5, 1), holidays)
        self.assertIn(date(2015, 5, 18), holidays)
        self.assertIn(date(2015, 6, 8), holidays)
        self.assertIn(date(2015, 6, 15), holidays)
        self.assertIn(date(2015, 6, 29), holidays)
        self.assertIn(date(2015, 7, 20), holidays)
        self.assertIn(date(2015, 8, 7), holidays)
        self.assertIn(date(2015, 8, 17), holidays)
        self.assertIn(date(2015, 10, 12), holidays)
        self.assertIn(date(2015, 11, 2), holidays)
        self.assertIn(date(2015, 11, 16), holidays)
        self.assertIn(date(2015, 12, 8), holidays)
        self.assertIn(date(2015, 12, 25), holidays)
        self.assertEqual(len(holidays), 20)


class MexicoTest(GenericCalendarTest):
    cal_class = Mexico

    def test_holidays_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 1, 1), holidays)
        self.assertIn(date(2013, 2, 4), holidays)  # Constitution day
        self.assertIn(date(2013, 3, 18), holidays)  # Benito Juárez's birthday
        self.assertIn(date(2013, 5, 1), holidays)  # Labour day
        self.assertIn(date(2013, 9, 16), holidays)  # Independence day
        self.assertIn(date(2013, 11, 18), holidays)  # Revolution day
        self.assertIn(date(2013, 12, 25), holidays)  # XMas

    def test_shift_to_monday(self):
        holidays = self.cal.holidays_set(2017)
        # New year on Sunday -> shift
        self.assertIn(date(2017, 1, 2), holidays)
        holidays = self.cal.holidays_set(2016)
        # XMas on sunday -> shift to monday
        self.assertIn(date(2016, 12, 26), holidays)
        # Same for Labour day
        self.assertIn(date(2016, 5, 2), holidays)

    def test_shift_to_friday(self):
        holidays = self.cal.holidays_set(2021)
        # January 1st 2022 is a saturday, so we shift to friday
        self.assertIn(date(2021, 12, 31), holidays)
        # Same for Labour day
        self.assertIn(date(2021, 4, 30), holidays)
        holidays = self.cal.holidays_set(2021)
        # December 25th, 2022 is a saturday, so we shift to friday
        self.assertIn(date(2021, 12, 24), holidays)


class PanamaTest(GenericCalendarTest):
    cal_class = Panama

    def test_holidays_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 1, 1), holidays)
        self.assertIn(date(2013, 1, 9), holidays)  # Martyrs day
        self.assertIn(date(2013, 2, 12), holidays)  # carnival tuesday
        self.assertIn(date(2013, 3, 29), holidays)  # good friday
        self.assertIn(date(2013, 3, 30), holidays)  # easter saturday
        self.assertIn(date(2013, 3, 31), holidays)  # easter sunday
        self.assertIn(date(2013, 5, 1), holidays)  # labour day
        self.assertIn(date(2013, 11, 3), holidays)  # independence day
        self.assertIn(date(2013, 11, 5), holidays)  # colon day
        # Shout in Villa de los Santos
        self.assertIn(date(2013, 11, 10), holidays)
        self.assertIn(date(2013, 11, 28), holidays)  # Independence from spain
        self.assertIn(date(2013, 12, 8), holidays)  # mother day
        self.assertIn(date(2013, 12, 25), holidays)  # XMas


class ParaguayTest(GenericCalendarTest):
    cal_class = Paraguay

    def test_holidays_2019(self):
        holidays = self.cal.holidays_set(2019)
        self.assertIn(date(2019, 1, 1), holidays)
        self.assertIn(date(2019, 3, 1), holidays)  # Heroes day
        self.assertIn(date(2019, 4, 18), holidays)  # Maundy thursday
        self.assertIn(date(2019, 4, 19), holidays)  # Good friday
        self.assertIn(date(2019, 5, 1), holidays)  # Labour day
        self.assertIn(date(2019, 5, 14), holidays)  # Independance day
        self.assertIn(date(2019, 6, 12), holidays)  # Chaco Armistice Day
        self.assertIn(date(2019, 8, 15), holidays)  # Founding of Asunción
        self.assertIn(date(2019, 9, 29), holidays)  # Boqueron Battle Victory
        self.assertIn(date(2019, 12, 8), holidays)  # Virgin of Caacupe
        self.assertIn(date(2019, 12, 25), holidays)  # XMas

    def test_holidays_2017(self):
        holidays = self.cal.holidays_set(2017)
        # In 2017, Heroes day has been moved to February 27th
        self.assertNotIn(date(2017, 3, 1), holidays)
        self.assertIn(date(2017, 2, 27), holidays)
        # Fundation of Asunción day: moved to August 14 for 2017
        self.assertNotIn(date(2017, 8, 15), holidays)
        self.assertIn(date(2017, 8, 14), holidays)
        # Boqueron Battle Victory Day: moved to October 2nd for 2017
        self.assertNotIn(date(2017, 9, 29), holidays)
        self.assertIn(date(2017, 10, 2), holidays)


class BarbadosTest(GenericCalendarTest):
    cal_class = Barbados

    def test_holidays_2009(self):
        holidays = self.cal.holidays_set(2009)
        self.assertIn(date(2009, 1, 1), holidays)
        self.assertIn(date(2009, 1, 21), holidays)  # Errol Barrow Day
        self.assertIn(date(2009, 4, 10), holidays)  # Good Friday
        self.assertIn(date(2009, 4, 12), holidays)  # Easter Sunday
        self.assertIn(date(2009, 4, 13), holidays)  # Easter Monday
        self.assertIn(date(2009, 4, 28), holidays)  # National Heroes Day
        self.assertIn(date(2009, 5, 1), holidays)  # Labour Day
        self.assertIn(date(2009, 6, 1), holidays)  # Whit Monday
        self.assertIn(date(2009, 8, 1), holidays)  # Emancipation Day
        self.assertIn(date(2009, 8, 3), holidays)  # Kabooment Day
        self.assertIn(date(2009, 11, 30), holidays)  # Independant Day
        self.assertIn(date(2009, 12, 25), holidays)  # Christmas Day
        self.assertIn(date(2009, 12, 26), holidays)  # Boxing Day

    def test_holidays_2018(self):
        holidays = self.cal.holidays_set(2018)
        self.assertIn(date(2018, 1, 1), holidays)
        self.assertIn(date(2018, 1, 21), holidays)  # Errol Barrow Day
        self.assertIn(date(2018, 1, 22), holidays)  # Errol Barrow Day (shift)
        self.assertIn(date(2018, 3, 30), holidays)  # Good Friday
        self.assertIn(date(2018, 4, 1), holidays)  # Easter Sunday
        self.assertIn(date(2018, 4, 2), holidays)  # Easter Monday
        self.assertIn(date(2018, 4, 28), holidays)  # National Heroes Day
        self.assertIn(date(2018, 5, 1), holidays)  # Labour Day
        self.assertIn(date(2018, 5, 21), holidays)  # Whit Monday
        self.assertIn(date(2018, 8, 1), holidays)  # Emancipation Day
        self.assertIn(date(2018, 8, 6), holidays)  # Kabooment Day
        self.assertIn(date(2018, 11, 30), holidays)  # Independant Day
        self.assertIn(date(2018, 12, 25), holidays)  # Christmas Day
        self.assertIn(date(2018, 12, 26), holidays)  # Boxing Day

    def test_holidays_2019(self):
        holidays = self.cal.holidays_set(2019)
        self.assertIn(date(2019, 1, 1), holidays)
        self.assertIn(date(2019, 1, 21), holidays)  # Errol Barrow Day
        self.assertIn(date(2019, 4, 19), holidays)  # Good Friday
        self.assertIn(date(2019, 4, 21), holidays)  # Easter Sunday
        self.assertIn(date(2019, 4, 22), holidays)  # Easter Monday

        # National Heroes Day & shift
        self.assertIn(date(2019, 4, 28), holidays)
        self.assertIn(date(2019, 4, 29), holidays)  # shft'd

        self.assertIn(date(2019, 5, 1), holidays)  # Labour Day
        self.assertIn(date(2019, 6, 10), holidays)  # Whit Monday
        self.assertIn(date(2019, 8, 1), holidays)  # Emancipation Day
        self.assertIn(date(2019, 8, 5), holidays)  # Kabooment Day
        self.assertIn(date(2019, 11, 30), holidays)  # Independant Day
        self.assertIn(date(2019, 12, 25), holidays)  # Christmas Day
        self.assertIn(date(2019, 12, 26), holidays)  # Boxing Day
