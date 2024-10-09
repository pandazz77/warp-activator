import base64
import random
import os

WARP_BASE64IP = "MTYyLjE1OS4xOTMu"
WARP_BASE64PORTS = (
    "NTAw",
    "MjQwOA==",
    "NDUwMA=="
)

WARP_IP = base64.b64decode(WARP_BASE64IP).decode()
WARP_PORTS = tuple(base64.b64decode(b64port).decode() for b64port in WARP_BASE64PORTS)

def generate():
    return f"{WARP_IP}{random.randint(1,11)}:{random.choice(WARP_PORTS)}"

def activate():
    connection = generate()
    print("Using address:",connection)

    print("Disconnect:")
    os.system( "warp-cli --accept-tos disconnect")
    print("Set endpoint:")
    os.system(f"warp-cli --accept-tos tunnel endpoint set {connection}")
    print("Connect:")
    os.system( "warp-cli --accept-tos connect")


if __name__ == "__main__":
    activate()
    print("endpoint was changed, try to connect")