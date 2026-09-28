import pandas as pd

def tratar_pedidos(orders, order_items, payments, reviews):
    for col in [
        "order_purchase_timestamp",
        "order_delivered_customer_date",
        "order_estimated_delivery_date",
    ]:
        orders[col] = pd.to_datetime(orders[col], errors="coerce")

    orders["dias_entrega"] = (
        orders["order_delivered_customer_date"]
        - orders["order_purchase_timestamp"]
    ).dt.days

    orders["atraso"] = (
        orders["order_delivered_customer_date"]
        > orders["order_estimated_delivery_date"]
    )

    order_items = order_items.copy()
    order_items["valor_item"] = order_items["price"] + order_items["freight_value"]

    reviews_agg = reviews.groupby("order_id")["review_score"].mean().reset_index()

    fato = (
        order_items.merge(orders, on="order_id", how="left")
        .merge(reviews_agg, on="order_id", how="left")
    )

    return fato.drop_duplicates(subset=["order_id", "order_item_id"])