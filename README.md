## Motivation

I need to generate a changelog based on git content. I want to controle the structure of the changelog but I don't want to manage the git content.

```markdown
### from 2016-01 to 2016-05

  We implements feature activation ...

  * 2016-04-13 : Fabien Arcellier : feat: activate ...
  * 2016-04-10 : Fabien Arcellier : feat: add index ...
  * 2016-04-10 : Fabien Arcellier : feat: add search ...
  * ...
```

I need to manage the format and the place of content myself and let git generate some contents from a file ``CHANGELOG.md.in``

```markdown
### from 2016-01 to 2016-05

  We implements feature activation ...

  * @tsincluder git log --date=short --pretty=format:'%ad : %aN : %s'  --abbrev-commit --since="1/1/2016" --until="4/31/2016" | grep feat
```

To generate ``CHANGELOG.md``, run

```bash
tsincluder CHANGELOG.md.in > CHANGELOG.md
```

## Synopsis

``tsincluder`` means Text Script Inclusion Manager.
``tsincluder`` is a ``cli`` and a ``library`` you can call from a python script that will replace a markup as ``@tsincluder echo hello world`` by ``hello world``.

It keep the content that prefix the markup to generate a valid format as markdown and add it
on all the lines if tsincluder generate many lines.

## The latest version

You can find the latest version to ...

    git clone https://github.com/FabienArcellier/tsincluder.git

## Usage

run tsincluder to replace the markers @tsinclude (text script include) by the content generate by the command on stdout

```python
python -m tsincluder file.in
```

to use it as a library

```python
from tsincluder import Processor

line = " * @tsincluder git log --date=short --pretty=format:'%ad : %aN : %s'  --abbrev-commit --since="1/1/2016" --until="4/31/2016" | grep feat"
processor = Processor()
content = processor.process(line)
print(content)
```

As tsincluder executes a subprocess command, the script can configure the working directory and markup

```python
from tsincluder import Processor

processor = Processor(working_directory="/tmp", markup="@other_markup")
```

## Installation

Install tsincluder using PyPi

```bash
pip install tsincluder
```

Install tsincluder from the source

```bash
python setup.py install
```

## Tests

Use make to execute unit tests.

    make tests

## Contributors

* Fabien Arcellier

## License

```
This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.
```
