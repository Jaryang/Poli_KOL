import zhon.hanzi as hanzi
import pandas as pd
import jieba
import re

PUNC = hanzi.punctuation
with open("data/baidu_stopwords.txt") as f:
    STOPWORDS = [line.strip() for line in f.readlines()]

EXTRA_STOPWORDS = ['…','全文','链接','我们','他们','自己','一个','没有','问题','这个','进行','时间','已经','今天','就是','认为','可以','因为','不是','网页','目前',
          '日前','什么','一直','你们','看到','表示','到底','一点','没想到','知道','最后','网友','至少','一起','两个','通过','包括','今年','任何','来说','网上',
          '一张','近日','为了','这一','其他','指出','一只','事情','如今','行为','一位','使用','小时','即将','所以','其中','获得','一段','重新','上午','提供',
           '对此','过去','以及','当时','那些','任何','还有','最近','大家','即将','除了','终于','发生','三个','两名','分钟','不明','每年','瞬间','造成',
           '正在','这样','怎样','几乎','带来','甚至','不能','虽然','完全','每天','看看','一份','但是','昨晚','为什么','小时','本月','同样',
          'via','截止','容易','时刻','不到','刚刚','VS','下面','更是','原来','微博','...']

STOPWORDS.extend(EXTRA_STOPWORDS)


def read_dta(filepath):
    """
    Load data set and transform the date type
    """
    
    tweet_dta = pd.read_csv(filepath, index_col=[0])
    tweet_dta['date'] = pd.to_datetime(tweet_dta['date'])
    
    return tweet_dta
          

def strip_line(text_lst):
    """
    Strip each line of the text list and eliminate empty strings
    
    Inputs:
        text_lst: a list of strings
    Outputs:
        new_lst: a cleaned list of strings
    """
    new_lst = []
    
    for text in text_lst:
        text = re.sub(r"[%s]+" %PUNC, "", text) # eliminate punctuations
        text = re.sub(r"[\s|\d]+", "", text) # eliminate whitespace & digits
        text = text.strip()
        if text != "":
            new_lst.append(text)
    
    return new_lst


def tokenize(text):
    """
    Tokenize the text
    
    Inputs: 
        text: string
    Outputs: a list of tokens
    """
    
    return jieba.lcut(text)


def get_tokens(text_lst):
    """
    Tokenize each text and store them in an integrated list
    
    Inputs:
        text_lst: a list of strings
    Outputs:
        token_lst: a list of lists containing the tokens
    """
    
    token_lst = []
    text_lst = strip_line(text_lst)
    
    for text in text_lst:
        sub_lst = []
        
        tokens = tokenize(text)
            
        for token in tokens:
            if (token not in STOPWORDS) and (token not in PUNC) \
                and len(token) > 1 and re.match(r'哈+', token) == None:
                sub_lst.append(token)
        
        token_lst.extend(sub_lst)
    
    return token_lst


def df_to_dict(tweet_dta):
    """
    Transform the data frame to a list of dicts with keys including
    'date','tweet', and 'related_news'
    
    Inputs:
        tweet_dta: a pd.DataFrame
    Outputs:
        tweet_dict_lst:  a list of dicts
    """
    
    tweet_dict_lst = []
    
    for _, date, tweet, news in tweet_dta.itertuples():
        tweet_dict = dict()
        tweet_dict['date'], tweet_dict['tweet'], tweet_dict['news'] = date, tweet, news
        tweet_dict['tokens'] = get_tokens([tweet, news])
        tweet_dict_lst.append(tweet_dict)
    
    return tweet_dict_lst
        

def tokenize_data(tweet_dta):
    """
    Return tweet data in the form of pd.DataFrame and a list of dictionaries
    """
    
    tweet_dict_lst = df_to_dict(tweet_dta)

    return tweet_dict_lst
