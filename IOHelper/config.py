import json, codecs, os

# Porteinstellungen
portConf = "conf/portsConf.cfg"

# Verbindungsboxeinstellungen
wiringConf = "conf/wiringConf.cfg"

# Triggereinstellungen
triggerConf = "conf/triggerConf.cfg"


# gibt eine Liste mit allen Ports und ihren Einstellungen zurück.
def loadPorts():
    return loadConfig(portConf)


# gibt die Verbindungseinstellungen der Connectorbox zurück.
def loadWiring():
    return loadConfig(wiringConf)


# Lädt alle Triggereinstellungen
def loadTriggers():
    return loadConfig(triggerConf)


# Speichert die ganze Portsconf
def savePorts(content):
    saveConfig(portConf, content)


# Speichert die Verbindungseinstellungen
def saveWiring(content):
    saveConfig(wiringConf, content)


# Speichert die Triggereinstellungen
def saveTriggers(content):
    saveConfig(triggerConf, content)


# Lädt eine Einstellungsdatei
def loadConfig(configLink):
    with open(configLink, "r", encoding='utf-8') as configfile:
        conf = json.load(configfile)
        return conf


# Speichert eine Einstellunsdatei
def saveConfig(configLink, content):
    with open(configLink, "w", encoding='utf-8') as configfile:
        json.dump(content, configfile, indent=4)
