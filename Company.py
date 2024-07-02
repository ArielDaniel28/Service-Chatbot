class Company:
    def __init__(self):
        self.policies = {
            "Return Policy": "The customer can return most items within 30 days of purchase for a full refund or "
            "exchange."
            "Items must be in their original condition, with all tags and packaging intact."
            "The customer must bring the receipt or proof of purchase when returning items.",
            "Non-returnable Items": "Certain items such as clearance merchandise, perishable goods, and personal care "
            "items are non-returnable."
            "The customer can check the product description or ask for human representative for more details.",
            "Refund": "Refunds will be issued to the original form of payment."
            "If the customer paid by credit card, the refund will be credited to the card."
            "If the customer paid by cash or check, they will receive a cash refund.",
        }

    def get_policies_text(self):
        return "\n\n".join([f"{key}: {value}" for key, value in self.policies.items()])
