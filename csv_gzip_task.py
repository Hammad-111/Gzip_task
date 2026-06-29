import io
import gzip

csv = "name,age\nAlice,30\nBob,25\n"

s = io.StringIO()
s.write(csv)
s.seek(0)
text = s.read()

data = text.encode("utf-8")

buf = io.BytesIO()
with gzip.GzipFile(fileobj=buf, mode="wb") as gz:
    gz.write(data)

buf.seek(0)
with gzip.GzipFile(fileobj=buf, mode="rb") as gz:
    out = gz.read()

result = io.StringIO(out.decode("utf-8")).read()

print(result)
print(text == result)
