"""
Inventory management module with functions to add, remove,
load, save, and report stock data.
"""

import json
from datetime import datetime


# Global inventory data
stock_data = {}


def add_item(item="default", qty=0, logs=None):
    """Add item to inventory with optional logging."""
    if not item:
        return
    if logs is None:
        logs = []
    try:
        qty = int(qty)
    except (ValueError, TypeError):
        return
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


def remove_item(item, qty):
    """Remove item from inventory, handling missing items."""
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        pass


def get_qty(item):
    """Return quantity of item in inventory."""
    return stock_data.get(item, 0)


def load_data(file="inventory.json"):
    """Load inventory data from JSON file."""
    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)
        stock_data.clear()
        stock_data.update(data)



def save_data(file="inventory.json"):
    """Save inventory data to JSON file."""
    with open(file, "w", encoding="utf-8") as f:
        json.dump(stock_data, f)


def print_data():
    """Print current inventory items and quantities."""
    print("Items Report")
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")


def check_low_items(threshold=5):
    """Return list of items below threshold."""
    result = []
    for item, qty in stock_data.items():
        if qty < threshold:
            result.append(item)
    return result


def main():
    """Run demo inventory operations."""
    add_item("apple", 10)
    add_item("banana", -2)
    add_item(123, "ten")
    remove_item("apple", 3)
    remove_item("orange", 1)
    print("Apple stock:", get_qty("apple"))
    print("Low items:", check_low_items())
    save_data()
    load_data()
    print_data()
    print("eval used")


if __name__ == "__main__":
    main()
