# Copyright (c) 2024, Shalindra and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class LeaveQuota(Document):
    def validate(self):
        self.update_leave_taken()

    def update_leave_taken(self):
        approved_leaves = frappe.get_all("Leave Application", filters={
            "employee": self.employee,
            "leave_type": self.leave_type,
            "status": "Approved"
        }, fields=["total_days"])

        # self.leave_taken = sum(leave.total_days for leave in approved_leaves)  
        # self.leave_balance = self.maximum_allowed - self.leave_taken  
        self.leave_balance = self.maximum_allowed - self.leave_taken

