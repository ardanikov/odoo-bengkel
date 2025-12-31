from odoo import models, fields, api


class Perbaikan(models.Model):
    _name = 'bengkel.perbaikan'
    _description = 'Perbaikan Mobil'

    name = fields.Char(string='Nama Perbaikan', required=True)
    deskripsi = fields.Text(string='Deskripsi')
    biaya = fields.Float(string='Biaya')
    status = fields.Selection([
        ('baru', 'Baru'),
        ('proses', 'Dalam Proses'),
        ('selesai', 'Selesai'),
    ], string='Status', default='baru')

