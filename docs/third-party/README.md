# Third Party Dependencies

<!--[[[fill sbom_sha256()]]]-->
The [SBOM in CycloneDX v1.4 JSON format](https://git.sr.ht/~sthagen/turvallisuusneuvonta/blob/default/sbom/cdx.json) with SHA256 checksum ([0472e15e ...](https://git.sr.ht/~sthagen/turvallisuusneuvonta/blob/default/sbom/cdx.json.sha256 "sha256:0472e15e8cda71cf13df7c012c3892369ccd503342552c7d7c3ea9d838e27fd3")).
<!--[[[end]]] (checksum: 3abac7c5aa1a1fa06e59f4b6e2d51677)-->
## Licenses

JSON files with complete license info of: [direct dependencies](direct-dependency-licenses.json) | [all dependencies](all-dependency-licenses.json)

### Direct Dependencies

<!--[[[fill direct_dependencies_table()]]]-->
| Name                                                | Version                                             | License                                             | Author                 | Description (from packaging data)                                                                        |
|:----------------------------------------------------|:----------------------------------------------------|:----------------------------------------------------|:-----------------------|:---------------------------------------------------------------------------------------------------------|
| [jmespath](https://github.com/jmespath/jmespath.py) | [1.0.1](https://pypi.org/project/jmespath/1.0.1/)   | MIT License                                         | James Saryerwinnie     | JSON Matching Expressions                                                                                |
| [langcodes](https://github.com/rspeer/langcodes)    | [3.3.0](https://pypi.org/project/langcodes/3.3.0/)  | MIT License                                         | Elia Robyn Speer       | Tools for labeling human languages with IETF language tags                                               |
| [lazr.uri](https://launchpad.net/lazr.uri)          | [1.0.6](https://pypi.org/project/lazr.uri/1.0.6/)   | GNU Library or Lesser General Public License (LGPL) | "LAZR Developers" team | A self-contained, easily reusable library for parsing, manipulating,                                     |
| [msgspec](https://jcristharif.com/msgspec/)         | [0.16.0](https://pypi.org/project/msgspec/0.16.0/)  | BSD License                                         | Jim Crist-Harif        | A fast serialization and validation library, with builtin support for JSON, MessagePack, YAML, and TOML. |
| [pydantic](https://github.com/pydantic/pydantic)    | [1.10.9](https://pypi.org/project/pydantic/1.10.9/) | MIT License                                         | Samuel Colvin          | Data validation and settings management using python type hints                                          |
| [typer](https://github.com/tiangolo/typer)          | [0.9.0](https://pypi.org/project/typer/0.9.0/)      | MIT License                                         | Sebastián Ramírez      | Typer, build great CLIs. Easy to code. Based on Python type hints.                                       |
<!--[[[end]]] (checksum: 6ff82ccfe1a3325badfaf00f09344dd4)-->

### Indirect Dependencies

<!--[[[fill indirect_dependencies_table()]]]-->
| Name                                                             | Version                                                    | License                            | Author                                                                                | Description (from packaging data)                                       |
|:-----------------------------------------------------------------|:-----------------------------------------------------------|:-----------------------------------|:--------------------------------------------------------------------------------------|:------------------------------------------------------------------------|
| [click](https://palletsprojects.com/p/click/)                    | [8.1.3](https://pypi.org/project/click/8.1.3/)             | BSD License                        | Armin Ronacher                                                                        | Composable command line interface toolkit                               |
| [setuptools](https://github.com/pypa/setuptools)                 | [67.8.0](https://pypi.org/project/setuptools/67.8.0/)      | MIT License                        | Python Packaging Authority                                                            | Easily download, build, install, upgrade, and uninstall Python packages |
| [typing_extensions](https://github.com/python/typing_extensions) | [4.4.0](https://pypi.org/project/typing_extensions/4.4.0/) | Python Software Foundation License | "Guido van Rossum, Jukka Lehtosalo, Łukasz Langa, Michael Lee" <levkivskyi@gmail.com> | Backported and Experimental Type Hints for Python 3.7+                  |
<!--[[[end]]] (checksum: 5cd326c55608c5f70cc290e004712f1a)-->

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
└── setuptools [required: Any, installed: 67.8.0]
msgspec==0.16.0
pydantic==1.10.9
└── typing-extensions [required: >=4.2.0, installed: 4.4.0]
typer==0.9.0
├── click [required: >=7.1.1,<9.0.0, installed: 8.1.3]
└── typing-extensions [required: >=3.7.4.3, installed: 4.4.0]
````
<!--[[[end]]] (checksum: 4a28c713d90f53d87d4b387c9f259fb3)-->
