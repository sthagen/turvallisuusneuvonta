# Third Party Dependencies

<!--[[[fill sbom_sha256()]]]-->
The [SBOM in CycloneDX v1.4 JSON format](https://git.sr.ht/~sthagen/turvallisuusneuvonta/blob/default/sbom.json) with SHA256 checksum ([a3c2b5ed ...](https://git.sr.ht/~sthagen/turvallisuusneuvonta/blob/default/sbom.json.sha256 "sha256:a3c2b5ed835b05294c62d851647cf68dac8a9dad1ff73e35626b15c1ce5eb52b")).
<!--[[[end]]] (checksum: 5104fefb1e5966dd03bafab330717991)-->
## Licenses

JSON files with complete license info of: [direct dependencies](direct-dependency-licenses.json) | [all dependencies](all-dependency-licenses.json)

### Direct Dependencies

<!--[[[fill direct_dependencies_table()]]]-->
| Name                                                | Version                                             | License                                             | Author                 | Description (from packaging data)                                             |
|:----------------------------------------------------|:----------------------------------------------------|:----------------------------------------------------|:-----------------------|:------------------------------------------------------------------------------|
| [jmespath](https://github.com/jmespath/jmespath.py) | [1.0.1](https://pypi.org/project/jmespath/1.0.1/)   | MIT License                                         | James Saryerwinnie     | JSON Matching Expressions                                                     |
| [langcodes](https://github.com/rspeer/langcodes)    | [3.3.0](https://pypi.org/project/langcodes/3.3.0/)  | MIT License                                         | Elia Robyn Speer       | Tools for labeling human languages with IETF language tags                    |
| [lazr.uri](https://launchpad.net/lazr.uri)          | [1.0.6](https://pypi.org/project/lazr.uri/1.0.6/)   | GNU Library or Lesser General Public License (LGPL) | "LAZR Developers" team | A self-contained, easily reusable library for parsing, manipulating,          |
| [msgspec](https://jcristharif.com/msgspec/)         | [0.11.0](https://pypi.org/project/msgspec/0.11.0/)  | BSD License                                         | Jim Crist-Harif        | A fast and friendly JSON/MessagePack library, with optional schema validation |
| [pydantic](https://github.com/pydantic/pydantic)    | [1.10.2](https://pypi.org/project/pydantic/1.10.2/) | MIT License                                         | Samuel Colvin          | Data validation and settings management using python type hints               |
| [typer](https://github.com/tiangolo/typer)          | [0.7.0](https://pypi.org/project/typer/0.7.0/)      | MIT License                                         | Sebastián Ramírez      | Typer, build great CLIs. Easy to code. Based on Python type hints.            |
<!--[[[end]]] (checksum: b69f8983ec80f4d004ecfd142cfe894d)-->

### Indirect Dependencies

<!--[[[fill indirect_dependencies_table()]]]-->
| Name                                             | Version                                               | License     | Author                     | Description (from packaging data)                                       |
|:-------------------------------------------------|:------------------------------------------------------|:------------|:---------------------------|:------------------------------------------------------------------------|
| [click](https://palletsprojects.com/p/click/)    | [8.1.3](https://pypi.org/project/click/8.1.3/)        | BSD License | Armin Ronacher             | Composable command line interface toolkit                               |
| [setuptools](https://github.com/pypa/setuptools) | [65.6.3](https://pypi.org/project/setuptools/65.6.3/) | MIT License | Python Packaging Authority | Easily download, build, install, upgrade, and uninstall Python packages |
<!--[[[end]]] (checksum: 7aace7203578d639df84d5b07ba0be96)-->

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
  - setuptools [required: Any, installed: 65.6.3]
msgspec==0.11.0
pydantic==1.10.2
  - typing-extensions [required: >=4.1.0, installed: 4.4.0]
typer==0.7.0
  - click [required: >=7.1.1,<9.0.0, installed: 8.1.3]
````
<!--[[[end]]] (checksum: 73e85f3fbb6fe1668543d0fbd9843066)-->