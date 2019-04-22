from coalib.bearlib.abstractions.Linter import linter
from coalib.settings.Setting import path
from coalib.results.RESULT_SEVERITY import RESULT_SEVERITY


@linter(executable='pyright',
        global_bear=False,
        normalize_line_numbers=False,
        normalize_column_numbers=False,
        output_format='regex',
        output_regex=r'\s+(?P<message>(?P<severity>(?:Import)?).+)'
                     r'\s+\((?P<line>\d+)'
                     r',\s(?P<column>\d+).*\n',
        severity_map={'Import': RESULT_SEVERITY.INFO})
class PyrightBear:
    """
    Checks the code with ``pyright`` on each file separately.

    See https://github.com/Microsoft/pyright/blob/master/docs for info.
    """

    LANGUAGES = {'Python 3'}
    AUTHORS = {'The coala developers'}
    AUTHORS_EMAILS = {'coala-devel@googlegroups.com'}
    LICENSE = 'AGPL-3.0'
    # This detects typing errors, which is pretty unique -- it doesn't
    # make sense to add a category for it.
    CAN_DETECT = set()

    @staticmethod
    def create_arguments(filename,
                         file,
                         config_file,
                         pyright_config: path = '',
                         typeshed_path: path = '',
                         venv_path: path = '',
                         watch: bool = False,
                         stats: bool = False):
        """
        :param pyright_config: Path to configuration file
        :param typeshed_path:  Path to typeshed type stubs
        :param venv_path:      Path to virtual environments
        :param watch:          Continue to run and watch for changes
        :param stats:          Print detailed performance stats
        """
        args = (filename,)
        if pyright_config:  # pragma: no cover
            args += ('-p', pyright_config)
        if typeshed_path:  # pragma: no cover
            args += ('-t', typeshed_path)
        if venv_path:  # pragma: no cover
            args += ('-v', venv_path)
        if watch:  # pragma: no cover
            args += ('--watch',)
        if stats:  # pragma: no cover
            args += ('--stats',)

        return args
