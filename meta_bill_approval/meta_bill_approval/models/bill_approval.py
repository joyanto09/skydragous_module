# -*- coding: utf-8 -*-
from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.exceptions import UserError
from odoo.tools import float_is_zero, float_compare, DEFAULT_SERVER_DATETIME_FORMAT

class BillApproval(models.Model):
    
    _inherit = 'account.move'
    
    state = fields.Selection(selection=[
        ('draft', 'Draft'),
        ('first_approval', 'Manager Approval'),
        ('second_approval', 'Head of Finance Approval'),
        ('third_approval', 'CEO Approval'),
        ('to approve', 'Approved'),
        ('posted', 'Posted'),
        ('cancel', 'Cancelled')
        ], string='Status', required=True, readonly=True, copy=False, tracking=True, default='draft')
       
    
    def bill_operation_send_approval(self):
        return self.write({'state': 'first_approval'})
        
    def first_approval(self):
        return self.write({'state': 'second_approval'})
    
    def first_approval_reject(self):
        return self.write({'state': 'cancel'})
    
    def second_approval(self):
        return self.write({'state': 'third_approval'})
    
    def second_approval_reject(self):
        return self.write({'state': 'cancel'})
    
    def third_approval(self):
        return self.write({'state': 'to approve'})
    
    def third_approval_reject(self):
        return self.write({'state': 'cancel'})
    
    
    
    
    
    
         