from .hockeybot import HockeyBot


def setup(bot):
    h = HockeyBot(bot)
    bot.add_cog(h)
