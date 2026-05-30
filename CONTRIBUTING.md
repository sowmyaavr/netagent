# Contributing to NetAgent

Thanks for your interest in NetAgent! This is an active M.Tech (AI/ML) dissertation project at BITS Pilani, and contributions, suggestions, and discussions are welcome.

## How to contribute

1. **Bug reports** — open an issue with a minimal reproduction and your environment details.
2. **Feature requests** — open an issue describing the use case before sending a PR.
3. **Documentation** — typo fixes and clarity improvements are always welcome.
4. **New fault scenarios** — high-value contributions: add a scenario YAML under `testbed/fault_scenarios/` following the existing schema.

## Development setup

```bash
git clone https://github.com/sowmyaavr/netagent.git
cd netagent
python3.11 -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
pre-commit install
```

## Coding standards

- Python 3.11+
- Format with `black` (line length 100)
- Lint with `ruff`
- Type-check with `mypy`
- Tests with `pytest`

Run all checks before submitting:
```bash
ruff check .
black --check .
mypy netagent/
pytest tests/ -v
```

## Commit messages

Follow conventional commits:
- `feat: add OSPF MTU mismatch scenario`
- `fix: handle empty BGP table in parser`
- `docs: clarify clarification policy thresholds`
- `test: add ablation eval test`

## License

By contributing, you agree your contributions are licensed under the [MIT License](LICENSE).
