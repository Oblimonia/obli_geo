{
    "name": "Obli Geo",
    "summary": "Geospatial utilities for Odoo (Oblimonia)",
    "version": "17.0.1.0.0",
    "category": "Tools",
    "author": "Oblimonia",
    "website": "https://github.com/oblimonia/obli_geo",
    "license": "",
    "depends": ["base", "base_address_extended",  "contacts"],
    "data": [
        "security/ir.model.access.csv",
        "data/res.country.state.csv",
        "data/region.unit.csv",
        # "data/region.municipality.csv",

        "views/country_views.xml",
        "views/region_views.xml",
        "views/regional_unit_views.xml",
        "views/municipality_views.xml",
        "views/city_views.xml",
    ],
    "application": True,
    "installable": True,
}
