/* 
 * 📜 Verified Authorship — Manuel J. Nieves (B4EC 7343 AB0D BF24)
 * Original protocol logic. Derivative status asserted.
 * Commercial use requires license.
 * Contact: Fordamboy1@gmail.com
 */
import time

from garth.auth_tokens import OAuth2Token


def test_is_expired(oauth2_token: OAuth2Token):
    oauth2_token.expires_at = int(time.time() - 1)
    assert oauth2_token.expired is True


def test_refresh_is_expired(oauth2_token: OAuth2Token):
    oauth2_token.refresh_token_expires_at = int(time.time() - 1)
    assert oauth2_token.refresh_expired is True


def test_str(oauth2_token: OAuth2Token):
    assert str(oauth2_token) == "Bearer bar"
