import sys
from flake8.main.cli import main as flake8_main

def cli():
    # I don't love this as `flake8_main` technically isn't a public API, but we
    # can't use `subprocess.run` as `pipx run ...` doesn't make `flake8`
    # available on PATH. I think this workaround is probably OK as
    # `flake8_main` hasn't changed in ~3yrs.
    flake8_main(["--select", "QKT"] + sys.argv[1:])
