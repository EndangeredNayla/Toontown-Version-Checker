# =============================================================================
# Toontown Version Reader
# Author: Cranky Supertoon
# Date: 12/18/2020#
# Purpose: Detects Versions for Toontown Clients
# Requires: No Additional Files or Software
# =============================================================================

with open("Configrc.prc", 'r') as prc:
    prc_data = prc.read()

version = prc_data.split("server-version", 1)[-1].split()[0]

print(version)
