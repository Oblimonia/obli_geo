# Obli Geo

> Greek administrative geography for Odoo: Regions, Regional Units & Municipalities — with `res.city` integration.

![Odoo Version](https://img.shields.io/badge/odoo-17.0%20%7C%2018.0-blue)
![License: LGPL-3](https://img.shields.io/badge/license-LGPL--3-green)

---

## Overview

**Obli Geo** adds 3-level administrative hierarchy to Odoo and links it to contacts/addresses.
It introduces **Regions**, **Regional Units**, and **Municipalities** and extends Odoo's `res.city` so each city can be attached to its Municipality and Regional Unit.

> ℹ️ *City dataset is **not** included.* The module only extends the `res.city` model and views, so you can link cities to Municipalities; you can import your own cities with zip codes later.

---

## Features

- **Data included** (Greece):
  - **13** Regions (`res.country.state`)
  - **74** Regional Units (`region.unit`)
  - **332** Municipalities (`region.municipality`)
- `res.city` enhancement:
  - `municipality_id` (M2O) with country/region-aware domain
  - `regional_unit_id` and `state_id` (related, stored) for consistent hierarchy
- Smart, restrictive domains and `ondelete="restrict"` to protect data integrity

---

## Installation

1. Copy this module into your Odoo `addons` path.
2. Update the app list and install **Obli Geo** from Apps.

---

## License

Licensed under **LGPL-3**. See [LICENSE](./LICENSE).

---

## Author

**Oblimonia**, 2025
