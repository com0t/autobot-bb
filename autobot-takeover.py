import os, requests, sys, time, re
from datetime import datetime

takeover = 'https://discord.com/api/webhooks/814389502608277524/d6s49TIDkhbca1FX2CPfVsyXNarKFIEcnpOkGOP090kpIjd-_hPPde4CvXQjqw-4P-fL'
nuclei = 'https://discord.com/api/webhooks/815248081229709372/HQiNhX2LOLii4B7k49D9M67t7RnXBqqEpS9JCgimal9NL4zhlgEuVe9WN5GL3fKsW8g3'

data = {
        "content": "test"
        }
n = 40
importan = ['[AZURE]']
content = 'empty'

if len(sys.argv) < 3:
    print(f'{sys.argv[0]} takeover|nuclei file-result.txt') 
    exit(1)

if sys.argv[1] == 'takeover':
    url = takeover
elif sys.argv[1] == 'nuclei':
    url = nuclei

with open(sys.argv[2], 'r') as fp:
    content = fp.read()

if content:
    try:
        contents = content.split('\n')
        try:
            contents.remove('')
        except:
            pass
        
        start = 0
        end = 1
        count = 0
        with open('domain-takeover-bot.log', 'w+') as fp:
            while end <= len(contents):
                content = '\n'.join([c for c in contents[start:end]])
                if len(content) < 2000 and end <= len(contents):
                    end += 1
                    continue

                end -= 1
                content = '\n'.join([c for c in contents[start:end]])
                start = end

                content = f'> **Block {count}**\n> **Date: {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}**\n' + content
                count += 1
                for i in importan:
                    content = content.replace(i, f'**{i}**')
                data["content"] = content
                resp = requests.post(url, json=data)

                if resp.status_code != 204:
                    print(resp.status_code)
                    print(resp.content)
                    fp.write(resp.content.decode('utf-8')+"\n---"+content+"\n\n\n")
                    if resp.status_code == 429:
                        m = re.match('"retry_after": (.*)', resp.content.decode('utf-8'))
                        time.sleep(m.groups()[0])

                if (count+9)/30 == 0:
                    time.sleep(60)

    except Exception as e:
        print(e)
        pass
else:
    print("exit")