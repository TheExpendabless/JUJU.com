import core
import model
import settings

#  MySQL-python==1.2.5 没满足，MySQL-Python不支持Python3.X的MySQL驱动

def get_communitylist():
	res = []
	for community in model.Community.select():
		res.append(community.title)
	return res

if __name__=="__main__":
    regionlist = settings.REGIONLIST # only pinyin support
    model.database_init()
	core.GetNewsFlash()
    core.GetHouseByRegionlist(regionlist)
    core.GetRentByRegionlist(regionlist)
    core.GetCommunityByRegionlist(regionlist) # Init,scrapy celllist and insert database; could run only 1st time
    communitylist = get_communitylist() # Read celllist from database
    core.GetSellByCommunitylist(communitylist)
