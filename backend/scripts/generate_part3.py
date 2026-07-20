from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
KB = BASE_DIR / "knowledge_base"

folders = [
    "prime",
    "products"
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
# PRIME
# ===================================================

write_doc(
    "prime",
    "Prime_Membership.md",
    "Amazon Prime Membership",
    [

        ("Overview",
"""
Amazon Prime is a subscription service that offers shopping,
entertainment and delivery benefits.
"""),

        ("Membership Plans",
"""
Monthly Plan

Quarterly Plan

Annual Plan

Student Plan
"""),

        ("Benefits",
"""
• Free Fast Delivery

• Prime Video

• Prime Music

• Prime Reading

• Early Access Deals
"""),

        ("Eligibility",
"""
Prime benefits begin immediately after successful payment.

Membership automatically renews unless cancelled.
"""),

        ("FAQ",
"""
Q. Can I cancel Prime?

A. Yes.

Q. Can I renew later?

A. Yes.
""")
    ]
)

write_doc(
    "prime",
    "Prime_Benefits.md",
    "Prime Benefits",
    [

        ("Shopping",
"""
Free One-Day Delivery

Free Same-Day Delivery

Exclusive Discounts

Lightning Deals
"""),

        ("Entertainment",
"""
Prime Video

Prime Music

Prime Reading

Gaming Benefits
"""),

        ("Family",
"""
Household Sharing

Kids Content

Family Delivery
"""),

        ("Notes",
"""
Benefits may vary depending on region.
""")
    ]
)

write_doc(
    "prime",
    "Prime_Cancellation.md",
    "Prime Cancellation",
    [

        ("Overview",
"""
Customers may cancel Prime membership from the Prime Membership page.
"""),

        ("Steps",
"""
1. Login

2. Prime Membership

3. Manage Membership

4. Cancel Membership
"""),

        ("Refund Policy",
"""
Eligible customers may receive a partial or full refund
depending on Prime usage.
""")
    ]
)

write_doc(
    "prime",
    "Prime_FAQ.md",
    "Prime FAQ",
    [

        ("Questions",
"""
Q. What is Prime?

Q. How much does it cost?

Q. Can I cancel anytime?

Q. What benefits do I receive?

Q. Can I share Prime?
""")
    ]
)


# ===================================================
# PRODUCTS
# ===================================================

write_doc(
    "products",
    "Kindle.md",
    "Amazon Kindle",
    [

        ("Overview",
"""
Kindle is Amazon's eBook reader.
"""),

        ("Features",
"""
• E-Ink Display

• Adjustable Brightness

• Long Battery Life

• Dictionary Support

• Highlight Notes
"""),

        ("Models",
"""
Kindle

Kindle Paperwhite

Kindle Oasis

Kindle Scribe
"""),

        ("FAQ",
"""
Q. Does Kindle support PDFs?

A. Yes.

Q. Can I read offline?

A. Yes.
""")
    ]
)

write_doc(
    "products",
    "Echo.md",
    "Amazon Echo",
    [

        ("Overview",
"""
Echo is Amazon's smart speaker powered by Alexa.
"""),

        ("Features",
"""
Voice Commands

Smart Home

Music Streaming

Timers

Reminders

Weather Updates
"""),

        ("Supported Devices",
"""
Echo Dot

Echo Pop

Echo Studio

Echo Show
""")
    ]
)

write_doc(
    "products",
    "FireTV.md",
    "Amazon Fire TV",
    [

        ("Overview",
"""
Fire TV lets customers stream entertainment content.
"""),

        ("Features",
"""
Netflix

Prime Video

Disney+

YouTube

Alexa Voice Search
"""),

        ("Requirements",
"""
HDMI TV

Internet Connection

Amazon Account
""")
    ]
)

write_doc(
    "products",
    "Alexa_FAQ.md",
    "Alexa FAQ",
    [

        ("Questions",
"""
Q. What is Alexa?

Q. Can Alexa control lights?

Q. Can Alexa play music?

Q. Does Alexa support routines?

Q. Can Alexa answer questions?
""")
    ]
)

print("Knowledge Base Part 3 Created Successfully!")