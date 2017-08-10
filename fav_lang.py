#OrderedDict keeps track of order of insertion of key-value pairsgi
from collections import OrderedDict

fav_lang=OrderedDict()

fav_lang['john']='python'
fav_lang['mary']='c'
fav_lang['jane']='ruby'
fav_lang['james']='java'

for name, lang in fav_lang.items():
    print(name.title() + ": " + lang.title())




