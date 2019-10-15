import asyncio

async def Cikartma(Sayi,SayiOrjinal):
    while True:
        Sayi-=10
        if Sayi % 50000 == 0:
            await asyncio.sleep(0.00000000001)
        if Sayi == 0:
            return print("Gönderdiniz {} üzerinde işlem yapıldı ve sonuç {}".format(SayiOrjinal,Sayi))


async def main():
    await asyncio.gather(

     Cikartma(10000000,10000000),
     Cikartma(1000000,1000000),
     Cikartma(100000,100000))


asyncio.run(main())