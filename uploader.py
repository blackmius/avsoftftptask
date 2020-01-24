import asyncio
import aioftp
import json

class Config(dict):
    """Reads json file with given path and represent as dict"""
    def __init__(self, path: str):
        with open(path, 'r') as json_config:
            data = json.load(json_config)
            self.update(data) 

class Uploader:
    """Сreates an uploader for a given configuration"""
    def __init__(self, config: Config):
        self.client = aioftp.Client()
        self.files = config.get('files', [])
        self.config = config

    async def _connect(self):
        host, port, username, password = map(
            lambda x: self.config.get(x, ''),
            ['host', 'port', 'username', 'password'])

        await self.client.connect(host, port)
        await self.client.login(username, password)

    async def upload(self):
        await self._connect()

        uploads = [ self.client.upload(f['src'], f['dst'], write_into=True) for f in self.files ]
        await asyncio.wait(uploads)    
        

if __name__ == '__main__':
    # not quite a multithreading
    loop = asyncio.get_event_loop()

    config = Config('./config.json')
    uploader = Uploader(config)

    loop.run_until_complete(uploader.upload())
    loop.close()
    
