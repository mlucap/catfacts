# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.2.0] - Custom prefixes - 2020-08-14

### Added

- Custom prefixes. Allows server admins to change the prefix to their liking. Tagging the bot will display it's current prefix
- Prefixes.json file to store prefixs. May change this to some sort of database in the near future, this file works for the time being
- New presence statuses.

### Changed

- Updated help command embed


## [1.1.1] - Custom Help Command! - 2020-08-02

### Added

- Custom help command. Now returns a nice looking embed.
- Uptime command. Allows users to check how long the bot has been online for.
- Vote command. Returns no URL yet. Awaiting approval from top.gg.

### Changed

- Bot now changes status every 10 seconds from 60 (60s->10s). In the future I plan on adding other status messages, as for right now this is to update the number of guilds the bot is showing on its status.


### Removed

- Default help command.


## [1.1.0] - Core command update - 2020-08-02

### Added

- All core commands, these include: bug, catfact, github, and the support command. Also added an error module that notifies users when a command is on cooldown
- Bot has been submitted to [Top.gg](https://top.gg/)

### Changed

- Changed the catfact command to use an embed now instead of just text.
- Hosting now on a vps
### Removed

- Procfile.

### Plans

- Custom help command. Although not needed, a custom and better looking help command would fit really nice with the bot.


## [1.0.0] - Initial Release - 2020-07-31

### Added

- All initial files
- Framework for the 'catfact' command and subsequent commands

### Plans
- Submit bot to [Top.gg](https://top.gg/)


[1.0.0]: https://github.com/mlucap/catfacts
[1.1.0]: https://github.com/mlucap/catfacts/blob/master/cogs/
[1.1.1]: https://github.com/mlucap/catfacts/blob/master/cogs/help.py
[1.2.0]: https://github.com/mlucap/catfacts/blob/master/cogs/prefix.py
