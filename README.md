# nose-hipchat
Nose testing plugin for posting to hipchat

This plugin makes it possible for the nose testing system to publish results directly to a HipChat channel.
Example usage:

```bash
$ nosetests --with-nose-hipchat --hipchat-url=https://your-company.hipchat.com/v2/room/12345/notification?auth_token=ABC123 --hipchat-epilogue="Thanks for your time. See test logs in `hostname`:/tmp/noselogs.log for more detail" intentional_failures >> /tmp/noselogs.log 2>&1
```

Results in something like this:

Or this:

```bash
$ nosetests --with-nose-hipchat --hipchat-url=https://your-company.hipchat.com/v2/room/12345/notification?auth_token=ABC123 --hipchat-epilogue="Thanks for your time. See test logs in `hostname`:/tmp/noselogs.log for more detail" test >> /tmp/noselogs.log 2>&1
```

Results in something like this:
