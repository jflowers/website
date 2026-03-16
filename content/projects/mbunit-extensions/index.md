---
title: "MbUnit Extensions (Retired)"
description: "Custom extensions and patterns for the MbUnit testing framework"
weight: 11
---

## MbUnit Extensions

Contributions to the [MbUnit](https://www.hanselman.com/blog/mbunit-unit-testing-on-crack) testing framework, which Scott Hanselman called "Unit Testing on Crack."

### Contributions

- **Row-Based Testing** -- Using the `[Row]` attribute to pass multiple sets of data into a single test method, reducing test suite redundancy
- **Factory Object Fixture** -- Pattern for generating test fixtures programmatically
- **Integration Test Separation** -- Patterns for distinguishing fast unit tests from slower integration tests that require external resources

### Philosophy

MbUnit's metadata-driven approach to testing allowed developers to express test intent more clearly than traditional frameworks. The `[Row]` attribute pattern was later adopted by xUnit, NUnit 3, and other frameworks as parameterized tests.

### Related Posts

- [MbUnit Extensions](/wiki/mbunit-extensions/)
