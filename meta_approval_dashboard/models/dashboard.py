# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

from collections import defaultdict


class DashBoard(models.Model):
    _name = "dash.board"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    # _inherits = ['purchase.order']

    name = fields.Char(string="Name", default="Approvals")
    #purchase
    total_p_first_approval = fields.Integer(string="Total", compute="get_total")
    total_p_second_approval = fields.Integer(string="Total", compute="get_total")
    total_p_third_approval = fields.Integer(string="Total", compute="get_total")
    total_P_fourth_approval = fields.Integer(string="Total", compute="get_total")
    #sale
    total_s_first_approval = fields.Integer(string="Total", compute="get_total")
    total_s_second_approval = fields.Integer(string="Total", compute="get_total")
    total_s_third_approval = fields.Integer(string="Total", compute="get_total")
    total_s_fourth_approval = fields.Integer(string="Total", compute="get_total")
    #payment
    total_pay_first_approval = fields.Integer(string="Total", compute="get_total")
    total_pay_second_approval = fields.Integer(string="Total", compute="get_total")
    total_pay_third_approval = fields.Integer(string="Total", compute="get_total")
    #journal
    total_jrn_first_approval = fields.Integer(string="Total", compute="get_total")
    total_jrn_second_approval = fields.Integer(string="Total", compute="get_total")
    total_jrn_third_approval = fields.Integer(string="Total", compute="get_total")

    #Bill
    total_bill_first_approval = fields.Integer(string="Total", compute="get_total")
    total_bill_second_approval = fields.Integer(string="Total", compute="get_total")
    total_bill_third_approval = fields.Integer(string="Total", compute="get_total")

    #Bill
    total_invoice_first_approval = fields.Integer(string="Total", compute="get_total")
    total_nvoice_second_approval = fields.Integer(string="Total", compute="get_total")
    total_nvoice_third_approval = fields.Integer(string="Total", compute="get_total")

    #customer_payment
    total_customer_payment_first_approval = fields.Integer(string="Total", compute="get_total")
    total_customer_payment_second_approval = fields.Integer(string="Total", compute="get_total")
    total_customer_payment_third_approval = fields.Integer(string="Total", compute="get_total")

    @api.depends('name')
    def get_total(self):
        #purchase
        recp1 = self.env['purchase.order'].search_count([('state', '=', 'first_approval')])
        recp2 = self.env['purchase.order'].search_count([('state', '=', 'second_approval')]) 
        recp3 = self.env['purchase.order'].search_count([('state', '=', 'third_approval')])
        recp4 = self.env['purchase.order'].search_count([('state', '=', 'fourth_approval')])
        #sale
        recs1 = self.env['sale.order'].search_count([('state', '=', 'first_approval')])
        recs2 = self.env['sale.order'].search_count([('state', '=', 'second_approval')])
        recs3 = self.env['sale.order'].search_count([('state', '=', 'third_approval')])
        recs4 = self.env['sale.order'].search_count([('state', '=', 'fourth_approval')])
        #account_payment
        recpay1 = self.env['account.payment'].search_count([('state', '=', 'first_approval'), ('partner_type', '=', 'supplier')])
        recpay2 = self.env['account.payment'].search_count([('state', '=', 'second_approval'), ('partner_type', '=', 'supplier')])
        recpay3 = self.env['account.payment'].search_count([('state', '=', 'third_approval'), ('partner_type', '=', 'supplier')])
        #journal_bil
        recjrn1 = self.env['account.move'].search_count([('state', '=', 'first_approval'), ('type', '=', 'entry')])
        recjrn2 = self.env['account.move'].search_count([('state', '=', 'second_approval'), ('type', '=', 'entry')])
        recjrn3 = self.env['account.move'].search_count([('state', '=', 'third_approval'), ('type', '=', 'entry')])

        # bills approval
        recbill1 = self.env['account.move'].search_count([('state', '=', 'first_approval'), ('type', '=', 'in_invoice')])
        recbill2 = self.env['account.move'].search_count([('state', '=', 'second_approval'), ('type', '=', 'in_invoice')])
        recbill3 = self.env['account.move'].search_count([('state', '=', 'third_approval'), ('type', '=', 'in_invoice')])
        
        # invoice approval
        recinv1 = self.env['account.move'].search_count([('state', '=', 'first_approval'), ('type', '=', 'out_invoice')])
        recinv2 = self.env['account.move'].search_count([('state', '=', 'second_approval'), ('type', '=', 'out_invoice')])
        recinv3 = self.env['account.move'].search_count([('state', '=', 'third_approval'), ('type', '=', 'out_invoice')])
        #customer_payment
        reccustomerpay1 = self.env['account.payment'].search_count([('state', '=', 'first_approval'), ('partner_type', '=', 'customer')])
        reccustomerpay2 = self.env['account.payment'].search_count([('state', '=', 'second_approval'), ('partner_type', '=', 'customer')])
        reccustomerpay3 = self.env['account.payment'].search_count([('state', '=', 'third_approval'), ('partner_type', '=', 'customer')])

        #purchase
        self.total_p_first_approval=recp1
        self.total_p_second_approval=recp2
        self.total_p_third_approval=recp3
        self.total_P_fourth_approval=recp4
        #sale
        self.total_s_first_approval=recs1
        self.total_s_second_approval=recs2
        self.total_s_third_approval=recs3
        self.total_s_fourth_approval=recs4
        #vendor_account_payment
        self.total_pay_first_approval=recpay1
        self.total_pay_second_approval=recpay2
        self.total_pay_third_approval=recpay3
         #journal
        self.total_jrn_first_approval=recjrn1
        self.total_jrn_second_approval=recjrn2
        self.total_jrn_third_approval=recjrn3
         #Bills
        self.total_bill_first_approval = recbill1
        self.total_bill_second_approval = recbill2
        self.total_bill_third_approval = recbill3
        #Invoice
        self.total_invoice_first_approval = recinv1
        self.total_nvoice_second_approval = recinv2
        self.total_nvoice_third_approval = recinv3
        #Customer_account_payment
        self.total_customer_payment_first_approval = reccustomerpay1
        self.total_customer_payment_second_approval = reccustomerpay2
        self.total_customer_payment_third_approval = reccustomerpay3

        

    # Purchase Approval
    def open_purchase_first_approval_list(self):

        return {
            'name': _('Purchase'),
            'domain': [('state', '=', 'first_approval')],
            'res_model': 'purchase.order',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
            'target' : 'current',
        }


    def open_purchase_second_approval_list(self):

        return {
            'name': _('Purchase'),
            'domain': [('state', '=', 'second_approval')],
            'res_model': 'purchase.order',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }

    def open_purchase_third_approval_list(self):

        return {
            'name': _('Purchase'),
            'domain': [('state', '=', 'third_approval')],
            'res_model': 'purchase.order',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }

    def open_purchase_fourth_approval_list(self):

        return {
            'name': _('Purchase'),
            'domain': [('state', '=', 'fourth_approval')],
            'res_model': 'purchase.order',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }

    # Sales Approval
    def open_sales_first_approval_list(self):

        return {
            'name': _('Sales'),
            'domain': [('state', '=', 'first_approval')],
            'res_model': 'sale.order',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }
    
    def open_sales_second_approval_list(self):

        return {
            'name': _('Sales'),
            'domain': [('state', '=', 'second_approval')],
            'res_model': 'sale.order',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }

    def open_sales_third_approval_list(self):

        return {
            'name': _('Sales'),
            'domain': [('state', '=', 'third_approval')],
            'res_model': 'sale.order',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }
    
    def open_sales_fourth_approval_list(self):

        return {
            'name': _('Sales'),
            'domain': [('state', '=', 'fourth_approval')],
            'res_model': 'sale.order',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }
    

    #Vendor Payments Approval
    def open_payments_first_approval_list(self):

        return {
            'name': _('Vendor Payments'),
            'domain': [('state', '=', 'first_approval'), ('partner_type', '=', 'supplier')],
            'res_model': 'account.payment',
            'view_id': False,
            'views': [(self.env.ref('account.view_account_supplier_payment_tree').id, 'tree'), (self.env.ref('account.view_account_payment_form').id, 'form')],
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }
    
    def open_payments_second_approval_list(self):

        return {
            'name': _('Vendor Payments'),
            'domain': [('state', '=', 'second_approval'), ('partner_type', '=', 'supplier')],
            'res_model': 'account.payment',
            'view_id': False,
            'views': [(self.env.ref('account.view_account_supplier_payment_tree').id, 'tree'), (self.env.ref('account.view_account_payment_form').id, 'form')],
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }

    # self.env.ref('account.invoice_tree').id,
    def open_payments_third_approval_list(self):

        return {
            'name': _('Vendor Payments'),
            'domain': [('state', '=', 'third_approval'), ('partner_type', '=', 'supplier')],
            'res_model': 'account.payment',
            'view_id': False,
            'views': [(self.env.ref('account.view_account_supplier_payment_tree').id, 'tree'), (self.env.ref('account.view_account_payment_form').id, 'form')],
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }

    #Customer Payments Approval
    def open_customer_payments_first_approval_list(self):

        return {
            'name': _('Customer Payments'),
            'domain': [('state', '=', 'first_approval'), ('partner_type', '=', 'customer')],
            'res_model': 'account.payment',
            'view_id': False,
            'views': [(self.env.ref('account.view_account_supplier_payment_tree').id, 'tree'), (self.env.ref('account.view_account_payment_form').id, 'form')],
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }
    
    def open_customer_payments_second_approval_list(self):

        return {
            'name': _('Customer Payments'),
            'domain': [('state', '=', 'second_approval'), ('partner_type', '=', 'customer')],
            'res_model': 'account.payment',
            'view_id': False,
            'views': [(self.env.ref('account.view_account_supplier_payment_tree').id, 'tree'), (self.env.ref('account.view_account_payment_form').id, 'form')],
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }

    # self.env.ref('account.invoice_tree').id,
    def open_customer_payments_third_approval_list(self):

        return {
            'name': _('Customer Payments'),
            'domain': [('state', '=', 'third_approval'), ('partner_type', '=', 'customer')],
            'res_model': 'account.payment',
            'view_id': False,
            'views': [(self.env.ref('account.view_account_supplier_payment_tree').id, 'tree'), (self.env.ref('account.view_account_payment_form').id, 'form')],
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }

    
    # Journal Approval
    def open_journal_first_approval_list(self):

        return {
            'name': _('Journal'),
            'domain': [('state', '=', 'first_approval'), ('type', '=', 'entry')],
            'res_model': 'account.move',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }
    
    def open_journal_second_approval_list(self):

        return {
            'name': _('Journal'),
            'domain': [('state', '=', 'second_approval'), ('type', '=', 'entry')],
            'res_model': 'account.move',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }

    def open_journal_third_approval_list(self):

        return {
            'name': _('Journal'),
            'domain': [('state', '=', 'third_approval'), ('type', '=', 'entry')],
            'res_model': 'account.move',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }

    # Bill Approval
    def open_bill_first_approval_list(self):
        return {
            'name': _('Bills'),
            'domain': [('state', '=', 'first_approval'), ('type', '=', 'in_invoice')],
            'res_model': 'account.move',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }

    def open_bill_second_approval_list(self):
        return {
            'name': _('Bills'),
            'domain': [('state', '=', 'second_approval'), ('type', '=', 'in_invoice')],
            'res_model': 'account.move',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }

    def open_bill_third_approval_list(self):
        return {
            'name': _('Bills'),
            'domain': [('state', '=', 'third_approval'), ('type', '=', 'in_invoice')],
            'res_model': 'account.move',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }
    
    # Invoice Approval
    def open_invoice_first_approval_list(self):
        return {
            'name': _('Invoice'),
            'domain': [('state', '=', 'first_approval'), ('type', '=', 'out_invoice')],
            'res_model': 'account.move',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }

    def open_invoice_second_approval_list(self):
        return {
            'name': _('Invoice'),
            'domain': [('state', '=', 'second_approval'), ('type', '=', 'out_invoice')],
            'res_model': 'account.move',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }

    def open_invoice_third_approval_list(self):
        return {
            'name': _('Invoice'),
            'domain': [('state', '=', 'third_approval'), ('type', '=', 'out_invoice')],
            'res_model': 'account.move',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }

    def send_mail(self):

        template_obj = self.env['mail.mail']
        template_data = {
            'subject': 'Test : ',
            'body_html': 'ABcde',
            'email_from': 'joyanto359@gmail.com',
            'email_to': 'joyanto858@gmail.com',
        }
        template_id = template_obj.create(template_data)
        template_obj.send(template_id)

        # template_id = template_obj.create(template_data)
        # template_obj.send(template_id)
   
   
