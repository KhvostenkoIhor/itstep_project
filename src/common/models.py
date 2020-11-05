from django.db import models
from django.conf import settings


# STATICFILE_DIR = settings.STATICFILES_DIRS[0]
# UPLOAD_DIR = os.path.join(STATICFILE_DIR)

class Photo(models.Model):
    image = models.ImageField(upload_to="upload/images/")
    is_avatar = models.BooleanField(default=False)


