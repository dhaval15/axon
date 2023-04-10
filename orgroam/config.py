from django.conf import settings


def org_roam_path_transformer(path: str):
    return path.replace(settings.ORG_ROAM_ORIG_DIRECTORY, settings.ORG_ROAM_DIRECTORY, 1)
