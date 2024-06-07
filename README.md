# Capture Card Reconnection Script

This Python script allows for the continuous capture of frames from a capture card connected to a Raspberry Pi, with automatic reconnection functionality in case of disconnection.

## Overview

The script dynamically searches for available capture devices and attempts to reconnect to the capture card if it gets disconnected due to vibrations or other reasons. It provides a robust solution for uninterrupted frame capture, ensuring smooth operation even in challenging environments.

## Features

- Dynamic device detection: Searches for all available capture devices.
- Automatic reconnection: Attempts to reconnect to the capture card if it gets disconnected.
- Error handling: Provides error messages for easier debugging and troubleshooting.

## Usage

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/ArsalanKhan22/Capture-Card-Reconnection.git
