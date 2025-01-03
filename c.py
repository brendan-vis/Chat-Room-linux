import asyncio
import aioconsole


async def async_input(writer):
    while True:
          # envoyer des données
        msg = await aioconsole.ainput("Entrez un message : ")
        writer.write(msg.encode())
        await writer.drain()

async def async_receive(reader):
      while True:
        # lire des données qui arrive du serveur
        data = await reader.read(1024)
        if data:
            # print("Il n'y a pas de msg")
            print(data.decode())
            
        # print(data.decode())


async def main():
    # ouvrir une connexion vers un serveur
    reader, writer = await asyncio.open_connection(host="localhost", port=8080)
    while True:
      tasks = [ async_input(writer), async_receive(reader) ]
      await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
