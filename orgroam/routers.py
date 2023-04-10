
class OrgRoamRouter(object): 
    def db_for_read(self, model, **hints):
        "Point all operations on chinook models to 'org-roam'"
        if model._meta.app_label == 'orgroam':
            return 'org-roam'
        return 'default'

    def db_for_write(self, model, **hints):
        "Point all operations on chinook models to 'org-roam'"
        if model._meta.app_label == 'orgroam':
            return 'org-roam'
        return 'default'
    
    def allow_relation(self, obj1, obj2, **hints):
        "Allow any relation if a both models in  app"
        if obj1._meta.app_label == 'orgroam' and obj2._meta.app_label == 'orgroam':
            return True
        # Allow if neither is  app
        elif '' not in [obj1._meta.app_label, obj2._meta.app_label]: 
            return True
        return False
    
    def allow_syncdb(self, db, model):
        if db == 'org-roam' or model._meta.app_label == "orgroam":
            return False # we're not using syncdb on our legacy database
        else: # but all other models/databases are fine
            return True
