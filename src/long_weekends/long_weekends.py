import numpy as np
import pandas as pd
import dateutil.parser as parser
from datetime import datetime, timedelta
from typing import Union, Tuple


def spot_holiday_bridges(start: Union[str, datetime],
                         end: Union[str, datetime],
                         holidays: Union[np.ndarray, list]) -> Tuple[list, list]:
    """
    Spot holiday "bridges" (called like this for a lack of a better name in English -
    in Italy we call them "ponti"). These are single working days that are preceded
    and followed by a weekend and/or a public holiday. For example, a normal
    working Monday followed by a public holiday Tuesday would fall in this category.
    People typically take these days off work to enjoy long vacations.
    Additionally, spot "long weekends" intended as a series of 3 or more days classified
    as weekend, holiday, or holiday "bridge".
    :param start: first day of the time period of interest
    :param end: last day of the time period of interest
    :param holidays: a list or a numpy array of public holiday dates
    :return: two lists of datetime objects, the former corresponding to holiday bridges
        and the latter to long weekends
    """
    if isinstance(start, str):
        start = parser.parse(start)
    if isinstance(end, str):
        end = parser.parse(end)
    if end <= start:
        raise ValueError("Start date must be before end date.")
    # create Series of dates with 1 day padding left and right
    dates = pd.Series(pd.date_range(start - timedelta(days=1), end + timedelta(days=1)))
    # compute day_of_week (0=Monday, 6=Sunday)
    dow = dates.dt.dayofweek
    # compute is_weekend
    is_weekend = dow.isin([5, 6])
    # compute is_holiday
    is_holiday = dates.isin(holidays)
    # compute union of weekends and holidays
    is_non_working = is_weekend | is_holiday
    # spot bridges
    cs_br = is_non_working.ne(is_non_working.shift()).cumsum()
    is_bridge = (cs_br.map(cs_br.value_counts()) == 1) & (~is_non_working)
    # list of bridge dates without the padding
    bridges = dates.iloc[1:-1].loc[is_bridge.iloc[1:-1]].tolist()
    # compute union of weekend, holidays, and bridges
    is_vacation = is_non_working | is_bridge
    # spot long weekends
    cs_lw = is_vacation.ne(is_vacation.shift()).cumsum()
    is_long_weekend = (cs_lw.map(cs_lw.value_counts()) > 2) & is_vacation
    # list of long weekend dates without the padding
    long_weekends = dates.iloc[1:-1].loc[is_long_weekend.iloc[1:-1]].tolist()

    return bridges, long_weekends
