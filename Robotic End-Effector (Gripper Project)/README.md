# Robotic End-Effector

A collaborative engineering project connecting a physical gripper with a Python package-ordering and collection workflow.

[Back to portfolio](../README.md) · [Project report](1P13_Project_Report.pdf) · [Python source](<GRIPPER CODE.py>)

## Project overview

The team developed a multi-claw, 3D-printed end-effector for package handling. The software brings together account access, product lookup, order records, robotic collection, and receipt generation.

## Software components

- User registration and password verification using `bcrypt`.
- Product and price lookup from CSV records.
- Item-specific Q-Arm positions for collection.
- Order receipts and customer purchase summaries.
- Persistent user and order records through file I/O.

## Files

| File | Contents |
| --- | --- |
| `GRIPPER CODE.py` | Account, order, and robotic collection workflow |
| `1P13_Project_Report.pdf` | Engineering project report |

## Runtime requirements and current limitations

This upload documents the original lab project; it is not a standalone application.

The script depends on `bcrypt`, a configured Q-Arm object named `arm`, a `scan_barcode()` function, and a `sleep` function supplied or imported by the surrounding environment. Those integrations are not defined in the uploaded script.

It also expects local CSV files such as `products.csv` and `users.csv`; the supporting datasets are not included. The code writes order records to `orders.csv`.

## Team credit

The source lists Aravinthan Vivekananthan, Chak Pui Sze, Ali Ashmal Molwani, Navid Rouf, and Yaseen Nabag as authors. This repository presents the work as a team project.
