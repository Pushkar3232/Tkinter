def evaluate_expression(expression):
    try:
        # Evaluate the math expression safely
        result = eval(expression, {"__builtins__": None}, {})
        return result
    except Exception:
        return "Error"
