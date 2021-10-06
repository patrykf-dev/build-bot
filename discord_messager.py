from discord import Webhook, RequestsWebhookAdapter, Embed

import config


def send_message(builds, short_description):
    webhook = Webhook.from_url(config.bot_config["discord_hook"], adapter=RequestsWebhookAdapter())
    description = f"{short_description}\n\n"
    for build in builds:
        description += f"[{build[0]}]({build[1]})\n"
    embed = Embed()
    embed.title = "New builds!"
    embed.description = description
    webhook.send(embed=embed)
