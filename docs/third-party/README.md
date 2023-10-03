# Third Party Dependencies

<!--[[[fill sbom_sha256()]]]-->
The [SBOM in CycloneDX v1.4 JSON format](https://git.sr.ht/~sthagen/turvallisuusneuvonta/blob/default/etc/sbom/cdx.json) with SHA256 checksum ([50d867d4 ...](https://git.sr.ht/~sthagen/turvallisuusneuvonta/blob/default/etc/sbom/cdx.json.sha256 "sha256:50d867d4c6efc00fbab3f6e8d211c72e5c2f11cffe4438f120f9ccb191ed9568")).
<!--[[[end]]] (checksum: f55332b9e584eec5ac56000e878e55bc)-->
## Licenses

JSON files with complete license info of: [direct dependencies](direct-dependency-licenses.json) | [all dependencies](all-dependency-licenses.json)

### Direct Dependencies

<!--[[[fill direct_dependencies_table()]]]-->
| Name                                                | Version                                            | License                                             | Author                                                                                                                                                                                                                                                        | Description (from packaging data)                                                                        |
|:----------------------------------------------------|:---------------------------------------------------|:----------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------|
| [jmespath](https://github.com/jmespath/jmespath.py) | [1.0.1](https://pypi.org/project/jmespath/1.0.1/)  | MIT License                                         | James Saryerwinnie                                                                                                                                                                                                                                            | JSON Matching Expressions                                                                                |
| [langcodes](https://github.com/rspeer/langcodes)    | [3.3.0](https://pypi.org/project/langcodes/3.3.0/) | MIT License                                         | Elia Robyn Speer                                                                                                                                                                                                                                              | Tools for labeling human languages with IETF language tags                                               |
| [lazr.uri](https://launchpad.net/lazr.uri)          | [1.0.6](https://pypi.org/project/lazr.uri/1.0.6/)  | GNU Library or Lesser General Public License (LGPL) | "LAZR Developers" team                                                                                                                                                                                                                                        | A self-contained, easily reusable library for parsing, manipulating,                                     |
| [msgspec](https://jcristharif.com/msgspec/)         | [0.18.3](https://pypi.org/project/msgspec/0.18.3/) | BSD License                                         | Jim Crist-Harif                                                                                                                                                                                                                                               | A fast serialization and validation library, with builtin support for JSON, MessagePack, YAML, and TOML. |
| [pydantic](https://github.com/pydantic/pydantic)    | [2.4.2](https://pypi.org/project/pydantic/2.4.2/)  | MIT License                                         | Samuel Colvin <s@muelcolvin.com>, Eric Jolibois <em.jolibois@gmail.com>, Hasan Ramezani <hasan.r67@gmail.com>, Adrian Garcia Badaracco <1755071+adriangb@users.noreply.github.com>, Terrence Dorsey <terry@pydantic.dev>, David Montague <david@pydantic.dev> | Data validation using Python type hints                                                                  |
| [typer](https://github.com/tiangolo/typer)          | [0.9.0](https://pypi.org/project/typer/0.9.0/)     | MIT License                                         | Sebastián Ramírez                                                                                                                                                                                                                                             | Typer, build great CLIs. Easy to code. Based on Python type hints.                                       |
<!--[[[end]]] (checksum: 6d59fdd9abb4305d90f55b78c6f4a239)-->

### Indirect Dependencies

<!--[[[fill indirect_dependencies_table()]]]-->
| Name                                                                                      | Version                                                    | License                            | Author                                                                                                                                  | Description (from packaging data)                                       |
|:------------------------------------------------------------------------------------------|:-----------------------------------------------------------|:-----------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------|
| [annotated-types](https://github.com/annotated-types/annotated-types/blob/main/README.md) | [0.5.0](https://pypi.org/project/annotated-types/0.5.0/)   | MIT License                        | Samuel Colvin <s@muelcolvin.com>, Adrian Garcia Badaracco <1755071+adriangb@users.noreply.github.com>, Zac Hatfield-Dodds <zac@zhd.dev> | Reusable constraint types to use with typing.Annotated                  |
| [click](https://palletsprojects.com/p/click/)                                             | [8.1.6](https://pypi.org/project/click/8.1.6/)             | BSD License                        | Pallets <contact@palletsprojects.com>                                                                                                   | Composable command line interface toolkit                               |
| [pydantic_core](https://github.com/pydantic/pydantic-core)                                | [2.10.1](https://pypi.org/project/pydantic_core/2.10.1/)   | MIT License                        | Samuel Colvin <s@muelcolvin.com>                                                                                                        | UNKNOWN                                                                 |
| [setuptools](https://github.com/pypa/setuptools)                                          | [68.2.2](https://pypi.org/project/setuptools/68.2.2/)      | MIT License                        | Python Packaging Authority                                                                                                              | Easily download, build, install, upgrade, and uninstall Python packages |
| [typing_extensions](https://github.com/python/typing_extensions)                          | [4.7.1](https://pypi.org/project/typing_extensions/4.7.1/) | Python Software Foundation License | "Guido van Rossum, Jukka Lehtosalo, Łukasz Langa, Michael Lee" <levkivskyi@gmail.com>                                                   | Backported and Experimental Type Hints for Python 3.7+                  |
<!--[[[end]]] (checksum: cd95ade9e642912a75079c2419ff2876)-->

## Dependency Tree(s)

JSON file with the complete package dependency tree info of: [the full dependency tree](package-dependency-tree.json)

### Rendered SVG

Base graphviz file in dot format: [Trees of the direct dependencies](package-dependency-tree.dot.txt)

<img src="./package-dependency-tree.svg" alt="Trees of the direct dependencies" title="Trees of the direct dependencies"/>

### Console Representation

<!--[[[fill dependency_tree_console_text()]]]-->
````console
jmespath==1.0.1
langcodes==3.3.0
lazr.uri==1.0.6
└── setuptools [required: Any, installed: 68.2.2]
msgspec==0.18.3
pydantic==2.4.2
├── annotated-types [required: >=0.4.0, installed: 0.5.0]
├── pydantic-core [required: ==2.10.1, installed: 2.10.1]
│   └── typing-extensions [required: >=4.6.0,!=4.7.0, installed: 4.7.1]
└── typing-extensions [required: >=4.6.1, installed: 4.7.1]
typer==0.9.0
├── click [required: >=7.1.1,<9.0.0, installed: 8.1.6]
└── typing-extensions [required: >=3.7.4.3, installed: 4.7.1]
````
<!--[[[end]]] (checksum: 242f6e00671abd82260b4f4659972518)-->
