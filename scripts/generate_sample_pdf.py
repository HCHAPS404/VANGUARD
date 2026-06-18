import fitz

doc = fitz.open()
page = doc.new_page()
text = """AWS Privacy Policy

1. Data Collection
We collect personal data to provide our services. We may collect your IP address, name, and email.

2. Data Usage
We use your data to improve our services. We do not sell your data to third parties.

3. Security
We implement strict security measures to protect your data. All data is encrypted at rest and in transit.
"""
page.insert_text((50, 50), text, fontsize=12)
doc.save("tests/documents/aws_privacy_policy.pdf")
print("Sample PDF generated.")
