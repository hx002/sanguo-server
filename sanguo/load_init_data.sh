#!/bin/bash

# data="server_list.json
#       hero_quality.json
#       hero.json
#       get_hero.json"

data = "server_list.json
        get_hero.json"

for d in $data
do
    python manage.py loaddata $d
done
