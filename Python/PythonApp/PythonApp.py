#基于概率统计的文本分析

#统计分析文本内容。首先需要使用ngram模型来把文章进行分词并统计频率。因为文章生成主要依据马尔可夫模型，所以使用了2-gram，这样可以统计出一个单词出现在另一个单词后的概率。生成新文章是基于分析大量随机事件的马尔可夫模型。随机事件的特点是在一个离散事件发生之后，另一个离散事件将在前一个事件的条件下以一定的概率发生。
#————————————————
#原文链接：https://blog.csdn.net/qq_31258245/article/details/78743966

from random import randint
import re


def buildWordDict(text):
    text = re.sub('(\n|\r|\t)+', " ", text)
    text = re.sub('\"', "", text)

    punctuation = [',', '.', ';', ':']
    for symbol in punctuation:
        text = text.replace(symbol, " " + symbol + " ")

    words = text.split(' ')

    words = [word for word in words if word != ""]
    wordDict = {}
    for i in range(1, len(words)):
        if words[i-1] not in wordDict:
            wordDict[words[i-1]] = {}
        if words[i] not in wordDict[words[i-1]]:
            wordDict[words[i-1]][words[i]] = 0
        wordDict[words[i-1]][words[i]] = wordDict[words[i-1]][words[i]] + 1

    return wordDict



def randomFirstWord(wordDict):
    randomIndex = randint(0, len(wordDict))
    return list(wordDict.keys())[randomIndex]


def retrieveRandomWord(wordList):

    randomIndex = randint(1, wordListSum(wordList))
    for word, value in wordList.items():
        randomIndex -= value
        if randomIndex <= 0:
            return word

def wordListSum(wordList):
    sum = 0
    for word, value in wordList.items():
        sum = sum + value
    return sum


text = """ 
我曾经,爱过你：爱情，也许
在我的心灵里,还没有完全消亡，
但愿,它不会,再打扰你，
我也不想,再使你难过悲伤。
世界上,最遥远的距离
世界上,最遥远的距离
不是,生与死
而是,我就站在你的面前
你却不知道,我爱你
世界上,最遥远的距离
不是我站在你面前
你却不,知道,我爱你
而是,明明知道,彼此相爱
却不能,在一起
世界上,最遥远的距离
不是,明明知道,彼此相爱
却不能,在一起
而是,明明无法抵挡,这股想念
却还得,故意装作,丝毫没有,把你放在心里
世界上,最遥远的距离
不是,明明无法,抵挡这股想念
却还得,故意装作,丝毫没有,把你放在心里
而是,用己冷漠的心
为爱你的人,挖掘了一条无法跨越的沟渠.
"""


wordDict = buildWordDict(text)

length = 100
chain = ""
currentWord = randomFirstWord(wordDict)
for i in range(0, length):
    chain += currentWord + " "
    currentWord = retrieveRandomWord(wordDict[currentWord])

print(chain)
