# Pro-Level-Inventory-Tracker-CLI-

# Pro-Inventory CLI: Market-Ready Foundation

## Overview
This is a professional Inventory Management System built with Python. It shows how to handle persistent data, validate user input, and organize code into a scalable, modular structure.

## Market-Relevant Skills Demonstrated
- **Modular Programming:** Separating UI logic from business logic.
- **Data Persistence:** Using JSON as a simple database.
- **Defensive Programming:** Using `try-except` blocks to handle "dirty" data and prevent crashes.
- **Type Hinting:** Using Python's Type Hints to make code clearer and easier to maintain.

## Core Features
- **Persistent Storage:** Data is saved to `data/inventory.json`.
- **Search & Filter:** Search for items by name or ID.
- **Stock Alerts:** Automatically flags items that are running low (less than 5 units).
- **Formatted Reporting:** Outputs a clean table view of current assets.

## Project Structure
```text
.
├── main.py              # The UI and Menu Loop
├── inventory_logic.py   # The "Engine" (CRUD & File I/O)
├── data/
│   └── inventory.json   # Where your data lives
└── README.md
```

## Installation & Usage
1. Clone this repository.
2. Run the application:
   ```bash
   python inventory_manager.py
   ```
