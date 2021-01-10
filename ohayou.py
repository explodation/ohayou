import discord,asyncio,subprocess
from random import choice
from time import sleep

client = discord.Client()

token = ""

dice = True
ohayou = False
fuck = ["曲者！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！"]
tables = []
class Table:
    def __init__(self,x,y,z,gam,prg,rea):
        self.members=x
        self.memberids=y
        self.tableid=z
        self.game=gam
        self.inprogress=prg
        self.ready=rea
class Chinchirorin:
    gameid = "chinchirorin"
    def __init__(self,score):
        self.scores = score
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.author.bot and message.author.id != 797553292497518632:
        return
    if message.content == "<@!558919170666790932>":
        await message.channel.send("おはようございます！`\"h`")
    if message.content == "\"kill" and message.author.id == 465104296430796812 or message.content == "\"kill" and message.author.id == 797553292497518632:
        await message.channel.send("あ……えっと……私、何かしました……？……ひぃっ！ごめんなさい、あっ、たすけ……")
        quit()
    if message.content == "\"update shanghai" and message.author.id == 465104296430796812:
        await message.channel.send("お前が死ぬんやで")
        await asyncio.sleep(1)
        subprocess.run("start \"shanghai\" py shanghai.py",shell=True)
    if message.content == "\"ohayou":
        global ohayou
        if ohayou == False:
            ohayou = True
            await message.channel.send("ohayou : `disabled`")
        else:
            ohayou = False
            await message.channel.send("ohayou : `enabled`")
    if ohayou:
        return

    #table

    global tables
    global nam
    nowtable = list(filter(lambda o:message.author.id in o.memberids,tables))
    nam = message.author.nick
    if nam == None:
        nam = message.author.name
    if message.content.startswith("fuckyoubitch"):
        print(message.content)
    if message.content.startswith("\"table ") and nowtable == []:
        try:
            tablename = message.content[7:]
        except IndexError:
            pass
        else:
            if list(filter(lambda w:w.tableid == tablename,tables)) == []:
                tables += [Table([message.author],[message.author.id],tablename,None,False,[False])]
                await message.channel.send("set up and joined `"+ tablename + "`")
            else:
                v = tables.index(list(filter(lambda w:w.tableid == tablename,tables))[0])
                tables[v].memberids += [message.author.id]
                tables[v].members += [message.author]
                tables[v].ready += [False]
                await message.channel.send("`" + nam + "` joined `"+ tablename + "`")
    elif message.content.startswith("\"table "):
        await message.channel.send("`" + nam + "` is arleady in `" + nowtable[0].tableid +"`")
    if message.content == ("\"tableinfo"):
        motherfucker = "tableid : `none`"
        if nowtable != []:
            mems = ""
            for mem in nowtable[0].members:
                if nowtable[0].members[0] == mem and mem.nick == None:
                    mems 
                elif mem.nick == None:
                    mems += mem.name
                else:
                    mems += mem.nick
            motherfucker = "tableid : `"+ nowtable[0].tableid +"`\nmembers: `"+ mems
        await message.channel.send()
    if message.content == "\"exit" and nowtable != []:
        v = tables.index(nowtable[0])
        w = tables[v].memberids.index(message.author.id)
        if nowtable[0].inprogress:
            await message.channel.send("`"+ nam +"` resigned `" + tables[v].tableid + " " + tables[v].game.gameid + "`")
        host = False
        if tables[v].memberids[0] == message.author.id:
            host = True
        del tables[v].ready[w]
        del tables[v].memberids[w]
        del tables[v].members[w]
        await message.channel.send("`" + nam + "` left from `" + tables[v].tableid + "`")
        if tables[v].members == []:
            motherfucker = tables[v].tableid
            del tables[v]
            await message.channel.send("removed `" + motherfucker + "`")
        elif host and tables[v].members[0].nick != None:
            await message.channel.send("`"+ tables[v].tableid +"` host has been `"+ tables[v].members[0].nick +"`")
        elif host:
            await message.channel.send("`"+ tables[v].tableid +"` host has been `"+ tables[v].members[0].name +"`")
    elif message.content == "\"exit":
        await message.channel.send("`" + nam + "` is not at any table")

    #dice
    
    if message.content == "\"dice":
        global dice
        if dice == False:
            dice = True
            await message.channel.send("dice : `enabled`")
        else:
            dice = False
            await message.channel.send("dice : `disabled`")
    if message.content.startswith("dice") and dice and "d" in message.content[5:] and message.content.endswith("="):
        put = ""
        putc = 0
        puta = 0
        while putc < int(message.content.split("d")[1][3:]):
            putaput = choice(range(1,int(message.content.split("d")[2].split("=")[0])+1))
            put += " " + str(putaput)
            putc += 1
            puta += putaput
        else:
            await message.channel.send("`" + message.content + "`" + put + " (" + str(puta) + ")")
    if message.content.startswith("ice") and dice and "d" in message.content[4:] and message.content.endswith("="):
        put = ""
        putc = 0
        puta = 1
        while putc < int(message.content.split("d")[0][3:]):
            putaput = choice(range(1,int(message.content.split("d")[1].split("=")[0])+1))
            put += " " + str(putaput)
            putc += 1
            puta *= putaput
        else:
            await message.channel.send("`" + message.content + "`" + put + " (" + str(puta) + ")")
    
    #ohayou

    if message.content == "おはよう":
        await message.channel.send("おはよう！！！！！１１！！１！１１１")
    if message.content == "ヤッホー！":
        await message.channel.send(choice(["Yahoo!","ヤフー！"]))
    if message.content == "バカヤロー！":
        await message.channel.send("何だとテメー！")
    if message.content == "すみませーん！":
        await message.channel.send("こちらこそー！")
    if message.content == "ヤマー！":
        await message.channel.send("カワー！")
    if message.content == "今何時ー！":
        await message.channel.send("そうね大体ねー！")
    if message.content == "いち足すいちはー？":
        await message.channel.send("……")
    if message.content == "\"h":
        await message.channel.send("dices : `\"hdice`\nmisc. : `\"hmisc`\ndeveloper commands : `\"hdev`\nabout shanghai : `\"hshanghai`\ncredits : `\"credit`")
    if message.content == "\"hdice":
        await message.channel.send("`\"dice` : dice、およびiceを無効/有効にします\n`dice[x]d[y]=` : [x]個の[y]面ダイスを振ります(加算)\n`ice[x]d[y]=` : [x]個の[y]面ダイスを振ります(乗算)")
    if message.content == "\"hmisc":
        await message.channel.send("`\"ohayou` : ohayouの機能を全般的に無効/有効にします\nその他`おはよう`等、特定の語句に反応することがあります")
    if message.content == "\"hdev":
        await message.channel.send("`\"kill(developer only)` : ohayouを終了します\n`\"update shanghai(developer only)` : shanghaiを再起動します")
    if message.content == "\"hshanghai":
        await message.channel.send("shanghaiはohayouの開発補助botです\n`\"shanghai>[x]` : [x]を喋らせます。ただしdeveloper onlyコマンドは使用できません\n`\"shanghei update(developer only)` : ohayouを再起動します")
    if message.content == "\"credit":
        await message.channel.send("develop : `Ectoplasm#3044(@explodation)`")

    #other
    
    if message.content.startswith("\"gyatei>") and message.author.id == 465104296430796812:
        pass
    if message.content == "↑お前自分のコメもう一度見返してみ":
        global fuck
        pass
    else:
        fuck += [[message.content,message.channel.id]]
    
client.run(token)
