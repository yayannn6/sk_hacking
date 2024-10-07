# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    @api.ondelete(at_uninstall=False)
    def _unlink_except_confirmed(self):
        # Override fungsi ini untuk menonaktifkan pembatasan penghapusan
        pass  # Tidak ada logika yang menimbulkan UserError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()
        for order in self:
            for line in order.order_line:
                line.product_updatable = True
        return res
