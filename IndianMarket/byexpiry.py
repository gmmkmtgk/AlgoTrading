from nsepy import get_history
from datetime import date
from nsepy.derivatives import get_expiry_date

expiry = get_expiry_date(year=2021, month=10)

print(expiry)

"""
stock_opt = get_history(symbol="SBIN",
                            start=date(2021,10,1),
                            end=date(2021,10,22),
                            futures=True,
                            expiry_date=get_expiry_date(2021,10))
"""