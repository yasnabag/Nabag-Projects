# Vending Machine

A command-line Python simulation of two vending machines, separating the machine model from user interaction.

[Back to portfolio](../README.md)

## Features

- Product selection, prices, and stock tracking.
- Credit insertion using accepted denominations.
- Purchases, remaining credit, and refunds.
- Custom exceptions for invalid selections, depleted stock, and insufficient credit.
- Independent state for two machine instances.

## Design

| File | Responsibility |
| --- | --- |
| `vending_machine.py` | Product inventory, credit, revenue, and transaction rules |
| `break_room.py` | Menus, user input, error messages, and application entry point |

This separation keeps transaction logic in the model and presentation in the interface.

## Run

Requires Python 3. No third-party packages are needed.

From the repository root:

```bash
cd Vending_Machine
python break_room.py
```

Choose a menu option to add credit, purchase a product, return change, or exit. Use `python3` if that is your system's Python command.

## Scope

This is an educational simulation. State is held in memory and resets when the program restarts. It does not process real payments.
