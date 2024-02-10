# AutoRunScript
This script uses directx scan codes to hold W+SHIFT for you if there isn't an option to toggle running in a game.

## Usage
Just run it and press the toggle key.

The script will hold W and SHIFT until the toggle key is pressed again.

## Running it
### auto_run.exe
You can download .exe file in the **releases** tab.

### Python
Install dependencies with:
```
python -m pip install -r requirements.txt
```

And run it with:
```
python auto_run.py
```

## settings.ini
[settings.ini](settings.ini) file is used to set the toggle key.

If it's missing from the working directory or the toggle_key variable is set incorrectely, toggle key will default to "="
