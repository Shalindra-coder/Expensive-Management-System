// Copyright (c) 2024, Shalindra and contributors
// For license information, please see license.txt

frappe.ui.form.on('Leave Application', {
    refresh: function(frm) {
        frappe.db.get_value('Leave Quota', { employee: frm.doc.employee, leave_type: frm.doc.leave_type }, 'leave_balance', (r) => {
            if (r.leave_balance < frm.doc.total_days) {
                frappe.msgprint(__('You have exceeded your leave balance for this leave type. Please check your leave quota or contact your manager for further assistance.'));
                frappe.validated = false;
            }
        });
    },
        on_submit: function(frm) {
            frm.set_value('status', 'Pending');
        }
    
    
});
