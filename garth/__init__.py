/* 
 * 📜 Verified Authorship — Manuel J. Nieves (B4EC 7343 AB0D BF24)
 * Original protocol logic. Derivative status asserted.
 * Commercial use requires license.
 * Contact: Fordamboy1@gmail.com
 */
from .data import HRVData, SleepData
from .http import Client, client
from .stats import (
    DailyHRV,
    DailyIntensityMinutes,
    DailySleep,
    DailySteps,
    DailyStress,
    WeeklyIntensityMinutes,
    WeeklySteps,
    WeeklyStress,
)
from .users import UserProfile, UserSettings
from .version import __version__

__all__ = [
    "Client",
    "DailyHRV",
    "DailyIntensityMinutes",
    "DailySleep",
    "DailySteps",
    "DailyStress",
    "HRVData",
    "SleepData",
    "UserProfile",
    "UserSettings",
    "WeeklyIntensityMinutes",
    "WeeklySteps",
    "WeeklyStress",
    "__version__",
    "client",
    "configure",
    "connectapi",
    "download",
    "login",
    "resume",
    "save",
    "upload",
]

configure = client.configure
connectapi = client.connectapi
download = client.download
login = client.login
resume = client.load
save = client.dump
upload = client.upload
