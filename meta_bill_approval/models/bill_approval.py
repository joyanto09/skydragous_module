# -*- coding: utf-8 -*-
from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.exceptions import UserError
from odoo.tools import float_is_zero, float_compare, DEFAULT_SERVER_DATETIME_FORMAT

class BillApproval(models.Model):
    
    _inherit = 'account.move'
    
    state = fields.Selection(selection=[
        ('draft', 'Draft'),
        ('first_approval', 'Accounting'),
        ('second_approval', 'Finance'),
        ('third_approval', 'CEO'),
        ('to approve', 'Approved'),
        ('posted', 'Posted'),
        ('cancel', 'Cancelled')
        ], string='Status', required=True, readonly=True, copy=False, tracking=True, default='draft')

    journal_blank = fields.Boolean(string="Journal Blank", default=True)
       
    
    def bill_operation_send_approval(self):
        try:
            users=self.env['res.users'].search([('active','=',True)])
            users_group = self.env['res.groups'].search([('name','=','Internal User')])
            # ref = self.name
            
            users.notify_success("Operator Sent a Journal Approval To Accounting")
            
            if not self.env['mail.channel'].search([('name','=','Journal Approval Notification')]):
                self.env['mail.channel'].create({'name': 'Journal Approval Notification','public':'public', 'group_ids': users_group, 'email_send': True})
            payments_message= self.env['mail.channel'].search([('name','=','Journal Approval Notification')])

            payments_message.message_post(
            subject='Operator Sent a Journal Approval',
            body='''Operator Sent a Journal Approval To Accounting''',
            subtype='mail.mt_comment')
        
        except:
            pass

        return self.write({'state': 'first_approval'})
        
    def first_approval(self):
        try:
            users=self.env['res.users'].search([('active','=',True)])
            # ref = self.name
            users.notify_success("Accounting Approved a Journal Bill")

            channel_id = self.env['mail.channel'].search([('name','=','Journal Approval Notification')])

            channel_id.message_post(
            subject='Accounting Approved a Journal',
            body='''Accounting Approved a Journal Bill & Approval Sent To Head of Finance ''',
            subtype='mail.mt_comment')
        
        except:
            pass

        return self.write({'state': 'second_approval'})
    
    def first_approval_reject(self):
        try:
            users=self.env['res.users'].search([('active','=',True)])
            # ref = self.name
            users.notify_info("Manager Canceled a Journal Bill")

            channel_id = self.env['mail.channel'].search([('name','=','Journal Approval Notification')])

            channel_id.message_post(
            subject='Accounting Canceled a Journal',
            body='''Accounting Canceled a Journal Bill''',
            subtype='mail.mt_comment')
        
        except:
            pass

        return self.write({'state': 'cancel'})
    
    def second_approval(self):
        try:
            users=self.env['res.users'].search([('active','=',True)])
            # ref = self.name
            users.notify_success("Finance Approved a Journal Bill ")

            channel_id = self.env['mail.channel'].search([('name','=','Journal Approval Notification')])

            channel_id.message_post(
            subject='Finance Approved a Journal',
            body='''Finance Approved a Journal Bill & Approval Sent To CEO ''',
            subtype='mail.mt_comment')
        
        except:
            pass

        return self.write({'state': 'third_approval'})
    
    def second_approval_reject(self):
        try:
            users=self.env['res.users'].search([('active','=',True)])
            # ref = self.name
            users.notify_info("Head of Finance Canceled a Journal Bill ")

            channel_id = self.env['mail.channel'].search([('name','=','Journal Approval Notification')])

            channel_id.message_post(
            subject='Finance Canceled a Journal',
            body='''Finance Canceled a Journal Bill''',
            subtype='mail.mt_comment')
        
        except:
            pass

        return self.write({'state': 'cancel'})
    
    def third_approval(self):
        try:
            users=self.env['res.users'].search([('active','=',True)])
            # ref = self.name
            users.notify_success("CEO Approved a Journal Bill ")

            channel_id = self.env['mail.channel'].search([('name','=','Journal Approval Notification')])

            channel_id.message_post(
            subject='CEO Approved a Journal',
            body='''CEO Approved a Journal Bill & Now a Journal Bill Approved ''',
            subtype='mail.mt_comment')
        
        except:
            pass

        return self.write({'state': 'to approve'})
    
    def third_approval_reject(self):
        try:
            users=self.env['res.users'].search([('active','=',True)])
            # ref = self.name
            users.notify_info("CEO Canceled a Journal Bill")

            channel_id = self.env['mail.channel'].search([('name','=','Journal Approval Notification')])

            channel_id.message_post(
            subject='CEO Canceled a Journal',
            body='''CEO Canceled a Journal Bill''',
            subtype='mail.mt_comment')
        
        except:
            pass

        return self.write({'state': 'cancel'})

    # @api.onchange('journal_blank')
    # def journal_blank_show(self):
    #
    #     if self.journal_blank == True:
    #         self.journal_id = False
    #
    #     else:
    #         self.journal_id = True
    
    
    
    
    
    
         