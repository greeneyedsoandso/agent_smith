# Baby's First Slackbot #
*If running locally during development, skip ssh and scp commands*
## setup ##
**SSH to matrix**

`ssh -i your-pem.key opc@its.public.ip`

**one time venv creation**

`python -V`

use the python version in following command

`python3.6 -m venv ~/matrix`

**activate venv**

`source ~/matrix/bin/activate`

**get packages**

`pip3 install slack_bolt`

**on local machine**

`scp /Users/you/agent_smith/app.py opc@its.public.ip:~`

**one time setup**

set environment variables for 

SLACK_BOT_TOKEN, SLACK_APP_TOKEN, SLACK_SIGNING_SECRET

make app.py executable

**start script and safely exit ssh session without Agent Smith turning off**

`nohup ./app.py &`

`exit`

## Future ##

**SSH to matrix**

`ssh -i your-pem.key opc@its.public.ip`

**view script output, if any**

`nano nohup.out`
