<h1>Project deployment</h1>
ansible-playbook -i inventory/hosts.yaml playbook.yaml

<h1>Code update</h1>
ansible-playbook -i inventory/hosts.yaml playbook.yaml --tags "update"

<h1>Logger usage</h1>
...<br>
logger = Logger()<br>
...<br>
@bot.message_handler(...)<br>
@logger.crash_log # handles exceptions<br> 
def some_function(message):<br>
    ...
    logger.log('log type ('INFO' or 'WARN')', 'log message')<br>

<h1>Project secret files</h1>
Make sure you have file named .env in your project directory with telegram bot token:

TELEGRAM_BOT_TOKEN=!TOKEN_DATA!