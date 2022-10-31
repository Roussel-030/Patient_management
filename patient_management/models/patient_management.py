# -*- coding: utf-8 -*-

from odoo import api, models, fields, _

class PatientManagement(models.Model):
     _inherit = ['mail.thread', 'mail.activity.mixin']
     _name = 'patient.management'
     _description = 'module patient management'

     name = fields.Char(compute='_compute_name',string="Nom complet")
     firstname = fields.Char(string="Prénom")
     lastname = fields.Char(string="Nom")
     age = fields.Integer(string="Age", track_visibility="always")
     state = fields.Selection([('new','Nouveau'),('consult','Consulter'),('treaty','Traité'),('cancelled','Annulé')],
                              default='new')

     # STATE
     def set_consult(self):
          self.state = 'consult'
     def set_treaty(self):
          self.state = 'treaty'
     def set_cancelled(self):
          self.state = 'cancelled'
     def set_renew(self):
          self.state = 'new'

     # WIZARD
     def open_wizard(self):
          return {
               'name': _('Test Window Action'),
               'view_mode': 'form',
               'res_model': 'patient.popup',
               'type': 'ir.actions.act_window',
               'target': 'new'
          }

     @api.depends('firstname','lastname')
     def _compute_name(self):
          for record in self:
               record.name = record.firstname+" "+record.lastname if record.lastname != False else record.firstname