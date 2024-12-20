import sys

from metaflow import Config, FlowSpec, conda, pypi, step, config_expr


class HelloCondaFlow(FlowSpec):
    v1_yml = Config(
        "v1_yml", default="v1.yml", parser="metaflow_dep_parsers.yml_parser"
    )
    v2_req = Config(
        "v2_req", default="v2.txt", parser="metaflow_dep_parsers.req_parser"
    )

    @step
    def start(self):
        print("HelloCondaFlow is starting.")
        self.next(self.v1, self.v2)

    @conda(config_expr("v1_yml"))
    @step
    def v1(self):
        import regex

        self.lib_version = regex.__version__  # Should be '2.5.148'
        print("Python: %s; library version: %s" % (sys.version, self.lib_version))
        self.next(self.join)

    @pypi(**v2_req)
    @step
    def v2(self):
        import regex

        self.lib_version = regex.__version__  # Should be '2.5.147'
        print("Python: %s; library version: %s" % (sys.version, self.lib_version))
        self.next(self.join)

    @step
    def join(self, inputs):
        self.next(self.end)

    @step
    def end(self):
        pass


if __name__ == "__main__":
    HelloCondaFlow()
