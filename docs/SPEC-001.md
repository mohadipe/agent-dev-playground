# SPEC-001: Hello Gibbs Team Script

## 1. Goal
The goal of this project is to create a simple Python script that outputs a specific greeting message ("Hello from Gibbs Team") followed by the current date and time. This serves as a basic proof-of-concept for the development environment setup.

## 2. Architecture
The project will consist of a single Python script located in the source directory.

**File Structure:**
```
/
├── src/
│   └── main.py
└── docs/
    └── SPEC-001.md
```

## 3. Requirements
*   **Language:** Python 3.8 or higher
*   **Libraries:** Standard library only (specifically `datetime`)
*   **OS:** Cross-platform (Linux, macOS, Windows)

## 4. Implementation Details
1.  Create a file named `src/main.py`.
2.  Import the `datetime` module from the standard library.
3.  Define a main execution block (`if __name__ == "__main__":`).
4.  Inside the main block:
    *   Print the string "Hello from Gibbs Team" to stdout.
    *   Get the current time using `datetime.datetime.now()`.
    *   Format the time as a string (e.g., ISO format or readable string).
    *   Print the current time to stdout.
