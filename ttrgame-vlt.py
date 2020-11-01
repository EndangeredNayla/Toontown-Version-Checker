# =============================================================================
# Toontown Version Reader
# Author: Cranky Supertoon
# Date: 10/29/2020
#
# Purpose: Detects Versions for Toontown Online Clients
# =============================================================================
vlt = open('TTRGame.vlt', 'r', encoding="iso-8859-15")
config = vlt.read()
config = config[99:120].split()[0]
print(config)
