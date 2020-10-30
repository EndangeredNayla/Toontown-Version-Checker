# =============================================================================
# Toontown Version Reader
# Author: Cranky Supertoon
# Date: 10/29/2020
#
# Purpose: Detects Versions for Toontown Online Clients
# =============================================================================
from panda3d.core import *
from panda3d import core

key = "t@@V'[T'bm"

virfile = core.VirtualFileSystem.getGlobalPtr()
test = virfile.getFile('Configrc.pre').openReadFile(False)
config = loadPrcFile('Configrc.pre')
config.readEncryptedPrc(test, key)
config = str(config)
for out in config:
	out.split()
config = str(config).split('\n')
for out in config:
	if 'server-version ' in out:
		sv_version = out.split(' ')[1]
print(sv_version)
