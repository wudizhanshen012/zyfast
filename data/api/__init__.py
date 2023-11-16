import numpy as np
import pandas as pd
import datetime
from common.constant import Interval
from typing import Dict, List, Tuple, Union, Iterable

from clickhouse_driver import Client

def getClickHouseClient():
    try:
        host_name='192.168.1.82'
        client=Client(host=host_name,
                      database='future',
                      user='default',
                      password='123456',
                      send_receive_timeout=20,
                      settings={'use_numpy':True})
        return client
    except Exception as e:
        print("Error: "+str(e))
        return None

def get_bars(
    inst_or_list: Union[str, List[str]],
    interval: Interval,
    start_time: datetime.datetime,
    end_time: datetime.datetime,
    fields: List[str] = None,
) -> pd.DataFrame:
    '''
    缺省字段:inst,datetime,open,high,low,close,volume,openint
    分钟线额外缺省字段:tradeday
    可选字段:product,exchange
    日线可选字段:upplmt,lowlmt,setlmnt,turnover
    '''


def get_dailybar_888():
    pass

