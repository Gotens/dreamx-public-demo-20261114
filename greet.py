def greet(name: str) -> str:
    name = name.strip()
    if not name:
        raise ValueError("Name must not be blank")
    return f"Hello, {name}"
