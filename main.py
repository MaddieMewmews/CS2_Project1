from controller import *
import sys
def main():

    app = QApplication(sys.argv)
    window = Controller()
    window.show()
    sys.exit(app.exec_())



if __name__ == '__main__':
    main()
