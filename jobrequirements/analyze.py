import pandas as pd
import plotly.express as px
import re

def dataAnalyst():
    keywords = [""]

    df = pd.read_csv("jobscrapy/dataanalyst_jobreq.csv")
    wordDict = {}
    for html in df["html"]:
        words = html.replace("|", "").split(" ")
        for word in words:
            sWord = str(word)
            if sWord in wordDict:
                wordDict[sWord] = wordDict[sWord] + 1
            else:
                wordDict[sWord] = 1

    sortedDict = dict(sorted(wordDict.items(), key=lambda item: item[1]))
    present = {
        "SAS":sortedDict["SAS"],
        "R":sortedDict["R"],
        "Python":sortedDict["Python"] + sortedDict["python"],
        "Tableau":sortedDict["Tableau"],
        "PowerBI":sortedDict["BI"] + sortedDict["PowerBI"],
        "Excel":sortedDict["Excel"] + sortedDict["excel"],
        "SQL":sortedDict["SQL"] + sortedDict["sql"],
        "Java":sortedDict["Java"],
        "Hadoop":sortedDict["Hadoop"],
        "Spark":sortedDict["Spark"],
        "NoSQL":sortedDict["NoSQL"]
    }
    keys, values = zip(*present.items())
    df2 = pd.DataFrame.from_dict({"key":keys, "count":values})
    fig = px.bar(df2, x="key", y="count", title="Keywords For Data Analyst", color=df2["key"])
    fig.update_xaxes(categoryorder="total ascending")
    fig.show()
    
def dataEngineer():
    keywords = [""]

    df = pd.read_csv("jobscrapy/dataengineer_jobreq.csv")
    wordDict = {}
    for html in df["html"]:
        words = html.replace("|", "").split(" ")
        for word in words:
            sWord = str(word)
            if sWord in wordDict:
                wordDict[sWord] = wordDict[sWord] + 1
            else:
                wordDict[sWord] = 1
        
    sortedDict = dict(sorted(wordDict.items(), key=lambda item: item[1]))
    
    present = {
        "SAS":sortedDict["SAS"],
        "R":sortedDict["R"],
        "Python":sortedDict["Python"] + sortedDict["python"],
        "Tableau":sortedDict["Tableau"] + sortedDict["tableau"],
        "PowerBI":sortedDict["BI"] + sortedDict["PowerBI"],
        "Excel":sortedDict["Excel"] + sortedDict["excel"],
        "SQL":sortedDict["SQL"] + sortedDict["sql"],
        "C/C++":sortedDict["C++"] + sortedDict["C"],
        "Java":sortedDict["Java"] + sortedDict["java"],
        "Hadoop":sortedDict["Hadoop"] + sortedDict["hadoop"],
        "Spark":sortedDict["Spark"] + sortedDict["spark"],
        "NoSQL":sortedDict["NoSQL"]
    }
    keys, values = zip(*present.items())
    df2 = pd.DataFrame.from_dict({"key":keys, "count":values})
    fig = px.bar(df2, x="key", y="count", title="Keywords For Data Engineer", color=df2["key"])
    fig.update_xaxes(categoryorder="total ascending")
    fig.show()
    
def dataScientist():
    keywords = [""]

    df = pd.read_csv("jobscrapy/datascientist_jobreq.csv")
    wordDict = {}
    for html in df["html"]:
        words = html.replace("|", "").split(" ")
        for word in words:
            sWord = str(word)
            if sWord in wordDict:
                wordDict[sWord] = wordDict[sWord] + 1
            else:
                wordDict[sWord] = 1
        
    sortedDict = dict(sorted(wordDict.items(), key=lambda item: item[1]))
    
    present = {
        "SAS":sortedDict["SAS"],
        "R":sortedDict["R"],
        "Python":sortedDict["Python"] + sortedDict["python"],
        "Tableau":sortedDict["Tableau"],
        "PowerBI":sortedDict["BI"] + sortedDict["PowerBI"],
        "Excel":sortedDict["Excel"] + sortedDict["excel"],
        "SQL":sortedDict["SQL"],
        "C/C++":sortedDict["C++"] + sortedDict["C"],
        "Java":sortedDict["Java"],
        "Hadoop":sortedDict["Hadoop"] + sortedDict["hadoop"],
        "Spark":sortedDict["Spark"],
        "NoSQL":sortedDict["NoSQL"]
    }
    keys, values = zip(*present.items())
    df2 = pd.DataFrame.from_dict({"key":keys, "count":values})
    fig = px.bar(df2, x="key", y="count", title="Keywords For Data Scientist", color=df2["key"])
    fig.update_xaxes(categoryorder="total ascending")
    fig.show()

dataAnalyst()
dataScientist()
dataEngineer()