from modules.lists import list_HLayouts, list_all_button
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout

main_V = QVBoxLayout() #
#
for line in range(5):
    list_HLayouts.append(QHBoxLayout())

def addToLayout():
    for button in list_all_button:
        #
        index = list_all_button.index(button)
        #
        for button1 in button:
            #
            list_HLayouts[index].addWidget(button1)
    #
    for el in list_HLayouts:
        #
        main_V.addLayout(el)