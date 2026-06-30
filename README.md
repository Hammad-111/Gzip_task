# Convert CSV to a Gzipped Binary Stream

A small Python project that takes a CSV text, compresses it in memory using
gzip, then decompresses it and checks that the data is still the same.
Nothing is written to disk, everything happens in RAM.

## Idea

```
CSV text -> bytes -> gzip compress -> gzip decompress -> bytes -> text -> check
```

## Files

- `csv_gzip_task.py` - the actual short task, ready to run.
- `learn_gzip.py` - the same thing step by step, each step prints its own explanation.
- `learn_gzip.txt` - plain reading notes (nothing to run).

## How to run

```bash
python3 csv_gzip_task.py
```

The CSV is printed and you should see `True` at the end.
`True` means the data stayed exactly the same after compress/decompress.

To learn step by step:

```bash
python3 learn_gzip.py
```

## What you learn

- Using `io.StringIO` to handle a text stream.
- Using `io.BytesIO` to handle binary data.
- Converting between strings and bytes (`.encode` / `.decode`).
- Compressing and decompressing with `gzip`.

## Note

A tiny file can look bigger after compression (25 -> 45 bytes) because gzip
adds its own header. The real benefit shows up on larger data.
