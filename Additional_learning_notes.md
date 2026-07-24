# Additional Learning Notes

## OOP

### What is a class?

A class is a blueprint used to create objects.

### What is an object?

An object is an instance of a class.

---

## Magic Methods

### __str__()

Defines how an object is represented as a string when using `print()`.

---

## Data Structures

### to_dict()

A custom method that converts an object into a dictionary.

Useful when saving objects to JSON.

---

## Decorators

### @classmethod

A method that belongs to the class instead of an object.

---

## Git

### HEAD

...

---

## Python

### self

...





# `__name__` and `__main__`

Every Python file has a special built-in variable called `__name__`.

- If the file is **executed directly**, Python sets:

```python
__name__ == "__main__"
```

- If the file is **imported as a module**, `__name__` becomes the module's name.

Example:

```python
# main.py

def main():
    print("Program started")

if __name__ == "__main__":
    main()
```

### Why use it?

It prevents code from running automatically when the file is imported into another module.

Without:

```python
main()
```

would execute every time someone imports `main.py`.

With:

```python
if __name__ == "__main__":
    main()
```

`main()` runs **only** when `main.py` is the program's entry point.

### Key Takeaway

- `__name__` → built-in variable containing the module name.
- `"__main__"` → value assigned when the file is executed directly.
- `if __name__ == "__main__":` → standard way to define the entry point of a Python program.