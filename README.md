# Monoprice Select Mini V2 - Home Assistant Integration

This repository contains the configuration and scripts to integrate the Monoprice Select Mini V2 3D printer with Home Assistant.

## Features

- Monitor printer status
- Control printer remotely

## Requirements

- Home Assistant
- Monoprice Select Mini V2 3D printer

<!-- ha-marketplace:exclude-start -->
## Installation (Marketplace) - Recommended
[![Open your Home Assistant instance and open a repository in the Marketplace.](https://my.home-assistant.io/badges/marketplace_repository.svg)](https://my.home-assistant.io/redirect/marketplace_repository/?owner=danielhelmstedt&repository=ha-monoprice-select-mini-v2&category=Integration)

1. Add `https://github.com/danielhelmstedt/ha-monoprice-select-mini-v2` to Marketplace as a
   [custom repository](https://next.home-assistant.io/integrations/marketplace/#custom-repositories).
2. In Marketplace, find **Monoprice Select Mini V2** and click **Install**.
3. Complete the setup flow. 

## Installation (Manual)

1. Download this repository as a ZIP and unzip the archive.
2. Copy `custom_components/mp_select_mini_v2` into
   `/config/custom_components/mp_select_mini_v2`.
   - Create the `custom_components` folder if it does not exist.
3. Restart Home Assistant.
4. Go to **Settings → Devices & services → Add integration**, search for
   **Monoprice Select Mini V2**, and complete setup.
<!-- ha-marketplace:exclude-end -->

## Configuration

Use the Home Assistant UI to configure the integration via the config flow.


