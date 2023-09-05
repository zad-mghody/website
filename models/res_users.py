from odoo import models, fields, api


class ResUsers(models.Model):
    _inherit = 'res.users'

    phone_number = fields.Char('Phone Number', store=True)
