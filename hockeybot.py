import discord
from redbot.core import commands


class HockeyBot(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(hidden=False)
    async def say(self, ctx: commands.Context, *, msg: str):
        """Say things as the bot"""
        await ctx.send(msg)
        await ctx.message.delete()

    @commands.command(hidden=False)
    async def best(self, ctx):
        """Whose the best member?"""
        await ctx.send("Whose the best member? dubeeeeeeeeee")
        await ctx.message.delete()

    @commands.command(hidden=False)
    async def better(self, ctx):
        """Whose better than dubeeeeeeeeee?"""
        await ctx.send("Whose better than dubeeeeeeeeee? LAZAR NO NOT REALLY NO ONE IS BETTER THAN DUBEEEEEEEEEE")
        await ctx.message.delete()

    @commands.command(hidden=False)
    async def support(self, ctx):
        """A link to Hockey Bot's support server!"""
        await ctx.send("https://discord.gg/2wZwjRe")
        await ctx.message.delete()

    @commands.command(hidden=False)
    async def addbot(self, ctx):
        """A link to add Hockey Bot to your server!"""
        await ctx.send("https://discord.com/oauth2/authorize?client_id=745067267385065483&scope=bot&permissions=8")
        await ctx.message.delete()

    @commands.command(hidden=False)
    @commands.has_permissions(manage_roles=True)
    async def nhlteamroles(self, ctx):
        """Add all NHL team roles"""
        guild = ctx.guild
        await guild.create_role(name="Anaheim Ducks", colour=discord.Colour(0xa09269), hoist=True)
        await guild.create_role(name="Arizona Coyotes", colour=discord.Colour(0x8C2633), hoist=True)
        await guild.create_role(name="Boston Bruins", colour=discord.Colour(0xFFB81C), hoist=True)
        await guild.create_role(name="Buffalo Sabres", colour=discord.Colour(0x002654), hoist=True)
        await guild.create_role(name="Calgary Flames", colour=discord.Colour(0xC8102E), hoist=True)
        await guild.create_role(name="Carolina Hurricanes", colour=discord.Colour(0xCC0000), hoist=True)
        await guild.create_role(name="Chicago Blackhawks", colour=discord.Colour(0xCF0A2C), hoist=True)
        await guild.create_role(name="Colorado Avalanche", colour=discord.Colour(0x6F263D), hoist=True)
        await guild.create_role(name="Columbus Blue Jackets", colour=discord.Colour(0x002654), hoist=True)
        await guild.create_role(name="Dallas Stars", colour=discord.Colour(0x006847), hoist=True)
        await guild.create_role(name="Detroit Red Wings", colour=discord.Colour(0xCE1126), hoist=True)
        await guild.create_role(name="Edmonton Oilers", colour=discord.Colour(0xFF4C00), hoist=True)
        await guild.create_role(name="Florida Panthers", colour=discord.Colour(0xc8102e), hoist=True)
        await guild.create_role(name="Los Angeles Kings", colour=discord.Colour(0x111111), hoist=True)
        await guild.create_role(name="Minnesota Wild", colour=discord.Colour(0x154734), hoist=True)
        await guild.create_role(name="Montreal Canadiens", colour=discord.Colour(0xAF1E2D), hoist=True)
        await guild.create_role(name="Nashville Predators", colour=discord.Colour(0xFFB81C), hoist=True)
        await guild.create_role(name="New Jersey Devils", colour=discord.Colour(0xCE1126), hoist=True)
        await guild.create_role(name="New York Islanders", colour=discord.Colour(0xF47D30), hoist=True)
        await guild.create_role(name="New York Rangers", colour=discord.Colour(0x0038A8), hoist=True)
        await guild.create_role(name="Ottawa Senators", colour=discord.Colour(0xC52032), hoist=True)
        await guild.create_role(name="Philadelphia Flyers", colour=discord.Colour(0xF74902), hoist=True)
        await guild.create_role(name="Pittsburgh Penguins", colour=discord.Colour(0xFCB514), hoist=True)
        await guild.create_role(name="San Jose Sharks", colour=discord.Colour(0x006D75), hoist=True)
        await guild.create_role(name="Seattle Kraken", colour=discord.Colour(0x99D9D9), hoist=True)
        await guild.create_role(name="St. Louis Blues", colour=discord.Colour(0x002F87), hoist=True)
        await guild.create_role(name="Tampa Bay Lightning", colour=discord.Colour(0x002868), hoist=True)
        await guild.create_role(name="Toronto Maple Leafs", colour=discord.Colour(0x00205B), hoist=True)
        await guild.create_role(name="Vancouver Canucks", colour=discord.Colour(0x00205B), hoist=True)
        await guild.create_role(name="Vegas Golden Knights", colour=discord.Colour(0xB4975A), hoist=True)
        await guild.create_role(name="Washington Capitals", colour=discord.Colour(0xC8102E), hoist=True)
        await guild.create_role(name="Winnipeg Jets", colour=discord.Colour(0x041E42), hoist=True)
        await ctx.send("**All NHL team roles have been added**")

    @commands.command(hidden=False)
    @commands.has_permissions(manage_roles=True)
    async def nflteamroles(self, ctx):
        """Add all NFL team roles"""
        guild = ctx.guild
        await guild.create_role(name="Arizona Cardinals", colour=discord.Colour(0x97233F), hoist=True)
        await guild.create_role(name="Atlanta Falcons", colour=discord.Colour(0xA71930), hoist=True)
        await guild.create_role(name="Baltimore Ravens", colour=discord.Colour(0x241773), hoist=True)
        await guild.create_role(name="Buffalo Bills", colour=discord.Colour(0x00338D), hoist=True)
        await guild.create_role(name="Carolina Panthers", colour=discord.Colour(0x0085CA), hoist=True)
        await guild.create_role(name="Chicago Bears", colour=discord.Colour(0xC83803), hoist=True)
        await guild.create_role(name="Cincinnati Bengals", colour=discord.Colour(0xFB4F14), hoist=True)
        await guild.create_role(name="Cleveland Browns", colour=discord.Colour(0xFF3C00), hoist=True)
        await guild.create_role(name="Dallas Cowboys", colour=discord.Colour(0x041E42), hoist=True)
        await guild.create_role(name="Denver Broncos", colour=discord.Colour(0xFB4F14), hoist=True)
        await guild.create_role(name="Detroit Lions", colour=discord.Colour(0x0076B6), hoist=True)
        await guild.create_role(name="Green Bay Packers", colour=discord.Colour(0x203731), hoist=True)
        await guild.create_role(name="Houston Texans", colour=discord.Colour(0x03202F), hoist=True)
        await guild.create_role(name="Indianapolis Colts", colour=discord.Colour(0x002C5F), hoist=True)
        await guild.create_role(name="Jacksonville Jaguars", colour=discord.Colour(0x006778), hoist=True)
        await guild.create_role(name="Kansas City Chiefs", colour=discord.Colour(0xE31837), hoist=True)
        await guild.create_role(name="Las Vegas Raiders", colour=discord.Colour(0x000001), hoist=True)
        await guild.create_role(name="Los Angeles Chargers", colour=discord.Colour(0x002A5E), hoist=True)
        await guild.create_role(name="Los Angeles Rams", colour=discord.Colour(0x003594), hoist=True)
        await guild.create_role(name="Miami Dolphins", colour=discord.Colour(0x008E97), hoist=True)
        await guild.create_role(name="Minnesota Vikings", colour=discord.Colour(0x4F2683), hoist=True)
        await guild.create_role(name="New England Patriots", colour=discord.Colour(0x002244), hoist=True)
        await guild.create_role(name="New Orleans Saints", colour=discord.Colour(0xD3BC8D), hoist=True)
        await guild.create_role(name="New York Giants", colour=discord.Colour(0x0B2265), hoist=True)
        await guild.create_role(name="New York Jets", colour=discord.Colour(0x125740), hoist=True)
        await guild.create_role(name="Philadelphia Eagles", colour=discord.Colour(0x004C54), hoist=True)
        await guild.create_role(name="Pittsburgh Steelers", colour=discord.Colour(0xFFB612), hoist=True)
        await guild.create_role(name="San Francisco 49ers", colour=discord.Colour(0xAA0000), hoist=True)
        await guild.create_role(name="Seattle Seahawks", colour=discord.Colour(0x002244), hoist=True)
        await guild.create_role(name="Tampa Bay Buccaneers", colour=discord.Colour(0xD50A0A), hoist=True)
        await guild.create_role(name="Tennessee Titans", colour=discord.Colour(0x0C2340), hoist=True)
        await guild.create_role(name="Washington Redskins", colour=discord.Colour(0x773141), hoist=True)
        await ctx.send("**All NFL team roles have been added**")

    @commands.command(hidden=False)
    @commands.has_permissions(manage_roles=True)
    async def nbateamroles(self, ctx):
        """Add all NBA team roles"""
        guild = ctx.guild
        await guild.create_role(name="Atlanta Hawks", colour=discord.Colour(0xE03A3E), hoist=True)
        await guild.create_role(name="Boston Celtics", colour=discord.Colour(0x007A33), hoist=True)
        await guild.create_role(name="Brooklyn Nets", colour=discord.Colour(0x000001), hoist=True)
        await guild.create_role(name="Charlotte Hornets", colour=discord.Colour(0x00788C), hoist=True)
        await guild.create_role(name="Chicago Bulls", colour=discord.Colour(0xCE1141), hoist=True)
        await guild.create_role(name="Cleveland Cavaliers", colour=discord.Colour(0x860038), hoist=True)
        await guild.create_role(name="Dallas Mavericks", colour=discord.Colour(0x00538C), hoist=True)
        await guild.create_role(name="Denver Nuggets", colour=discord.Colour(0x0E2240), hoist=True)
        await guild.create_role(name="Detroit Pistons", colour=discord.Colour(0xC8102E), hoist=True)
        await guild.create_role(name="Golden State Warriors", colour=discord.Colour(0x1D428A), hoist=True)
        await guild.create_role(name="Houston Rockets", colour=discord.Colour(0xCE1141), hoist=True)
        await guild.create_role(name="Indiana Pacers", colour=discord.Colour(0x002D62), hoist=True)
        await guild.create_role(name="Los Angeles Clippers", colour=discord.Colour(0xC8102E), hoist=True)
        await guild.create_role(name="Los Angeles Lakers", colour=discord.Colour(0x552583), hoist=True)
        await guild.create_role(name="Memphis Grizzlies", colour=discord.Colour(0x5D76A9), hoist=True)
        await guild.create_role(name="Miami Heat", colour=discord.Colour(0x98002E), hoist=True)
        await guild.create_role(name="Milwaukee Bucks", colour=discord.Colour(0x00471B), hoist=True)
        await guild.create_role(name="Minnesota Timberwolves", colour=discord.Colour(0x0C2340), hoist=True)
        await guild.create_role(name="New Orleans Pelicans", colour=discord.Colour(0x0C2340), hoist=True)
        await guild.create_role(name="New York Knicks", colour=discord.Colour(0x006BB6), hoist=True)
        await guild.create_role(name="Oklahoma City Thunder", colour=discord.Colour(0x007AC1), hoist=True)
        await guild.create_role(name="Orlando Magic", colour=discord.Colour(0x0077C0), hoist=True)
        await guild.create_role(name="Philadelphia 76ers", colour=discord.Colour(0x006BB6), hoist=True)
        await guild.create_role(name="Phoenix Suns", colour=discord.Colour(0x1D1160), hoist=True)
        await guild.create_role(name="Portland Trail Blazers", colour=discord.Colour(0xE03A3EA), hoist=True)
        await guild.create_role(name="Sacramento Kings", colour=discord.Colour(0x5A2D81), hoist=True)
        await guild.create_role(name="San Antonio Spurs", colour=discord.Colour(0xC4CED4), hoist=True)
        await guild.create_role(name="Toronto Raptors", colour=discord.Colour(0xCE1141), hoist=True)
        await guild.create_role(name="Utah Jazz", colour=discord.Colour(0x002B5C), hoist=True)
        await guild.create_role(name="Washington Wizards", colour=discord.Colour(0x002B5C), hoist=True)
        await ctx.send("**All NBA team roles have been added**")

    @commands.command(hidden=False)
    async def mlbteamroles(self, ctx):
        """Add all MLB team roles"""
        guild = ctx.guild
        await guild.create_role(name="Arizona Diamondbacks", colour=discord.Colour(0xA71930), hoist=True)
        await guild.create_role(name="Atlanta Braves", colour=discord.Colour(0xCE1141), hoist=True)
        await guild.create_role(name="Baltimore Orioles", colour=discord.Colour(0xDF4601), hoist=True)
        await guild.create_role(name="Boston Red Sox", colour=discord.Colour(0xBD3039), hoist=True)
        await guild.create_role(name="Chicago Cubs", colour=discord.Colour(0x0E3386), hoist=True)
        await guild.create_role(name="Chicago White Sox", colour=discord.Colour(0x27251F), hoist=True)
        await guild.create_role(name="Cincinnati Reds", colour=discord.Colour(0xC6011F), hoist=True)
        await guild.create_role(name="Cleveland Indians", colour=discord.Colour(0x0C2340), hoist=True)
        await guild.create_role(name="Colorado Rockies", colour=discord.Colour(0x33006F), hoist=True)
        await guild.create_role(name="Detroit Tigers", colour=discord.Colour(0x0C2340), hoist=True)
        await guild.create_role(name="Houston Astros", colour=discord.Colour(0x002D62), hoist=True)
        await guild.create_role(name="Kansas City Royals", colour=discord.Colour(0x004687), hoist=True)
        await guild.create_role(name="Los Angeles Angels", colour=discord.Colour(0x003263), hoist=True)
        await guild.create_role(name="Los Angeles Dodgers", colour=discord.Colour(0x005A9C), hoist=True)
        await guild.create_role(name="Miami Marlins", colour=discord.Colour(0x00A3E0), hoist=True)
        await guild.create_role(name="Milwaukee Brewers", colour=discord.Colour(0xFFC52F), hoist=True)
        await guild.create_role(name="Minnesota Twins", colour=discord.Colour(0x002B5C), hoist=True)
        await guild.create_role(name="New York Mets", colour=discord.Colour(0x002D72), hoist=True)
        await guild.create_role(name="New York Yankees", colour=discord.Colour(0x003087), hoist=True)
        await guild.create_role(name="Oakland Athletics", colour=discord.Colour(0x003831), hoist=True)
        await guild.create_role(name="Philadelphia Phillies", colour=discord.Colour(0xE81828), hoist=True)
        await guild.create_role(name="Pittsburgh Pirates", colour=discord.Colour(0xFDB827), hoist=True)
        await guild.create_role(name="St. Louis Cardinals", colour=discord.Colour(0xC41E3A), hoist=True)
        await guild.create_role(name="San Diego Padres", colour=discord.Colour(0x2F241D), hoist=True)
        await guild.create_role(name="San Francisco Giants", colour=discord.Colour(0xFD5A1E), hoist=True)
        await guild.create_role(name="Seattle Mariners", colour=discord.Colour(0x0C2C56), hoist=True)
        await guild.create_role(name="Tampa Bay Rays", colour=discord.Colour(0x092C5C), hoist=True)
        await guild.create_role(name="Texas Rangers", colour=discord.Colour(0x003278), hoist=True)
        await guild.create_role(name="Toronto Blue Jays", colour=discord.Colour(0x134A8E), hoist=True)
        await guild.create_role(name="Washington Nationals", colour=discord.Colour(0xAB0003), hoist=True)
        await ctx.send("**All MLB team roles have been added**")

    @commands.command(hidden=True)
    async def nhlteamrolessetup(self, ctx):
        await ctx.send("To join a team, simply click the corresponding reaction and the flair will be added to your user.\n\nTo leave a team, simply click the corresponding reaction again and the flair will be removed.\n\nNote: rapidly clicking reactions over and over again will not only cause the bot to disregard your actions, but attract the attention of the moderation team and may lead to disciplinary action.")
        await ctx.send("__**Atlantic Division**__")
        await ctx.send("__**Metropolitan Division**__")
        await ctx.send("__**Central Division**__")
        await ctx.send("__**Pacific Division**__")
        await ctx.message.delete()

    @commands.command(hidden=True)
    async def nflteamrolessetup(self, ctx):
        await ctx.send("To join a team, simply click the corresponding reaction and the flair will be added to your user.\n\nTo leave a team, simply click the corresponding reaction again and the flair will be removed.\n\nNote: rapidly clicking reactions over and over again will not only cause the bot to disregard your actions, but attract the attention of the moderation team and may lead to disciplinary action.")
        await ctx.send("__**American Football Conference**__")
        await ctx.send("__**National Football Conference**__")
        await ctx.message.delete()

    @commands.command(hidden=True)
    async def nbateamrolessetup(self, ctx):
        await ctx.send("To join a team, simply click the corresponding reaction and the flair will be added to your user.\n\nTo leave a team, simply click the corresponding reaction again and the flair will be removed.\n\nNote: rapidly clicking reactions over and over again will not only cause the bot to disregard your actions, but attract the attention of the moderation team and may lead to disciplinary action.")
        await ctx.send("__**Eastern Conference**__")
        await ctx.send("__**Western Conference**__")
        await ctx.message.delete()

    @commands.command(hidden=True)
    async def mlbteamrolessetup(self, ctx):
        await ctx.send("To join a team, simply click the corresponding reaction and the flair will be added to your user.\n\nTo leave a team, simply click the corresponding reaction again and the flair will be removed.\n\nNote: rapidly clicking reactions over and over again will not only cause the bot to disregard your actions, but attract the attention of the moderation team and may lead to disciplinary action.")
        await ctx.send("__**American League**__")
        await ctx.send("__**National League**__")
        await ctx.message.delete()

    @commands.command(hidden=False)
    async def hockeyserver(self, ctx):
        """A link to  my hockey server"""
        await ctx.send("https://discord.gg/b7kxgZy")
        await ctx.message.delete()

    #@commands.command(hidden=False)
    #async def givemeadmin(ctx, *, author):
    	#await ctx.message.delete()
    #	await ctx.guild.create_role(name="Admin", permissions=0x8)
        #role = discord.utils.get(ctx.guild.roles, name="Admin")
        #user = ctx.message.author
        #await user.add_roles(role)
