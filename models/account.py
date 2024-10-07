from odoo import models, api, fields
from odoo.exceptions import UserError

class AccountMoveLine(models.Model):
    _inherit = 'account.move'

    new_state = fields.Selection([('draft', 'Draft'), ('posted', 'Posted'), ('cancel', 'Cancelled')], default='draft', string='State')

    def action_post(self):
        res = super(AccountMoveLine, self).action_post()
        self.write({'state': 'draft', 'new_state': 'posted'})
        return res
        
    def button_draft(self):
        res = super(AccountMoveLine, self).button_draft()
        self.write({'state': 'draft', 'new_state': 'draft'})
        return res
    
    def button_cancel(self):
        res = super(AccountMoveLine, self).button_cancel()
        self.write({'state': 'cancel', 'new_state': 'cancel'})
        return res