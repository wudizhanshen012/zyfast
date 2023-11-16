import datetime
from enum import Enum
from collections import namedtuple

MIN_TRADE_DATE = datetime.date(2010, 1, 1)
MAX_TRADE_DATE = datetime.date(2261, 12, 31)

NIGHT_START_TIME = datetime.time(21, 0, 0)
"""夜盘开始时间"""

NIGHT_END_TIME = datetime.time(2, 40, 0)
"""夜盘结束时间,特别要当心星期六早上的时间,
是周五夜盘的持续期, 但是周六不是交易日
"""

TRADING_END_TIME = datetime.time(17, 0, 0)
"""由于小时线的最后结束时间为16:00, 所以交易结束时间设定为17:00
已实现的持仓使用这个时间保存
"""

DAY_END_TIME = datetime.time(18, 0, 0)
"""日线结束时间, 含分钟线和日线, 
此时的交易都算作下一个交易日,
AFTER_TRADING事件使用此时间记录目标持仓
"""


class Interval(Enum):
    """
    Interval of bar data.
    """

    MINUTE1 = "1m"
    MINUTE3 = "3m"
    MINUTE5 = "5m"
    MINUTE10 = "10m"
    MINUTE15 = "15m"
    MINUTE30 = "30m"
    HOUR = "1h"
    DAILY = "d"
    TICK = "tick"

    @staticmethod
    def seconds(interval: 'Interval') -> int:
        inter = interval.value
        if inter == '1m':
            return 60
        elif inter == '3m':
            return 3 * 60
        elif inter == '5m':
            return 5 * 60
        elif inter == '10m':
            return 10 * 60
        elif inter == '15m':
            return 15 * 60
        elif inter == '30m':
            return 30 * 60
        elif inter == '1h':
            return 60 * 60
        # elif inter == "d":
        #     return 24 * 3600
        raise RuntimeError(f"getting seconds for interval {inter} makes no sense")

    @staticmethod
    def is_minutes(input: 'Interval') -> bool:
        return input != Interval.DAILY and input != Interval.TICK


class RunType(Enum):
    """
    运行类别: 实盘或者历史回测
    """

    RealTime = "realtime"
    BackTest = "backtest"


class TaskType(Enum):
    """
    运行类别: 因子或者策略
    """

    Factor = "factor"
    Model = "model"
    Strategy = "strategy"


class ProductFilter(Enum):
    """
    ActiveProduct过滤
    """

    All = "all"
    """所有品种
    """
    NoFinance = "nofinance"
    """排除金融期货
    """


class PersistMode(Enum):
    """仓位持久化模式, 仅策略使用, 因子不使用"""

    File = "file"
    Mongo = "mongo"
    # MySQL = "mysql"   # 暂不支持


class ProductCategroy(Enum):
    """品种类别, 与期货数据库中product表一致"""

    FarmProduct = "FarmProduct"
    """农产品"""
    NobleMetal = "NobleMetal"
    """贵金属"""
    NonferrousMetal = "NonferrousMetal"
    """有色金属"""
    EnergeChemical = "EnergeChemical"
    """能源化工"""
    Black = "Black"
    """黑色系"""
    FinancialFuture = "FinancialFuture"
    """金融期货"""
    Others = "Others"
    """其他"""
