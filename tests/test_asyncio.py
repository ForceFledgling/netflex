import asyncio

async def telnet_client(host, port):
    reader, writer = await asyncio.open_connection(host, port)

    async def send_telnet_command(command, option=b''):
        writer.write(b'\xff' + command + option)
        await writer.drain()

    async def handle_telnet_command(data):
        # Обработка полученных TELNET-команд от сервера
        print(f'Received TELNET command: {data}')

    # Отправляем команду "echo" (WILL ECHO)
    await send_telnet_command(b'\xfb', b'\x01')

    # Отправляем данные
    writer.write(b'Hello, server!\r\n')
    await writer.drain()

    while True:
        # Получаем ответ
        data = await reader.read(100)
        if not data:
            break

        # Проверяем наличие TELNET-команд в ответе
        if data.startswith(b'\xff'):
            await handle_telnet_command(data)
        else:
            print(f'Received: {data.decode()}')

    # Закрываем соединение
    writer.close()
    await writer.wait_closed()

HOST = '10.2.18.88'
asyncio.run(telnet_client(HOST, 23))
