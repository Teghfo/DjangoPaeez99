import asyncio
import time

# async def sleep_async_hello():
#     print("hi")
#     await asyncio.sleep(2)
#     print("ashkan")


# async def main():
#     await asyncio.gather(sleep_async_hello(), sleep_async_hello())


# asyncio.run(main())


async def chess_play():
    for _ in range(5):
        time.sleep(2)
        print("herfei")
        await asyncio.sleep(10)
        print("amateur")


async def main():
    await asyncio.gather(chess_play(), chess_play(), chess_play(), chess_play(), chess_play(), chess_play())


start = time.time()
asyncio.run(main())

end = time.time()
zaman = end - start
print(f"zaman ejra {zaman}")
