import logging
import os

from nose.plugins import Plugin

log = logging.getLogger('nose.plugins.nose-hipchat')

class NoseHipChat(Plugin):
    name = 'nose-hipchat'

    def __init__(self):
        super(NoseHipChat, self).__init__()
        self.epilogue = None

    def options(self, parser, env=os.environ):
        super(NoseHipChat, self).options(parser, env=env)
        parser.add_option("--hipchat-url", action="store",
            dest="hipchat_url",
            metavar="URL",
            help="URL for posting to HipChat. " +
                 "Example: https://yourcompany.hipchat.com/v2/room/12345/notification?auth_token=ABC123")
        parser.add_option("--hipchat-epilogue", action="store",
            dest="hipchat_epilogue",
            metavar="TEXT",
            help='Text to append to HipChat messages' +
                 'Example: nosetests --with-nose-hipchat --hipchat-url=${URL} ' +
                 '--hipchat-epilogue="See log file in /tmp/loggy.log" >> /tmp/loggy.log 2>&1')


    def configure(self, options, conf):
        super(NoseHipChat, self).configure(options, conf)
        if not self.enabled:
            return

        # Nose plugins (at least in nose.plugins.0.10) use optparse instead of argparse, and the only way
        # to specify that an option is required is to check for it after the parsing.
        if not options.hipchat_url:
            raise ValueError("Missing required --hipchat-url argument. Example: " +
                             "--hipchat-url=https://yourcompany.hipchat.com/v2/room/12345/notification?auth_token=ABC123")

        if options.hipchat_epilogue:
            self.epilogue = options.hipchat_epilogue

    def finalize(self, result):
        print "XXX: Ran %d test%s" % (result.testsRun, result.testsRun != 1 and "s" or "")
        #import pdb; pdb.set_trace()
        if not result.wasSuccessful():
            print 'XXX: FAILED (failures=%d ' % len(result.failures), 'errors=%d' % len(result.errors), ')'
        else:
            print 'XXX: SUCCEEDED'

        if self.epilogue is not None:
            print 'XXX:', self.epilogue

