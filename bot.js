var Discord = require("discord.js");
var auth = require("./auth.json");
// Initialize Discord Bot
const bot = new Discord.Client();
//bot.on("ready", function(evt) {});
bot.on("message", msg => {
  if (msg.content.startsWith("!gamble")) {
    const user = msg.author;
    msg.reply("You win this time!");
  }
});
bot.login(auth.token);
