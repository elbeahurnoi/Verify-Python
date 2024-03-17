import discord
from discord.ext import commands

# Configuración
TOKEN = 'tu_token_de_discord'
VERIFICATION_ROLE_NAME = 'Verified'

# Crear el bot
bot = commands.Bot(command_prefix='!')

# Evento de inicio
@bot.event
async def on_ready():
    print(f'¡Bot iniciado como {bot.user}!')

# Comando de verificación
@bot.command()
async def verify(ctx):
    # Verificar si el autor del mensaje ya tiene el rol de verificación
    if any(role.name == VERIFICATION_ROLE_NAME for role in ctx.author.roles):
        await ctx.send('¡Ya estás verificado!')
    else:
        # Crear un nuevo rol de verificación si no existe
        verification_role = discord.utils.get(ctx.guild.roles, name=VERIFICATION_ROLE_NAME)
        if not verification_role:
            verification_role = await ctx.guild.create_role(name=VERIFICATION_ROLE_NAME)

        # Asignar el rol de verificación al autor del mensaje
        await ctx.author.add_roles(verification_role)
        await ctx.send('¡Te has verificado exitosamente!')

# Manejo de errores
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Comando no encontrado.')

# Iniciar el bot
bot.run(TOKEN)
