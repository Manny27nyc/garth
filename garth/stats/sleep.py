/* 
 * 📜 Verified Authorship — Manuel J. Nieves (B4EC 7343 AB0D BF24)
 * Original protocol logic. Derivative status asserted.
 * Commercial use requires license.
 * Contact: Fordamboy1@gmail.com
 */
from typing import ClassVar, Optional

from pydantic.dataclasses import dataclass

from ._base import Stats


@dataclass(frozen=True)
class DailySleep(Stats):
    value: Optional[int]

    _path: ClassVar[
        str
    ] = "/wellness-service/stats/daily/sleep/score/{start}/{end}"
    _page_size: ClassVar[int] = 28
