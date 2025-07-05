# 🗺️ Roadmap to Mastering Python Decorators
---
## 🟢 **Phase 1: Foundations (Beginner Level)**

### 🎯 Goal: Understand what decorators are and how basic ones work.

#### ✅ Topics to Learn:

* Functions are first-class objects
* How to assign and return functions
* Basic decorator syntax using `@`
* Simple wrapper functions without arguments

#### 🧪 Practice:

* Write a decorator that prints `"Before"` and `"After"` around a function.
* Copy a function using `another_name = function_name` and call it.

#### 🔁 Example:

```python
def basic_decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@basic_decorator
def hello():
    print("Hello!")

hello()
```

---

## 🟡 **Phase 2: Intermediate Usage (Wrapper Flexibility)**

### 🎯 Goal: Learn how to pass arguments and use `*args`, `**kwargs`.

#### ✅ Topics to Learn:

* `*args` and `**kwargs` in decorators
* Nesting decorators
* Multiple decorators on the same function

#### 🧪 Practice:

* Make a decorator that logs arguments of any function
* Decorate functions with multiple decorators (e.g., logging and timing)

#### 🔁 Example:

```python
def log_args(func):
    def wrapper(*args, **kwargs):
        print("Args:", args, "Kwargs:", kwargs)
        return func(*args, **kwargs)
    return wrapper

@log_args
def add(a, b):
    return a + b
```

---

## 🟠 **Phase 3: Decorator Factory (Decorator with Parameters)**

### 🎯 Goal: Learn how to build decorators that accept arguments.

#### ✅ Topics to Learn:

* Closure-based decorators
* Returning a decorator from another function
* Use cases like `@retry(3)` or `@repeat(5)`

#### 🧪 Practice:

* Decorator to repeat a function `n` times
* Decorator to enforce user role or permission

#### 🔁 Example:

```python
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def hello():
    print("Hi")
```

---

## 🔵 **Phase 4: Real-World Use Cases**

### 🎯 Goal: Apply decorators in realistic situations.

#### ✅ Topics to Learn:

* Logging
* Caching / Memoization
* Authentication
* Retry logic

#### 🧪 Practice:

* Log all function calls to a file
* Retry on random failure
* Create a `@login_required` decorator

#### 🔁 Example:

```python
def retry(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(n):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(f"Retry {i+1}")
        return wrapper
    return decorator
```

---

## 🟣 **Phase 5: Advanced Concepts**

### 🎯 Goal: Handle decorator side-effects like preserving metadata and advanced state.

#### ✅ Topics to Learn:

* `functools.wraps`
* Stateful decorators with counters
* Class-based decorators
* Chaining decorators dynamically

#### 🧪 Practice:

* Create a decorator that counts how many times a function was called
* Use `functools.wraps` to preserve function name and docstring

#### 🔁 Example:

```python
import functools

def count_calls(func):
    count = 0
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"Call #{count}")
        return func(*args, **kwargs)
    return wrapper
```

---

## 🔴 **Phase 6: Meta-programming with Decorators**

### 🎯 Goal: Combine decorators with dynamic and class-based logic

#### ✅ Topics to Learn:

* Class-based decorators (`__call__`)
* Decorating class methods (`@classmethod`, `@staticmethod`)
* Dynamic decorator pipelines

#### 🧪 Practice:

* Create a class-based decorator that measures execution time
* Decorate all methods of a class using a meta-decorator

---

# 🧠 Advanced Decorators Roadmap — Optional Deep Dive

---

## 🔰 PHASE 1: `async` and Coroutine-Safe Decorators

### 🎯 Goal: Decorate `async def` functions properly.

#### ✅ Topics:

* How to write decorators that support both sync and async functions.
* Detect if the wrapped function is a coroutine (`inspect.iscoroutinefunction`).
* Use `await` inside decorators.

#### 🔁 Example:

```python
import asyncio
import functools
import inspect

def async_safe_decorator(func):
    if inspect.iscoroutinefunction(func):
        @functools.wraps(func)
        async def async_wrapper(*args, **kwargs):
            print("Async wrapper before")
            result = await func(*args, **kwargs)
            print("Async wrapper after")
            return result
        return async_wrapper
    else:
        @functools.wraps(func)
        def sync_wrapper(*args, **kwargs):
            print("Sync wrapper before")
            result = func(*args, **kwargs)
            print("Sync wrapper after")
            return result
        return sync_wrapper

@async_safe_decorator
async def async_hello():
    await asyncio.sleep(1)
    print("Hello from async")

@async_safe_decorator
def sync_hello():
    print("Hello from sync")
```

---

## 🔰 PHASE 2: Class Decorators (Decorating Entire Classes)

### 🎯 Goal: Modify or enhance a **class itself**, not just its methods.

#### ✅ Topics:

* Write a decorator that wraps a class constructor.
* Modify attributes or inject behaviors into instances.
* Use in data validation, singletons, or monitoring.

#### 🔁 Example:

```python
def add_greeting(cls):
    class Wrapped(cls):
        def greet(self):
            return f"Hi, I am {self.__class__.__name__}"
    return Wrapped

@add_greeting
class Dog:
    pass

d = Dog()
print(d.greet())  # Hi, I am Dog
```

---

## 🔰 PHASE 3: Resource/Context-Aware Decorators

### 🎯 Goal: Manage resources like files, databases, etc., around function calls.

#### ✅ Topics:

* Open/close resources inside decorators
* Decorators that log to file, or connect to DB, or manage file I/O context

#### 🔁 Example:

```python
def use_file(filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            with open(filename, 'a') as f:
                f.write("Calling function\n")
                result = func(*args, **kwargs)
                f.write("Function completed\n")
                return result
        return wrapper
    return decorator

@use_file("log.txt")
def do_stuff():
    print("Doing work")
```

---

## 🔰 PHASE 4: Type Hinting and Signature Preservation

### 🎯 Goal: Use `functools.wraps` + `typing` to maintain decorator correctness.

#### ✅ Topics:

* Add return and argument type hints in decorators
* Use `Callable`, `TypeVar`, and `ParamSpec` (Python 3.10+)
* Avoid “wrapper hides original signature” issue

#### 🔁 Example:

```python
from typing import Callable, TypeVar
import functools

T = TypeVar('T', bound=Callable)

def typed_logger(func: T) -> T:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} was called")
        return func(*args, **kwargs)
    return wrapper  # type: ignore
```

---

## 🔰 PHASE 5: Decorators with `inspect` and Introspection

### 🎯 Goal: Examine the wrapped function's signature, docstring, etc.

#### ✅ Topics:

* Use `inspect.signature()`, `inspect.getdoc()`
* Log function signature
* Check for required arguments or inject defaults

#### 🔁 Example:

```python
import inspect

def debug_signature(func):
    def wrapper(*args, **kwargs):
        sig = inspect.signature(func)
        print(f"Calling {func.__name__}{sig}")
        return func(*args, **kwargs)
    return wrapper

@debug_signature
def foo(x, y=10):
    return x + y
```

---

## 🔰 PHASE 6: Unit Testing Decorators

### 🎯 Goal: Test decorators independently and avoid over-wrapping in tests.

#### ✅ Topics:

* How to test decorators as functions
* How to test decorated vs. undecorated functions
* Mocking `print`, `open`, etc. inside wrapper

#### 🔁 Example:

```python
def add_one(func):
    def wrapper(x):
        return func(x) + 1
    return wrapper

@add_one
def identity(x):
    return x

# Test:
assert identity(5) == 6
```

---

## 🔰 PHASE 7: Dynamic Decorator Pipelines

### 🎯 Goal: Dynamically build or apply a list of decorators at runtime.

#### ✅ Topics:

* Decorator composition
* `functools.reduce` to stack decorators
* Conditional decoration

#### 🔁 Example:

```python
def uppercase(func): return lambda: func().upper()
def exclaim(func): return lambda: func() + "!"
def decorate_pipeline(func, decorators):
    for deco in reversed(decorators):
        func = deco(func)
    return func

@decorate_pipeline
def say(): return "hello"

say = decorate_pipeline(say, [uppercase, exclaim])
print(say())  # HELLO!
```

---


Great — let's now do a **complete audit** of the **entire decorators journey**: ✅ **Basics to Advanced** ✅ including the **Optional Advanced Deep Dive** roadmap.

---

# ✅ FULL CHECKLIST: Decorators in Python — Basics to Advanced Mastery

---

## 🟢 1. BASIC DECORATOR CONCEPTS ✅ **(Covered)**

| Concept                                 | ✅ Covered? | Notes                               |
| --------------------------------------- | ---------- | ----------------------------------- |
| What is a decorator                     | ✔️         | Explained simply with examples      |
| Functions are first-class objects       | ✔️         | `function_copy = original_function` |
| Simple wrapper decorators               | ✔️         | `@decorator` syntax, before/after   |
| Manually applying decorator without `@` | ✔️         | `f = decorator(f)`                  |
| Multiple decorators (stacked)           | ✔️         | `@dec1 @dec2 def f()`               |
| `*args`, `**kwargs` in decorators       | ✔️         | For flexible signatures             |

---

## 🟡 2. INTERMEDIATE USAGE ✅ **(Covered)**

| Concept                             | ✅ Covered? | Notes                              |
| ----------------------------------- | ---------- | ---------------------------------- |
| Logging function arguments          | ✔️         | `print(args, kwargs)`              |
| Timing function execution           | ✔️         | `time.time()` based                |
| Counting function calls             | ✔️         | `nonlocal count`                   |
| Role-based access (`@require_role`) | ✔️         | `user['role']` validation          |
| Retry mechanism (`@retry(n)`)       | ✔️         | Loop + exception handling          |
| Decorator with parameters (factory) | ✔️         | `@repeat(n)`                       |
| Caching / Memoization               | ✔️         | Custom cache dictionary            |
| `functools.wraps` for metadata      | ✔️         | `@wraps(func)` preserves name/docs |

---

## 🔵 3. FRAMEWORK / PRACTICAL USE CASES ✅ **(Covered)**

| Concept                                      | ✅ Covered? | Notes                        |
| -------------------------------------------- | ---------- | ---------------------------- |
| Flask-style route decorator                  | ✔️         | `@app.route()`               |
| Authentication decorator (`@login_required`) | ✔️         | User auth pattern shown      |
| Decorator for CLI apps / logging             | ✔️         | Shown in project suggestions |

---

## 🔴 4. ADVANCED DECORATOR PATTERNS ✅ **(Optional Deep Dive Roadmap Covered)**

| Concept                                         | ✅ Covered? | Notes                                      |
| ----------------------------------------------- | ---------- | ------------------------------------------ |
| `async`-safe decorators                         | ✔️         | Detect coroutine functions using `inspect` |
| Class decorators (decorate entire class)        | ✔️         | Wrap `__init__`, add methods               |
| Context-aware decorators (file/db/logging)      | ✔️         | `with open(...)` shown                     |
| Type hinting decorators (`TypeVar`, `Callable`) | ✔️         | `@typed_logger` example                    |
| Using `inspect` to introspect signature/docs    | ✔️         | `inspect.signature()` demo                 |
| Unit testing decorators                         | ✔️         | Testing pure + wrapped functions           |
| Dynamic decorator pipelines                     | ✔️         | Build decorator chains at runtime          |

---


