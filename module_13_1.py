import asyncio
import time

async def start_strongman(name, power):

    print(f'Силач {name} начал соревнования')

    for i in range(1, 6):
        sleep_time = 10 // power
        await asyncio.sleep(sleep_time)
        print(f'Силач {name} поднял {i}')

    print(f'Силач {name} закончил соревнования')

async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Pasha', 3))
    task2 = asyncio.create_task(start_strongman('Denis', 4))
    task3 = asyncio.create_task(start_strongman('Apollon', 5))
    await task1
    await task2
    await task3

if __name__ == '__main__':
    time_start = time.time()
    asyncio.run(start_tournament())
    time_finish = time.time()
    print(time_finish - time_start)