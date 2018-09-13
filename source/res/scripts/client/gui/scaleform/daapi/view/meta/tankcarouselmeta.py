# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/TankCarouselMeta.py
from gui.Scaleform.framework.entities.DAAPIModule import DAAPIModule

class TankCarouselMeta(DAAPIModule):

    def showVehicleInfo(self, vehicleId):
        self._printOverrideError('showVehicleInfo')

    def toResearch(self, compactDescr):
        self._printOverrideError('toResearch')

    def vehicleSell(self, inventoryId):
        self._printOverrideError('vehicleSell')

    def vehicleChange(self, vehicleInventoryId):
        self._printOverrideError('vehicleChange')

    def buySlot(self):
        self._printOverrideError('buySlot')

    def buyTankClick(self):
        self._printOverrideError('buyTankClick')

    def setVehiclesFilter(self, nation, tankType, ready):
        self._printOverrideError('setVehiclesFilter')

    def favoriteVehicle(self, compact, isFavorite):
        self._printOverrideError('favoriteVehicle')

    def showVehicleStats(self, compact):
        self._printOverrideError('showVehicleStats')

    def getVehicleTypeProvider(self):
        self._printOverrideError('getVehicleTypeProvider')

    def as_setCarouselFilterS(self, filter):
        if self._isDAAPIInited():
            return self.flashObject.as_setCarouselFilter(filter)

    def as_setParamsS(self, params):
        if self._isDAAPIInited():
            return self.flashObject.as_setParams(params)

    def as_updateVehiclesS(self, vehiclesData, isSet):
        if self._isDAAPIInited():
            return self.flashObject.as_updateVehicles(vehiclesData, isSet)

    def as_showVehiclesS(self, compactDescrList):
        if self._isDAAPIInited():
            return self.flashObject.as_showVehicles(compactDescrList)
