# API

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

