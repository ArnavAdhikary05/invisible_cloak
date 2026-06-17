# Invisible Cloak

A Python project that uses computer vision and color detection to create an invisible cloak effect. By capturing the HSV color values of a cloth and applying real-time background substitution, this project makes the cloth appear invisible in video footage, revealing whatever is behind it.

## How It Works

The invisible cloak effect is achieved through HSV (Hue, Saturation, Value) color space detection:
1. **Color Capture** - Records the exact color range of your cloth
2. **Real-time Detection** - Identifies pixels matching that color in the video stream
3. **Background Replacement** - Replaces detected pixels with the background, making the cloth invisible

## Workflow

### Step 1: Capture Cloth Color
1. Run `capture_color.py`
2. Hold cloth in box
3. Press **C** to capture
4. HSV color values are saved to `cloak_color.txt`

### Step 2: Run Invisible Cloak
1. Run `invisible_cloak.py`
2. Program loads HSV values from file
3. Cloth becomes invisible in the video feed

## Files

- `capture_color.py` - Captures and records the HSV color of the cloth
- `invisible_cloak.py` - Main program that makes the cloth invisible
- `cloak_color.txt` - Stores the HSV color data
- `requirements.txt` - Project dependencies
- `pyproject.toml` - Project configuration

## Requirements

See `requirements.txt` for dependencies.

## Usage

Follow the workflow steps above to capture your cloth's color and then run the invisible cloak effect.
