## How to build this game for Mac OSX?

### Installing PyInstaller

Install PyInstaller on your system:

```
pip3 install pyinstaller
```

### Create the .spec file and build the application

```
pyinstaller --onefile --windowed --noconsole --icon sleepdungeon.ico --additional-hooks-dir pyinstaller_hooks bin/sleepdungeon
```


## How to build this game for Windows?

### Installing PyInstaller

Install PyInstaller on your system:

```
python -m pip install pyinstaller
```

### Create the .spec file and build the application

Execute the following command to create the initial .spec file for the game:

```
pyinstaller.exe --onefile --windowed --noconsole --icon .\sleepdungeon.ico --additional-hooks-dir .\pyinstaller_hooks .\bin\sleepdungeon
```

You will find the generated executable at `dist/sleepdungeon.exe`
