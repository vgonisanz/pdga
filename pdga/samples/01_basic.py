import time

from pdga.engine.core import Engine
from pdga.engine.enums import Colors

def hello_world():
    print("Hello world")
    time.sleep(0.5)

if __name__ == "__main__":
    engine = Engine(width=800, height=600,
                    title="Basic example", debug=True)

    engine.set_run_bucle(hello_world)
    engine.set_background(Colors.White)
    engine.run()