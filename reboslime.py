import sys
import platform
import json
import socket
import time
import struct
import signal
from libs.inputimeout import inputimeout, TimeoutOccurred
from libs.rebocap import rebocap_ws_sdk
from rich.console import Console


CONFIG = json.load(open('config.json'))
VERSION = CONFIG['version']
REBOCAP_IMUS = CONFIG['rebocap_imus']
CONSOLE_TIMEOUT = CONFIG['console_timeout']
SLIME_IP = CONFIG['slime_ip']  # SlimeVR Server
SLIME_PORT = CONFIG['slime_port']  # SlimeVR Server
# SlimeVR packet frequency. Keep below 300 (above 300 has weird behavior)
TPS = CONFIG['tps']
ZERO_QUAT = [1, 0, 0, 0]
ALL_CONNECTED = False
PACKET_COUNTER = 0
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sdk = None
global_quats = []
PYTHON_VER = sys.version

# Pose data callback
def pose_msg_callback(self: rebocap_ws_sdk.RebocapWsSdk, tran: list, pose24: list, static_index: int, ts: float):
    for i in range(24):
        if i in CONFIG["imus"][str(REBOCAP_COUNT)]:
            update_imu_quat(i, pose24[i][0], - pose24[i][1],
                            pose24[i][2], pose24[i][3])
            # if i == 10:
            #     console.log(rebocap_ws_sdk.REBOCAP_JOINT_NAMES[i], ["%.5f" % num for num in pose24[i]])
            # console.log(rebocap_ws_sdk.REBOCAP_JOINT_NAMES[i], ["%.5f" % num for num in pose24[i]])
            # time.sleep(0.1)


# Unexpected disconnect — handle reconnection or error here
def exception_close_callback(self: rebocap_ws_sdk.RebocapWsSdk):
    global sdk
    try:
        sdk.close()
        init_rebocap_ws()
    except:
        print("exception_close_callback")


def init_rebocap_ws():
    global sdk
    # Initialize SDK
    sdk = rebocap_ws_sdk.RebocapWsSdk(
        coordinate_type=rebocap_ws_sdk.CoordinateType.UnityCoordinate,
        use_global_rotation=True
    )
    # Set pose callback
    sdk.set_pose_msg_callback(pose_msg_callback)
    # Set disconnect callback
    sdk.set_exception_close_callback(exception_close_callback)
    # Start connection
    open_ret = sdk.open(7690)
    # Checking connection status
    if open_ret == 0:
        console.print("Rebocap client connected successfully!")
    else:
        console.print("Rebocap client connection failed!", open_ret)
        if open_ret == 1:
            console.print("Rebocap client status error!")
        elif open_ret == 2:
            console.print("Rebocap client connection failed!")
        elif open_ret == 3:
            console.print("Rebocap client authentication failed!")
        else:
            console.print("Unknown error! Code:", open_ret)
        exit(1)


def build_handshake():
    fw_string = "ReboSlime"
    buffer = b'\x00\x00\x00\x03'  # packet 3 header
    buffer += struct.pack('>Q', PACKET_COUNTER)  # packet counter
    buffer += struct.pack('>I', 0)  # board ID
    buffer += struct.pack('>I', 0)  # IMU type
    buffer += struct.pack('>I', 0)  # MCU type
    buffer += struct.pack('>III', 0, 0, 0)  # IMU info
    buffer += struct.pack('>I', 0)  # Build
    buffer += struct.pack('B', len(fw_string))  # length of fw string
    buffer += struct.pack(str(len(fw_string)) + 's',
                          fw_string.encode('UTF-8'))  # fw string
    # MAC address (just using a placeholder of 31:31:31:31:31:31 for now)
    buffer += struct.pack('6s', '111111'.encode('UTF-8'))
    buffer += struct.pack('B', 255)
    return buffer


def add_imu(id):
    global PACKET_COUNTER
    buffer = b'\x00\x00\x00\x0f'  # packet 15 header
    buffer += struct.pack('>Q', PACKET_COUNTER)  # packet counter
    # tracker id (shown as IMU Tracker #x in SlimeVR)
    buffer += struct.pack('B', id)
    buffer += struct.pack('B', 0)  # sensor status
    buffer += struct.pack('B', 0)  # sensor type
    sock.sendto(buffer, (SLIME_IP, SLIME_PORT))
    # print("Add IMU: " + str(trackerID))
    PACKET_COUNTER += 1


def add_imus(ids):
    for id in ids:
        # SlimeVR has been missing "add IMU" packets so we just send them 3 times to make sure they get through
        for z in range(3):
            add_imu(id)


def build_rotation_packet(qw: float, qx: float, qy: float, qz: float, tracker_id: int):
    # qw,qx,qy,qz: parts of a quaternion / trackerID: Tracker ID
    buffer = b'\x00\x00\x00\x11'  # packet 17 header
    buffer += struct.pack('>Q', PACKET_COUNTER)  # packet counter
    # tracker id (shown as IMU Tracker #x in SlimeVR)
    buffer += struct.pack('B', tracker_id)
    buffer += struct.pack('B', 1)  # data type (use is unknown)
    buffer += struct.pack('>ffff', qx, -qz, qy, qw)  # quaternion as x,z,y,w
    # calibration info (seems to not be used by SlimeVR currently)
    buffer += struct.pack('B', 0)
    return buffer


# mac_addrs: Table of mac addresses. Just used to get number of trackers
def send_all_imus(mac_addrs):
    global TPS, PACKET_COUNTER
    while True:
        for z in range(TPS):
            for i in range(len(mac_addrs)):
                sensor = globals()['sensor' + str(i) + 'data']
                rot = build_rotation_packet(
                    sensor.qw, sensor.qx, sensor.qy, sensor.qz, i)
                sock.sendto(rot, (SLIME_IP, SLIME_PORT))
                PACKET_COUNTER += 1
                # Accel is not ready yet
                # accel = build_accel_packet(sensor.ax, sensor.ay, sensor.az, i)
                # sock.sendto(accel, (SLIME_IP, SLIME_PORT))
                # PACKET_COUNTER += 1
            # time.sleep(1 / TPS)


def update_imu_quat(id, qx, qy, qz, qw):
    global TPS, PACKET_COUNTER
    try:
        rot = build_rotation_packet(qw, qx, qy, qz, id)
        sock.sendto(rot, (SLIME_IP, SLIME_PORT))
        PACKET_COUNTER += 1
    except ValueError:
        pass


# Main
console = Console()
console.print(" ___       _          ___  _  _             \n\
| _ \\ ___ | |__  ___ / __|| |(_) _ __   ___ \n\
|   // -_)|  _ \\/ _ \\\\__ \\| || || '  \\ / -_)\n\
|_|_\\\\___||____/\\___/|___/|_||_||_|_|_|\\___|  v" + VERSION + "\n\
")
console.print("Python " + PYTHON_VER + "\n")
console.print("About IMU point configurations:\n\
·  6 points: Chest + Hip + Thigh + Shin\n\
·  8 points: Chest + Waist + Thigh + Shin + Foot\n\
· 10 points: Chest + Waist + Thigh + Shin + Foot + Upper Arm\n\
· 12 points: Chest + Waist + Thigh + Shin + Foot + Upper Arm + Forearm\n\
· 15 points: Full body\n")

try:
    REBOCAP_COUNT = inputimeout(
        "How many tracking points do you want to use? "
        "If no input is given, it will start in "
        + str(CONSOLE_TIMEOUT)
        + " seconds in "
        + str(REBOCAP_IMUS)
        + "-point mode (please enter 6 / 8 / 10 / 12 / 15): ",
        CONSOLE_TIMEOUT
    )
except TimeoutOccurred:
    REBOCAP_COUNT = REBOCAP_IMUS

# Connect to Rebocap
init_rebocap_ws()

# Connected To SlimeVR Server
handshake = build_handshake()
sock.sendto(handshake, (SLIME_IP, SLIME_PORT))
PACKET_COUNTER += 1
console.print("Successfully connected to SlimeVR server!")
time.sleep(0.1)

# Add additional IMUs. SlimeVR only supports one "real" tracker per IP so the workaround is to make all the
# trackers appear as extensions of the first tracker.
if int(REBOCAP_COUNT) in (6, 8, 10, 12, 15):
    imus = CONFIG['imus'][str(REBOCAP_COUNT)]
    add_imus(imus)
    console.print("Add IMUs: " + str(imus))
else:
    console.print("Currently only 6 / 8 / 10 / 12 / 15 points are supported!")
    exit()

time.sleep(.5)
ALL_CONNECTED = True

console.print(
    "Tracking started! To stop ReboSlime, press Ctrl-C several times."
)

try:
    # TODO: Gracefully wait
    time.sleep(1000000)
except KeyboardInterrupt:
    sdk.close()
