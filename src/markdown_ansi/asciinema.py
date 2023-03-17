#
from io import StringIO

from asciinema import asciicast

from markdown_ansi import ansi


def _open_asciicast(source):
    source_io = StringIO(source)
    first_line = source_io.readline()

    try:  # try v2 first
        return asciicast.v2.open_from_file(first_line, source_io)
    except asciicast.v2.LoadError:  # try v1 next
        return asciicast.v1.open_from_file(first_line, source_io)


def fence_code_format(source, *args, **kwargs):
    output = StringIO()
    with _open_asciicast(source) as a:
        for _, _type, text in a.stdout_events():
            output.write(text)

    return ansi.fence_code_format(output.getvalue(), *args, **kwargs)
