# Random Password Generator

A small Python CLI project that generates strong passwords by user input.

## Features

-Numeric passwords(digits only)
-Alphabetical passwords(mixed lowercase + uppercase letters)
-Alphanumeric passwords(half digits, half letters)
-User chooses type and length

## Input Flow

1. Choose password type:
    -1: Numeric
    -2: Alphabetical
    -3: Alphanumeric
    -4: Exit or I don't need a password
2. Enter password length

## Implementation Notes

- Use `input()` to capture user selection
- Convert selections/length to correct types(strings or integers)
- Use Python `random` utilities for randomness

## Running

- Run the script with 'python3 app.py or python app.py'
- Follow prompts to generate a password
