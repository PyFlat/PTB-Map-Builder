
from __future__ import annotations


from cx_Freeze import Executable, setup

try:
    from cx_Freeze.hooks import get_qt_plugins_paths
except ImportError:
    get_qt_plugins_paths = None
include_files = ["icons", "src", "textures", "style.qss"]

if get_qt_plugins_paths:
    include_files += get_qt_plugins_paths("PySide6", "platform")

base = "Win32GUI"

build_exe_options = {
    "includes": ["urllib.request",
                "threading",
                "datetime",
                "re",
                "os",
                "configparser",
                "sys",
                "subprocess",
                "shutil",
                "zipfile",
                "html.parser",
                "uuid",
                "json",
                "requests"],
    "bin_excludes": ["libqpdf.so", "libqpdf.dylib"],
    "excludes": ["selenium",
                "pygments",
                "superqt",
                "chardet",
                "ctypes.wintypes",
                "fileinput",
                "optparse",
                "xml.etree.ElementTree",
                "asyncio",
                "http.cookies",
                "wget",
                "bs4",
                "tkinter",
                "unittest",
                "PyQt5",
                "PyQt6",
                "decord",
                "numpy",
                "panda3d",
                "pandas",
                "playwright",
                "scipy",
                "requests",
                "tensorflow",
                "tesseract",
                "matplotlib",
                "Cryptodome",
                "jedi",
                "test",
                "lxml",
                "Cython",
                "setuptools",
                "IPython",
                "prompt_toolkit",
                "docutils",
                "mutagen",
                "pkg_resources",
                "pywin32_system32",
                "trio",
                "distutils",
                "io",
                "PIL",
                "yt_dlp",
                "pygments",
                "cryptography",
                "PySide6.Qt6Network",
                "PySide6.QtOpenGL",
                "PySide6.Qt6Quick"],
    "include_files": include_files,
    "zip_include_packages": ["PySide6"],
}

executables = [Executable("main.py", base=base)]

setup(
    name="Map_Builder",
    version="2.0.0",
    description="PTB Map Builder",
    options={"build_exe": build_exe_options},
    executables=executables,
)
