# ? ------------------------- Imports --------------------------------
# ? built-in modules


# ? Third Party Module
# * nextcord module
import nextcord
from nextcord import Interaction
from nextcord.ext import commands

# ? custom module


# ? ------------------------- Main Class -----------------------------
class hellocmd(commands.Cog):
    def __init__(self, client):
        self.client = client

# ? ------------------------- Main Code ------------------------------
# * ------------------------- Hello Command --------------------------
    @nextcord.slash_command(name="hello", description="Say hello")
    async def cash_transfer(self, interaction: Interaction):
        embed = nextcord.Embed(
                        title=f"Hey {interaction.user.name}",
                        color=nextcord.Colour.green()
                    )
        await interaction.send_message(embed=embed)

# ? ------------------------- setup function -------------------------
def setup(client):
    client.add_cog(hellocmd(client))