<!--
SPDX-FileCopyrightText: Magenta ApS <https://magenta.dk>
SPDX-License-Identifier: MPL-2.0
-->

# OS2mo: role automation engine

The role automation engine keeps the rolebindings in OS2mo in sync with the
rolebinding rules. It runs as a service alongside OS2mo.

A **rolebinding rule** connects a [CEL](https://cel.dev) expression to a role.
Each role belongs to an IT system. When at least one rolebinding rule evaluates
to `true` for an IT user, a **rolebinding** must exist between that IT user and
the rule's role. The engine creates and deletes rolebindings so that this
statement always (eventually) holds.


## Testing

Testing requires a running [OS2mo](https://github.com/os2mo/os2mo) stack. Tests
can be run using [pytest](https://pytest.org), for example:

```sh
docker compose run --rm role-automation pytest tests/integration/test_something.py::test_foo
```


## Why is this not a part of OS2mo?

Role automation is conceptually a core feature of OS2mo. OS2mo stores the
rolebinding rules, but only this engine applies them. The engine must therefore
always run alongisde OS2mo for OS2mo to keep its promises.

For this reason, it can seem like an odd choice that the engine is not a part
of the OS2mo codebase. It is implemented this way for the following reasons:

* The engine can reuse the existing tooling for OS2mo integrations, such as the
  CI templates and [FastRAMQPI](https://github.com/magenta-aps/fastramqpi).
* The team already knows how to build, maintain, and run integrations built on
  that tooling.

Moving the engine into the OS2mo codebase would also be a valid choice.
