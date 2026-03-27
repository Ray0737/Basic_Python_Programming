# Classwork | Basic Python Programming

A weekly exercise repository covering **Python fundamentals through GUI development**, completed during M.4 Semester 1 as part of the E-AI curriculum.

---

## Overview

This repository contains 11 weekly Python modules that progressively build from basic syntax and variables all the way to building graphical user interfaces with Tkinter. Each file is a standalone script targeting a specific concept, plus a final exam mock-up and a comprehensive summary cheat-sheet.

---

## Topics Covered

| Week | File | Topic | Description |
| :--- | :--- | :--- | :--- |
| 01 | `W01.py` | String & Print | String formatting with `%d`, `%s`, `%.2f`, and variable output. |
| 02 | `W02.py` | Input Commands | Reading user input and performing calculations. |
| 03 | `W03.py` | Data Types & Structures | Lists, tuples, sets, and type conversion. |
| 04 | `W04.py` | Conditional Statements | `if`, `elif`, `else` branching logic. |
| 05 | `W05.py` | Loops | `while` and `for` loops with `range()` and loop control (`break`, `continue`). |
| 06 | `W06.py` | Functions | Defining functions, default parameters, `*args`, `**kwargs`, and lambda expressions. |
| 07 | `W07.py` | Tuples & Dictionaries | Advanced dictionary manipulation, key-value operations, and tuple unpacking. |
| 08 | `W08.py` | Object-Oriented Programming | Classes, constructors (`__init__`), inheritance, method overriding, and encapsulation. |
| 09 | `W09.py` | GUI – Part 1 | Introduction to Tkinter: creating windows, labels, and absolute positioning with `.place()`. |
| 10 | `W10.py` | GUI – Part 2 | Interactive buttons, grid layout, dynamic label updates, and a live clock widget. |
| 11 | `W11.py` | GUI – Part 3 | A cafe ordering system with image buttons, order tallying, receipt generation via `messagebox`, and real-time timestamps. |

---

## Additional Files

| File | Description |
| :--- | :--- |
| `Summary.py` | A comprehensive Python cheat-sheet (455 lines) covering syntax, data structures, control flow, functions, OOP, modules, exception handling, file I/O, decorators, generators, comprehensions, and regex. |
| `Final Exam.py` | Mock-up based on the 2025 final exam. Includes an **ATM banking system** (login, register, deposit, withdraw with banknote breakdown) and a **terminal triangle** pattern printer using nested loops. |

---

## How It Was Built

- **Language:** Python 3
- **GUI Framework:** Tkinter (standard library)
- **Concepts Applied:** The course follows a bottom-up teaching approach — starting with raw `print()` and `input()`, building through loops and functions, and culminating in interactive desktop applications using event-driven programming.
- **Structure:** Each `WXX.py` file corresponds to a weekly in-class exercise, designed to be run independently.

---

## How to Run

```bash
# Run any weekly exercise
python W01.py

# Run the GUI cafe ordering system (requires images in /pic folder)
python W11.py

# Run the final exam mock-up
python "Final Exam.py"
```

---

## Recommended Resource

🎥 [Bro Code – Python Full Course (YouTube)](https://youtu.be/ix9cRaBkVe0?si=qnEyhYN4wBzHq9s8)
