#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import functools
from datadog import statsd
import speedtest

log = logging.getLogger('speedtest_datadog')
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


# Decoration of the functions of speedtest
speedtest.Speedtest.download = DatadogGauge('speedtest.download')(
    speedtest.Speedtest.download
)

speedtest.Speedtest.upload = DatadogGauge('speedtest.upload')(
    speedtest.Speedtest.upload
)

speedtest.Speedtest.get_best_server = DatadogGaugeLatency('speedtest.latency')(
    speedtest.Speedtest.get_best_server
)

# required for the command line entry point.
main = speedtest.main

if __name__ == '__main__':
    main()
