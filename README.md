# Huawei Charger Home Assistant Integration

This is a custom Home Assistant integration for the Huawei EV Charger.

## Features
- Auto-discovered via Home Assistant Integrations UI
- Reads voltages, current, total power
- Controls:
  - Max charging power (0–22 kW)
  - Charging mode (Off, Paused, Charging)

## Installation
1. Clone or download this repository:
   ```bash
   git clone https://github.com/emavap/huawei_charger.git
   ```

2. Copy the `custom_components/huawei_charger` folder into your Home Assistant config directory:
   ```bash
   cp -r huawei_charger/custom_components/huawei_charger ~/.homeassistant/custom_components/
   ```

3. Restart Home Assistant.

4. In Home Assistant UI:
   - Go to **Settings → Devices & Services**
   - Click **+ Add Integration**
   - Search for **Huawei Charger**
   - Enter IP and port of your charger

## Configuration Options
- **IP address**: IP of the Huawei charger (default: `192.168.5.118`)
- **Port**: TCP port (default: `502`)

## Development Roadmap
- Replace placeholders with real TCP register communication
- Add polling interval setting
- Add diagnostics & logs panel

## License
MIT