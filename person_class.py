class Person:
    def __init__(self, first_name: str, last_name: str, birth: int, cpf: int) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.birth = birth
        self.cpf = cpf

    def __str__(self) -> str:
        return f"{self.__dict__}"
    

class Employee(Person):
    def __init__(self, first_name: str,
                last_name: str,
                birth: int,
                cpf: int,
                registration_code: int, 
                function: str,
                salary: float
            ) -> None:
        super().__init__(first_name, last_name, birth, cpf)
        self.registration_code = registration_code
        self.function = function
        self.salary = f'${salary}'


employee = Employee("Aron", "McCarthur", 12011985, 99999999999, 121314, "Python Developer", 12000 )
print(employee)