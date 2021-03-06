# nose-hipchat
Nose testing plugin for posting to hipchat

This plugin makes it possible for the nose testing system to publish results directly to a HipChat channel.

Example usage:
```bash
$ nosetests --with-nose-hipchat --hipchat-url=https://your-company.hipchat.com/v2/room/12345/notification?auth_token=ABC123 --hipchat-epilogue="Thanks for your time. See test logs in `hostname`:/tmp/noselogs.log for more detail" intentional_failures >> /tmp/noselogs.log 2>&1
```

Results in something like this:
![Image](failure.png?raw=true)

Or this:
```bash
$ nosetests --with-nose-hipchat --hipchat-url=https://your-company.hipchat.com/v2/room/12345/notification?auth_token=ABC123 --hipchat-epilogue="Thanks for your time. See test logs in `hostname`:/tmp/noselogs.log for more detail" test >> /tmp/noselogs.log 2>&1
```

Results in something like this:
![Image](success.png?raw=true)

## Installation

### Install the nose-hipchat plugin
```bash
pip install nose-hipchat
```

### Enable HipChat Publishing
The first thing you'll need is a HipChat account. If you don't have one of those, I can't help you.
Once you've taken care of that, get an API key for posting to HipChat by using a web browser to log into your HipChat account, navigate to the list of rooms, and create a new integration for the room you want:

| Link to Integrations |
| --- |
| ![Image](hipchat-1.png?raw=true) |


| Click on "Build Your Own" Integration |
| --- |
| ![Image](hipchat-3.png?raw=true) |

| Name your integration |
| --- |
| ![Image](hipchat-2.png?raw=true) |

This should result in a URL that has a room ID and an API key in it, with a form something like:
```
https://your-company.hipchat.com/v2/room/12345/notification?auth_token=ABC123
```

You'll need that URL when running nose tests, as seen in the usage description at the top of this page.
