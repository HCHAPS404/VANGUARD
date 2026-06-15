# Script placeholders — implement during sprint

| Script | Owner | Day |
|--------|-------|-----|
| `run_tests.sh` | DEV | 0 |
| `run_agent.py` | DEV | 2 |
| `run_pipeline.py` | DEV | 4 |

### Usage (target):

```powershell
uv run python scripts/run_agent.py intake
uv run python scripts/run_pipeline.py --pdf tests/documents/sample.pdf
```

### Tests
#### Run all tests (Linux)
```sh
uv run pytest tests/test_llm.py -v
```