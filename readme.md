# Mabinogi-2021-summer-vote

瑪奇仲夏躍動祭投票活動(https://event.beanfun.com/mabinogi/E20210715/Index.aspx)

目前功能：
1. 每種類別固定投三票
2. 支援多帳號

## 使用說明
### 選項一、直接下載[最新版本執行檔](https://github.com/andyChuang/Mabinogi-2021-summer-vote-bot/releases/tag/1.0.0)
1. 下載Mabinogi-2021-summer-vote.zip並解壓縮
2. 在同Mabinogi-2021-summer-vote資料夾內建立`account.json`，格式如下：
```
[
{
"account": "帳號1",
"password": "密碼1",
"game_account": "遊戲帳號1"
},
{
"account": "帳號2",
"password": "密碼2",
"game_account": "遊戲帳號2"
},
.
.
.
{
"account": "帳號N",
"password": "密碼N",
"game_account": "遊戲帳號N"
}
]
```
3. 在同Mabinogi-2021-summer-vote資料夾內建立`vote.json`，設定你想要投的作品名稱，格式如下：
```
{
	"1": ["神繪一手作品名稱1", "神繪一手作品名稱2", "神繪一手作品名稱3"], 
	"2": ["絕景特攝作品名稱1", "絕景特攝作品名稱2", "絕景特攝作品名稱3"],
	"3": ["超絕穿搭作品名稱1", "超絕穿搭作品名稱2", "超絕穿搭作品名稱3"],
	"4": ["浪漫憧憬作品名稱1", "浪漫憧憬作品名稱2", "浪漫憧憬作品名稱3"],
	"5": ["Coser演舞作品名稱1", "Coser演舞作品名稱2", "Coser演舞作品名稱3"],
	"6": ["談音高唱作品名稱1", "談音高唱作品名稱2", "談音高唱作品名稱3"]
}
```
4. 執行Mabinogi-2021-summer-vote.exe

### 選項二、如果你擔心我會偷你的帳密，你可以直接下載原始碼，檢查過後再用
1. 首先你要有裝python3 (建議3.7)
1. Clone this repository to wherever you want
1. `cd Mabinogi-2021-summer-vote`
1. `pip install -r requirement.txt`
1. 同目錄下建立`account.json`，格式如下：
```
[
{
"account": "帳號1",
"password": "密碼1",
"game_account": "遊戲帳號1"
},
{
"account": "帳號2",
"password": "密碼2",
"game_account": "遊戲帳號2"
},
.
.
.
{
"account": "帳號N",
"password": "密碼N",
"game_account": "遊戲帳號N"
}
]
```
1. 在同Mabinogi-2021-summer-vote資料夾內建立`vote.json`，設定你想要投的作品名稱，格式如下：
```
{
	"1": ["神繪一手作品名稱1", "神繪一手作品名稱2", "神繪一手作品名稱3"], 
	"2": ["絕景特攝作品名稱1", "絕景特攝作品名稱2", "絕景特攝作品名稱3"],
	"3": ["超絕穿搭作品名稱1", "超絕穿搭作品名稱2", "超絕穿搭作品名稱3"],
	"4": ["浪漫憧憬作品名稱1", "浪漫憧憬作品名稱2", "浪漫憧憬作品名稱3"],
	"5": ["Coser演舞作品名稱1", "Coser演舞作品名稱2", "Coser演舞作品名稱3"],
	"6": ["談音高唱作品名稱1", "談音高唱作品名稱2", "談音高唱作品名稱3"]
}
```
7. python play.py --cd _[[Waiting time between accounts in second]]_ --ignore _[[Ignored accounts split by comma]]_   可以都不帶

## To-do
1. Vote report (為求保險, 可以看到有沒有哪個帳號其實沒投成功)

## Change Log
### 20210722
支援設定自己想要投的作品


