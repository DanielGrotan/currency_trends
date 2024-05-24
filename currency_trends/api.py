from datetime import date

import pandas as pd
import streamlit as st
from pandas import DataFrame

from .utils import get_absolute_path


@st.cache_data
def get_currency_trend(
    currency_code: str, start_date: date, end_date: date
) -> DataFrame:
    url = f"https://data.norges-bank.no/api/data/EXR/B.{currency_code}.NOK.SP?format=csv&startPeriod={start_date}&endPeriod={end_date}&locale=no&bom=include"

    df = pd.read_csv(url, sep=";", decimal=",")
    df = df[["BASE_CUR", "Basisvaluta", "TIME_PERIOD", "OBS_VALUE"]]
    df.columns = ["Code", "Currency", "Date", "Exchange Rate"]
    df["Date"] = pd.to_datetime(df["Date"], format="%Y-%m-%d")

    return df


@st.cache_data
def get_currency_codes() -> list[str]:
    with open(get_absolute_path(__file__, "currency_codes.txt")) as f:
        return f.read().splitlines()
