from main_gui import *
import sys
from final_hit import posper,negper

MainWindow.show()
ui.pushButton.clicked.connect(fetch_query_from_gui)
ui.checkBox.clicked.connect(pos_check)
ui.checkBox_2.clicked.connect(neg_check)
ui.checkBox_3.clicked.connect(nut_check)
ui.actionQuit.triggered.connect(all_sub_close)
ui.pushButton_2.clicked.connect(reset_all)
ui.actionRestart.triggered.connect(restart)
ui.actionCredits.triggered.connect(openCredits)
ui.actionHelp.triggered.connect(open_Help)
ui.actionHelp_2.triggered.connect(open_Help)

sys.exit(app.exec_())
