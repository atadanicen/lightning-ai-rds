from lightning_sdk import Machine, Status, Studio
from rich import print

# You can change the machine here (T4,V100,etc..)
MACHINE = Machine.CPU
# Change the user details here
NAME = "projects"
TEAMSPACE = "demos"
USER = "atadanicen"


def wake_studio():
    studio = Studio(name=NAME, teamspace=TEAMSPACE, user=USER)
    print("\n :zap::zap: Welcome to the Lightning Studio :zap::zap:\n")
    if studio.status == Status.Stopped:
        print("Server is starting...", end="\r")
        studio.start(machine=MACHINE)
        if studio.status == Status.Running:
            print("Server is started!   \n")
    elif studio.status == Status.Running:
        print("Server is already running!\n")
    elif studio.status == Status.Stopping:
        print("Server is stopping...\n")


wake_studio()
