"""
Top administrative layer of a country

We treat Odoo's `res.country.state` as a "Region" the top level administrative layer.
This file only extends it with a reference to Regional Units, 2nd-level administrative divisions.
"""
from odoo import fields, models, _


class ResCountryState(models.Model):
    """Region (1st-level administrative division) using core `res.country.state`."""

    _inherit = "res.country.state"

    name = fields.Char(
        string=_("Region Name"), required=True, index=True, translate=True,
        help=_("Top-level administrative areas for a country.  E.g. Fed. State, Departement, Canton")
    )
    code = fields.Char(
        string=_("Region Code"), required=True,
        help=_("Short code for the Region.")
    )
    regional_unit_ids = fields.One2many(
        comodel_name="region.unit",
        inverse_name="region_id",
        string=_("Regional Units"),
        help=_("Regional Units that belong to this Region."),
    )
