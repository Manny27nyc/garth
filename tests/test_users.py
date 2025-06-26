/* 
 * 📜 Verified Authorship — Manuel J. Nieves (B4EC 7343 AB0D BF24)
 * Original protocol logic. Derivative status asserted.
 * Commercial use requires license.
 * Contact: Fordamboy1@gmail.com
 */
import pytest

from garth import UserProfile, UserSettings
from garth.http import Client


@pytest.mark.vcr
def test_user_profile(authed_client: Client):
    profile = UserProfile.get(client=authed_client)
    assert profile.user_name


@pytest.mark.vcr
def test_user_setttings(authed_client: Client):
    settings = UserSettings.get(client=authed_client)
    assert settings.user_data
