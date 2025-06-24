### ✅ What is `assert isinstance()` in Python?

`assert isinstance()` is a **debugging and type-checking tool** that ensures a value is of a certain type at runtime.

---

### 🧠 Syntax:

```python
assert isinstance(object, class_or_tuple), "Optional error message"
```

* `object`: the variable or value you want to check
* `class_or_tuple`: the expected type(s) — can be one type or a tuple of types
* If the check fails, Python raises an `AssertionError`.

---

### 🧪 Examples

#### ✅ Correct usage:

```python
x = 42
assert isinstance(x, int)  # Passes
```

#### ❌ Fails and throws AssertionError:

```python
x = "hello"
assert isinstance(x, int), "x must be an integer"
```

**Output:**

```
AssertionError: x must be an integer
```

#### ✅ With multiple possible types:

```python
x = 3.14
assert isinstance(x, (int, float))  # Passes
```

---

### 🔍 Why use `assert isinstance()`?

* ✅ **Validate function inputs** early (type-safe code)
* ✅ **Catch bugs** quickly during development
* 🚫 Not recommended for production code that must run even with wrong input

---

### 🎯 How to Learn `assert isinstance()` — Step-by-Step

#### 📘 1. **Read the official Python docs**

* [`isinstance()` doc](https://docs.python.org/3/library/functions.html#isinstance)
* [`assert` statement doc](https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement)

#### 🧑‍💻 2. **Try examples in a Python script or REPL**

```python
def square(x):
    assert isinstance(x, (int, float)), "x must be numeric"
    return x * x
```

#### 🧪 3. **Create your own tests**

```python
print(square(3))       # ✅ 9
print(square("test"))  # ❌ AssertionError
```


---

### 💡 Pro Tip: Use `assert` for dev/debug mode, and use `if not isinstance(...)` for production-safe error handling.

