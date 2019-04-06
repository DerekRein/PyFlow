from PyFlow.Packages.PyflowBase import PACKAGE_NAME
from PyFlow.UI.Widgets.InputWidgets import REGISTER_UI_INPUT_WIDGET_PIN_FACTORY
from PyFlow.UI.Canvas.UINodeBase import REGISTER_UI_NODE_FACTORY
from PyFlow.UI.Canvas.UIPinBase import REGISTER_UI_PIN_FACTORY
from PyFlow.Packages.PyflowBase.Factories.PinInputWidgetFactory import getInputWidget
from PyFlow.Packages.PyflowBase.Factories.UINodeFactory import createUINode
from PyFlow.Packages.PyflowBase.Factories.UIPinFactory import createUIPin


REGISTER_UI_INPUT_WIDGET_PIN_FACTORY(PACKAGE_NAME, getInputWidget)
REGISTER_UI_NODE_FACTORY(PACKAGE_NAME, createUINode)
REGISTER_UI_PIN_FACTORY(PACKAGE_NAME, createUIPin)
