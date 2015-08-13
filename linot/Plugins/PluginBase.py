from __future__ import print_function
from linot.LinotArgParser import LinotArgParser


class PluginBase:
    CMD_PREFIX = None  # The identifier for subparser
    _started = False

    def __init__(self, line):
        self._line = line

    def setup(self, sub_parser):
        ap = LinotArgParser(self.CMD_PREFIX, sub_parser, self._cmd_process, self._line)
        self._setup_argument(ap)

    def is_start(self):
        return self._started

    def start(self):
        if not self._started:
            self._start()
            self._started = True

    def stop(self):
        if self._started:
            self._stop()
            self._started = False

    # Plugin should be designed to be safely stopped and re-started at anytime
    def _start(self):
        # Plugin start working!
        raise NotImplementedError

    def _stop(self):
        # Plugin stops
        raise NotImplementedError

    def _setup_argument(self, cmd_group):
        # Add the plugin specific arguments
        raise NotImplementedError

    def _cmd_process(self, args, sender):
        # process argument input
        if args is None:
            # no known arguments
            self._line.sendMessageToClient(sender, 'Unknown commands.')
        self._line.sendMessageToClient(sender, 'Command is not implemented yet')
