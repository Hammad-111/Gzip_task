# CSV ko Gzip me Convert karna

Ek chhota Python project jisme ek CSV text ko memory me gzip se compress
kiya jata hai, phir decompress karke check kiya jata hai ke data same hai.
Koi file disk par nahi banti, sab kuch RAM me hota hai.

## Idea

```
CSV text -> bytes -> gzip compress -> gzip decompress -> bytes -> text -> check
```

## Files

- `csv_gzip_task.py` - asli short task, seedha chalane ke liye.
- `learn_gzip.py` - wahi cheez step-by-step, har step apna explanation print karta hai.
- `learn_gzip.txt` - sirf padhne wali notes (kuch run nahi karna).

## Chalane ka tariqa

```bash
python3 csv_gzip_task.py
```

Output me CSV print hoga aur niche `True` aana chahiye.
`True` ka matlab compress/decompress ke baad data bilkul same raha.

Seekhne ke liye:

```bash
python3 learn_gzip.py
```

## Kya seekhne ko milta hai

- `io.StringIO` se text stream handle karna.
- `io.BytesIO` se binary data handle karna.
- string aur bytes ke beech convert karna (`.encode` / `.decode`).
- `gzip` se compress aur decompress karna.

## Note

Chhoti file compress hone par size bada lag sakta hai (25 -> 45 bytes)
kyunki gzip apna header lagata hai. Bade data par hi asli faida dikhta hai.
