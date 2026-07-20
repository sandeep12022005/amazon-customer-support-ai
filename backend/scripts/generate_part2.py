from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
KB = BASE_DIR / "knowledge_base"

folders = [
    "returns",
    "billing"
]

for folder in folders:
    (KB / folder).mkdir(parents=True, exist_ok=True)


def write_doc(folder, filename, title, sections):

    path = KB / folder / filename

    with open(path, "w", encoding="utf-8") as f:

        f.write(f"# {title}\n\n")

        for heading, body in sections:
            f.write(f"## {heading}\n\n")
            f.write(body)
            f.write("\n\n")


# ===================================================
# RETURNS
# ===================================================

write_doc(
    "returns",
    "Return_Policy.md",
    "Amazon Return Policy",
    [

        ("Overview",
"""
Most items sold on Amazon are eligible for return within 30 days of delivery.

Some products have different return windows depending on category.
"""),

        ("Eligible Products",
"""
• Electronics

• Clothing

• Books

• Kitchen Items

• Home Appliances

• Toys
"""),

        ("How to Return",
"""
1. Login

2. Open Your Orders

3. Select Item

4. Click Return Item

5. Choose Reason

6. Print Label

7. Ship Package
"""),

        ("Exceptions",
"""
Items that cannot usually be returned:

• Gift Cards

• Digital Downloads

• Opened Software

• Certain Grocery Products
"""),

        ("FAQ",
"""
Q. How many days do I have?

A. Usually within 30 days.

Q. Can I return damaged items?

A. Yes.
""")
    ]
)

write_doc(
    "returns",
    "Refund_Process.md",
    "Amazon Refund Process",
    [

        ("Overview",
"""
Refunds begin after Amazon receives and inspects the returned product.
"""),

        ("Refund Timeline",
"""
Credit Card

3-5 Business Days

Debit Card

5-7 Business Days

Amazon Pay Balance

Within 24 Hours

Gift Card

Instant
"""),

        ("Status",
"""
Requested

Processing

Approved

Completed
"""),

        ("FAQ",
"""
Q. Where is my refund?

A. Check Refund Status.

Q. Can refund fail?

A. Yes, if payment information is invalid.
""")
    ]
)

write_doc(
    "returns",
    "Replacement_Guide.md",
    "Replacement Guide",
    [

        ("Overview",
"""
Replacement is available for eligible products.

Replacement is generally faster than refund.
"""),

        ("When Replacement is Allowed",
"""
Wrong Product

Damaged Product

Missing Accessories

Defective Item
"""),

        ("Process",
"""
Return Item

↓

Inspection

↓

Replacement Approved

↓

New Shipment
""")
    ]
)

# ===================================================
# BILLING
# ===================================================

write_doc(
    "billing",
    "Payment_Methods.md",
    "Amazon Payment Methods",
    [

        ("Supported Methods",
"""
Credit Card

Debit Card

UPI

Net Banking

Amazon Pay

EMI

Gift Card
"""),

        ("Payment Failure",
"""
Reasons:

• Wrong CVV

• Low Balance

• Expired Card

• Bank Server Down
"""),

        ("Retry",
"""
Customers can retry payment after updating payment information.
""")
    ]
)

write_doc(
    "billing",
    "Invoices.md",
    "Invoices",
    [

        ("Download Invoice",
"""
1. Login

2. Orders

3. Invoice

4. Download PDF
"""),

        ("GST Invoice",
"""
Business customers can request GST invoices for eligible orders.
"""),

        ("FAQ",
"""
Q. Invoice missing?

A. Contact Seller or Amazon Support.
""")
    ]
)

write_doc(
    "billing",
    "Gift_Cards.md",
    "Amazon Gift Cards",
    [

        ("Overview",
"""
Gift Cards can be redeemed to Amazon Pay balance.
"""),

        ("Validity",
"""
Gift Cards are valid according to the applicable terms shown at purchase.
"""),

        ("FAQ",
"""
Q. Can Gift Cards be refunded?

A. Usually No.

Q. Can Gift Cards expire?

A. Check the applicable terms and validity period.
""")
    ]
)

print("Knowledge Base Part 2 Created Successfully!")