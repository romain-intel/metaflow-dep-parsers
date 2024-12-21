# Dependency parsers for Metaflow

With the introduction of Configs in
[Metaflow 2.13](https://github.com/Netflix/metaflow/releases/tag/2.13), it
is now possible to provide data to decorators using Configs.

This package allows you to use the following syntax:
``` python
from metaflow import Config, pypi, FlowSpec, step

class MyFlow(FlowSpec):
    reqs = Config("reqs", default="requirements.txt", parser="metaflow_dep_parsers.req_parser")

    @pypi(**reqs)
    @step
    def start(self):
        self.next(self.end)

    @step
    def end(self):
        pass
```

You only need to install this library on the machine launching the Metaflow flow above
(notice that the parser is a string).

## Available parsers

This library includes two parsers:
  - `req_parser` which is meant to be used with `@pypi` or `@pypi_base`. It will parse
    a `requirements.txt` file (subset).
 - `yml_parser` which is meant to be used with `@conda` or `@conda_base`. It will
   parse a `environment.yml` file (subset).

## Metaflow Netflix Extensions

If you are using the [Netflix Extensions](https://github.com/Netflix/metaflow-nflx-extensions),
you do not need this package and can instead do:
``` python
from metaflow import Config, pypi, FlowSpec, step, req_parser

class MyFlow(FlowSpec):
    reqs = Config("reqs", default="requirements.txt", parser=req_parser)

    @pypi(**reqs)
    @step
    def start(self):
        self.next(self.end)

    @step
    def end(self):
        pass
```

The parsers present in this package offer a subset of the functionality present in the
Netflix Extension (since the `@pypi` and `@conda` decorators in the mainline Metaflow
are not as featured as those in the Netflix Extension).

# Contributing

This package is provided as a small convenience for the community. Bug reports and PRs are
more than welcome.
