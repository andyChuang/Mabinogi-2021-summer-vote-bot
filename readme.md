# Mabinogi-2021-summer-vote

瑪奇仲夏躍動祭投票活動(https://event.beanfun.com/mabinogi/E20210715/Index.aspx)

目前功能會連續幫你登入所有帳號以及依序執行以下：
1. 每種類別固定投三票

## Quick Start
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
1. python play.py --cd _[[Waiting time between accounts in second]]_ --ignore _[[Ignored accounts split by comma]]_

## To-do
1. Vote report (為求保險, 可以看到有沒有哪個帳號其實沒投成功)

## Change Log


