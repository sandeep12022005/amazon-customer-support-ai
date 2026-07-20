def detect_intent(message):

    message = message.lower()

    account = [
        "login",
        "password",
        "otp",
        "account",
        "sign in",
        "signin",
        "email",
        "locked",
        "verification"
    ]

    orders = [
        "order",
        "delivery",
        "track",
        "tracking",
        "package",
        "shipping",
        "arrive",
        "dispatch"
    ]

    returns = [
        "return",
        "refund",
        "replace",
        "replacement",
        "cancel order"
    ]

    billing = [
        "payment",
        "invoice",
        "card",
        "charged",
        "upi",
        "credit",
        "debit",
        "billing"
    ]

    prime = [
        "prime",
        "membership",
        "subscription"
    ]

    product = [
        "product",
        "price",
        "pricing",
        "feature",
        "compare",
        "kindle",
        "echo",
        "fire tv"
    ]

    complaint = [
        "complaint",
        "bad",
        "poor",
        "worst",
        "late",
        "damaged",
        "broken",
        "terrible"
    ]

    for x in account:
        if x in message:
            return "account"

    for x in orders:
        if x in message:
            return "orders"

    for x in returns:
        if x in message:
            return "returns"

    for x in billing:
        if x in message:
            return "billing"

    for x in prime:
        if x in message:
            return "prime"

    for x in product:
        if x in message:
            return "product"

    for x in complaint:
        if x in message:
            return "complaint"

    return "faq"