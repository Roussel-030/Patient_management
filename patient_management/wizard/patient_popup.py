from odoo import fields, models
import datetime

class PatientPopup(models.TransientModel):
    _name = 'patient.popup'
    _rec_name = 'birthday'

    birthday = fields.Date(string='Birthday')

    def update_birthday(self):
        year_birth_patient = self.birthday.year
        year_now = datetime.date.today().year
        patient_management = self.env['patient.management']
        active_id = self.env.context.get('active_id')
        patient_management_id =patient_management.browse(active_id)
        patient_management_id.age = year_now-year_birth_patient

