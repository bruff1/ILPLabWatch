from Services.PortService import PortService
from Services.TriggerService import TriggerService

PS = PortService()
TS = TriggerService()
PS.setTriggerService(TS)
