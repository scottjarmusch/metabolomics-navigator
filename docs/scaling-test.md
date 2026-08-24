# Scaling test

The catalogue architecture was stress-tested before broad population by generating 500 synthetic but schema-valid tool records in a temporary copy of the repository.

## Result

- Synthetic tools added: 500
- Total tool pages generated: 512
- Protocol pages generated: 2
- Schema/catalogue validation: passed
- Validation time: 2.46 seconds
- Static site build time: 3.02 seconds
- Tools catalogue HTML: 0.60 MB
- Tool JSON export: 0.65 MB
- Total generated site: 5.86 MB

## Interpretation

The current static GitHub Pages architecture is comfortably suitable for a catalogue on the order of several hundred tool records. The filter/search interface still renders all tool records into one catalogue page, which keeps the implementation simple and fast at this scale.

Browser performance should be re-evaluated when the real catalogue approaches roughly 1,000 records or if testing on lower-powered mobile devices reveals noticeable filtering lag. At that point pagination, indexed client-side search, or virtualized rendering can be introduced without changing the YAML source-of-truth model.

## Re-running the test

```bash
python scripts/stress_test.py --tools 500
```

The script works in a temporary directory and does not modify the real catalogue.
