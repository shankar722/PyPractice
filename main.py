def postfix_conversion(prefix):
    operators = []
    expression = ""

    def is_operator(op_item: str) -> bool:
        is_valid = False
        operators_list = ['+', '-', '*', '/']
        if op_item in operators_list:
            is_valid = True
        return is_valid

    for index, item in enumerate(prefix):
        if is_operator(item):
            operators.append(item)
        else:
            expression += item
            if not is_operator(prefix[index - 1]):
                expression += operators.pop()

    for operator in reversed(operators):
        expression += operator

    print('postfix', expression)


postfix_conversion('-+AB*CD')
