import discord
from discord.ext import commands

# Configuración
TOKEN = 'token'
VERIFICATION_ROLE_NAME = 'Verified'

# Crear el bot
bot = commands.Bot(command_prefix='!', intents=discord.Intents().all())

# Evento de inicio
@bot.event
async def on_ready():
    print(f'¡Bot iniciado como {bot.user}!')

# Comando de verificación
@bot.command()
async def verify(ctx):
    # Verificar si el autor del mensaje ya tiene el rol de verificación
    if any(role.name == Verified for role in ctx.author.roles):
        await ctx.send('¡Ya estás verificado!')
    else:
        # Crear un nuevo rol de verificación si no existe
        verification_role = discord.utils.get(ctx.guild.roles, name=Verified)
        if not verification_role:
            verification_role = await ctx.guild.create_role(name=Verified)

        # Asignar el rol de verificación al autor del mensaje
        await ctx.author.add_roles(Verified)
        await ctx.send('¡Te has verificado exitosamente!')

# Manejo de errores
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Comando no encontrado.')

# Iniciar el bot
bot.run('token')
