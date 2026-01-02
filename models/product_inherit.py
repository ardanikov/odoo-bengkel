from odoo import models, fields, api

class ProductTemplateInherit(models.Model):
    _inherit = 'product.template'

    is_spa_product = fields.Boolean(string='Produk Spa', default=False, help='Tandai produk ini sebagai produk Spa & Salon')

    

    