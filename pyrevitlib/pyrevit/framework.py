"""Provide access to DotNet Framework.

Example:
    >>> from pyrevit.framework import Assembly, Windows
"""

#pylint: disable=W0703,C0302,C0103,W0614,E0401,W0611,C0413,ungrouped-imports
import os.path as op
import pyrevit.compat as compat

import clr
import System


clr.AddReference('System.Core')
clr.AddReference('System.Management')
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Drawing')
clr.AddReference('PresentationCore')
clr.AddReference('PresentationFramework')
clr.AddReference('System.Xml.Linq')
clr.AddReference('WindowsBase')

# add linq extensions?
if compat.PY2:
    clr.ImportExtensions(System.Linq)

from System import AppDomain, Version
from System import Type
from System import Uri, Guid
from System import EventHandler
from System import Array, IntPtr, Enum, Byte
from System import Convert
from System.Text import Encoding
from System.Text.RegularExpressions import Regex
from System.Collections import ObjectModel
from System.Collections.ObjectModel import ObservableCollection
from System.Collections import IEnumerator, IEnumerable
from System.Collections.Generic import List, Dictionary
from System.Collections.Generic import IList, IDictionary
from System import DateTime, DateTimeOffset

from System import Diagnostics
from System.Diagnostics import Process
from System.Diagnostics import Stopwatch

from System import Reflection
from System.Reflection import Assembly, AssemblyName
from System.Reflection import TypeAttributes, MethodAttributes
from System.Reflection import CallingConventions
from System.Reflection import BindingFlags
from System.Reflection.Emit import AssemblyBuilderAccess
from System.Reflection.Emit import CustomAttributeBuilder, OpCodes

from System import IO
from System.IO import IOException, DriveInfo, Path, StringReader, File

from System import Net
from System.Net import WebClient, WebRequest, WebProxy

from System import ComponentModel
from System import Drawing
from System import Windows
from System.Windows import Forms
from System.Windows.Forms import Clipboard
from System.Windows import Controls
from System.Windows import Documents
from System.Windows import Media
from System.Windows import Threading
from System.Windows import Interop
from System.Windows import Input
from System.Windows import Data
from System.Windows.Media import Imaging, SolidColorBrush, Color
from System import Math
from System.Management import ManagementObjectSearcher
from System.Runtime.Serialization import FormatterServices

from System.Linq import Enumerable

import pyrevit.engine as eng

wpf = None
clr.AddReference(
    '{prefix}IronPython.Wpf'.format(prefix=eng.EnginePrefix)
    )
if compat.PY3:
    import IronPython
    wpf = IronPython.Modules.Wpf
else:
    import wpf

CPDialogs = None
try:
    clr.AddReference('Microsoft.WindowsAPICodePack')
    clr.AddReference('Microsoft.WindowsAPICodePack.Shell')
    import Microsoft.WindowsAPICodePack.Dialogs as CPDialogs #pylint: disable=ungrouped-imports
except Exception:
    pass


# try loading some utility modules shipped with revit
NSJson = None
try:
    clr.AddReference('pyRevitLabs.Json')
    import pyRevitLabs.Json as NSJson
except Exception:
    pass


# do not import anything from pyrevit before this
from pyrevit import BIN_DIR


ASSEMBLY_FILE_TYPE = 'dll'


def get_type(fw_object):
    """Return CLR type of an object."""
    return clr.GetClrType(fw_object)


def get_dll_file(assembly_name):
    """Return path to given assembly name."""
    addin_file = op.join(BIN_DIR, assembly_name + '.dll')
    if op.exists(addin_file):
        return addin_file


def get_current_thread_id():
    """Return manageed thread id of current thread."""
    return System.Threading.Thread.CurrentThread.ManagedThreadId
