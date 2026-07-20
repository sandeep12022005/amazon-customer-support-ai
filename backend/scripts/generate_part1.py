from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
KB = BASE_DIR / "knowledge_base"

folders = [
    "account",
    "orders"
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


# ---------------- ACCOUNT ----------------

write_doc(
    "account",
    "Login_Guide.md",
    "Amazon Login Guide",
    [

        ("Overview",
         """Customers can log in using their registered email address or mobile number together with their password."""),

        ("Common Problems",
         """
• Forgot password

• Incorrect password

• OTP not received

• Account temporarily locked

• Verification issues
"""),

        ("Password Reset",
         """
1. Open Amazon Login page.

2. Click Forgot Password.

3. Verify using Email or Mobile.

4. Create a new password.

5. Login again.
"""),

        ("Security Tips",
         """
• Never share OTP.

• Enable Two Factor Authentication.

• Use strong passwords.

• Don't reuse passwords.
"""),

        ("FAQ",
         """
Q. I forgot my password.

A. Use Forgot Password.

Q. My account is locked.

A. Wait 30 minutes and verify identity.

Q. OTP not received.

A. Retry after 60 seconds.
""")
    ]
)

write_doc(
    "account",
    "Account_Security.md",
    "Amazon Account Security",
    [

        ("Overview",
         """Amazon protects customer accounts using multiple authentication mechanisms."""),

        ("Best Practices",
         """
• Enable 2FA

• Verify email

• Verify phone

• Never share passwords

• Check login history
"""),

        ("Suspicious Activity",
         """
If suspicious activity is detected:

• Password reset

• Device verification

• Login restriction

• Identity verification
""")
    ]
)

# ---------------- ORDERS ----------------

write_doc(
    "orders",
    "Track_Order.md",
    "Track Your Amazon Order",
    [

        ("Overview",
         """Customers can monitor their order status from the Orders page."""),

        ("Order Status",
         """
Pending

Confirmed

Packed

Shipped

Out for Delivery

Delivered
"""),

        ("Tracking Steps",
         """
1. Login

2. Orders

3. Select Order

4. Track Package
"""),

        ("FAQ",
         """
Q. My package is delayed.

A. Check tracking information.

Q. Tracking not updated.

A. Wait 24 hours.
""")
    ]
)

write_doc(
    "orders",
    "Shipping_Methods.md",
    "Amazon Shipping Methods",
    [

        ("Shipping Types",
         """
Standard Shipping

One-Day Delivery

Same-Day Delivery

Scheduled Delivery
"""),

        ("Delivery Times",
         """
Standard

3-7 Business Days

Prime

1-2 Business Days
"""),

        ("Notes",
         """
Delivery time depends on

• Seller

• Warehouse

• Weather

• Holidays
""")
    ]
)

print("Knowledge Base Part 1 Created Successfully!")