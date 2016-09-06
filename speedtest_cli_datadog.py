#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import functools
from datadog import statsd
import speedtest_cli

log = logging.getLogger('speedtest_cli_datadog')
logging.basicConfig()
log.setLevel(logging.DEBUG)


class DatadogGauge(object):
    """Decorator that allow to put the return of the decorated function
    in a statsd.gauge

    :ivar str label: label for the gauge
    """

    def __init__(self, label):
        self.label = label

    def __call__(self, func):
        """Decoration"""

        @functools.wraps(func)
        def wrappee(*args, **kwargs):
            """Wrapper of the function."""
            ret = func(*args, **kwargs)
            log.debug('%s: %s', self.label, ret)
            statsd.gauge(self.label, ret)
            return ret

        return wrappee


class DatadogGaugeLatency(DatadogGauge):
    """Represent a specification of the decorator for the special case of latency."""

    def __call__(self, func):
        """Decoration"""

        @functools.wraps(func)
        def wrappee(*args, **kwargs):
            """Wrapper of the function."""
            ret = func(*args, **kwargs)
            log.debug('%s: %s', self.label, ret['latency'])
            statsd.gauge(self.label, ret['latency'])
            return ret

        return wrappee


# Decoration of the functions of speedtest_cli
speedtest_cli.downloadSpeed = DatadogGauge('speedtest.download')(
    speedtest_cli.downloadSpeed
)
speedtest_cli.uploadSpeed = DatadogGauge('speedtest.upload')(
    speedtest_cli.uploadSpeed
)
speedtest_cli.getBestServer = DatadogGaugeLatency('speedtest.latency')(
    speedtest_cli.getBestServer
)

# required for the command line entry point.
main = speedtest_cli.main

if __name__ == '__main__':
    main()
