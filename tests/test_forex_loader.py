import pandas as pd
from io import StringIO
from scripts.data_pipeline.forex_loader import ForexLoader
from pathlib import Path

fixture_path = Path(__file__).parent / "fixtures"

def test_load_daily_forex():
    f = fixture_path / "forex_daily_sample.txt"
    loader = ForexLoader(str(f), "day")
    df = loader.load()

    assert not df.empty
    assert list(df.columns) == ["date", "open", "high", "low", "close", "volume", "datetime"]
    assert pd.api.types.is_datetime64_any_dtype(df["datetime"])


def test_load_hourly_forex():
    f = fixture_path / "forex_hourly_sample.txt"
    loader = ForexLoader(str(f), "hour")
    df = loader.load()

    assert not df.empty
    assert "datetime" in df.columns
    assert pd.Timestamp("2010-01-01 12:00:00") in df["datetime"].values


def test_load_30min_forex():
    f = fixture_path / "forex_30min_sample.txt"
    loader = ForexLoader(str(f), "hour")
    df = loader.load()

    assert not df.empty
    assert "datetime" in df.columns
    assert pd.Timestamp("2010-01-03 17:30:00") in df["datetime"].values


def test_load_1min_forex():
    f = fixture_path / "forex_1min_sample.txt"
    loader = ForexLoader(str(f), "hour")
    df = loader.load()

    assert not df.empty
    assert "datetime" in df.columns
    assert pd.Timestamp("2023-12-11 00:00:00") in df["datetime"].values