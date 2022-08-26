def open_file_dialog(
    _filter='TEXT\0*.txt\0',
    _customfilter='Other file types\0*.*\0',
    _initdir='', # either the full path or relative path
    _envvar = '', # if defining an environment varible as part of your path, define the remaining path in initdir
    _file="MyFile", DefExt="txt", 
    _title='Select file to open',
    _filterindex=0,
    _multiselect=False # if enabled will allow selecting multiple files and returns a list; [0] is the directory name
):
    '''
    author: PVTCompyle
    upated: 26-AUG-2022
    DESC: Opens a file dialog box so you can select a file for use in your program. By default, a single filename
    with directory is returned as a string. If multiselect mode is enabled, a list containg the directory name at [0] 
    and filenames in [1:]. 
    '''
    import win32gui
    import win32con
    import os

    if _envvar:
        initdir = f'{os.environ[_envvar]}\{initdir}'

    if _multiselect:
        _flags = win32con.OFN_ALLOWMULTISELECT | win32con.OFN_EXPLORER
    else:
        _flags = win32con.OFN_EXPLORER
    
    try:
        fname, _customfilter, flags=win32gui.GetOpenFileNameW(
            InitialDir = _initdir,
            Flags = _flags,
            File = _file,
            Title = _title,
            Filter = _filter,
            CustomFilter = _customfilter,
            FilterIndex = _filterindex
        )
    except Exception as e:
        return f'UserAborted: {e}'
    
    if _multiselect: # converts fname to a list for easier handling
        fname = fname.split('\x00')   

    return fname