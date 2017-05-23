
# Seva Alekseyev with National Institutes of Health, 2016

from . import ZipReader

from UM.i18n import i18nCatalog
catalog = i18nCatalog("cura")

def getMetaData():
    return {
        "plugin": {
            "name": catalog.i18nc("@label", "ZIP Reader"),
            "author": "Tiger",
            "version": "0.5",
            "description": catalog.i18nc("@info:whatsthis", "Provides support for reading ZIP files."),
            "api": 3
        },
        "mesh_reader": [
            {
                "extension": "zip",
                "description": catalog.i18nc("@item:inlistbox", "ZIP File")
            }
        ]
    }

def register(app):
    return { "mesh_reader": ZipReader.ZipReader() }
