# Third Party Dependencies

<!--[[[fill sbom_sha256()]]]-->
The [SBOM in CycloneDX v1.4 JSON format](https://git.sr.ht/~sthagen/turvallisuusneuvonta/blob/default/etc/sbom/cdx.json) with SHA256 checksum ([41176085 ...](https://git.sr.ht/~sthagen/turvallisuusneuvonta/blob/default/etc/sbom/cdx.json.sha256 "sha256:41176085dcd664351e91a5c8d97eba85e3ee9c8eb6d61592daa2a05bbe755770")).
<!--[[[end]]] (checksum: 88015d33054f381d073a64bb867b7e7b)-->
## Licenses

JSON files with complete license info of: [direct dependencies](direct-dependency-licenses.json) | [all dependencies](all-dependency-licenses.json)

### Direct Dependencies

<!--[[[fill direct_dependencies_table()]]]-->
| Name                                                | Version                                            | License                                             | Author                                                                                                                                                                                                                                                                                                                                                                                                                           | Description (from packaging data)                                                                        |
|:----------------------------------------------------|:---------------------------------------------------|:----------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------|
| [jmespath](https://github.com/jmespath/jmespath.py) | [1.0.1](https://pypi.org/project/jmespath/1.0.1/)  | MIT License                                         | James Saryerwinnie                                                                                                                                                                                                                                                                                                                                                                                                               | JSON Matching Expressions                                                                                |
| [langcodes](https://github.com/rspeer/langcodes)    | [3.3.0](https://pypi.org/project/langcodes/3.3.0/) | MIT License                                         | Elia Robyn Speer                                                                                                                                                                                                                                                                                                                                                                                                                 | Tools for labeling human languages with IETF language tags                                               |
| [lazr.uri](https://launchpad.net/lazr.uri)          | [1.0.6](https://pypi.org/project/lazr.uri/1.0.6/)  | GNU Library or Lesser General Public License (LGPL) | "LAZR Developers" team                                                                                                                                                                                                                                                                                                                                                                                                           | A self-contained, easily reusable library for parsing, manipulating,                                     |
| [msgspec](https://jcristharif.com/msgspec/)         | [0.18.4](https://pypi.org/project/msgspec/0.18.4/) | BSD License                                         | Jim Crist-Harif                                                                                                                                                                                                                                                                                                                                                                                                                  | A fast serialization and validation library, with builtin support for JSON, MessagePack, YAML, and TOML. |
| [pydantic](https://github.com/pydantic/pydantic)    | [2.5.2](https://pypi.org/project/pydantic/2.5.2/)  | MIT License                                         | Samuel Colvin <s@muelcolvin.com>, Eric Jolibois <em.jolibois@gmail.com>, Hasan Ramezani <hasan.r67@gmail.com>, Adrian Garcia Badaracco <1755071+adriangb@users.noreply.github.com>, Terrence Dorsey <terry@pydantic.dev>, David Montague <david@pydantic.dev>, Serge Matveenko <lig@countzero.co>, Marcelo Trylesinski <marcelotryle@gmail.com>, Sydney Runkle <sydneymarierunkle@gmail.com>, David Hewitt <mail@davidhewitt.io> | Data validation using Python type hints                                                                  |
| [typer](https://github.com/tiangolo/typer)          | [0.9.0](https://pypi.org/project/typer/0.9.0/)     | MIT License                                         | Sebastián Ramírez                                                                                                                                                                                                                                                                                                                                                                                                                | Typer, build great CLIs. Easy to code. Based on Python type hints.                                       |
<!--[[[end]]] (checksum: 40488f7304945cb51950c692e6b14971)-->

### Indirect Dependencies

<!--[[[fill indirect_dependencies_table()]]]-->
| Name                                                                                      | Version                                                    | License                            | Author                                                                                                                                  | Description (from packaging data)                                       |
|:------------------------------------------------------------------------------------------|:-----------------------------------------------------------|:-----------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------|
| [annotated-types](https://github.com/annotated-types/annotated-types/blob/main/README.md) | [0.5.0](https://pypi.org/project/annotated-types/0.5.0/)   | MIT License                        | Samuel Colvin <s@muelcolvin.com>, Adrian Garcia Badaracco <1755071+adriangb@users.noreply.github.com>, Zac Hatfield-Dodds <zac@zhd.dev> | Reusable constraint types to use with typing.Annotated                  |
| [click](https://palletsprojects.com/p/click/)                                             | [8.1.6](https://pypi.org/project/click/8.1.6/)             | BSD License                        | Pallets <contact@palletsprojects.com>                                                                                                   | Composable command line interface toolkit                               |
| [pydantic_core](https://github.com/pydantic/pydantic-core)                                | [2.14.5](https://pypi.org/project/pydantic_core/2.14.5/)   | MIT License                        | Samuel Colvin <s@muelcolvin.com>                                                                                                        | UNKNOWN                                                                 |
| [setuptools](https://github.com/pypa/setuptools)                                          | [69.0.2](https://pypi.org/project/setuptools/69.0.2/)      | MIT License                        | Python Packaging Authority                                                                                                              | Easily download, build, install, upgrade, and uninstall Python packages |
| [typing_extensions](https://github.com/python/typing_extensions)                          | [4.7.1](https://pypi.org/project/typing_extensions/4.7.1/) | Python Software Foundation License | "Guido van Rossum, Jukka Lehtosalo, Łukasz Langa, Michael Lee" <levkivskyi@gmail.com>                                                   | Backported and Experimental Type Hints for Python 3.7+                  |
<!--[[[end]]] (checksum: a9beb0f87974dbabd35db01d96fcede7)-->

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
└── setuptools [required: Any, installed: 69.0.2]
msgspec==0.18.4
pydantic==2.5.2
├── annotated-types [required: >=0.4.0, installed: 0.5.0]
├── pydantic-core [required: ==2.14.5, installed: 2.14.5]
│   └── typing-extensions [required: >=4.6.0,!=4.7.0, installed: 4.7.1]
└── typing-extensions [required: >=4.6.1, installed: 4.7.1]
typer==0.9.0
├── click [required: >=7.1.1,<9.0.0, installed: 8.1.6]
└── typing-extensions [required: >=3.7.4.3, installed: 4.7.1]
````
<!--[[[end]]] (checksum: 3816cb74e5976765d8d468b90b4bd50d)-->
