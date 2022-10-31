from src.application import GardenSimulatorApp
from src.interface import Interface


def injector():
    app = GardenSimulatorApp()
    gui = Interface(app)
    gui.run()


if __name__ == "__main__":
    with open("assets/description.txt", "r", encoding="utf-8") as file:
        print(file.read())
    injector()
