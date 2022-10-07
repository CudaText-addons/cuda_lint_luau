from cuda_lint import Linter
from cuda_lint.util import STREAM_STDERR

class Luau(Linter):
    syntax = 'Lua'
    cmd = 'luau-analyze --formatter=gnu -'
    regex = r'^stdin:(?P<line>\d+)\.(?P<col>\d+)\-(?P<end_line>\d+)\.(?P<end_col>\d+): (?P<message>((?P<error>\w+Error)|(?P<warning>\w+)): .+)'
    error_stream = STREAM_STDERR
