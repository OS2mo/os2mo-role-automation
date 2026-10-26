<!--
SPDX-FileCopyrightText: Magenta ApS <https://magenta.dk>
SPDX-License-Identifier: MPL-2.0
-->

# OS2mo: role automation

## Testing

Testing requires a running [OS2mo](https://github.com/os2mo/os2mo) stack. Tests
can be run using [pytest](https://pytest.org), for example:

```sh
docker compose run --rm role-automation pytest tests/integration/test_something.py::test_foo
```
