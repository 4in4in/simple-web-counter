import os

import aiofiles


class SimpleFileCounter:

    current_value: int

    def __init__(
        self, 
        filename: str = "data/counter.txt"
    ) -> None:
        self.filename = filename
        self.__init_value_from_file()

    def __init_value_from_file(self):
        if os.path.exists(self.filename):
            with open(self.filename) as file:
                self.current_value = int(file.read())
        else:
            self.current_value = 0

    async def increment(self):
        self.current_value += 1
        await self.__write_to_file()

    async def __write_to_file(self):
        async with aiofiles.open(self.filename, "w") as file:
            await file.write(str(self.current_value))
