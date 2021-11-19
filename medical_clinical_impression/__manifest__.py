# Copyright 2021 Creu Blanca
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Medical Clinical Impression",
    "summary": """
        Medical Clinical Impression based on FHIR""",
    "version": "13.0.1.0.0",
    "license": "AGPL-3",
    "author": "Creu Blanca,Odoo Community Association (OCA)",
    "website": "www.creublanca.es",
    "depends": [
        "medical_workflow",
        "medical_clinical",
        "medical_clinical_condition",
        "medical_administration_practitioner_specialty",
    ],
    "data": [
        "views/assets.xml",
        "security/medical_security.xml",
        "security/ir.model.access.csv",
        "data/ir_sequence_data.xml",
        "wizards/create_impression_from_patient.xml",
        "views/medical_clinical_investigation.xml",
        "views/medical_clinical_impression.xml",
        "views/medical_encounter.xml",
        "views/medical_patient.xml",
        "views/medical_clinical_finding.xml",
        "views/medical_family_member_history.xml",
    ],
    "qweb": ["static/src/xml/widget_warning_dropdown.xml"],
    "demo": [],
}
