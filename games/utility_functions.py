def validated_input(valid_options: list) -> str:
    message = "Enter:"
    for s in valid_options:
        message += f" {s}"
    
    while True:
        user_input = input()
        if user_input in valid_options:
            return user_input
        print("Invalid input. Please try again.")
        print(message)
