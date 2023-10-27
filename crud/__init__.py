from .crud import Crud

__red_end_user_data_statement__ = "User email addresses are stored persistently."


async def setup(bot):
    await bot.add_cog(Crud(bot))
