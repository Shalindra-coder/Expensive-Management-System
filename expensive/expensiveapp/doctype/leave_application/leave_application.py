# Copyright (c) 2024, Shalindra and contributors
# For license information, please see license.txt
from datetime import datetime, timedelta
import frappe
from frappe.model.document import Document

class LeaveApplication(Document):
    def before_save(self):
        self.calculate_total_days()

    def calculate_total_days(self):
        if isinstance(self.start_date, str):
            self.start_date = datetime.strptime(self.start_date, "%Y-%m-%d").date()
            
        if isinstance(self.end_date, str):
            self.end_date = datetime.strptime(self.end_date, "%Y-%m-%d").date()

        if self.start_date and self.end_date:
            if self.end_date >= self.start_date: 
                total_days = 0
                current_date = self.start_date
                
                while current_date <= self.end_date:
                    if current_date.weekday() != 6:  # Skip Sundays (6 = Sunday)
                        total_days += 1
                    current_date += timedelta(days=1)

                self.total_days = total_days  # Set the total days excluding Sundays
            else:
                frappe.throw("End date cannot be before start date.")
        else:
            self.total_days = 0
    def validate(self):
        self.fetch_leave_quota()
        # self.check_leave_quota()

    def fetch_leave_quota(self):
        leave_quota = frappe.get_doc("Leave Quota", {"employee": self.employee, "leave_type": self.leave_type})
        if leave_quota:
            self.leave_taken = leave_quota.leave_taken 
            self.leave_balance = leave_quota.leave_balance 
        else:
            frappe.throw("Leave quota not found for this employee and leave type.")

    # def check_leave_quota(self):
    #     leave_quota = frappe.get_doc("Leave Quota", {"employee": self.employee, "leave_type": self.leave_type})

    #     if leave_quota.leave_balance is None:
    #         leave_quota.leave_balance = 0 

    #     if self.total_days is None:
    #         self.total_days = 0

