##sh3nokam3: For making http get and post requests
import requests
##sh3nokam3: For parsing json data
import json
##sh3nokam3: For collecting data with regular expressions
import re
##sh3nokam3: For generating uuid for betpawa
import uuid
##sh3nokam3: For generating 12 digit random number to be used in placing a betking bet
from random import randint
##sh3nokam3: Helps make warnings and errors more eye catching
from colorama import Fore, Back, Style
##sh3nokam3: Betpawa places a bet, gets an Id and has to keep rechecking to see if games places
import time


##sh3nokam3: Representative Ids for each betting site according to breaking bet
Naija = 42
Sporty = 43
B9ja = 33
Merry = 34
Golden = 36
Naira = 38
Pawa = 44
BetKing = 49
Access = 59
Afriplay = 60

##sh3nokam3: Calculate amount on other side rounded to nearest 100
def two_sides(bet_a, odds_a, odds_b):
	#!x = (bet_a/((1/odds_a)/((1/odds_a)+(1/odds_b))))-bet_a
	other_amount = int(bet_a*0.1*odds_a/odds_b)*10
	#!return x
	return other_amount

##sh3nokam3: @Crestward Comment generously
class Games():
    def __init__(self):
        ## Crestward: This currently appends all matches, includes the same match over and over. I pass the headache over to you
        self.all_arbs = []
        self.raw_arbs = []
    def get_game(self):
        break_sess = '33b140d4799e5376b19efda7c5a7f524'
        url = 'https://breaking-bet.com/users/48251/settings/prematch'
        cookies = {'_breakingbet_session': f'{break_sess}'}
        response = requests.get(url, cookies=cookies)
        token = response.json()['arbs_api_token']
        print(token)
        cookies = {'_breakingbet_session': f'{break_sess}'}
        headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/x-www-form-urlencoded',
        }
        ##sh3nokam3: Manually set the bookmakers you want in the required_bookmakers array
        data = '{"l2":true,"l3":true,"level":0,"min":"0","max":"0","skip_integer":false,"skip_quarter":false,"age":24,"inner":false,"rules":true,"allowed_bookmakers":[38,42],"required_bookmakers":[],"coeffs_ranges":{},"sports":[1,2,3,4,5,6,7,8,9,10,11,12],"in_break_only_sports":[],"skip_arbs":[],"skip_sections":[],"sort":"percent","type":"prematch","min_level":0,"max_level":0,"lifetime_min_minutes":"0","lifetime_max_minutes":"0","lifetime_min_seconds":"0","lifetime_max_seconds":"0","initiating_bookmakers":[21,59,39,33,49,6,23,3,62,14,25,63,8,55,60,68,5,34,52,42,38,54,7,64,9,67,43,71,18,36,4,44],"opponent_bookmakers":[21,59,39,33,49,6,23,3,62,14,25,63,8,55,60,68,5,34,52,42,38,54,7,64,9,67,43,71,18,36,4,44],"required_initiators":[]}'
        url='https://breaking-bet.com/api/v1/prematch/arbs/search'
        time.sleep(5)
        while True:
           response=requests.post(url, cookies=cookies, headers=headers, data=data)
           data = response.json()
           if data != {'text': 'accepted'}:
               break
        #data = response.json()
        self.raw_arbs = data
        arbs = data['Arbs']
        print(arbs)
        events = data['Events']
        #!all_arbs = {}
        self.all_arbs = []
        for i in range(len(arbs)):
            breaking_ev = arbs[i]['Ev']
            start_time = events[str(breaking_ev)]['Start']
            team1 = events[str(breaking_ev)]['Team1']
            team2 = events[str(breaking_ev)]['Team2']
            sportid = events[str(breaking_ev)]['SportId']
            arb_interest = arbs[i]['Hv']
            num_of_arbs = len(arbs[i]['Odds'])
            arbs_available = arbs[i]['Odds']
            temp = []
            for p in range(len(arbs[i]['Odds'])):
                odd = arbs[i]['Odds'][p]['Val']
                #oddid = arbs[i]['Odds'][p]['OID']
                breaking_eventid = arbs[i]['Odds'][p]['Ev']
                bookmaker = arbs[i]['Odds'][p]['Book']
                if bookmaker == 60:
                    oddid = arbs[i]['Odds'][p]['Crumbs']['id'] 
                elif bookmaker == 44:
                    oddid = arbs[i]['Odds'][p]['Crumbs']
                else:
                    oddid = arbs[i]['Odds'][p]['OID']
                #if bookmaker == 60:
                #    oddid = arbs[i]['Odds'][p]['Crumbs']['id']
                eventid = events[str(breaking_ev)]['Sub'][str(breaking_eventid)]['original_id']
                temp.append({'odd': odd, 'oddid': oddid, 'bookmaker': bookmaker, 'eventid': eventid})
                temp[-1]['leagueid'] = events[str(breaking_ev)]['Sub'][str(breaking_eventid)]['crumbs']['league_id'] if bookmaker == 42 else 0
            #!all_arbs["Arb" + str(i)] = {"Time": start_time, "team1": team1, "team2": team2, "Sport": sportid, "ROI": arb_interest, "numodds" : num_of_arbs, "details":temp}
            self.all_arbs.append({'Time': start_time, 'team1': team1, 'team2': team2, 'Sport': sportid, 'ROI': arb_interest, 'numodds' : num_of_arbs, 'b_eventid': breaking_eventid, 'details':temp})
        #print (all_arbs)


##sh3nokam3: Class structure for making bets
class BetBot:
    ##sh3nokam3: Initialize class with siteid, manually input username and password of each site to use
    def __init__(self, siteid):
        self.bookmaker = siteid
        if self.bookmaker == 34:
            self.username = ''
            self.password = ''
        if self.bookmaker == 36:
            self.username = ''
            self.password = ''
        if self.bookmaker == 38:
            self.username = 'Layool'
            self.password = 'Layway1995'
        if self.bookmaker == 42:
            self.username = 'Layoolar'
            self.password = 'layway1995'
        #if self.bookmaker == 43:
        #    self.username = '8102650584'
        #    self.password = 'Betwell5'
        if self.bookmaker == 44:
            self.username = ''
            self.password = ''
        if self.bookmaker == 49:
            self.username = ''
            self.password = ''
        if self.bookmaker == 59:
            self.username = ''
            self.password = ''
        if self.bookmaker == 60:
            self.username = ''
            self.password = ''
        self.login()
    ##sh3nokam3: Login method sets self.cookies to re-useable cookies for balance checking and placing bets
    ##sh3nokam3: Login method returns true is login succeed and false if login fails
    def login(self):
        if self.bookmaker == 60:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:101.0) Gecko/20100101 Firefox/101.0'}
            response = requests.get(f'https://ps.afriplay.com/ps/ips/login?username={self.username}&password={self.password}&brandId=1', headers=headers)
            try:
                self.cookies = response.json()['sessionKey']
                return True
            except:
                return False
        if self.bookmaker == 42:
            data = {
            'sec': '400001',
            'subsec': 'check',
            'login': 'Proceed',
            'username': self.username,
            'password': self.password,
            }
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:101.0) Gecko/20100101 Firefox/101.0'}
            response = requests.post('https://www.naijabet.com/getdata.php', headers=headers, data=data)
            try:
                self.cookies = response.headers['Set-Cookie'].split(';')[0].split('=')[1]
                return True
            except:
                return False
        if self.bookmaker == 49:
            url = 'https://auth-api-betagy.betagy.services/oauth/Token'
            #!data = f'username={self.username}&password={self.password}&brandId=1901&grant_type=password'
            #!headers={'Content-Type': 'application/x-www-form-urlencoded'}
            json_data = {'username': self.username, 'password': self.password, 'brandId': 1901, 'grant_type': 'password'}
            response = requests.post(url, json_data) #, headers=headers)
            try:
                self.cookies = response.json()['access_token']
                return True
            except:
                return False
        if self.bookmaker == 44:
            url = 'https://www.betpawa.ng/api/user/v1/authenticate'
            json_data = {'username': self.username, 'password': self.password, 'country': 'NG'}
            headers = {'jurId': '4'}
            response = requests.post(url, headers=headers, json=json_data)
            ##sh3nokam3: Pardon the exessive use of splits, challenged myself not to use regex here
            try:
                spl = response.headers['set-cookie'].split('=')
                spli = str(spl).split(', ')
                index = spli.index("x-pawa-token'")
                self.cookies = spli[19].replace("'",'').replace('; Path', '')
                return True
            except:
                return False
        if self.bookmaker == 59:
            url = 'https://sport.accessbet.com/rest/customer/session/login'
            json_data = {'login': self.username, 'password': self.password, 'channel': 'desktop', 'browser': 'firefox', 'device': 'desktop'}
            response = requests.post(url, json=json_data)
            try:
                self.cookies = response.headers['X-ODDS-SESSION']
                return True
            except:
                return False		
        if self.bookmaker == 38:
            url = 'https://www.nairabet.com/rest/customer/session/login'
            json_data = {'login': self.username, 'password': self.password, 'channel': 'desktop', 'browser': 'firefox', 'device': 'desktop'}
            response = requests.post(url, json=json_data)
            try:
                self.cookies = response.headers['X-ODDS-SESSION']
                return True
            except:
                return False		
        if self.bookmaker == 36:
            url = 'https://www.winnersgoldenbet.com/rest/customer/session/login'
            json_data = {'login': self.username, 'password': self.password, 'channel': 'desktop', 'browser': 'firefox', 'device': 'desktop'}
            response = requests.post(url, json=json_data)
            try:
                self.cookies = response.headers['X-ODDS-SESSION']
                return True
            except:
                return False		
        if self.bookmaker == 34:
            url = 'https://www.merrybet.com/rest/customer/session/login'
            json_data = {'login': self.username, 'password': self.password, 'channel': 'desktop', 'browser': 'firefox', 'device': 'desktop'}
            response = requests.post(url, json=json_data)
            try:
                self.cookies = response.headers['X-ODDS-SESSION']
                return True
            except:
                return False
    ##sh3nokam3: Returns balance 
    def get_balance(self):
        self.check_if_logged_in()
        print(self.balance) 
    ##sh3nokam3: Returns true or false if logged in or not. Also checks and sets balance. Get_balance function calls this to set balance
    def check_if_logged_in(self):
        if self.bookmaker == 60:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:101.0) Gecko/20100101 Firefox/101.0'}
            response = requests.get(f'https://ps.afriplay.com/ps/ips/getBalanceSimple?sessionKey={self.cookies}&brandId=1', headers=headers)
            try:
                self.balance = float(response.json()['withdrawableBalance'])
                return True
            except:
                return False
        if self.bookmaker == 42:
            cookies = {'PHPSESSID': self.cookies}
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:101.0) Gecko/20100101 Firefox/101.0'}
            response = requests.get('https://www.naijabet.com/balance/', cookies=cookies, headers=headers)
            try:
                self.balance = float(response.text.split('₦')[1].split('<')[0].replace(' ',''))
                return True
            except:
                return False
        if self.bookmaker == 49:
            url = 'https://website-api-betking.betagy.services/api/Finance/Accounts/ByPlaySource/web'
            response = requests.get(url, headers={'Authorization': f'Bearer {self.cookies}'})
            try:
                self.balance = response.json()['Result'][0]['Balance']
                return True
            except:
                return False
        if self.bookmaker == 44:
            url = 'https://www.betpawa.ng/api/wallet/v1/balance'
            cookies = {'x-pawa-token': self.cookies}
            headers = {'jurId': '4'}
            response = requests.get(url, headers=headers, cookies=cookies)
            try:
                self.balance = response.json()['balance']
                return True
            except:
                return False
        if self.bookmaker == 59:
            url = 'https://sport.accessbet.com/rest/customer/account/personal-data'
        if self.bookmaker == 38:
            url = 'https://www.nairabet.com/rest/customer/account/personal-data'
        if self.bookmaker == 36:
            url = 'https://www.winnersgoldenbet.com/rest/customer/account/personal-data'
        if self.bookmaker == 34:
            url = 'https://www.merrybet.com/rest/customer/account/personal-data'
        cookies = {'X-ODDS-SESSION': self.cookies}
        headers = {'x-odds-session': f'{self.cookies}'}
        response = requests.get(url,cookies=cookies,headers=headers)
        try:
            self.balance = response.json()['data']['accountBalance']
            return True
        except:
            return False        
	##Crestward: Why are cookies an input here? It wasn't used
	##sh3nokam3: Cookies were not used 😐
	##sh3nokam3: Checks if bet can be placed
    def check_if_bet_placeable(self, eventid, oddid, odd, leagueid):
        self.eventid = eventid
        self.oddid = oddid
        self.leagueid = leagueid
        if self.bookmaker == 60:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:101.0) Gecko/20100101 Firefox/101.0'}
            response = requests.get(f'https://nodeprm.tsports.online/cache/42/en/ng/{eventid}/single-pre-event.json', headers=headers)
            print(eventid,oddid,odd)
            try:
                self.odd = response.json()['odds'][f'{oddid}']['odd_value']
                self.event = response.json()['info']
                self.odd_details = response.json()['odds'][f'{oddid}']
                if  float(self.odd) >= float(odd):
                    self.odd = float(self.odd)
                    #print('Bet Placable on AfriPlay. Proceed With EXTREME Caution')
                    #Additional setup
                    params = {
                    'token': self.cookies,
                    'franchise': '42',
                    }
                    response = requests.get('https://nodeusr.tsports.online/42/en/init.json', params=params)
                    self.player_id = response.json()['player']['id']
                else:
                    print('Bet Not Placable. Odd Wrong')
                    return False
            except:
                print('Bet Not Placable')
                return False
            self.uid = uuid.uuid4()
            params = {
            'player_id': self.player_id,
            }
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:101.0) Gecko/20100101 Firefox/101.0'}
            json_data = {
            'player_id': int(self.player_id),
            'selections': [
            {
            'id': int(self.oddid),
            'selection_id': f'{self.uid}',
            'event_odd_id': int(self.oddid),
            'event_id': int(self.odd_details['event_id']),
            'odd_value': self.odd,
            'odd_id': int(self.odd_details['odd_id']),
            'denominator': int(self.odd_details['denominator']),
            'numerator': int(self.odd_details['numerator']),
            'frozen': False,
            'deleted': False,
            'add_value': self.odd_details['additional_value_raw'],
            'title': self.odd_details['defaultName'],
            'info': f'{self.event["teams"]["home"]} - {self.event["teams"]["away"]}',
            'packet': False,
            'is_live': False,
            'status': 0,
            'date_start': self.event['date_start'],
            'short_id': self.event['short_id'],
            'team_side': self.odd_details['team_side'],
            'ttl': '',
            'team_player': 0,
            'variation_id': 0,
            'sport_id': self.event['sport_id'],
            'tournament_id': self.event['tournament_id'],
            'league': f'{self.event["country_name"]["en"]} - {self.event["tournament_name"]["en"]}',
            'sp_only': False,
            'is_boosted': None,
            'min_express_combination': 0,
            'filter_id': self.odd_details['filter_id'],
            'filter_name': self.odd_details['defaultName'].split('-')[0],
            'betbuilder_enabled': False,
            'betbuilderV2_enabled': False,
            'event': self.event,
            'created': int(time.time()*1000),
            'isDisabledStake': False,
            },
            ],
            'logged_in': True,
            }
            try:
                json_data['selections'][0]['group_id'] = self.odd_details['group_id']
            except:
                pass
            try:
                del json_data['selections'][0]['event']['bets']
                del json_data['selections'][0]['event']['main_odds']
                del json_data['selections'][0]['event']['count']
                del json_data['selections'][0]['event']['featured']
            except:
                pass
            response2 = requests.post('https://nodeusr.tsports.online/42/en/to_bet_slip', params=params, headers=headers, json=json_data)
            self.json_data = json_data
            print(self.json_data)
            print(response2.json())
            try:
                if 'VALIDATION_OK' in response2.json()['selections'][0]['message']:
                    print(f'Bet Placable. Fun Fact, Max Stake is {response2.json()["bets"][0]["max_stake"]}')
                    return True
                else:
                    print(f'Bet Not Placable. {response2.json()["selections"][0]["message"]}')
                    return False
            except:
                print('Bet Not Placable. Go and Debug')
                return False
        if self.bookmaker == 42:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:101.0) Gecko/20100101 Firefox/101.0'}
            response = requests.get(f'https://www.naijabet.com/getdata.php?sec=100003&subsec=DisplayBetableEvents&league_ids[]={self.leagueid}&extended_layout=1&event_ids[]={self.eventid}', headers=headers)
            try:
                self.odd = response.text.split(f'{oddid}')[1].split('odds&quot;:')[1].split(',')[0]
                if  float(self.odd) >= float(odd):
                    self.odd = float(self.odd)
                    print('Bet Placable on NaijaBet. Proceed With EXTREME Caution')
                    return True
                else:
                    print('Bet Not Placable. Odd Wrong')
                    return False
            except:
                print('Bet Not Placable')
                return False
        if self.bookmaker == 49:
            data = '{}'
            headers={'Authorization': f'Bearer {self.cookies}'}
            response = requests.post(f'https://sportsapi.betagy.services/api/BetCoupons/AddSelections/en?selectionIds[0]={self.oddid}', data=data, headers=headers)
            # print(response.json()
            try:
                self.odd = response.json()['BetCoupon']['Odds'][0]['OddValue']
                if  float(self.odd) >= float(odd):
                    self.odd = float(self.odd)
                    self.gamedict = {'BetCoupon': response.json()['BetCoupon']}
                    self.gamedict['AllowOddChanges'] = True
                    self.gamedict['AllowStakeReduction'] = False
                    self.gamedict['TransferStakeFromAgent'] = False
                    random_number = randint(100000000000, 999999999999)
                    self.gamedict['RequestTransactionId'] = str(random_number)+response.json()['BetCoupon']['UserId']
                    print('Bet Placable. Proceed With Caution')
                    return True
                else:
                    print('Bet Not Placable. Odd Wrong')
                    return False
            except:
                print('Bet Not Placable')
                return False
        if self.bookmaker == 44:
            #return False
            headers = {'jurId': '4'}
            response = requests.get(f'https://www.betpawa.ng/api/events/getPricesForEvent/{self.eventid}', headers=headers)
            #info = re.search(str(self.oddid)+'.{100}', json.dumps(response.json()))
            #self.odd = info.group(0).split('"')[5]
            try:
                self.odd = response.json()['Data']['Markets'][int(self.oddid['m'])][int(self.oddid['o'])]['PriceRaw']
                if (float(self.odd) < float(odd)+0.2) and (float(self.odd) > float(odd)-0.2):
                    self.odd = float(self.odd)
                    self.oddid = response.json()['Data']['Markets'][int(self.oddid['m'])][int(self.oddid['o'])]['Id']
                    print('Bet Placable. Proceed Caution')
                    return True
                else:
                    print('Bet Not Placable. Odd Wrong')
                    return False
            except:
                print('Bet Not Placable')
                return False
        if self.bookmaker == 59:
            url = f'https://sport.accessbet.com/rest/market/events/{self.eventid}'
        if self.bookmaker == 38:
            url = f'https://nairabet.com/rest/market/events/{self.eventid}'
        if self.bookmaker == 36:
            url = f'https://www.winnersgoldenbet.com/rest/market/events/{self.eventid}'
        if self.bookmaker == 34:
            url = f'https://www.merrybet.com/rest/market/events/{self.eventid}'
        response=requests.get(url)
        # print(response.json())
        info = re.search(str(self.oddid)+'.{100}', json.dumps(response.json()))
        #Verify if odd is as says and status is 100
        #print(response.json())
        self.sportid = response.json()['data']['treatAsSport']
        odd_group = info.group(0)
        odd_group2 = re.search("Odds\":(\s+)?(\d+(\.\d+)?)", odd_group)
        odd_present = odd_group2.group(2)
        if  float(odd) <= float(odd_present):
            print('Bet Placable. Proceed caution')
            self.odd = float(odd_present)
            return True
        else:
            return False
	##sh3nokam3: Places bet
    def place_bet(self,amount):
        if self.bookmaker == 60:
            params = {
            'token': self.cookies,
            'franchise': '42',
            'player_id': self.player_id,
            }
            json_data = {
            'selections': self.json_data['selections'],
            'stakes': [
            {
            'type': 1,
            'stake': amount,
            'input_stake': f'{amount}',
            'max_exceed_action': 0,
            'is_each_way': False,
            'taxes': 0,
            'isStakeDisabled': False,
            'additional_info': {
            'event_odd_id': int(self.oddid),
            'selection_id': f'{self.uid}',
            'odd_id': int(self.odd_details['odd_id']),
            'event_id': int(self.odd_details['event_id']),
            'add_value': self.odd_details['additional_value_raw'],
            'no_risk_bet_id': False,
            },
            },
            ],
            'stake_way': 0,
            'max_exceed_action': 0,
            'is_one_click_bet': False,
            'auth_token': self.cookies,
            }
            json_data['selections'][0]['correct_score'] = None
            #print(json_data)
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:101.0) Gecko/20100101 Firefox/101.0'}
            response = requests.post('https://nodeusr.tsports.online/42/en/place_bet', params=params, headers=headers, json=json_data)
            balance = self.balance
            self.get_balance()
            if self.balance != balance:
                print(Fore.GREEN + f'Bet Placed On Afriplay')
                print(Style.RESET_ALL)
                return True
            else:
                print(Fore.RED + 'Warning. Bet Not Placed On Afriplay')
                print(Style.RESET_ALL)
                return False
#            try:
#                self.slipId = response.json()['success']
#                if self.slipId == False or 'alse' in self.slipId:
#                   return False
#                else:
#                   return True
#                print(Fore.GREEN + f'Bet {self.slipId} Placed On Afriplay')
#                print(Style.RESET_ALL)
#                return True
#            except:
#                print(Fore.RED + 'Warning. Bet Not Placed On Afriplay')
#                print(Style.RESET_ALL)
#                return False
        if self.bookmaker == 42:
            cookies = {
            'PHPSESSID': self.cookies,
            'currency': 'NGN',
            'saved_oids': f'{self.oddid}',
            'default_stake_single': f'{amount}',
            'default_stake_combined': '',
            'default_stake_system': ''
            }
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:101.0) Gecko/20100101 Firefox/101.0'}
            #Using a value of 9999999 can get max stake
            #Odds can be checked by trying to bet on wrong odd
            json_data = {
            'stake[]': f'{amount}.00',
            'oid[]': f'{self.oddid}',
            'odds[]': f'{self.odd}',
            'buypoints[]': '0',
            'live[]': '0',
            'syst': '',
            'banker': '',
            'withdraw_type[]': 'none',
            'lay[]': '',
            'accept_higher': 'false',
            'accept_any': 'false',
            'pitchers_action[]': '',
            'is_booking_number': '0',
            'print_coupon': '0',
            'sms_coupon': '0',
            }
            response = requests.post('https://www.naijabet.com/placebet/single/', cookies=cookies, headers=headers, data=json_data)
            try:
                self.slipId = response.json()['bet']
                print(Fore.GREEN + f'Bet {self.slipId} Placed On NaijaBet')
                print(Style.RESET_ALL)
                return True
            except:
                print(Fore.RED + 'Warning. Bet Not Placed On NaijaBet')
                print(Style.RESET_ALL)
                val = False
                n = 15
                print(f"Trying again...... in {n} seconds")
                for i in range(1):
                    ## Crestward:          
                    time.sleep(n)
                    response = requests.post('https://www.naijabet.com/placebet/single/', cookies=cookies, headers=headers, data=json_data)
                    try: 
                        self.slipId = response.json()['bet']
                        print(Fore.GREEN + f'Bet {self.slipId} Finally Placed on NaijaBet')
                        print(Style.RESET_ALL)
                    ## Crestward: works?   
                        val = True
                        break
                    except:
                        print(Fore.RED + 'Warning. Bet Still Not Placed On NaijaBet')
                        print(Style.RESET_ALL) 
                        print(f"Inside the for loop. Trying again in {n} seconds......")               
                        continue
                return val
        if self.bookmaker == 44:
            cookies = {'x-pawa-token': f'{self.cookies}'}
            headers = {'jurId': '4'}
            id = uuid.uuid4()
            json_data = {
            'AcceptAnyPrice': False,
            'CombinationType': 'ACCUMULATOR',
            'CurrencyCode': 'NGN',
            'Items': [
            {
            'EligibleForBonus': True,
            'PriceId': int(self.oddid),
            'PriceRaw': float(self.odd),
            'Price': f'{self.odd}',
            },
            ],
            'LegBonusSchemeId': 18,
            'Stake': int(amount),
            'notEligibleForBonus': False,
            'cashoutable': True,
            'uuid': f'{id}',
            }
            try:
                response = requests.post('https://www.betpawa.ng/api/fixed-odds-bets/user/betslip/placeBet', cookies=cookies, headers=headers, json=json_data)
                self.slipId = response.json()["Data"]["BetslipId"]
                count = 5
                for i in range(5):
                    response = requests.get(f'https://www.betpawa.ng/api/fixed-odds-bets/user/betslip/getBetslipStatus/{self.slipId}', cookies=cookies, headers=headers)
                    time.sleep(1)
                    if response.json()['Data']['Placed'] == True:
                        print(Fore.GREEN + f'Bet {self.slipId} Placed On BetPawa')
                        return True
                print(Fore.RED + 'Warning. Bet {self.slipId} Does Not Seem To Be Placed On BetPawa. Timed Out on Checking')
                print(Style.RESET_ALL)
                return False
            except:
                print(Fore.RED + 'Warning. Bet Not Placed On BetPawa')
                print(Style.RESET_ALL)
                return False
        if self.bookmaker == 49:
            self.gamedict['BetCoupon']['MinWin'] = self.odd * amount
            self.gamedict['BetCoupon']['MaxWin'] = self.odd * amount
            self.gamedict['BetCoupon']['Stake'] = amount
            self.gamedict['BetCoupon']['StakeGross'] = amount
            self.gamedict['BetCoupon']['MinWinNet'] = self.odd * amount
            self.gamedict['BetCoupon']['MaxWinNet'] = self.odd * amount
            self.gamedict['BetCoupon']['NetStakeMaxWin'] = self.odd * amount
            self.gamedict['BetCoupon']['NetStakeMinWin'] = self.odd * amount
            self.gamedict['BetCoupon']['Groupings'][0]['MinWin'] = self.odd * amount
            self.gamedict['BetCoupon']['Groupings'][0]['MaxWin'] = self.odd * amount
            self.gamedict['BetCoupon']['Groupings'][0]['Stake'] = amount
            self.gamedict['BetCoupon']['Groupings'][0]['NetStake'] = amount
            self.gamedict['BetCoupon']['Groupings'][0]['NetMinWin'] = self.odd * amount
            self.gamedict['BetCoupon']['Groupings'][0]['NetMaxWin'] = self.odd * amount
            self.gamedict['BetCoupon']['Groupings'][0]['NetStakeMaxWin'] = self.odd * amount
            self.gamedict['BetCoupon']['Groupings'][0]['NetStakeMinWin'] = self.odd * amount
            response = requests.post(f'https://sportsapi.betagy.services/api/coupons/InsertCoupon', headers={'Authorization': f'Bearer {self.cookies}'}, json=self.gamedict)
            #print(response.json())
            try:
                #print('Hi')
                self.slipId = response.json()['CouponCode']
                #print('Hi')
                print(Fore.GREEN + f'Bet {self.slipId} Placed On BetKing')
                print(Style.RESET_ALL)
                return True
            except:
                print(Fore.RED + 'Warning. Bet Not Placed On BetKing')
                print(Style.RESET_ALL)
                return False
        if self.bookmaker == 59:
            url = 'https://sport.accessbet.com/rest/betting/bet/place-bet/web'
        if self.bookmaker == 38:
            url = 'https://nairabet.com/rest/betting/bet/place-bet/web'
        if self.bookmaker == 36:
            url = 'https://www.winnersgoldenbet.com/rest/betting/bet/place-bet/web'
        if self.bookmaker == 34:
            url = 'https://www.merrybet.com/rest/betting/bet/place-bet/web'
        cookies = {'X-ODDS-SESSION': self.cookies}
        headers = {'x-odds-session': f'{self.cookies}'}
        json_data = {'stake': amount, 'betType': 100, 'addAccumulator': 'false', 'acceptHigherOdds': 'true', 'acceptAnyOdds': 'false', 'outcomes': [{'outcomeLive': 'true', 'outcomeId': self.oddid, 'outcomeOdds': self.odd, 'banker': 'false', 'sportId': self.sportid, 'eventId': self.eventid, 'eventType': 2, 'optionalParameters': []}], 'blocks': [], 'countryCode': 'null', 'countdowned': 'false', 'betSlipHash': '', 'currencyCode': 'NGN'}
        response = requests.post(url, headers=headers, json=json_data)
        print(response.json())
        if response.status_code == 200:
            #self.slipId = response.json()['CouponCode']
            print(Fore.GREEN + f'Bet Placed on WAMN')
            print(Style.RESET_ALL)
            return True
        else:
            ## Crestward: Test this shit
            print(Fore.RED + 'Warning. Bet Not Placed On WAMN')
            print(Style.RESET_ALL)
            val = False
            n = 15
            print(f"Trying again...... in {n} seconds")
            for i in range(1):
                ## Crestward:          
                time.sleep(n)
                response = requests.post(url, headers=headers, json=json_data)
                print(response.json())
                if response.json()['code'] == 200:
                    print(Fore.GREEN + f'Bet Finally Placed on WAMN')
                    print(Style.RESET_ALL)
                ## Crestward: works?   
                    val = True
                    break
                else:
                    print(Fore.RED + 'Warning. Bet Still Not Placed On WAMN')
                    print(Style.RESET_ALL) 
                    print(f"Inside the for loop. Trying again in {n} seconds......")               
                    continue
            return val

books = {
    '60': 'Afriplay',
    '38': 'NairaBet',
    '59': 'AccessBet',
    '36': 'GoldenBet',
    '42': 'NaijaBet',
    '43': 'SportyBet',
    '34': 'MerryBet',
    '33': 'Bet9ja',
    '49': 'BetKing',
    '44': 'BetPawa'
}



## Crestward: List of dicts to store succcessful arbs
bets = []

#f = open('Arb_Placed.txt', 'a')

Count_File = open("Count.json", "r")
Count = json.loads(Count_File.read())
Count_File.close()





game = Games()
while True:
    print('Scanning.....')
    ## Crestward: Gets all available arbs
    try:
        game.get_game()
	##Fixed in code
        #game.get_game()
        arb = game.all_arbs
        print('Gotten arbs')
    except:
        continue
    print(arb)
    ## Crestward: Goes through all arbs and stores the number of sites per arb, roi, and the event IDs
    for i in arb:
        num_of_odds = i['numodds']
        roi = i['ROI']

        eventid1 = i['details'][0]['eventid']
        eventid2 = i['details'][1]['eventid']
        b_event = i['b_eventid']
        s_type = i['Sport']
        ## Crestward: Checks if the arb involves 2 sites and the roi is greater than 2%
        if int(num_of_odds) < 3 and float(roi) >= 1.5 and float(roi) <= 10: # and (int(s_type) == 1 or int(s_type) == 6):
            ## Crestward: Conditional to check if the current arb has been placed before
        #    if len(bets) != 0:
        #        for i in bets:
        #            if i["b_eventid"] == b_event:
        #                g = 1
            g = 1 if b_event in Count['Placed'] else 0
            ## Crestward: Store start time, sport type, match bookmakers, match event IDs
            if g == 0:
                print('Found valid arb')
                timed = i['Time']

                bookmaker1 = i['details'][0]['bookmaker']
                bookmaker2 = i['details'][1]['bookmaker']

                league_id1 = i['details'][0]['leagueid']
                league_id2 = i['details'][1]['leagueid']

                odd1 = i['details'][0]['odd']
                odd2 = i['details'][1]['odd']

                oddid1 = i['details'][0]['oddid']
                oddid2 = i['details'][1]['oddid']

                if bookmaker1 in (34,36,38,59) and bookmaker2 in (34,36,38,59):
                    continue

                ## Crestward: Specifically making sure Naijabet is the first bookmaker if it shows up
                if bookmaker2 in (34,36,38,59):
                    print("WAMN Spotted")
                    bet1 = BetBot(bookmaker2)
                    bet2 = BetBot(bookmaker1)
                    bookmaker1 = i['details'][1]['bookmaker']
                    odd1 = i['details'][1]['odd']
                    oddid1 = i['details'][1]['oddid']
                    bookmaker2 = i['details'][0]['bookmaker']
                    odd2 = i['details'][0]['odd']
                    oddid2 = i['details'][0]['oddid']
                    eventid1 = i['details'][1]['eventid']
                    eventid2 = i['details'][0]['eventid']
                    league_id1 = i['details'][1]['leagueid']
                    league_id2 = i['details'][0]['leagueid']
                else:
                    bet1 = BetBot(bookmaker1)
                    bet2 = BetBot(bookmaker2)

#                if bookmaker2 == 60:
#                    print("AfriPlay Spotted")
#                    bet1 = BetBot(bookmaker2)
#                    bet2 = BetBot(bookmaker1)
#                    bookmaker1 = i['details'][1]['bookmaker']
#                    odd1 = i['details'][1]['odd']
#                    oddid1 = i['details'][1]['oddid']
#                    bookmaker2 = i['details'][0]['bookmaker']
#                    odd2 = i['details'][0]['odd']
#                    oddid2 = i['details'][0]['oddid']
#                    eventid1 = i['details'][1]['eventid']
#                    eventid2 = i['details'][0]['eventid']
#                else:
#                    bet1 = BetBot(bookmaker1)
#                    bet2 = BetBot(bookmaker2) 
                ## Crestward: check if the accounts with the match bookmakers are logged in, and logs in if it is not 
                try:
                    bet1.check_if_logged_in()
                    print('Balance gotten')
                except:
                    try:
                        bet1.login()
                        bet1.check_if_logged_in()
                        print('Logged in on first site')
                        print('Balance gotten')
                    except:
                        print(f'Could Not Login on {books[str(bet1.bookmaker)]}')
                try:
                    bet2.check_if_logged_in()
                    print('Balance Gotten')
                except:
                    try:
                        bet2.login()
                        bet2.check_if_logged_in()
                        print('Logged in on Second Site')
                        print('Balance Gotten')
                    except:
                        print(f'Could not Login on {books[str(bet1.bookmaker)]}')
                ## Crestward: Checks if the arb bet in both sides is placeable and calculates the amount for both sides
                X = 1 if (bet1.check_if_bet_placeable(eventid1, oddid1, odd1, league_id1) and bet2.check_if_bet_placeable(eventid2, oddid2, odd2, league_id2)) else 0
                if X == 1:
                    print('Bet Placeable')
                    print(books[str(bet1.bookmaker)])
                    print(books[str(bet2.bookmaker)])
                    #exit()
                    #first_amount = 10000
                    #sec_amount = two_sides(first_amount,odd1, odd2)
                    #if bookmaker1 == 34:
                    #    first_amount = 8300
                    #    sec_amount = two_sides(first_amount,odd1, odd2)
                    if bookmaker2 == 42:
                        sec_amount= 10000
                        first_amount = two_sides(sec_amount, odd2, odd1)
                    ## Crestward: Checks if the amounts on both sides are enough to cover the bet
                    if bet1.balance >= first_amount:
                        if bet2.balance >= sec_amount:
                            if bet1.place_bet(first_amount):
                                if bet2.place_bet(sec_amount):
                                    print('Arb successfully placed')
                                    Count[f'{bookmaker1}']+=1
                                    Count[f'{bookmaker2}']+=1
                                    Count['Placed'].append(b_event)
                                    Count_File = open("Count.json", "w")
                                    Count_File.write(json.dumps(Count))
                                    Count_File.close()
                                    f = open('Arb_Placed.txt', 'a')
                                    f.write(f'{books[str(bet1.bookmaker)]} {books[str(bet2.bookmaker)]} {first_amount} {sec_amount} {odd1} {odd2} {roi} {time.strftime("%Y-%m-%d %H:%M:%S")} {i["Time"]} {eventid1} {eventid2}\n')
                                    f.close()
                                    exit()
    #                               bets.append({'time': timed, 'eventid1':eventid1, 'eventid2': eventid2, 'roi': roi, 'sport': s_type, 'bk1': books[str(bet1.bookmaker)], 'bk2': books[str(bet2.bookmaker)]})
                                else:
                                    print(f'Arb Unsuccessfully placed on {books[str(bet2.bookmaker)]}')
                                    f = open('Arb_Unplaced.txt', 'a')
                                    f.write(f'{books[str(bet1.bookmaker)]} {books[str(bet2.bookmaker)]} {first_amount} {sec_amount} {odd1} {odd2} {roi} {time.strftime("%Y-%m-%d %H:%M:%S")} {i["Time"]} {eventid1} {eventid2}\n')
                                    f.close()
                                    exit()
                            else:
                                print(f'Arb Unsuccessfully placed on {books[str(bet1.bookmaker)]}')
                                f = open('Arb_Unplaced.txt', 'a')
                                f.write(f'{books[str(bet1.bookmaker)]} {books[str(bet2.bookmaker)]} {first_amount} {sec_amount} {odd1} {odd2} {roi} {time.strftime("%Y-%m-%d %H:%M:%S")} {i["Time"]} {eventid1} {eventid2}\n')
                                f.close()
                                exit()
#                               bets.append({'time': timed, 'eventid1':eventid1, 'eventid2': eventid2, 'roi': roi, 'sport': s_type, 'bk1': books[str(bet1.bookmaker)], 'bk2': books[str(bet2.bookmaker)]})
                        else:
                            print(f'Deposit Needed {books[str(bet2.bookmaker)]}. Current Amount: {bet2.balance}. Amount needed {first_amount - bet2.balance}')
                    else:
                        print(f'Deposit Needed on {books[str(bet1.bookmaker)]}. Current Amount: {bet1.balance}. Amount needed {first_amount - bet1.balance}')
                else:
                    print("Bet Unplaceable")
        print('\n')
        print('Next Arb')
        print('\n')
    print('\n')

#C.check_if_bet_placeable(15593517,13081963270,2,214)
