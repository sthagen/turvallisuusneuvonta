# Usage

## Examples for Verifications

### Mandatory Rules from CSAF v2.0 CS01

```console
$ turvallisuusneuvonta verify tests/fixtures/rules/invalid/upstream/6-1-01-01.json
using configuration ({})
set of document properties only contains known properties
set of document properties is a proper subset of the known properties
advisory fails mandatory rules:
- undefined product ids
- invalid translator
```

```console
$ turvallisuusneuvonta verify tests/fixtures/rules/invalid/upstream/6-1-02-01.json
using configuration ({})
set of document properties only contains known properties
set of document properties is a proper subset of the known properties
advisory fails mandatory rules:
- invalid translator
- non-unique product ids
```

```console
$ turvallisuusneuvonta verify tests/fixtures/rules/invalid/upstream/6-1-04-01.json
using configuration ({})
set of document properties only contains known properties
set of document properties is a proper subset of the known properties
advisory fails mandatory rules:
- undefined group ids
- invalid translator
```

```console
$ turvallisuusneuvonta verify tests/fixtures/rules/invalid/upstream/6-1-05-01.json
using configuration ({})
set of document properties only contains known properties
set of document properties is a proper subset of the known properties
advisory fails mandatory rules:
- invalid translator
- non-unique group ids
```

```console
$ turvallisuusneuvonta verify tests/fixtures/rules/invalid/upstream/6-1-15-01.json
using configuration ({})
set of document properties only contains known properties
set of document properties is a proper subset of the known properties
advisory fails mandatory rules:
- invalid translator
```

```console
$ turvallisuusneuvonta verify tests/fixtures/rules/invalid/upstream/6-1-26-01.json
using configuration ({})
set of document properties only contains known properties
set of document properties is a proper subset of the known properties
advisory fails mandatory rules:
- invalid category
- invalid translator
```

### Verification of Other Documents

```console
$ turvallisuusneuvonta verify tests/fixtures/spam/advisory.json
using configuration ({})
OK
```

```console
$ turvallisuusneuvonta verify tests/fixtures/a-game-log4j/some-vex-csaf-document.json
using configuration ({})
set of document.aggregate_severity properties only contains known properties
set of document.aggregate_severity properties is a proper subset of the known properties
set of document properties only contains known properties
set of document properties is a proper subset of the known properties
advisory fails mandatory rules:
- undefined product ids
- invalid translator
```

## General Use

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

Asking for the version:

```console
$ turvallisuusneuvonta version
Security advisory (Finnish: turvallisuusneuvonta) audit tool. version 2022.2.14
```

Minimal verification (WIP):

Succeeding with advisory (lacking any product or vulnerabilit information):
```console
$ turvallisuusneuvonta verify tests/fixtures/example-com/example-com-123.json || echo "FAIL"
using configuration ({})
set of properties of document.acknowledgments[0] only contains known properties
set of document.aggregate_severity properties only contains known properties
set of document.aggregate_severity properties is a proper subset of the known properties
set of document properties only contains known properties
set of document properties is a proper subset of the known properties
OK
```

Empty object:
```console
$ turvallisuusneuvonta verify tests/fixtures/empty/advisory.json || echo "FAIL"
using configuration ({})
advisory is too short to be valid
FAIL
```

Failing top level mandatory elements:
```console
$ turvallisuusneuvonta verify tests/fixtures/spam/advisory.json || echo "FAIL"
using configuration ({})
missing document property (status)
FAIL
```
