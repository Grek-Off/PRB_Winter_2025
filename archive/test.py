PRODUCT_CATALOG = {
    "laptop": 1000,
    "mouse": 50,
    "keyboard": 80,
    "monitor": 300
}

orders = [
    {"id": 1, "items": [("laptop", 2), ("mouse", 1)], "status": "new", "total": 0},
    {"id": 2, "items": [("keyboard", 1), ("monitor", 1)], "status": "new", "total": 0},
    {"id": 3, "items": [("mouse", 3), ("laptop", 1)], "status": "delivered", "total": 0},
]

def calculate_order_total(order):
    total = 0
    for item, quantity in order["items"]:
        if item in PRODUCT_CATALOG:
            total += PRODUCT_CATALOG[item] * quantity
        else:
            print(f"Warning: Item '{item}' not found in catalog!")
    return total

def update_order_status(order_id, new_status, orders_list):
    for order in orders_list:
        if order["id"] == order_id:
            order["status"] = new_status
            print(f"Order {order_id} status updated to '{new_status}'.")
            return
    print(f"Order with ID {order_id} not found.")

def generate_report(orders_list):
    report = {}
    for order in orders_list:
        status = order["status"]
        report[status] = report.get(status, 0) + 1
    print("\nOrder Status Report:")
    for status, count in report.items():
        print(f"{status.capitalize()}: {count} orders")

def process_orders(orders_list):
    # 1. Рассчёт общей стоимости заказа
    for order in orders_list:
        order["total"] = calculate_order_total(order)

    # 2. Вывод заказов
    print("\nOrders with Calculed Totals:")
    for order in orders_list:
        print(order)

    # 3. Обновить статус первого заказа
    update_order_status(1, "processing", orders_list)

    # 4. Вывести отчёт
    generate_report(orders_list)

process_orders(orders)
    