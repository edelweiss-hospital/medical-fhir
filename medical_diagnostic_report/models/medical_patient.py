# Copyright 2021 CreuBlanca
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class MedicalPatient(models.Model):

    _inherit = "medical.patient"

    diagnostic_report_ids = fields.One2many(
        "medical.diagnostic.report", inverse_name="patient_id"
    )

    def action_view_observations_with_concept(self):
        self.ensure_one()
        action = self.env.ref(
            "medical_diagnostic_report."
            "medical_diagnostic_report_concepts_patient_act_window"
        ).read()[0]
        action["domain"] = [
            ("patient_id", "=", self.id),
            ("concept_id", "!=", False),
            ("state", "=", "final"),
        ]
        return action
