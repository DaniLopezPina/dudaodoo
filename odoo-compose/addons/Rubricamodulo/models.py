from odoo import models, fields

class Empresa(models.Model):
    _name = 'fct.empresa'
    name = fields.Char(string="Empresa", required=True)
    description = fields.Text()
    alumno_ids = fields.One2many(
        'fct.alumno', string="Alumno")

class Alumno(models.Model):
    _name = 'fct.alumno'
    name = fields.Char(string="Alumno", required=True)
    start_date = fields.Date()
    empresa_id = fields.Many2one('fct.empresa',
         string="Empresa Asociada")
 
   