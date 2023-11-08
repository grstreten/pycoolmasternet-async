from pycoolmasternet_async import CoolMasterNet
import asyncio

cool = CoolMasterNet("coolmaster")

# Supply the IP address and optional port number (default 10102).
cool = CoolMasterNet("10.0.1.118", port=4196, read_timeout=1)


# async func
async def main():
    # General information
    info = await cool.info()

    # Returns a dict of CoolMasterNetUnit objects. Keys are the unit IDs
    units = await cool.status()


# run async func
asyncio.run(main())
