from django.http import HttpResponse

from apps.character.models import CharHero

from core import GLOBAL
from core.battle.hero import BattleHero, MonsterHero
from core.battle.battle import Battle
from core.character import get_decoded_char_formation

from utils import pack_msg

import protomsg


class PVE(Battle):
    def load_my_heros(self):
        formation = get_decoded_char_formation(self.my_id)
        self.my_heros = []
        for hid in formation.hero_ids:
            if hid == 0:
                self.my_heros.append(None)
            else:
                hero_obj = CharHero.objects.get(id=hid)
                # FIXME
                h = BattleHero(hid, hero_obj.hero_id, hero_obj.exp, [])
                self.my_heros.append(h)



    def load_rival_heros(self):
        monster_ids = GLOBAL.STAGE[self.rival_id]['monsters']
        self.rival_heros = []
        for mid in monster_ids:
            if mid == 0:
                self.rival_heros.append(None)
            else:
                h = MonsterHero(mid)
                self.rival_heros.append(h)


def pve(request):
    msg = protomsg.Battle()

    req = request._proto
    print req

    _, _, char_id = request._decrypted_session.split(':')

    b = PVE(int(char_id), req.stage_id, msg)
    b.start()

    response = protomsg.PVEResponse()
    response.ret = 0
    response.stage_id = req.stage_id
    response.battle.MergeFrom(msg)

    data = pack_msg(response)
    return HttpResponse(data, content_type='text/plain')

