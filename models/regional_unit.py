"""
2nd-level administrative division below Region (`res.country.state`) and above Municipality.
"""
from odoo import fields, models, _


class RegionalUnit(models.Model):
    """Regional Unit (below Region, above Municipality)."""

    _name = "region.unit"
    _description = "Regional Unit (2nd-level administrative division)"
    _order = "region_id, code, name"

    name = fields.Char(
        string=_("Regional Unit"), required=True, translate=True, index=True,
        help=_("Human-readable name. Must be unique within the Region.")
    )
    code = fields.Char(
        string=_("Code"), required=True, index=True,
        help=_("Short code. Must be unique within the Region."),
    )
    region_id = fields.Many2one(
        comodel_name="res.country.state",
        string=_("Region"), required=True, index=True, ondelete="restrict",
        help=_("Parent Region."),
    )
    country_id = fields.Many2one(
        comodel_name="res.country", related="region_id.country_id",
        string=_("Country"), store=True, readonly=True,
        help=_("Country of the parent Region (related).")
    )
    municipality_ids = fields.One2many(
        comodel_name="region.municipality", inverse_name="regional_unit_id",
        string=_("Municipalities"),
        help=_("Municipalities that belong to this Regional Unit.")
    )

    _sql_constraints = [
        (
            "ru_code_unique_region", "unique(region_id, code)",
            "Regional Unit code must be unique within the Region."
        ),
        (
            "ru_name_unique_region", "unique(region_id, name)",
            "Regional Unit name must be unique within the Region.")
    ]
