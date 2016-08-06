import spidev
import time
from write_database import write_db

def adu(v_ref, bits):
    spi=spidev.SpiDev()
    spi.open(0,0)
    while True:
        antwort = spi.xfer([1,128,0])
        antwort=(antwort[1] * 256 + antwort[2])*(v_ref/(2**bits))
        write_db(antwort)
        time.sleep(1)

if __name__=="__main__":
    adu(5.0,10)
