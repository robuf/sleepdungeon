## How to build this game for Windows?

### Installing PyInstaller

Install PyInstaller on your system:

```
python -m pip install pyinstaller
```

### Create the .spec file

Execute the following command to create the initial .spec file for the game:

```
pyinstaller.exe --onefile --windowed --noconsole --icon .\sleepdungeon.ico --additional-hooks-dir .\pyinstaller_hooks .\bin\sleepdungeon
```

### Build it.

Simply run

```
pyinstaller.exe .\sleepdungeon.spec
```
