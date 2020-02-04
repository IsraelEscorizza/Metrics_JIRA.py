import configparser
from openpyxl import Workbook
from openpyxl.styles import PatternFill, Border, Side, Alignment, Protection, Font

config = configparser.ConfigParser()
config.sections()
config.read('ProjectConfig.ini')
projectList = [config.options('Projects'),[config['Projects'][x] for x in config.options('Projects')]]

produc = config['Environment'].getboolean('prod')

if produc:
    #production
    base_jira = 'jiraproducao.xxxxx'
else:
    #homolog enviornment
    base_jira = 'jirahomolog.xxxxx'
base_url = 'http://' + base_jira + '.com.br/rest/atm/1.0/'
user = config['Login']['User']
password = config['Login']['Pass']
CONSUMER_KEY = 'CONSUMER_KEY'
RSA_KEY = open('HERE THE FILE .pem','r').read()
access_token = '[HERE YOUR TOKEN]'
access_token_secret = '[HERE YOUR TOKEN SECRET]'