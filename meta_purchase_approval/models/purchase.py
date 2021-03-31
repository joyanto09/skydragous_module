# -*- coding: utf-8 -*-
from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.exceptions import UserError
from odoo.tools import float_is_zero, float_compare, DEFAULT_SERVER_DATETIME_FORMAT

class PurchaseOrder(models.Model):
    
    _inherit = 'purchase.order'


    state = fields.Selection([
        ('draft', 'Quotation'),
        ('sent', 'RFQ Sent'),
        ('first_approval', 'Internal Audit'),
        ('second_approval', 'External Audit'),
        ('third_approval', 'Purchase Committee'),
        ('fourth_approval', 'CEO'),
        ('to approve', 'Approved'),
        ('purchase', 'Purchase Order'),
        ('done', 'Locked'),
        ('cancel', 'Cancelled')
    ], string='Status', readonly=True, index=True, copy=False, default='draft', tracking=True)


    def operation_send_approve(self):
        
        try:
            users=self.env['res.users'].search([('active','=',True)])
            users_group = self.env['res.groups'].search([('name','=','Internal User')])
            ref = self.name
            users.notify_success("Operator Sent Approval To Internal Audit, Purchase Order Approval Number: " +" "+ ref)
            
            if not self.env['mail.channel'].search([('name','=','Purchase Approval Notification')]):
                self.env['mail.channel'].create({'name': 'Purchase Approval Notification','public':'public', 'group_ids': users_group, 'email_send': True})
            purchase_message= self.env['mail.channel'].search([('name','=','Purchase Approval Notification')])

            purchase_message.message_post(
            subject='Operator Sent a Purchase Approval',
            body='''Operator Sent a Purchase Approval To Internal Audit, Purchase Order Approval Number: ''' +" "+ ref,
            subtype='mail.mt_comment')

        except:
            pass

        return self.write({'state': 'first_approval'})
    # def operation_send_approve(self):
    #     return self.write({'state': 'first_approval'})
    

    def first_approval(self):
        
        try:
            users=self.env['res.users'].search([('active','=',True)])
            ref = self.name
            users.notify_success("Internal Audit Approved, Purchase Order Approval Number: " +" "+ ref)

            channel_id = self.env['mail.channel'].search([('name','=','Purchase Approval Notification')])

            channel_id.message_post(
            subject='Internal Audit Approved a Purchase Order',
            body='''Internal Audit Approved Purchase Order, Purchase Order Approval Number: ''' +" "+ ref,
            subtype='mail.mt_comment')
        
        except:
            pass

        return self.write({'state': 'second_approval'})
    # def first_approval(self):
    #     return self.write({'state': 'second_approval'})
    
    def first_approval_reject(self):
        try:
            users=self.env['res.users'].search([('active','=',True)])
            ref = self.name
            users.notify_info("Internal Audit Canceled, Canceled Purchase Order Number: " +" "+ ref)

            channel_id = self.env['mail.channel'].search([('name','=','Purchase Approval Notification')])

            channel_id.message_post(
            subject='Internal Audit Canceled a Purchase Order',
            body='''Internal Audit Canceled Purchase Order, Canceled Purchase Order Number: ''' +" "+ ref,
            subtype='mail.mt_comment')
        
        except:
            pass

        return self.write({'state': 'cancel'})
    
    def second_approval(self):
        try:
            users=self.env['res.users'].search([('active','=',True)])
            ref = self.name
            users.notify_success("External Audit Approved, Purchase Order Approval Number: " +" "+ ref)

            channel_id = self.env['mail.channel'].search([('name','=','Purchase Approval Notification')])

            channel_id.message_post(
            subject='External Audit Approved a Purchase Order',
            body='''External Audit Approved Purchase Order, Purchase Order Approval Number: ''' +" "+ ref,
            subtype='mail.mt_comment')

        except:
            pass

        return self.write({'state': 'third_approval'})
    # def second_approval(self):
    #     return self.write({'state': 'third_approval'})
    
    def second_approval_reject(self):
        try:
            users=self.env['res.users'].search([('active','=',True)])
            ref = self.name
            users.notify_info("External Audit Canceled Purchase Order, Canceled Purchase Order Number: " +" "+ ref)

            channel_id = self.env['mail.channel'].search([('name','=','Purchase Approval Notification')])

            channel_id.message_post(
            subject='External Audit Canceled a Purchase Order',
            body='''External Audit Canceled Purchase Order, Canceled Purchase Order Number: ''' +" "+ ref,
            subtype='mail.mt_comment')
        
        except:
            pass

        return self.write({'state': 'cancel'})
    
    def third_approval(self):
        try:
            users=self.env['res.users'].search([('active','=',True)])
            ref = self.name
            users.notify_success("Purchase Committee Approved, Purchase Order Approval Number: " +" "+ ref)

            channel_id = self.env['mail.channel'].search([('name','=','Purchase Approval Notification')])

            channel_id.message_post(
            subject='Purchase Committee Approved a Purchase Order',
            body='''Purchase Committee Approved Purchase Order, Purchase Order Approval Number: ''' +" "+ ref,
            subtype='mail.mt_comment')
        except:
            pass

        return self.write({'state': 'fourth_approval'})
    # def third_approval(self):
    #     return self.write({'state': 'fourth_approval'})
    
    def third_approval_reject(self):
        try:
            users=self.env['res.users'].search([('active','=',True)])
            ref = self.name
            users.notify_info("Purchase Committee Canceled Purchase Order, Canceled Purchase Order Number: " +" "+ ref)

            channel_id = self.env['mail.channel'].search([('name','=','Purchase Approval Notification')])

            channel_id.message_post(
            subject='Purchase Committee Canceled a Purchase Order',
            body='''Purchase Committee Canceled Purchase Order, Canceled Purchase Order Number: ''' +" "+ ref,
            subtype='mail.mt_comment')
        
        except:
            pass

        return self.write({'state': 'cancel'})
    
    def fourth_approval(self):
        try:
            users=self.env['res.users'].search([('active','=',True)])
            ref = self.name
            users.notify_success("CEO Approved, Purchase Order Approval Number: " +" "+ ref)

            channel_id = self.env['mail.channel'].search([('name','=','Purchase Approval Notification')])

            channel_id.message_post(
            subject='CEO Approved a Purchase Order',
            body='''CEO Approved Purchase Order, Purchase Order Approval Number: ''' +" "+ ref,
            subtype='mail.mt_comment')
        
        except:
            pass

        return self.write({'state': 'to approve'})
    # def fourth_approval(self):
    #     return self.write({'state': 'to approve'})
    
    def fourth_approval_reject(self):
        try:
            users=self.env['res.users'].search([('active','=',True)])
            ref = self.name
            users.notify_info("CEO Canceled Purchase Order, Canceled Purchase Order Number: " +" "+ ref)

            channel_id = self.env['mail.channel'].search([('name','=','Purchase Approval Notification')])

            channel_id.message_post(
            subject='CEO Canceled a Purchase Order',
            body='''CEO Canceled Purchase Order, Canceled Purchase Order Number: ''' +" "+ ref,
            subtype='mail.mt_comment')
        
        except:
            pass

        return self.write({'state': 'cancel'})
    
    def button_confirm(self):

        for order in self:
            if order.state not in ['draft', 'sent', 'to approve',]:
                continue
            order._add_supplier_to_product()
            # Deal with double validation process
            if order.company_id.po_double_validation == 'one_step'\
                    or (order.company_id.po_double_validation == 'two_step'\
                        and order.amount_total < self.env.company.currency_id._convert(
                            order.company_id.po_double_validation_amount, order.currency_id, order.company_id, order.date_order or fields.Date.today()))\
                    or order.user_has_groups('purchase.group_purchase_manager'):
                order.button_approve()
            else:
                order.write({'state': 'to approve'})
        return True


    

       
    
        
    