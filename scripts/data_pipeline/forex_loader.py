from typing import Literal, Optional
import pandas as pd


class ForexLoader:
    # load data from 4 different formats 

    HEADERS = {
        "day": ["date", "open", "high", "low", "close", "volume"],
        "hour": ["date", "time", "open", "high", "low", "close", "volume"],
        "30min": ["date", "time", "open", "high", "low", "close", "volume"],
        "1min": ["date", "time", "open", "high", "low", "close", "volume"],
    }


    def __init__(self, path: str, granularity: Literal["day", "hour", "30min", "1min"]):
        self.path = path
        self.granularity = granularity

    def load(self) -> pd.DataFrame:
        df = pd.read_csv(self.path, header=None, names=self.HEADERS[self.granularity])
        if self.granularity == "day":
            df["datetime"] = pd.to_datetime(df["date"], format="%Y%m%d")

        else: 
            df['datetime'] = pd.to_datetime(df["date"].astype(str) + " " + df["time"], format="%Y%m%d %H:%M:%S")

        return df
