def open_file_dialog(
    filter='TEXT\0*.txt\0',
    customfilter='Other file types\0*.*\0',
    initdir='',
    envvar = '', 
    file="MyFile", DefExt="txt", 
    title='Select file to open',
    filterindex=0,
    multiselect=False 
):
    '''
    author: PVTCompyle
    upated: 26-AUG-2022
    DESC: Opens a file dialog box so you can select a file for use in your program. By default, a single filename
    with directory is returned as a string. 
    
    If multiselect mode is enabled, a list containg the directory name at [0] 
    and filenames in [1:]. 

    if envvar is defined, the InitialDir will be set to %ENVVAR%\initdir, so set initdir as needed.
    '''
    import win32gui
    import win32con
    import os

    if envvar:
        initdir = f'{os.environ[envvar]}\{initdir}'

    if multiselect:
        flags = win32con.OFN_ALLOWMULTISELECT | win32con.OFN_EXPLORER
    else:
        flags = win32con.OFN_EXPLORER
    
    try:
        fname, customfilter, flags=win32gui.GetOpenFileNameW(
            InitialDir = initdir,
            Flags = flags,
            File = file,
            Title = title,
            Filter = filter,
            CustomFilter = customfilter,
            FilterIndex = filterindex
        )
    except Exception as e:
        return f'UserAborted: {e}'
    
    if multiselect: # converts fname to a list for easier handling
        fname = fname.split('\x00')   

    return fname