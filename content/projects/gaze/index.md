---
title: "Gaze"
description: "Test quality analysis via side effect detection for Go -- part of Unbound Force"
weight: 2
---

## Gaze

Gaze is a static analysis tool for Go, built as part of [Unbound Force](/projects/unbound-force/). It detects observable side effects in functions and computes CRAP scores combining cyclomatic complexity with test coverage.

Line coverage tells you which lines ran -- it does not tell you whether your tests actually verified anything. Gaze fixes this by working from first principles:

1. **Detect** every observable side effect a function produces (return values, error returns, mutations, I/O, channel sends, etc.)
2. **Classify** each effect as *contractual* (part of the function's public obligation), *incidental* (an implementation detail), or *ambiguous*
3. **Measure** whether your tests actually assert on the contractual effects -- and flag the ones they don't

### Key Metrics

- **Contract Coverage** -- The percentage of a function's contractual side effects that at least one test assertion verifies.
- **Over-Specification Score** -- The count and ratio of test assertions that target incidental effects (implementation details that break during refactoring).
- **GazeCRAP** -- A composite risk score that replaces line coverage with contract coverage in the CRAP formula, surfacing complex functions whose tests don't verify their contracts.

### Installation

```bash
# Homebrew (recommended)
brew install unbound-force/tap/gaze

# Go Install
go install github.com/unbound-force/gaze/cmd/gaze@latest
```

### Links

- [GitHub](https://github.com/unbound-force/gaze)
- [Unbound Force](https://unboundforce.dev/)
