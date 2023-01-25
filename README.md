# MISC FUNCTIONS
Misceleneous functions to perform generic tasks such as opening file dialog boxes or converting data types. Just whatever comes along that I need.

## Dialogs.py
This is to be used for various dialogs whether it be alerts or file selection.

### open_file_dialog()
```
    author: PVTCompyle
    upated: 26-AUG-2022
    DESC: Opens a file dialog box so you can select a file for use in your program. By default, a single filename
    with directory is returned as a string. 
    
    If multiselect mode is enabled, fname will return a list containg the directory name at [0] 
    and filenames in [1:].
    if envvar is defined, the InitDir will be set to %ENVVAR%\initdir, so set initdir as needed.

**EXAMPLES**
initial_directory = r'c:\users\myuser\'
