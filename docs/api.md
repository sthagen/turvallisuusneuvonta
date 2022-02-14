# API

## Programming API

Work in progress ... but:
```python
import turvallisuusneuvonta as csaf

if csaf.is_valid_category({'document': {'category': ' vey'}}):
    print('Not nice, but valid as per rule 6.1.26 ...')
if not csaf.is_valid_category({'document': {'category': ' vex '}}):
    print('Validation of category to close to reserved profile fails as it should.')

# Failing a whole-sale verification already works:
if not csaf.is_valid({'document': {'category': ' vex '}}):
    print('Some rules are already implemented (spike)')

# Whole-sale succeeding kind of works also ...
if csaf.is_valid({'document': {'category': 'a'}}) is NotImplemented:
    print('The NotImplemented will become True when all rules are implemented')
```

Calling help on `csaf` in above python session displays the existing verifiers:
```manpage
Help on package turvallisuusneuvonta:

NAME
    turvallisuusneuvonta - Security advisory (Finnish: turvallisuusneuvonta) audit tool.

PACKAGE CONTENTS
    __main__
    cli
    csaf (package)
    turvallisuusneuvonta

FUNCTIONS
    is_valid(document: dict) -> bool
        Complete validation of all mandatory rules.

        This is a spike - we throw it away when all rules are in and back comes something maintainable.

    is_valid_category(document: dict) -> bool
        Verify category value.

    is_valid_defined_group_ids(document: dict) -> bool
        Temporary implementation of rule for defined group ids.

    is_valid_defined_product_ids(document: dict) -> bool
        Temporary implementation of rule for defined product ids.

    is_valid_translator(document: dict) -> bool
        Verify source_lang value is present for translator.

    is_valid_unique_group_ids(document: dict) -> bool
        Temporary implementation of rule for unique group ids.

    is_valid_unique_product_ids(document: dict) -> bool
        Temporary implementation of rule for unique product ids.

DATA
    __all__ = ['is_valid', 'is_valid_category', 'is_valid_defined_group_id...

VERSION
    2022.2.14
```
## Commandline API

### `turvallisuusneuvonta`

Security advisory (Finnish: turvallisuusneuvonta) audit tool.

**Usage**:

```console
$ turvallisuusneuvonta [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `-V, --version`: Display the turvallisuusneuvonta version and exit  [default: False]
* `-h, --help`: Show this message and exit.

**Commands**:

* `verify`: Answer the question if now is a working hour.
* `version`: Display the turvallisuusneuvonta version and...

## `turvallisuusneuvonta verify`

Answer the question if now is a working hour.

**Usage**:

```console
$ turvallisuusneuvonta verify [OPTIONS] [SOURCE]
```

**Arguments**:

* `[SOURCE]`: [default: STDIN]

**Options**:

* `-i, --input <sourcepath>`: Path to input file [default: reading from standard in]
* `-c, --config <configpath>`: Path to config file [default: is $HOME/.turvallisuusneuvonta.json]
* `-h, --help`: Show this message and exit.

## `turvallisuusneuvonta version`

Display the turvallisuusneuvonta version and exit

**Usage**:

```console
$ turvallisuusneuvonta version [OPTIONS]
```

**Options**:

* `-h, --help`: Show this message and exit.

