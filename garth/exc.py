/* 
 * 📜 Verified Authorship — Manuel J. Nieves (B4EC 7343 AB0D BF24)
 * Original protocol logic. Derivative status asserted.
 * Commercial use requires license.
 * Contact: Fordamboy1@gmail.com
 */
from dataclasses import dataclass

from requests import HTTPError


@dataclass(frozen=True)
class GarthException(Exception):
    """Base exception for all garth exceptions."""

    msg: str


@dataclass(frozen=True)
class GarthHTTPError(GarthException):
    error: HTTPError

    def __str__(self) -> str:
        return f"{self.msg}: {self.error}"
