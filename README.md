# Computer Vision - Day 1

Twenty-five beginner-friendly Python and OpenCV exercises covering image
loading, pixel operations, image representation, sampling, quantization, and
basic geometric transformations.

Repository: <https://github.com/Gauravmy/COMPUTER-VISION-01>

## Getting started

From the repository root, create a virtual environment and install the
dependencies:

### Windows PowerShell

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

### macOS/Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Run any exercise from the repository root:

```bash
python day1/q03_dimensions.py
```

The scripts read `images/input.jpg` and write generated images to `outputs/`.
Replace the sample image with your own image using the same filename, or edit
the input path in the exercise you want to run.

## Structure

```
COMPUTER-VISION-01/
├── README.md
├── requirements.txt
├── images/
│   └── input.jpg          # sample test image used by the scripts
├── outputs/                # generated results (created when scripts run)
└── day1/
    ├── _display_helper.py  # shared helper (safe cv2.imshow wrapper)
    ├── q01_read_display.py
    ├── q02_check_loaded.py
    ├── ...
    └── q25_rotate_90.py
```

  `images/input.jpg` is a small sample image included so the exercises can be
  run immediately. The checked-in files in `outputs/` show example results from
  the exercises. New Python cache files and virtual environments are ignored by
  Git.

## Question list

| # | Topic | Script |
|---|-------|--------|
| 1 | Read & display an image | `q01_read_display.py` |
| 2 | Check image loaded successfully | `q02_check_loaded.py` |
| 3 | Print height, width, channels | `q03_dimensions.py` |
| 4 | Total pixel count | `q04_total_pixels.py` |
| 5 | Print image dtype | `q05_dtype.py` |
| 6 | Read & save with new filename | `q06_read_save_new_name.py` |
| 7 | Read directly in grayscale | `q07_read_grayscale.py` |
| 8 | Convert color to grayscale (`cvtColor`) | `q08_bgr_to_gray.py` |
| 9 | Display with Matplotlib, hide axis | `q09_matplotlib_no_axis.py` |
| 10 | Resize to 50% | `q10_resize_half.py` |
| 11 | Access pixel value at (x, y) | `q11_pixel_value.py` |
| 12 | Modify a pixel & save | `q12_modify_pixel.py` |
| 13 | Print B, G, R of a pixel | `q13_bgr_values.py` |
| 14 | Split channels & display each | `q14_split_channels.py` |
| 15 | Merge channels back together | `q15_merge_channels.py` |
| 16 | Min/max intensity of grayscale image | `q16_min_max_intensity.py` |
| 17 | Mean intensity | `q17_mean_intensity.py` |
| 18 | Mean and standard deviation | `q18_mean_std.py` |
| 19 | Create flat 256×256 gray (128) image | `q19_flat_gray_image.py` |
| 20 | Create 0→255 intensity ramp | `q20_intensity_ramp.py` |
| 21 | Quantize 8-bit → 4-bit | `q21_quantize_4bit.py` |
| 22 | Quantize 8-bit → 2-bit | `q22_quantize_2bit.py` |
| 23 | Downsample by factor of 2 | `q23_downsample.py` |
| 24 | Crop a rectangular ROI | `q24_crop_roi.py` |
| 25 | Rotate 90° & save | `q25_rotate_90.py` |

## Run all exercises

macOS/Linux:

```bash
for f in day1/q*.py; do python "$f"; done
```

Windows PowerShell:

```powershell
Get-ChildItem day1/q*.py | ForEach-Object { python $_.FullName }
```

Each script:
- Reads `images/input.jpg` by default (swap in your own image if you like).
- Prints its results to the console.
- Saves any generated/annotated image into `outputs/`.
- Calls `cv2.imshow()` to pop up a window **when a display is available**
  (your own PC). On headless machines (servers/CI) it automatically
  skips the popup and just saves the result, so nothing crashes.

## Notes

- `images/input.jpg` is a synthetic sample scene (sky/house/sun)
  generated with OpenCV/NumPy so every script can be run and verified
  immediately without needing an external file. Feel free to replace it
  with any real photo — just keep the filename, or update the `path`
  variable at the top of each script.
- Every script includes a docstring with: approach/logic, the code
  itself, and a note on the important OpenCV/NumPy functions used, per
  the assignment checklist.
