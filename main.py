# =============================================================================
# Toontown Version Reader
# Author: Cranky Supertoon
# Date: 5/8/2021
# Purpose: Detects Versions for Toontown Clients
# Requires: No Additional Files or Software
# =============================================================================

filetype = True
while filetype:
    print(
        """
    1. Toontown Online - Configrc.exe
    2. Toontown Online - Configrc.prc
    3. Toontown Online - Configrc.pre
    4. Toontown Rewritten - TTRGame.vlt
    5. Exit
    """
    )
    filetype = input("What would you like to do? ")
    if filetype == "1":
        import platform
        import subprocess
        import pathlib
        exefile = pathlib.Path("Configrc.exe")
        if exefile.exists ():
            libdtool = pathlib.Path("libdtool.exe")
            if libdtool.exists ():
                if platform.system() == "Linux" or platform.system() == "Darwin":
                    output = subprocess.Popen(
                        ["wine", "Configrc.exe", "-stdout"], stdout=subprocess.PIPE
                    ).communicate()[0]
                if platform.system() == "Windows":
                    output = subprocess.Popen(
                        ["Configrc.exe", "-stdout"], stdout=subprocess.PIPE
                    ).communicate()[0]
                output = output.split(b"\r\n")
                for out in output:
                    if b"server-version " in out:
                        version = out.split(b" ")[1].decode()
                print("\n" + version)
            else:
                print
                print("\n" + "ERROR! libdtool.dll or MSVCP .dll's not present! Quitting...")
        else:
            print
            print("\n" + "ERROR! Configrc.exe not present! Quitting...")
        break
    elif filetype == "2":
        import pathlib
        prcfile = pathlib.Path("Configrc.pre")
        if prcfile.exists ():
            with open("Configrc.prc", "r") as prc:
                prc_data = prc.read()
            version = prc_data.split("server-version", 1)[-1].split()[0]
            print("\n" + version)
        else:
            print
            print("\n" + "ERROR! Configrc.prc not present! Quitting...")
        break
    elif filetype == "3":
        import pathlib
        prefile = pathlib.Path("Configrc.pre")
        if prefile.exists ():
            try:
                import panda3d
            except ImportError as e:
                print
                print("\n" + "ERROR! Panda3D not present in PyPi! Quitting...")
                break
            from panda3d.core import *
            from panda3d import core
            pre_key = "t@@V'[T'bm"
            virfile = core.VirtualFileSystem.getGlobalPtr()
            test = virfile.getFile("Configrc.pre").openReadFile(False)
            config = loadPrcFile("Configrc.pre")
            config.readEncryptedPrc(test, pre_key)
            config = str(config)
            for out in config:
                out.split()
            config = str(config).split("\n")
            for out in config:
                if "server-version " in out:
                    version = out.split(" ")[1]
            print("\n" + version)                
        else:
            print
            print("\n" + "ERROR! Configrc.exe not present! Quitting...")
        break
    elif filetype == "4":
        import pathlib
        vltfile = pathlib.Path("TTRGame.vlt")
        if vltfile.exists ():
            with open("TTRGame.vlt", "rb") as ver:
                ver_data = ver.read()
            start_ver = ver_data.find(b"VERSION")
            end_ver = ver_data.find(b"\x00", start_ver)
            ver_str = ver_data[start_ver:end_ver].decode()
            version = ver_str.split("=", 1)[-1]
            print("\n" + version)
        else:
            print
            print("\n" + "ERROR! Configrc.exe not present! Quitting...")
        break    
    elif filetype == "5":
        print("\n" + "Goodbye")
        break
    else:
        print("\n" + "ERROR! No number selected! Quitting...")
        break
