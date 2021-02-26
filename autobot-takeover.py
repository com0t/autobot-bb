import os, requests, sys, time
from datetime import datetime

webhook = 'https://discord.com/api/webhooks/814389502608277524/d6s49TIDkhbca1FX2CPfVsyXNarKFIEcnpOkGOP090kpIjd-_hPPde4CvXQjqw-4P-fL'
data = {
        "content": "test"
        }
n = 40
importan = ['[AZURE]']

with open(sys.argv[1], 'r') as fp:
    content = fp.read()

if content:
    try:
        content = content.split('\n')
        content.remove('')
        contents = [content[i:i+n] for i in range(0,len(content), n)]

        with open('domain-takeover-bot.log', 'w+') as fp:
            c = 0
            for content in contents:
                content = '\n'.join([c for c in content])
                content = f'> **Block {c}**\n> **Date: {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}**\n' + content
                c += 1
                for i in importan:
                    content = content.replace(i, f'**{i}**')
                data["content"] = content
                resp = requests.post(webhook, json=data)

                if resp.status_code != 204:
                    print(resp.status_code)
                    print(resp.content)
                    fp.write(resp.content.decode('utf-8')+"\n---"+content+"\n\n\n")

                if (c+9)/30 == 0:
                    time.sleep(60)

    except Exception as e:
        print(e)
        pass
else:
    print("exit")