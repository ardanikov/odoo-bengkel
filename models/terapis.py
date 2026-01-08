from odoo import models, fields, api

class CdnTerapis(models.Model):
    _name = 'cdn.terapis'
    _description = 'Terapis'
    _inherits = {'res.partner': 'partner_id'}

    partner_id = fields.Many2one('res.partner', string='Partner', required=True, ondelete='cascade')

    kode = fields.Char(string='Kode Terapis', readonly=True, copy=False, default='New')
    
    # Field res.partner yang akan otomatis tersedia: name, phone, email, etc.
    # Kita gunakan jenis_kelamin dari res.partner (yang sudah di-inherit di res_partner_inherit.py)
    
    spesialis_ids = fields.Many2many(
        'cdn.spesialis',
        'cdn_terapis_spesialis_rel',
        'terapis_id',
        'spesialis_id',
        string='Spesialis'
    )
    
    @api.model
    def create(self, vals):
        if vals.get('kode', 'New') == 'New':
            vals['kode'] = self.env['ir.sequence'].next_by_code(
                'cdn.terapis'
            ) or 'New'
        
        # Set otomatis flag is_terapis di res.partner
        vals['is_terapis'] = True
        return super(CdnTerapis, self).create(vals)