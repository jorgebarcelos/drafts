def functional(payment: float, descount: float) -> float:
    operation = descount / 100 * payment
    result = operation
    final_value = payment - result
    return final_value


print(functional(20.00, 10.00))

