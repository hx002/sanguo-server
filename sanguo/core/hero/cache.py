# -*- coding: utf-8 -*-

from apps.item.cache import get_cache_equipment
from core.mongoscheme import MongoChar
from core.hero import get_hero
from utils import cache


def save_cache_hero(hero_obj):
    cache.set('hero:{0}'.format(hero_obj.id), hero_obj)
    return hero_obj


def get_cache_hero(_id):
    h = cache.get('hero:{0}'.format(_id))
    if h:
        return h

    obj = get_hero(_id)

    mongo_char = MongoChar.objects.only('sockets').get(id=obj.char_id)
    sockets = mongo_char.sockets
    for socket in sockets.values():
        if socket['hero'] == _id:
            for x in ['weapon', 'armor', 'jewelry']:
                if socket[x]:
                    add_extra_attr_to_hero(obj, socket[x])
            break

    h = save_cache_hero(obj)
    return h


def add_extra_attr_to_hero(hero_obj, eid):
    equip = get_cache_equipment(eid)
    attrs = equip.active_attrs()
    for name, value, is_precent in attrs:
        original_value = getattr(hero_obj, name)
        if is_precent:
            new_value = original_value * (1 + value / 100.0)
        else:
            new_value = original_value + value

        new_value = int(new_value)
        setattr(hero_obj, name, new_value)
