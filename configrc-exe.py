# =============================================================================
# Toontown Version Reader
# Author: Cranky Supertoon
# Date: 10/29/2020
#
# Purpose: Detects Versions for Toontown Online Clients
# =============================================================================
import platform
import subprocess

if platform.system() == 'Linux' or platform.system() == 'Darwin':
	output = subprocess.Popen(["wine", "Configrc.exe", "-stdout"], stdout=subprocess.PIPE).communicate()[0]
if platform.system() == 'Windows':
	output = subprocess.Popen(["Configrc.exe", "-stdout"], stdout=subprocess.PIPE).communicate()[0]
output = output.split(b'\r\n')
for out in output:
	if b'server-version ' in out:
		sv_version = out.split(b' ')[1].decode()
print(sv_version)
