# Copyright (c) 2024, Shalindra and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class ExpenseClaim(Document):
 def before_save(self):
    total = 0
    for item in self.add_items:
        total += item.amount
    self.total_amount = total
          
    