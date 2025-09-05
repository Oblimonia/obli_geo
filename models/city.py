"""
Extend `res.city` to link each City to a Municipality
without breaking Odoo's standard behavior.
"""
from odoo import fields, models, _


class ResCity(models.Model):
    _inherit = "res.city"

    municipality_id = fields.Many2one(
        comodel_name="region.municipality",
        string=_("Municipality"), index=True, ondelete="restrict",
        domain="[('region_id', '=', state_id), ('country_id', '=', country_id)]",
        help=_("Municipality of this City.")
    )
    regional_unit_id = fields.Many2one(
        comodel_name="region.unit",  related="municipality_id.regional_unit_id",
        string=_("Regional Unit"), store=True, readonly=True, index=True,
        help=_("Regional Unit of the parent Municipality (related).")
    )
    region_id = fields.Many2one(
        comodel_name="res.country.state", related="municipality_id.region_id",
        string=_("Region"), store=True, readonly=True, index=True,
        help=_("Region of the parent Municipality (related).")
    )
