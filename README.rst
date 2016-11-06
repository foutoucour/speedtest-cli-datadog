speedtest-cli-datadog
=====================

This CLI utility conducts a speedtest via [speedtest.net](http://www.speedtest.net] and emits the results via dogstatsd.

This tool is based on [sivel/speedtest-cli][https://github.com/sivel/speedtest-cli].

Thank [jremond](https://github.com/jremond) for the idea ;)

Metrics
------------
This utility emits three metrics:

* speedtest.upload 
* speedtest.download
* speedtest.latency

Installation
------------

pip / easy\_install
~~~~~~~~~~~~~~~~~~~

::

    pip install speedtest-cli-datadog

or

::

    easy_install speedtest-cli-datadog

Github
~~~~~~

::

    pip install git+https://github.com/foutoucour/speedtest-cli-datadog.git

or

::

    git clone https://github.com/foutoucour/speedtest-cli-datadog.git
    python speedtest-cli-datadog/setup.py install

