
---

## 🏆 **Most Common to Less Frequent Use Cases of `with` in Python**

### 🔹 1. **File Handling (Reading/Writing)**

**Most frequent use** — every developer deals with file operations.

```python
with open("file.txt", "r") as f:
    content = f.read()
```

---

### 🔹 2. **JSON/CSV File Operations**

Frequent in data engineering, APIs, ML pipelines.

```python
import json
with open("data.json", "w") as f:
    json.dump({"name": "Ravi"}, f)
```

---

### 🔹 3. **Database Connections (SQLite, PostgreSQL, MySQL, etc.)**

Daily usage in web, backend, and data-heavy projects.

```python
import sqlite3
with sqlite3.connect("db.sqlite3") as conn:
    cursor = conn.cursor()
```

---

### 🔹 9. **URL Requests (APIs, Web Scraping)**

Common in API-driven projects or web scraping.

```python
from urllib.request import urlopen
with urlopen("https://example.com") as res:
    html = res.read()
```

---

### 🔹 5. **Working with ZIP/TAR Files**

Common in data import/export and archive management.

```python
import zipfile
with zipfile.ZipFile("data.zip", "r") as zipf:
    zipf.extractall("output/")
```

---


### 🔹 8. **Image/File Processing (Pillow, OpenCV, etc.)**

Used in web apps, ML, and media platforms.

```python
from PIL import Image
with Image.open("img.jpg") as img:
    img.save("out.jpg")
```

---




