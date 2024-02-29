from lightning_sdk import Machine, Status, Studio
from rich import print

# you can change the machine here (T4,V100,etc..)
MACHINE = Machine.CPU


def wake_studio():
    studio = Studio(name="projects", teamspace="demos", user="atadanicen")
    print("\n :zap::zap: Welcome to the Lightning Studio :zap::zap:\n")
    if studio.status == Status.Stopped:
        print("Server is starting...", end="\r")
        studio.start(machine=MACHINE)
        print("Server is started!   \n")
    elif studio.status == Status.Running:
        print("Server is already running!\n")
    elif studio.status == Status.Stopping:
        print("Server is stopping...\n")


wake_studio()
