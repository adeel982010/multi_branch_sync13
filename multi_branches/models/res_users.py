# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _


class Users(models.Model):
    _inherit = 'res.users'

    branch_id = fields.Many2one("res.branch", string='Current Branch', default=lambda self: self.env.user.branch_id)
    branch_ids = fields.Many2many('res.branch', string='Allowed Branches', default=lambda self: self.env.user.branch_id)

    @api.onchange('company_ids')
    def _onchange_company_ids(self):
        if self.company_ids:
            self.branch_ids = self.env['res.branch'].search([('company_id', 'in', self.company_ids.ids)]) or False
            return {'domain': {'branch_ids': [('company_id', 'in', self.company_ids.ids)]}}
        else:
            self.branch_ids = False
            return {'domain': {'branch_ids': []}}
