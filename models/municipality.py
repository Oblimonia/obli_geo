"""
3rd-level administrative division below Regional Unit and above City.
"""
from odoo import fields, models, _


class ResRegionMunicipality(models.Model):
    """Municipality (below Regional Unit, above City)."""

    _name = "region.municipality"
    _description = "Municipality"
    _order = "regional_unit_id, code, name"

    name = fields.Char(
        string=_("Municipality"), required=True, translate=True, index=True,
        help=_("Municipality name. Must be unique within the Regional Unit.")
    )
    code = fields.Char(
        string=_("Code"), required=True, index=True,
        help=_("Short code. Must be unique within the Regional Unit.")
    )
    regional_unit_id = fields.Many2one(
        comodel_name="region.unit",
        string=_("Regional Unit"), required=True, index=True, ondelete="restrict",
        help=_("Parent Regional Unit.")
    )
    region_id = fields.Many2one(
        comodel_name="res.country.state", related="regional_unit_id.region_id",
        string=_("Region"), store=True, readonly=True, index=True,
        help=_("Region of the parent Regional Unit (related).")
    )
    country_id = fields.Many2one(
        comodel_name="res.country", related="regional_unit_id.country_id",
        string=_("Country"), store=True, readonly=True, index=True,
        help=_("Country of the parent Regional Unit (related).")
    )
    city_ids = fields.One2many(
        comodel_name="res.city"
    )
    city_ids = fields.One2many(
        comodel_name="res.city", inverse_name="municipality_id",
        string=_("Cities"),
        help=_("Cities that belong to this Municipality."),
    )

    _sql_constraints = [
        (
            "mun_code_unique_ru", "unique(regional_unit_id, code)",
            "Municipality code must be unique within the Regional Unit.",
        ),
        (
            "mun_name_unique_ru", "unique(regional_unit_id, name)",
            "Municipality name must be unique within the Regional Unit.",
        ),
    ]

