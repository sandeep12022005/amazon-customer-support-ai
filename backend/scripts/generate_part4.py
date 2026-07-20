from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
KB = BASE_DIR / "knowledge_base"

folders = [
    "complaints",
    "general"
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
# COMPLAINTS
# ===================================================

write_doc(
    "complaints",
    "Complaint_Process.md",
    "Amazon Complaint Process",
    [

        ("Overview",
"""
Customers may submit complaints regarding orders,
delivery, payments, products or customer service.
"""),

        ("Complaint Categories",
"""
• Late Delivery

• Damaged Product

• Wrong Product

• Payment Issues

• Seller Complaint

• Delivery Partner Complaint
"""),

        ("Resolution Steps",
"""
1. Customer submits complaint

2. Amazon verifies issue

3. Investigation begins

4. Resolution provided

5. Customer notified
"""),

        ("Resolution Time",
"""
Most complaints are resolved within
2–5 business days.
""")
    ]
)

write_doc(
    "complaints",
    "Damaged_Product.md",
    "Damaged Product",
    [

        ("Overview",
"""
If an item arrives damaged,
customers can request
replacement or refund.
"""),

        ("Evidence",
"""
Recommended:

• Photos

• Videos

• Packaging Images

• Order Number
"""),

        ("Available Options",
"""
Replacement

Refund

Repair (eligible products)
""")
    ]
)

write_doc(
    "complaints",
    "Delivery_Complaints.md",
    "Delivery Complaints",
    [

        ("Common Complaints",
"""
Late Delivery

Package Not Received

Delivered to Wrong Address

Damaged Package
"""),

        ("Investigation",
"""
Amazon verifies

GPS

Delivery Photo

Courier Scan

Customer Confirmation
""")
    ]
)

write_doc(
    "complaints",
    "Escalation.md",
    "Complaint Escalation",
    [

        ("Overview",
"""
If a complaint is unresolved,
customers may request escalation.
"""),

        ("Levels",
"""
Customer Support

↓

Senior Executive

↓

Specialist Team

↓

Final Resolution
""")
    ]
)


# ===================================================
# GENERAL
# ===================================================

write_doc(
    "general",
    "FAQ.md",
    "Amazon Frequently Asked Questions",
    [

        ("General Questions",
"""
Q. How do I track an order?

Q. How do I return an item?

Q. How do I reset password?

Q. How do I contact Amazon?

Q. What payment methods are accepted?
""")
    ]
)

write_doc(
    "general",
    "Contact_Support.md",
    "Contact Amazon Support",
    [

        ("Support Channels",
"""
Live Chat

Phone Support

Email Support

Help Center
"""),

        ("Availability",
"""
Support availability depends on
region and issue type.
""")
    ]
)

write_doc(
    "general",
    "Privacy.md",
    "Privacy Policy Summary",
    [

        ("Overview",
"""
Amazon collects information required
to process orders and improve services.
"""),

        ("Customer Data",
"""
Name

Address

Email

Phone Number

Payment Information
"""),

        ("Security",
"""
Customer information is protected using
industry-standard security measures.
""")
    ]
)

write_doc(
    "general",
    "Terms.md",
    "Terms and Conditions Summary",
    [

        ("Overview",
"""
By using Amazon services,
customers agree to Amazon's terms.
"""),

        ("Important Points",
"""
Orders may be cancelled.

Refund eligibility varies.

Product availability may change.

Prices can change without notice.
""")
    ]
)

print("Knowledge Base Part 4 Created Successfully!")