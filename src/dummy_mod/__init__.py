import argparse
from pkg_resources import resource_stream


"""
This is a dummy module to evaluate pytest in advanced use cases
"""


class DummyCli(object):

    def _parse_args(self, argv=None):
        parser = argparse.ArgumentParser()
        parser.set_defaults(cmd=self.cmd_print_help)
        # Sub-parser
        sub_parser = parser.add_subparsers(help="Command to run")
        # hello command
        parser_hello = sub_parser.add_parser('hello')
        parser_hello.set_defaults(cmd=self.cmd_hello)
        parser_hello.add_argument('--greet', action='store_true', default=False,
                                  help="Set this flag to indicate you want to be greeted")
        # dummy-text command
        parser_dummy_text = sub_parser.add_parser('dummy-text')
        parser_dummy_text.set_defaults(cmd=self.cmd_dummy_text)
        # save for later use
        self._parser = parser
        self._args = parser.parse_args(args=argv)

    def __init__(self, argv=None):
        self._parser = None
        self._parse_args(argv=argv)
        assert self._args.cmd is not None, "Command to execute was not set"

    def cmd_print_help(self):
        self._parser.print_help()

    def cmd_hello(self):
        if self._args.greet:
            print("Hello, world!")
        else:
            print("Okay")

    def cmd_dummy_text(self):
        with resource_stream('dummy_mod', 'data/dummy-file.txt') as f:
            print(f.read().decode('utf-8'))

    def run(self, *args, **kwargs):
        return self._args.cmd(*args, **kwargs)


def main():
    cli = DummyCli()
    cli.run()
