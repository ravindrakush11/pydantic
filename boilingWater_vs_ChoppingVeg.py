import asyncio

async def boiling_water():
    print("Boiling water...")
    await asyncio.sleep(2)
    print("Water boiled")

async def vegetable_chopping():
    print("Chopping vegetable...")
    await asyncio.sleep(1)
    print("chopped vegetable")


async def main():
    await asyncio.gather(boiling_water(), vegetable_chopping())

asyncio.run(main())