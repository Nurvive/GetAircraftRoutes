from getAircraftHistory import get_history
from getAircraftRegs import get_regs
from functools import reduce
import operator

airlineCode = 'su-afl'
aircraftType = 'SU95'

aircraftList = get_regs(airlineCode, aircraftType)
# generating list of routes. Iterating over aircraft, then making flat list
total_routes = []
for aircraft in aircraftList:
    total_routes.append(get_history(aircraft))
total_routes = reduce(operator.iconcat, total_routes, [])  # flat string of unique routes for all aircrafts

print("Total found number of routes: ", len(total_routes))
print(",".join(total_routes))
