# ----------------------------------------------------------------------------
# gsnodegraph Copyright 2019-2022 by Noah Rahm and contributors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# ----------------------------------------------------------------------------
import wx
import sys
from gui.interface_wx import MyFrame

# Install a custom displayhook to keep Python from setting the global
# _ (underscore) to the value of the last evaluated expression.
# If we don't do this, our mapping of _ to gettext can get overwritten.
# This is useful/needed in interactive debugging with PyShell.
def _displayHook(obj):
    """ Custom display hook to prevent Python stealing '_'. """

    if obj is not None:
        print(repr(obj))

# Add translation macro to builtin similar to what gettext does.
import builtins
builtins.__dict__['_'] = wx.GetTranslation

class MainApp(wx.App):
    def OnInit(self):
        # construct frame
        frame = MyFrame(None, size=(512, 512))
        frame.SetTitle("gsnodegraph demo")
        frame.Show()

        # Work around for Python stealing "_".
        sys.displayhook = _displayHook

        return True

    def Onexit(self):
        print("应用程序退出!")
        return 0

if __name__ == "__main__":
    app = MainApp()
    app.MainLoop()
