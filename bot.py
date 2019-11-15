import discord
import json
import InvalidInputException
from random import randint

with open('auth.json') as json_file:
    data = json.load(json_file)
    token = data['token']

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
        self.data = json.load(open('user-data.json'))

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == '!balance':
            if (str(message.author.id) not in self.data):
                self.data[str(message.author.id)]["coins"] = 500
                await message.channel.send("You have " + str(self.data[str(message.author.id)]["coins"]) + " coins")  
            else:
                await message.channel.send("You have " + str(self.data[str(message.author.id)]["coins"]) + " coins")
        elif '!gamble' in message.content:
            command = message.content.split(' ')
            try:
                amount = int(command[1])
                if amount < 0:
                    raise Exception()
                elif amount > balance:
                    await message.channel.send("You don't have enough coins!")
                    return 
            except Exception():
                await message.channel.send("Please enter a valid amount.")
                return
            balance = self.data[str(message.author.id)]["coins"]  
            result = randint(0, 9)
            if result != 5:
                result = f"You lost {amount} coins. "
                amount = -amount
            else:
                result = f"You won {amount} coins! "
            self.data[str(message.author.id)]["coins"] = balance + amount
            await message.channel.send(result + "Your new balance is " + str(self.data[str(message.author.id)]["coins"]) + " coins.") 
        elif '!buy' in message.content: 
            command = message.content.split(' ')
            item = command[1]
            if item == "title":
                
        elif message.content == '!end':
            with open('user-data.json', 'w') as to_write:
                json.dump(self.data, to_write)
            await self.logout()
            print("Logging off...")
              

client = MyClient()
client.run(token)
