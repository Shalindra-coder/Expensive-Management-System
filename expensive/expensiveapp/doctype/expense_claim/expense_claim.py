# Copyright (c) 2024, Shalindra and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class ExpenseClaim(Document):
  def validate(self):
        if self.amount <= 0:
            frappe.throw("Amount must be greater than zero.")

