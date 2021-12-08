# Example Usage

Maybe not yet. But if:

```console
$ turvallisuusneuvonta
Usage: turvallisuusneuvonta [OPTIONS] COMMAND [ARGS]...

  Security advisory (Finnish: turvallisuusneuvonta) audit tool.

Options:
  -V, --version  Display the turvallisuusneuvonta version and exit
  -h, --help     Show this message and exit.

Commands:
  verify   Answer the question if now is a working hour.
  version  Display the turvallisuusneuvonta version and exit
```

Minimal verification (WIP):

Empty object:
```console
$ turvallisuusneuvonta verify tests/fixtures/empty/advisory.json || echo "FAIL"
using configuration ({})
advisory is empty
FAIL
```
Failing top level mandatory elements:
```console
$ turvallisuusneuvonta verify tests/fixtures/spam/advisory.json || echo "FAIL"
using configuration ({})
missing document property (status)
FAIL
```
