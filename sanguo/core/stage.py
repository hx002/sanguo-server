from core.drives import document_stage

def get_already_stage(char_id):
    stages = document_stage.get(char_id, _id=0, new=0)
    if not stages:
        return None
    return {int(k): v for k, v in stages.iteritems()}

def get_new_stage(char_id):
    stages = document_stage.get(char_id, new=1)
    if not stages:
        return None
    return stages.get('new', None)
