import os
import json
import urllib2

class C_Riot_retrieval:
    _api_key=''
    _sName=''
    _summonerObj=None
    _recentGameObj=None
    
    def __init__(self,API_KEY,summonerName):       
        self._api_key = API_KEY
        self._sName = summonerName
        self.retrieve_summonerOBJ()        
        
        if self._summonerObj is None:
            print 'Warning: Unable to retrieve summoner info'            
        
        self.get_RecentGame()        
        if self._recentGameObj is None:
            print 'Warning: Unable to retrieve recent games info'
        
    def getRestResp(self,url):
        """ use urllib2 and json loads to fetch the data from RIOT """
        if not url or url is None:
            print 'No Url provided'
            return None
        _userResp = urllib2.urlopen(url, timeout=30).read()
        return json.loads(_userResp)      
        
    def print_summonerID(self):
        """ print summoner id of the summonername provided"""        
        print 'summoner id=',self._summonerObj['id']        
        return self._summonerObj['id']        
    
    def retrieve_summonerOBJ(self):
        """ Retrieve summonerID from the summoner name given"""
        _baseNameUrl='http://prod.api.pvp.net/api/lol/na/v1.1/summoner/by-name/'
        print 'api key=',self._api_key
        url=_baseNameUrl + self._sName + '?api_key=' + self._api_key        
        self._summonerObj = self.getRestResp(url)
    
    def get_RecentGame(self):
        """ Retrieve the recent games object """
        _baseNameUrl = 'http://prod.api.pvp.net/api/lol/na/v1.1/game/by-summoner/'
        _sumID = self._summonerObj['id']
        url = _baseNameUrl + str(_sumID) +'/recent?api_key=' + self._api_key
        print 'recent games url=',url        
        self._recentGameObj = self.getRestResp(url)
        

lycon_ro = C_Riot_retrieval('xxxx ur- API-key xxxx ','lycon13')
if lycon_ro is None:
    print 'Unable to retrieve info from RIOT on user'
sr = lycon_ro.print_summonerID()
rg_obj = lycon_ro._recentGameObj

"""getting games """
w_count = 0
l_count = 0
recentGames = rg_obj['games']
game_len = len(rg_obj['games'])
for i in range(game_len):
    for x in recentGames[i]['statistics']:
        if x['name'] == 'WIN':
            w_count += 1
        elif x['name'] == 'LOSE':
            l_count += 1    
        
print "win count:",w_count,"lose count:",l_count
#print recentGames[4]['statistics']


