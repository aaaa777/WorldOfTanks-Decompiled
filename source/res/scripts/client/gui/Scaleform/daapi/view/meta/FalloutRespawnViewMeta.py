# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FalloutRespawnViewMeta.py
"""
This file was generated using the wgpygen.
Please, don't edit this file manually.
"""
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class FalloutRespawnViewMeta(BaseDAAPIComponent):

    def onVehicleSelected(self, vehicleID):
        self._printOverrideError('onVehicleSelected')

    def onPostmortemBtnClick(self):
        self._printOverrideError('onPostmortemBtnClick')

    def as_initializeComponentS(self, mainData, slotsData):
        """
        :param mainData: Represented by FalloutRespawnViewVO (AS)
        :param slotsData: Represented by Vector.<VehicleSlotVO> (AS)
        """
        return self.flashObject.as_initializeComponent(mainData, slotsData) if self._isDAAPIInited() else None

    def as_updateTimerS(self, mainTimer, slotsStateData):
        """
        :param slotsStateData: Represented by Vector.<VehicleStateVO> (AS)
        """
        return self.flashObject.as_updateTimer(mainTimer, slotsStateData) if self._isDAAPIInited() else None

    def as_updateS(self, selectedVehicleName, slotsStateData):
        """
        :param slotsStateData: Represented by Vector.<VehicleStateVO> (AS)
        """
        return self.flashObject.as_update(selectedVehicleName, slotsStateData) if self._isDAAPIInited() else None

    def as_showGasAttackModeS(self):
        return self.flashObject.as_showGasAttackMode() if self._isDAAPIInited() else None
