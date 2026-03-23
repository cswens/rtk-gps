import serial
from threading import Event
from pygnssutils import GNSSNTRIPClient

SERIAL_PORT = "/dev/ttyUSB0"
BAUDRATE = 38400

NTRIP_SERVER = "ppntrip.services.u-blox.com"
NTRIP_PORT = 2101
NTRIP_USER = "fvmiqg6tTX5P"
NTRIP_PASSWORD = "AnHZW*6Cb_"
NTRIP_MOUNTPOINT = "NEAR-RTCM"

print(f"Opening serial port {SERIAL_PORT} at {BAUDRATE} baud...")

stop = Event()

with serial.Serial(SERIAL_PORT, BAUDRATE) as ser:
    print("Starting NTRIP client for ZED-X20P...")
    ntrip = GNSSNTRIPClient()
    ntrip.run(
        server=NTRIP_SERVER,
        port=NTRIP_PORT,
        mountpoint=NTRIP_MOUNTPOINT,
        ntripuser=NTRIP_USER,
        ntrippassword=NTRIP_PASSWORD,
        version="2.0",
        datatype="RTCM",        # NEAR mountpoint sends RTCM3 corrections
        ggamode=1,                # 1 = use fixed reference position
        ggainterval=10,           # Send GGA every 10 seconds
        reflat=46.729759000,      # TODO: set your latitude
        reflon=-100.694455333,    # TODO: set your longitude
        refalt=509.4000,          # TODO: set your altitude (m)
        output=ser,               # Write corrections to X20P serial port
        stopevent=stop,
    )

    try:
        while True:
            pass

    except KeyboardInterrupt:
        print("\nKeyboard interrupt received.")

        
    print("\nStopping stream...")
    stop.set()
    ntrip.stop()
