from .crowddata import CrowdData

__red_end_user_data_statement__ = "All explicitly stored user preferences are kept persistantly."


async def setup(bot):
    await bot.add_cog(CrowdData(bot))
