# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FalloutTankCarouselMeta.py
"""
This file was generated using the wgpygen.
Please, don't edit this file manually.
"""
from gui.Scaleform.daapi.view.lobby.hangar.carousels.basic.tank_carousel import TankCarousel

class FalloutTankCarouselMeta(TankCarousel):

    def changeVehicle(self, id):
        self._printOverrideError('changeVehicle')

    def clearSlot(self, vehicleId):
        self._printOverrideError('clearSlot')

    def shiftSlot(self, vehicleId):
        self._printOverrideError('shiftSlot')

    def as_setMultiselectionInfoS(self, data):
        """
        :param data: Represented by MultiselectionInfoVO (AS)
        """
        return self.flashObject.as_setMultiselectionInfo(data) if self._isDAAPIInited() else None

    def as_getMultiselectionDPS(self):
        return self.flashObject.as_getMultiselectionDP() if self._isDAAPIInited() else None
