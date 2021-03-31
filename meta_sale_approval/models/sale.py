# -*- coding: utf-8 -*-
from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.exceptions import UserError
from odoo.tools import float_is_zero, float_compare, DEFAULT_SERVER_DATETIME_FORMAT

class SaleOrder(models.Model):
    _inherit = "sale.order"
    
    state = fields.Selection([
        ('draft', 'Quotation'),
        ('sent', 'Quotation Sent'),
        ('first_approval', 'Marketing'),
        ('second_approval', 'Production'),
        ('third_approval', 'Finance'),
        ('fourth_approval', 'CEO'),
        ('to approve', 'Approved'),
        ('sale', 'Sales Order'),
        ('done', 'Locked'),
        ('cancel', 'Cancelled'),
        ], string='Status', readonly=True, copy=False, index=True, tracking=3, default='draft')
    
    def sale_operation_send_approval(self):
        try:
            users=self.env['res.users'].search([('active','=',True)])
            users_group = self.env['res.groups'].search([('name','=','Internal User')])
            ref = self.name
            users.notify_success("Operator Sent Approval To Marketing, Sales Order Approval Number: " +" "+ ref)
            
            if not self.env['mail.channel'].search([('name','=','Sales Approval Notification')]):
                self.env['mail.channel'].create({'name': 'Sales Approval Notification','public':'public', 'group_ids': users_group, 'email_send': True})
            purchase_message= self.env['mail.channel'].search([('name','=','Sales Approval Notification')])

            purchase_message.message_post(
            subject='Operator Sent a Sales Approval',
            body='''Operator Sent a Sales Approval To Marketing, Sales Order Approval Number: ''' +" "+ ref,
            subtype='mail.mt_comment')

        except:
            pass

        return self.write({'state': 'first_approval'})
    
    def first_approval(self):
        try:
            users=self.env['res.users'].search([('active','=',True)])
            ref = self.name
            users.notify_success("Marketing Approved Sales Order, Sales Order Approval Number: " +" "+ ref)

            channel_id = self.env['mail.channel'].search([('name','=','Sales Approval Notification')])

            channel_id.message_post(
            subject='Marketing Approved a Sales Order',
            body='''Marketing Approved Sales Order, Sales Order Approval Number: ''' +" "+ ref,
            subtype='mail.mt_comment')
        
        except:
            pass

        return self.write({'state': 'second_approval'})

    def first_approval_reject(self):
        try:
            users=self.env['res.users'].search([('active','=',True)])
            ref = self.name
            users.notify_info("Marketing Canceled Sales Order, Canceled Sales Order Number: " +" "+ ref)

            channel_id = self.env['mail.channel'].search([('name','=','Sales Approval Notification')])

            channel_id.message_post(
            subject='Marketing Canceled a Sales Order',
            body='''Marketing Canceled Sales Order, Canceled Sales Order Number: ''' +" "+ ref,
            subtype='mail.mt_comment')
        
        except:
            pass

        return self.write({'state': 'cancel'})

    def second_approval(self):
        try:
            users=self.env['res.users'].search([('active','=',True)])
            ref = self.name
            users.notify_success("Production Approved Sales Order, Sales Order Approval Number: " +" "+ ref)

            channel_id = self.env['mail.channel'].search([('name','=','Sales Approval Notification')])

            channel_id.message_post(
            subject='Production Approved a Sales Order',
            body='''Production Approved Sales Order, Sales Order Approval Number: ''' +" "+ ref,
            subtype='mail.mt_comment')
        
        except:
            pass

        return self.write({'state': 'third_approval'})

    def second_approval_reject(self):
        try:
            users=self.env['res.users'].search([('active','=',True)])
            ref = self.name
            users.notify_info("Production Canceled Sales Order, Canceled Sales Order Number: " +" "+ ref)

            channel_id = self.env['mail.channel'].search([('name','=','Sales Approval Notification')])

            channel_id.message_post(
            subject='Production Canceled a Sales Order',
            body='''Production Canceled Sales Order, Canceled Sales Order Number: ''' +" "+ ref,
            subtype='mail.mt_comment')
        
        except:
            pass

        return self.write({'state': 'cancel'})

    def third_approval(self):
        try:
            users=self.env['res.users'].search([('active','=',True)])
            ref = self.name
            users.notify_success("Finance Approved Sales Order, Sales Order Approval Number: " +" "+ ref)

            channel_id = self.env['mail.channel'].search([('name','=','Sales Approval Notification')])

            channel_id.message_post(
            subject='Finance Approved a Sales Order',
            body='''Finance Approved Sales Order, Sales Order Approval Number: ''' +" "+ ref,
            subtype='mail.mt_comment')
        
        except:
            pass

        return self.write({'state': 'fourth_approval'})

    def third_approval_reject(self):
        try:
            users=self.env['res.users'].search([('active','=',True)])
            ref = self.name
            users.notify_info("Finance Canceled Sales Order, Canceled Sales Order Number: " +" "+ ref)

            channel_id = self.env['mail.channel'].search([('name','=','Sales Approval Notification')])

            channel_id.message_post(
            subject='Finance Canceled a Sales Order',
            body='''Finance Canceled Sales Order, Canceled Sales Order Number: ''' +" "+ ref,
            subtype='mail.mt_comment')
        
        except:
            pass

        return self.write({'state': 'cancel'})

    def fourth_approval(self):
        try:
            users=self.env['res.users'].search([('active','=',True)])
            ref = self.name
            users.notify_success("CEO Approved Sales Order, Sales Order Approval Number: " +" "+ ref)

            channel_id = self.env['mail.channel'].search([('name','=','Sales Approval Notification')])

            channel_id.message_post(
            subject='CEO Approved a Sales Order',
            body='''CEO Approved Sales Order, Sales Order Approval Number: ''' +" "+ ref,
            subtype='mail.mt_comment')
        
        except:
            pass

        return self.write({'state': 'to approve'})

    def fourth_approval_reject(self):
        try:
            users=self.env['res.users'].search([('active','=',True)])
            ref = self.name
            users.notify_info("CEO Canceled Sales Order, Canceled Sales Order Number: " +" "+ ref)

            channel_id = self.env['mail.channel'].search([('name','=','Sales Approval Notification')])

            channel_id.message_post(
            subject='CEO Canceled a Sales Order',
            body='''CEO Canceled Sales Order, Canceled Sales Order Number: ''' +" "+ ref,
            subtype='mail.mt_comment')
        
        except:
            pass

        return self.write({'state': 'cancel'})


    
    