from datetime import datetime
from git import Repo

async def git_pushing(bot, msg, repo_link, target_dir):
    cmt_channel = bot.get_channel(1239221685698166785) # https://discord.com/channels/1233687647302455306/1239221685698166785
    current_time = datetime.now().strftime("%d/%m/%Y-%H:%M")
    repo_name = repo_link.split('/')[-1]
    repo = Repo(target_dir)

    await msg.response.send_message("Staging changes...")
    repo.git.add('.')
    await msg.channel.send("Committing changes...")
    repo.git.commit('-m', f"Log commit - {current_time}")
    await msg.channel.send("Pulling changes from remote repository...")
    repo.git.pull('origin', 'main')
    await msg.channel.send("Pushing changes to remote repository...")
    repo.git.push('origin', 'main')
    
    await msg.channel.send("Finished!")
    await cmt_channel.send(f'{repo_name} has been updated {repo_link}')