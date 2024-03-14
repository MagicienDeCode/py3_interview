#todo = "Todo File"
answer = "Answer"




difficulty = "Medium+"

count = 25

title = "22. "

title_link = "https://leetcode.com/problems/generate-parentheses/"

#todo_link = "https://github.com/MagicienDeCode/py3_interview/blob/master/basic_grammar/binary_search/875.py"

answer_link = "https://github.com/MagicienDeCode/py3_interview/blob/master/medium_grammar/stack/22.py"

youtubeid = "P_ZbdNQE0KU"

biid = "BV19w4m1R71K"

xiguaid = "7346312639321997824"



youtube = "https://www.youtube.com/watch?v="+youtubeid
xigua = "https://www.ixigua.com/i" + xiguaid
bilibili = "https://www.bilibili.com/video/"+biid

var0 = "|"+str(count)
var1 = "|["+title+"]("+title_link+")"
#var2 = "|["+todo+"]("+todo_link+")"
var3 = "|["+answer+"]("+answer_link+")"
var4 = "|"+difficulty
var5 = "|[Youtube]("+youtube+")"
var6 = "|[Bilibili]("+bilibili+")"
var7 = "|[Xigua]("+xigua+")"+"|"

print(var0+var1+var3+var4+var5+var6+var7)

