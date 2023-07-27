import datetime, time, math, discord, os, dotenv, asyncio

dotenv.load_dotenv()

# constants
EVENT_ORIGIN = datetime.datetime(2014, 10, 4, 0, 00, tzinfo=datetime.timezone.utc).timestamp()

# env
CHANNEL_ID = int(os.environ.get("DISCORD_BOT_CHANNEL_ID"))
TOKEN = os.environ.get("DISCORD_BOT_TOKEN")

# methods
async def send_message(client):
    channel = client.get_channel(CHANNEL_ID)
    if channel:
        await channel.send("The Raven has appeared 💀💀💀")

def is_event_today():
    now = time.time()
    time_elapsed = now - EVENT_ORIGIN
    days_elapsed = math.floor(time_elapsed / 60 / 60 / 24)

    return days_elapsed % 13 == 0

async def run_bot(client):
    has_sent = False
    while True:
        appeared = is_event_today()
        if appeared and not has_sent:
            await send_message(client)
            has_sent = True
        if not appeared:
            has_sent = False
        await asyncio.sleep(2)

# bot
intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    await run_bot(client)

client.run(TOKEN)