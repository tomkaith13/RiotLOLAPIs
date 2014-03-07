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
        try:
            _userResp = urllib2.urlopen(url, timeout=30).read()
        except:
            print 'Unable to open url',url,'and retrieve data'
            raise
        return json.loads(_userResp)      
        
    def print_summonerID(self):
        """ print summoner id of the summonername provided""" 
        try:
            summonerName=(self._summonerObj[self._sName.lower()])['id']
        except:
            print 'Unable to retrieve summoner ID from name:',self._sName
            raise       
        print 'summoner id=',summonerName        
        return summonerName        
    
    def retrieve_summonerOBJ(self):
        """ Retrieve summonerID from the summoner name given"""
        _baseNameUrl='https://prod.api.pvp.net/api/lol/na/v1.3/summoner/by-name/'
        print 'api key=',self._api_key
        url=_baseNameUrl + self._sName + '?api_key=' + self._api_key        
        self._summonerObj = self.getRestResp(url)
    
    def get_RecentGame(self):
        """ Retrieve the recent games object """
        _baseNameUrl = 'https://prod.api.pvp.net/api/lol/na/v1.3/game/by-summoner/'
        
        print self._summonerObj
        print self._sName.lower()
        print self._summonerObj[self._sName.lower()]
        print (self._summonerObj[self._sName.lower()])['id']
        _sumID = str((self._summonerObj[self._sName.lower()])['id'])
        url = _baseNameUrl + _sumID +'/recent?api_key=' + self._api_key
        print 'recent games url=',url        
        self._recentGameObj = self.getRestResp(url)
        
        

        
        
        
        
        

def main():    
    lycon_ro = C_Riot_retrieval('68cb0e3b-01cf-4293-aaeb-b93750f65021','lycon13')
    if lycon_ro is None:
        print 'Unable to retrieve info from RIOT on user'
    sr = lycon_ro.print_summonerID()
    rg_obj = lycon_ro._recentGameObj
    
    """getting games """
    w_count = 0
    l_count = 0
    print rg_obj
    recentGames = rg_obj['games']
    game_len = len(rg_obj['games'])
    print 'num of games:',game_len
    for i in range(game_len):
        player_stats = dict(recentGames[i]['stats'])
        print player_stats['win']
        if player_stats['win']:
            w_count+=1
        else:
            l_count+=1
            
      
            
    print "win count:",w_count,"lose count:",l_count
    #print recentGames[4]['statistics']

if __name__ == "__main__":
    main()



