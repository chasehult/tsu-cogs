from .padboard import PadBoard

__red_end_user_data_statement__ = "No personal data is stored persistantly."


async def setup(bot):
    await bot.add_cog(PadBoard(bot))
