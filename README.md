# Video Device Reconnection Script

This Python script allows for the continuous capture of frames from a video device connected to a Linux based SBC, with automatic reconnection functionality in case of disconnection.

## Overview

The script dynamically searches for available video devices and attempts to reconnect to the video device if it gets disconnected due to vibrations or other reasons. It provides a robust solution for uninterrupted frame capture, ensuring smooth operation even in challenging environments.

## Features

- Dynamic device detection: Searches for all available video devices.
- Automatic reconnection: Attempts to reconnect to the video device if it gets disconnected.
- Error handling: Provides error messages for easier debugging and troubleshooting.

## Usage

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/ArsalanKhan22/Capture-Card-Reconnection.git
