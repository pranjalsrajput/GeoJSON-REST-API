# https://docs.djangoproject.com/en/dev/ref/templates/builtins/#date
from django.conf.locale.en import formats as en_formats

en_formats.DATETIME_FORMAT = "d M Y H:i:s:u"

from api.admin.features import *
