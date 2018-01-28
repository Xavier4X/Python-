import easygui as g
import sys

while 1:
    g.msgbox('(｡･∀･)ﾉﾞ嗨，欢迎进入第一个界面小游戏')

    msg = '你希望学到什么知识？'
    title = '小游戏互动'
    choices = ['love','编程','开车','琴棋书画']

    choice = g.choicebox(msg,title,choices)

    g.msgbox('你的选择是:'+ str(choice),'结果')

    msg = '你希望重新开始小游戏吗?'
    title = '请选择'

    if g.ccbox(msg,title):
        pass
    else:
        sys.exit(0)
