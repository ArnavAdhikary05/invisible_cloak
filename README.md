# Invisible Cloak

A Python project that uses computer vision to create an invisible cloak effect by detecting and removing a colored cloth from video.

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
