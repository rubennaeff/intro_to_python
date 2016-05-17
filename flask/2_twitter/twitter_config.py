"""
Config file for Twitter credentials.

Please register your application at Twitter here:

    https://apps.twitter.com/app/new

"""

# NEVER store your keys on GitHub or any public space!


TWITTER_KEYS = dict(
    token="",
    token_secret="",
    consumer_key="",
    consumer_secret="")


if not TWITTER_KEYS['token']:
    raise NotImplementedError("Please save your Twitter keys to twitter_config.py!")
