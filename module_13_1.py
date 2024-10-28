import asyncio


async def start_tournament():
    task1 = asyncio.create_task(start_strongman("Ivan", 3.4))
    task2 = asyncio.create_task(start_strongman("Peter", 3))
    task3 = asyncio.create_task(start_strongman("Slava", 2))
    await task1
    await task2
    await task3


async def start_strongman(name, power):
    print(f"Силач {name} начал соревнования")
    for num in range(1, 6):
        await asyncio.sleep(1/power)
        print(f"Силач {name} поднял {num}")
    print(f"Силач {name} закончил соревнования")

if __name__ == "__main__":
    asyncio.run(start_tournament())

