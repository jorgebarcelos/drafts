from typing import Dict


def person(name: str, age: int) -> Dict:
    data = {'name': name, 'age': age}
    return data

resp = person('jorge', 42)
print(resp)
