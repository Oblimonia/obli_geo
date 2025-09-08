{
    "name": "Obli Geo",
    "summary": "Administrative geography for Odoo: Regions, Regional Units, Municipalities, and Cities.",
    "description": """
    This module provides complete 3 level administrative geography, integrated into Odoo's contact/address system.
    """,
    "version": "1.0",
    "category": "Localization",
    "author": "Oblimonia",
    "website": "https://github.com/Oblimonia/obli_geo",
    "license": "LGPL-3",
    "depends": ["base", "contacts", "base_address_extended"],
    "data": [
        "security/ir.model.access.csv",
        "data/res.country.state.csv",
        "data/region.unit.csv",
        "data/region.municipality.csv",
        "views/country_views.xml",
        "views/region_views.xml",
        "views/regional_unit_views.xml",
        "views/municipality_views.xml",
        "views/city_views.xml",
    ],
    "images": [
        "static/description/icon.png",
    ],
    "application": False,
    "installable": True,
}
