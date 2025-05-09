message=input(">")
words=message.split(' ')
output=""
emojis={
    ":)":"😀",
    "xD":"😉",
    "XD":"😉",
    "xd":"😉",
    ";)":"😉",
    ":(":"😔",
    "-_-":"😑",
    ">_<":"😣",
    "lol":"😂",
    "hehe":"😅"
}
for i in words:
    output+=emojis.get(i, i) + " "
print(output)
