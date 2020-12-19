# =============================================================================
# Toontown Version Reader
# Author: Cranky Supertoon
# Date: 12/18/2020
# Purpose: Detects Versions for Toontown Clients
# Requires: No Additional Files or Software
# =============================================================================

with open("TTRGame.vlt", 'rb') as vlt:
    vlt_data = vlt.read()

start_ver = vlt_data.find(b"VERSION")
end_ver = vlt_data.find(b"\x00", start_ver)
ver_str = vlt_data[start_ver:end_ver].decode()

version = ver_str.split("=", 1)[-1]
print(version)