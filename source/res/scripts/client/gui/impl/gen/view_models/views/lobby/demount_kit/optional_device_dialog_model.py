# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/demount_kit/optional_device_dialog_model.py
from gui.impl.gen.view_models.views.lobby.demount_kit.item_price_dialog_model import ItemPriceDialogModel

class OptionalDeviceDialogModel(ItemPriceDialogModel):
    __slots__ = ()

    def __init__(self, properties=17, commands=2):
        super(OptionalDeviceDialogModel, self).__init__(properties=properties, commands=commands)

    def getIsDeluxe(self):
        return self._getBool(16)

    def setIsDeluxe(self, value):
        self._setBool(16, value)

    def _initialize(self):
        super(OptionalDeviceDialogModel, self)._initialize()
        self._addBoolProperty('isDeluxe', False)
