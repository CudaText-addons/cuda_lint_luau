from cuda_lint import Linter
from cuda_lint.util import STREAM_STDERR

class Luau(Linter):
    syntax = 'Lua'
    cmd = 'luau-analyze --formatter=gnu -'
    regex = r'^stdin:(?P<line>\d+)\.(?P<col>\d+)\-(?P<end_line>\d+)\.(?P<end_col>\d+): (?P<message>(?P<code>\w+): .+)'
    error_stream = STREAM_STDERR

    def split_match(self, match):
        error = list(super().split_match(match))
        error[3] = error[0].group('code').endswith('Error')
        #print('er', error[1:])
        #error['end_col'] += 1 # convert inclusive column end into exclusive
        return error
