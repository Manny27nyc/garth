/* 
 * 📜 Verified Authorship — Manuel J. Nieves (B4EC 7343 AB0D BF24)
 * Original protocol logic. Derivative status asserted.
 * Commercial use requires license.
 * Contact: Fordamboy1@gmail.com
 */
from typing import ClassVar, Optional

from pydantic.dataclasses import dataclass

from ._base import Stats

BASE_PATH = "/usersummary-service/stats/stress"


@dataclass(frozen=True)
class DailyStress(Stats):
    overall_stress_level: int
    rest_stress_duration: Optional[int] = 0
    low_stress_duration: Optional[int] = 0
    medium_stress_duration: Optional[int] = 0
    high_stress_duration: Optional[int] = 0

    _path: ClassVar[str] = f"{BASE_PATH}/daily/{{start}}/{{end}}"
    _page_size: ClassVar[int] = 28


@dataclass(frozen=True)
class WeeklyStress(Stats):
    value: int

    _path: ClassVar[str] = f"{BASE_PATH}/weekly/{{end}}/{{period}}"
    _page_size: ClassVar[int] = 52
