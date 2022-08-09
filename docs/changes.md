# Change History

## 2022.8.9

* Bumped dependencies for development and test
* Migrated away from github
  * Moved documentation to https://codes.dilettant.life/docs/turvallisuusneuvonta
  * Moved tracker to https://todo.sr.ht/~sthagen/turvallisuusneuvonta
  * Moved normative source repo to https://git.sr.ht/~sthagen/turvallisuusneuvonta
* Added test coverage documentation at https://codes.dilettant.life/coverage/turvallisuusneuvonta

## Older
### 2022.2.14

* Hotfix making mandatory rules (spike) module a package (fixes #11)
* Removal of topical approach (for now) and code cleanup

### 2022.2.13

* Experimental implementations for unique as well as defined product and group ids, and translator 

### 2022.2.12

* Category rule test ready
* Added property based testing

### 2022.1.1

* Implemented first additional test cases from specification
* Migrated to model implementation for verification

### 2021.12.31

* Enhanced the new model implementation

### 2021.12.19

* Better test coverage (of the new model implementation)

### 2021.12.18

* Added pydantic dependency for annotation based model

### 2021.12.10

* Added langcodes dependency for language tag validation
* Added lazr.uri dependency for URI verification
* Added further CSAF existence verification rules
* Better test coverage

### 2021.12.9

* Added merely level zero existence tests on document properties 
* Migrated to JMESPath library for validation
* Migrated to faster JSON library (orjson)
* Better test coverage

### 2021.12.8

* Initial release on PyPI
