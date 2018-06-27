import re

def emails(string):
    """
    This Function Finds all the Emails Address present in the String.
    It Returns a list of emails addresses using Regular Expression.
    :param string:
    :return Emails:
    """
    Emails = []
    if string:
        emailPattern = re.compile('(\w+[.|\w]*\w+@\w+[.]\w+[.|\w+]\w+)')
        Emails = re.findall(pattern=emailPattern, string=string)
        # print("Emails ------->", Emails)
    return Emails

def findObjectId(textString):
    """
    This Function Finds All the ObjectID present in the String.
    It Returns a list of ObjectId using Regular Expression.
    :param textString:
    :return object_ids:
    """
    object_ids = re.findall("([a-f\d]{24})",textString)
    return object_ids

def isHtml(text):
    """
    This Function Check if the Text input Contatins any HTML Tags or Elements.
    Return True or False
    :param text:
    :return output:
    """
    from bs4 import BeautifulSoup
    output = bool(BeautifulSoup(text, "html.parser").find())
    return output

def onlyDigits(text):
    """
    This Function Returns Only Digits from a Input Text String
    :param text:
    :return output:
    """
    output = re.findall(r'\d+',text)
    return output

def phoneNumbers(string):
    """
    This Function All the Phone Numbers from A String Using Regular Expression.
    It Returns a list of Phone Numbers from a Text String.
    :param string:
    :return PhoneNumbers :
    """
    PhoneNumbers = []
    if string:
        phonePattern = re.compile("(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})")
        PhoneNumbers = re.findall(pattern=phonePattern, string=string)
    return PhoneNumbers

def removeNonAscii(s):
    """
    This Function Remove all the Non-Ascii Characters from Input String.
    It Returns a String without Ascii Characters
    :param s:
    :return output:
    """
    output = "".join(i for i in s if ord(i) < 128)
    return output

def removePunctuation(string):
    """
    This Function Remove All the Non-Alphabet Words from a Sentence String.
    It Returns a List of All the Alphabet Characters from Input.
    :param string:
    :return output:
    """
    output = re.findall(re.compile(r'(\w+)'),string)
    return output

def websites(string):
    """
    This Function is Used to findallthe Website type data from a string.
    It Returns a list of all the websites if presents in the string.
    :param string:
    :return websitez:
    """
    websitez = []
    if string:
        websitePattern = r'(?i)\b((?:[a-z][\w-]+:(?:/{1,3}|[a-z0-9%])|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))'
        website = re.findall(websitePattern,string)
        for web in website:
            for websit in web:
                if websit:
                    websitez.append(websit)
    return websitez

def replaceDigits(string,replacewith):
    """
    This Function is to remove Digits with Some Input.
    :param string:
    :param replacewith:
    :return output:
    """
    output = re.sub("\d", replacewith, string)
    return output
