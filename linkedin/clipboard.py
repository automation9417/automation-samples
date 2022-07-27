import win32clipboard

def clear_clipboard_data():
    try:
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
    finally:
        win32clipboard.CloseClipboard()

def get_clipboard_data():
    try:
        win32clipboard.OpenClipboard()
        data = win32clipboard.GetClipboardData()
        return data
    except:
        return ""
    finally:
        win32clipboard.CloseClipboard()